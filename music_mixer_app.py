import streamlit as st
import os
import yt_dlp
from pydub import AudioSegment
import zipfile
import tempfile
import smtplib
from email.message import EmailMessage

# Email Configuration
MAIL_SENDER = "parralexpie@gmail.com"
MAIL_PASS = "wkfp qytg woeu tpai"

# Page Setup
st.set_page_config(
    page_title="Audio Mixer Studio",
    page_icon="🎼",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #FF6B6B;
        text-align: center;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4ECDC4;
        color: white;
        font-size: 1.2rem;
        border-radius: 10px;
        padding: 0.75rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🎼 Audio Mixer Studio</p>', unsafe_allow_html=True)

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎤 Configuration")
    artist_query = st.text_input("Artist/Singer Name", placeholder="Enter artist name...")
    track_count = st.number_input("Number of Tracks", min_value=1, max_value=25, value=6, step=1)
    
with col2:
    st.subheader("⚙️ Settings")
    audio_mode = st.selectbox(
        "Audio Processing Mode",
        ["Trim Each Track", "Keep Full Length"]
    )
    
    if audio_mode == "Trim Each Track":
        clip_length = st.number_input("Seconds per Track", min_value=5, max_value=60, value=15, step=5)
    else:
        clip_length = 0

# Output settings
st.subheader("📤 Output Options")
col3, col4 = st.columns(2)

with col3:
    file_label = st.text_input("Output Name", value="audio_mix", placeholder="Enter filename...")

with col4:
    recipient_mail = st.text_input("Email Address", placeholder="your.email@example.com")


def process_audio_blend(artist_query, track_count, clip_length, file_label):
    """Process and blend audio tracks from YouTube"""
    try:
        workspace = tempfile.mkdtemp()
        media_folder = os.path.join(workspace, "media")
        os.makedirs(media_folder, exist_ok=True)

        download_config = {
            'format': 'bestaudio/best',
            'outtmpl': f'{media_folder}/%(title)s.%(ext)s',
            'quiet': True,
            'noplaylist': True,
            'ignoreerrors': True,
            'geo_bypass': True,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            },
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        yt_query = f"{artist_query} song -live -remix -cover"

        with yt_dlp.YoutubeDL(download_config) as downloader:
            downloader.download([f"ytsearch{track_count}:{yt_query}"])

        merged_track = AudioSegment.empty()
        track_exists = False

        for media_file in os.listdir(media_folder):
            if media_file.endswith(".mp3"):
                track_exists = True
                sound_segment = AudioSegment.from_mp3(os.path.join(media_folder, media_file))

                if clip_length == 0:
                    merged_track += sound_segment
                else:
                    merged_track += sound_segment[:clip_length * 1000]

        if not track_exists:
            return None, None, "Failed to download audio tracks. Try a different artist."

        final_mp3_path = os.path.join(workspace, f"{file_label}.mp3")
        merged_track.export(final_mp3_path, format="mp3")

        archive_path = os.path.join(workspace, f"{file_label}.zip")
        with zipfile.ZipFile(archive_path, 'w') as archive:
            archive.write(final_mp3_path, os.path.basename(final_mp3_path))

        return final_mp3_path, archive_path, None

    except Exception as error:
        return None, None, str(error)


def dispatch_email(recipient_mail, archive_path):
    """Send ZIP file via email"""
    email_msg = EmailMessage()
    email_msg['Subject'] = "🎼 Your Audio Mix is Ready!"
    email_msg['From'] = MAIL_SENDER
    email_msg['To'] = recipient_mail
    email_msg.set_content("Hello!\n\nYour custom audio mix has been created.\nPlease find the attached file.\n\nBest regards,\nAudio Mixer Studio 🎧")

    with open(archive_path, 'rb') as attachment:
        zip_data = attachment.read()
        zip_name = os.path.basename(archive_path)

    email_msg.add_attachment(zip_data,
                             maintype='application',
                             subtype='zip',
                             filename=zip_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail_server:
        mail_server.login(MAIL_SENDER, MAIL_PASS)
        mail_server.send_message(email_msg)


# Main action button
st.markdown("---")
if st.button("🎵 Generate Audio Mix"):

    if artist_query and file_label and recipient_mail:

        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("⏳ Searching and downloading tracks...")
        progress_bar.progress(25)
        
        result_mp3, result_zip, error_msg = process_audio_blend(
            artist_query,
            track_count,
            clip_length,
            file_label
        )
        
        progress_bar.progress(75)

        if error_msg:
            st.error(f"❌ Error: {error_msg}")

        elif result_mp3 and os.path.exists(result_mp3):
            
            progress_bar.progress(100)
            status_text.text("✅ Processing complete!")
            
            st.balloons()
            st.success("🎉 Audio Mix Created Successfully!")

            st.audio(result_mp3)

            with open(result_zip, "rb") as zip_file:
                st.download_button(
                    label="⬇️ Download ZIP Package",
                    data=zip_file,
                    file_name=os.path.basename(result_zip),
                    mime="application/zip"
                )

            # Email dispatch
            try:
                status_text.text("📧 Sending to email...")
                dispatch_email(recipient_mail, result_zip)
                st.success(f"✉️ Package sent successfully to {recipient_mail}")
            except Exception as mail_error:
                st.error(f"📧 Email delivery failed: {str(mail_error)}")

        else:
            st.error("❌ An unexpected error occurred during processing.")

    else:
        st.warning("⚠️ Please complete all required fields before proceeding.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with ❤️ using Streamlit | Audio Mixer Studio v2.0</p>",
    unsafe_allow_html=True
)
