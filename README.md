# 🎵 Songs Mashup Generator

A fully local Streamlit application that fetches popular tracks of a chosen artist from YouTube, stitches them into a single mashup, and sends the final result straight to your email.  
This project showcases how multiple technologies can work together, including:

- Web-based UI development  
- Audio processing pipelines  
- Online media extraction  
- Email automation  
- Local-first deployment setup  

---

## 🚀 What This App Can Do

- 🎤 Look up songs using a singer's name  
- 🎶 Choose how many tracks to include (even large batches)  
- ⏱ Pick a custom clip duration per song or use full tracks  
- 🎧 Generate a mashup automatically  
- 📦 Bundle results into a ZIP file  
- 📧 Send the mashup directly via email  
- 💾 Download files manually from the interface  
- 🖥 Run everything locally without cloud limitations  

---

## 🛠 Technology Stack

| Part | Tool |
|------|------|
| UI / Frontend | Streamlit |
| YouTube Downloader | yt-dlp |
| Audio Editing | pydub |
| Email Sending | SMTP (Gmail App Password) |
| Audio Engine | FFmpeg |

---

## 🖼 Demo Preview

**Screenshot 2026-02-14 130558**

The interface comes with a clean dark theme and includes:

- Field for singer name  
- Slider to control number of songs  
- Option for custom duration or full track  
- Output file naming  
- Email sending option  
- Live audio preview  
- Download + email confirmation  

---

## 📂 Folder Layout
```
songs_mashup/
│
├── app.py              # Streamlit interface + email sending
├── mashup.py           # Downloading + audio merging logic
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```

---

## ⚙️ Setup Guide (Run Locally)

### 1️⃣ Get the Code
```bash
git clone https://github.com/AnshulKaushal27/songs_mashup.git
cd songs_mashup
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Install FFmpeg

This project needs FFmpeg for audio extraction and merging.

**Windows**

- Download from: https://www.gyan.dev/ffmpeg/builds/
- Grab the Release Full build
- Extract it
- Add the bin folder to your PATH
- Check installation:
```bash
ffmpeg -version
```

**macOS**
```bash
brew install ffmpeg
```

**Linux**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 4️⃣ Set Up Gmail App Password

The app uses Gmail SMTP to send the ZIP file.

**Steps:**

1. Turn on 2-Step Verification in your Google account
2. Create an App Password:
   - App → Mail
   - Device → Windows Computer
3. Copy the 16-character password
4. Update these in `app.py`:
```python
SENDER_EMAIL = "yourgmail@gmail.com"
APP_PASSWORD = "your_generated_app_password"
```

⚠ **Do NOT use your normal Gmail password.**

### 5️⃣ Start the App
```bash
streamlit run app.py
```

Open the local URL shown in the terminal.

---

## 🔄 Behind the Scenes (How It Works)

1. User types a singer's name
2. The app searches YouTube using yt-dlp
3. Audio is downloaded and converted to MP3 with FFmpeg
4. Selected parts are trimmed using pydub
5. Clips are merged into one mashup
6. Output is exported as:
   - .mp3
   - .zip
7. The ZIP is:
   - Available for direct download
   - Sent to the user via email

### Processing Pipeline
```
YouTube Search
    → Audio Download
    → MP3 Conversion
    → Clip Trimming
    → Merging
    → Export
    → ZIP Creation
    → Email Delivery
```

---

## ⚠️ Deployment Notes

This project is intended **only for local use**.

Some cloud platforms may restrict YouTube scraping due to IP or policy limitations.  
For demos, assignments, and learning, local execution is the safest option.

---

## 📈 Ideas for Future Upgrades

- ☑ Smooth crossfade transitions
- ☑ Audio loudness normalization
- ☑ Beat matching
- ☑ Background task processing
- ☑ Docker support
- ☑ Safer config using environment variables
- ☑ Upload-based version for cloud hosting

---

## 🎓 Educational Value

This project demonstrates real-world usage of:

- Media data extraction
- Audio signal processing
- Backend automation
- SMTP-based communication
- Interactive UI building

It can serve as a base for a more advanced music processing system.

---

## 📜 Disclaimer

This project is built for **learning and demonstration only**.  
Users are responsible for respecting YouTube's terms of service and copyright rules.

---

## 📧 Contributing

If you have ideas, find bugs, or want to improve the project, feel free to open an issue or submit a pull request.

---

## 📝 License

Released under the MIT License.
