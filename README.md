# 🎵 Songs Mashup Generator

Songs Mashup Generator is a locally running Streamlit application that creates a custom music mashup using multiple songs from a selected singer. The app fetches audio from YouTube, processes and merges tracks, packages the result, and can send the final mashup directly to your email.

This project is built to demonstrate the practical use of:
- Interactive web interfaces  
- Audio processing with Python  
- YouTube media extraction  
- Automated email delivery  
- Fully local deployment workflow  

---

## 🚀 Key Features

- 🔍 Search songs using a singer’s name  
- 🎚 Choose how many tracks to include (supports large collections)  
- ⏱ Set custom duration per song or use full-length tracks  
- 🎧 Automatic mashup creation  
- 📦 Export output as MP3 and ZIP  
- 📩 Send mashup to email automatically  
- 💾 Download files directly from the app  
- 🖥 Runs completely on your local machine  

---

## 🛠 Technology Stack

| Component | Technology |
|----------|------------|
| Frontend / UI | Streamlit |
| YouTube Downloader | yt-dlp |
| Audio Processing | pydub |
| Audio Engine | FFmpeg |
| Email Service | SMTP (Gmail App Password) |

---

## 🖼 Screenshots / Demo

> 📌 Paste your screenshots here

Example:
- `![Home Screen](screenshots/home.png)`
- `![Mashup Output](screenshots/output.png)`
- `![Email Sent](screenshots/email.png)`

(Replace these with your own screenshots)

---

## 📂 Project Structure

songs_mashup/
│
├── app.py # Streamlit interface + email handling
├── mashup.py # YouTube download + audio merge logic
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AnshulKaushal27/songs_mashup.git
cd songs_mashup
2️⃣ Install Python Dependencies
pip install -r requirements.txt
3️⃣ Install FFmpeg
FFmpeg is required for audio conversion and merging.

Windows

Download from: https://www.gyan.dev/ffmpeg/builds/

Download “Release Full”

Extract the files

Add the bin folder to your system PATH

Verify installation:

ffmpeg -version
macOS

brew install ffmpeg
Linux

sudo apt update
sudo apt install ffmpeg
4️⃣ Configure Gmail App Password
This project uses Gmail SMTP to send the mashup ZIP file.

Steps:

Enable 2-Step Verification in your Google account

Generate an App Password

App → Mail

Device → Windows Computer

Copy the generated 16-character password

Update these values inside app.py:

SENDER_EMAIL = "yourgmail@gmail.com"
APP_PASSWORD = "your_generated_app_password"
⚠️ Do NOT use your normal Gmail password.

5️⃣ Run the Application
python -m streamlit run app.py
Open the local URL shown in the terminal.

🔄 How the System Works
User enters a singer’s name

The app searches YouTube using yt-dlp

Audio is downloaded and converted to MP3 using FFmpeg

Each track is trimmed (or kept full length)

All clips are merged using pydub

Final output is created as:

.mp3

.zip

The ZIP file is:

Available for direct download

Sent to the user via email

🧠 Processing Pipeline
YouTube Search
   → Audio Download
      → MP3 Conversion
         → Audio Trimming
            → Track Merging
               → Export File
                  → ZIP Packaging
                     → Email Delivery
⚠️ Deployment Notes
This project is intended for local use only.

Some cloud platforms may block YouTube downloads due to network or policy restrictions, such as:

Render

Railway

Streamlit Cloud

For reliable operation and demonstrations, local execution is recommended.

📈 Possible Improvements
Smooth crossfade between tracks

Audio loudness normalization

Beat matching

Background task processing

Docker support

Secure environment variable setup

Upload-based version for cloud deployment

🎓 Academic / Learning Purpose
This project demonstrates real-world integration of:

Media data extraction

Audio signal processing

Backend automation

Email communication

Interactive UI development

It can be expanded into a more advanced music processing system.

📜 Disclaimer
This project is created for educational and demonstration purposes only.
Users are responsible for following YouTube’s terms of service and copyright regulations.

📝 License
This project is distributed under the MIT License.

