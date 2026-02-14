import os
import streamlit as st
import yt_dlp
from pydub import AudioSegment
import zipfile
import tempfile
import smtplib
from email.message import EmailMessage
import shutil

# ========================= CONFIGURATION =========================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_EMAIL = "parralexpie@gmail.com"
EMAIL_APP_PASSWORD = "wkfp qytg woeu tpai"

# ========================= CORE FUNCTIONS =========================

def search_and_download_tracks(artist, track_count, temp_directory):
    """Search YouTube and download audio tracks for the specified artist"""
    download_folder = os.path.join(temp_directory, "audio_files")
    os.makedirs(download_folder, exist_ok=True)
    
    config = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'quiet': True,
        'noplaylist': True,
        'ignoreerrors': True,
        'geo_bypass': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        },
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    
    query = f"{artist} official song -remix -cover -karaoke"
    
    with yt_dlp.YoutubeDL(config) as downloader:
        downloader.download([f"ytsearch{track_count}:{query}"])
    
    return download_folder


def merge_audio_clips(audio_folder, clip_duration, output_name, temp_directory):
    """Merge multiple audio files into a single mashup"""
    combined = AudioSegment.empty()
    track_count = 0
    
    audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.mp3')]
    
    if not audio_files:
        return None, None, "Failed to download any audio tracks"
    
    for filename in audio_files:
        filepath = os.path.join(audio_folder, filename)
        audio_clip = AudioSegment.from_mp3(filepath)
        
        if clip_duration > 0:
            audio_clip = audio_clip[:clip_duration * 1000]
        
        combined += audio_clip
        track_count += 1
    
    # Export merged audio
    output_mp3_path = os.path.join(temp_directory, f"{output_name}.mp3")
    combined.export(output_mp3_path, format="mp3")
    
    # Create ZIP archive
    output_zip_path = os.path.join(temp_directory, f"{output_name}.zip")
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.write(output_mp3_path, os.path.basename(output_mp3_path))
    
    return output_mp3_path, output_zip_path, None


def generate_music_mashup(artist_name, number_of_tracks, segment_duration, file_name):
    """Main function to create a music mashup"""
    try:
        workspace = tempfile.mkdtemp()
        
        audio_folder = search_and_download_tracks(artist_name, number_of_tracks, workspace)
        
        mp3_output, zip_output, error_msg = merge_audio_clips(
            audio_folder, 
            segment_duration, 
            file_name, 
            workspace
        )
        
        return mp3_output, zip_output, error_msg
        
    except Exception as error:
        return None, None, f"Error occurred: {str(error)}"


def dispatch_email(recipient, attachment_path):
    """Send the mashup file via email"""
    email = EmailMessage()
    email['Subject'] = "Your Music Mashup is Ready! 🎵"
    email['From'] = SENDER_EMAIL
    email['To'] = recipient
    
    email.set_content(
        "Hello!\n\n"
        "Your custom music mashup has been created successfully.\n"
        "Please find the attached file.\n\n"
        "Enjoy your music!\n\n"
        "Best regards,\n"
        "Music Fusion Team"
    )
    
    with open(attachment_path, 'rb') as attachment:
        content = attachment.read()
        filename = os.path.basename(attachment_path)
    
    email.add_attachment(
        content,
        maintype='application',
        subtype='zip',
        filename=filename
    )
    
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, EMAIL_APP_PASSWORD)
        server.send_message(email)


# ========================= UI CONFIGURATION =========================

st.set_page_config(
    page_title="Music Fusion Studio",
    page_icon="🎧",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    .stApp {
        background: transparent;
    }
    
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.95);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }
    
    h1 {
        color: #ffffff;
        text-align: center;
        font-size: 3.5rem;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #ffffff;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .stTextInput > label, .stSlider > label, .stRadio > label {
        color: #4a5568;
        font-weight: 600;
        font-size: 1rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 700;
        font-size: 1.2rem;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    .stDownloadButton > button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        font-weight: 600;
        border-radius: 50px;
        border: none;
        padding: 0.75rem 2rem;
        width: 100%;
    }
    
    .stAlert {
        border-radius: 10px;
        border-left: 5px solid;
    }
    
    .feature-box {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ========================= MAIN UI =========================

st.markdown("<h1>🎧 Music Fusion Studio</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Create Amazing Audio Mashups in Seconds</p>", unsafe_allow_html=True)

with st.form("mashup_generator_form"):
    st.markdown("### 🎵 Mashup Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        artist_input = st.text_input(
            "Artist Name",
            placeholder="e.g., Taylor Swift, Ed Sheeran",
            help="Enter the name of your favorite artist"
        )
    
    with col2:
        track_count = st.slider(
            "Number of Songs",
            min_value=1,
            max_value=25,
            value=6,
            help="How many songs to include in the mashup"
        )
    
    duration_mode = st.radio(
        "Audio Length Mode",
        options=["Custom Clip Duration", "Use Complete Songs"],
        horizontal=True,
        help="Choose whether to use full songs or just clips"
    )
    
    if duration_mode == "Custom Clip Duration":
        clip_length = st.slider(
            "Clip Duration (seconds)",
            min_value=5,
            max_value=60,
            value=15,
            step=5,
            help="Duration of each song clip in the mashup"
        )
    else:
        clip_length = 0
    
    st.markdown("### 📁 Output Settings")
    
    col3, col4 = st.columns(2)
    
    with col3:
        output_name = st.text_input(
            "File Name",
            value="my_mashup",
            help="Name for your mashup file"
        )
    
    with col4:
        recipient_email = st.text_input(
            "Email Address",
            placeholder="your.email@example.com",
            help="Receive the mashup file in your inbox"
        )
    
    submit_button = st.form_submit_button("🎵 Create Mashup", use_container_width=True)

# ========================= PROCESSING =========================

if submit_button:
    if not artist_input or not output_name or not recipient_email:
        st.warning("⚠️ Please fill in all required fields")
    elif "@" not in recipient_email or "." not in recipient_email:
        st.error("❌ Please enter a valid email address")
    else:
        progress_container = st.container()
        
        with progress_container:
            with st.spinner("🎵 Searching and downloading tracks..."):
                mp3_file, zip_file, error = generate_music_mashup(
                    artist_input,
                    track_count,
                    clip_length,
                    output_name
                )
            
            if error:
                st.error(f"❌ {error}")
            
            elif mp3_file and os.path.exists(mp3_file):
                st.success("✅ Mashup created successfully!")
                
                st.markdown("### 🎧 Preview Your Mashup")
                st.audio(mp3_file, format='audio/mp3')
                
                col5, col6 = st.columns(2)
                
                with col5:
                    with open(zip_file, "rb") as file:
                        st.download_button(
                            label="📥 Download ZIP",
                            data=file,
                            file_name=os.path.basename(zip_file),
                            mime="application/zip",
                            use_container_width=True
                        )
                
                with col6:
                    if st.button("📧 Send via Email", use_container_width=True):
                        try:
                            with st.spinner("Sending email..."):
                                dispatch_email(recipient_email, zip_file)
                            st.success("✅ Email sent successfully!")
                        except Exception as email_error:
                            st.error(f"❌ Email failed: {str(email_error)}")
            
            else:
                st.error("❌ An unexpected error occurred while creating the mashup")

# ========================= FOOTER =========================

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: white; opacity: 0.7;'>"
    "Made with ❤️ by Music Fusion Studio | © 2026"
    "</p>",
    unsafe_allow_html=True
)
