# 🎵 Audio Mashup Studio

An intelligent desktop application that creates seamless audio mashups by fetching tracks from YouTube, processing them locally, and delivering your custom mix straight to your inbox.

---

## 📸 Application Preview

### Main Interface
![Application Dashboard](path/to/screenshot1.png)
*Caption: Clean and intuitive user interface for creating mashups*

### Mashup Creation Process
![Processing View](path/to/screenshot2.png)
*Caption: Real-time progress tracking during audio generation*

### Email Delivery Confirmation
![Email Success](path/to/screenshot3.png)
*Caption: Automatic delivery notification with download option*

---

## ✨ Core Capabilities

- **Artist-Based Search**: Input any artist name to fetch their popular tracks
- **Flexible Track Selection**: Choose anywhere from 5 to 50+ songs
- **Customizable Duration**: Set specific clip length or use full tracks
- **Intelligent Audio Merging**: Seamless concatenation with quality preservation
- **Dual Delivery System**: Both email dispatch and in-app download
- **Zero Cloud Dependencies**: Runs entirely on your local machine

---

## 🏗️ Architecture Stack

| Layer | Implementation |
|-------|---------------|
| User Interface | Streamlit Framework |
| Video Extraction | yt-dlp Library |
| Audio Manipulation | pydub + FFmpeg Engine |
| Mail Transport | SMTP with Gmail Integration |
| Processing Backend | Python 3.8+ |

---

## 📁 Repository Structure
```
audio-mashup-studio/
│
├── app.py                 # Main Streamlit application
├── mashup.py              # Core processing engine
├── requirements.txt       # Dependency specifications
├── .gitignore            # Version control exclusions
└── README.md             # Documentation (this file)
```

---

## 🔧 Local Setup Instructions

### Step 1: Repository Acquisition
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Step 2: Python Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: FFmpeg Installation

**For Windows Users:**
1. Visit [FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/)
2. Download the "release full" build
3. Extract to `C:\ffmpeg`
4. Add `C:\ffmpeg\bin` to System PATH
5. Verify: `ffmpeg -version`

**For macOS Users:**
```bash
brew install ffmpeg
```

**For Linux Users:**
```bash
sudo apt update && sudo apt install ffmpeg -y
```

### Step 4: Email Configuration

The application uses Gmail's SMTP server for delivery:

1. Enable **2-Factor Authentication** on your Google Account
2. Navigate to [App Passwords](https://myaccount.google.com/apppasswords)
3. Generate new app password:
   - Select **Mail** as the app
   - Select **Other** as the device
   - Name it "Mashup Studio"
4. Copy the 16-character password
5. Update credentials in `app.py`:
```python
SENDER_EMAIL = "your.email@gmail.com"
APP_PASSWORD = "xxxx xxxx xxxx xxxx"  # Your app password
```

> ⚠️ **Security Note**: Never commit credentials to version control

### Step 5: Launch Application
```bash
streamlit run app.py
```

Access the interface at `http://localhost:8501`

---

## 🎯 Usage Workflow

1. **Enter Artist Name** → System queries YouTube catalog
2. **Select Parameters** → Number of tracks + clip duration
3. **Generate Mashup** → Processing begins automatically
4. **Preview Result** → Built-in audio player
5. **Download/Email** → Choose delivery method

---

## ⚙️ Processing Pipeline
```
Artist Query → YouTube API Search → Stream Download → 
Audio Extraction → Format Conversion → Segment Cutting → 
Track Merging → Quality Optimization → Archive Creation → 
Email Dispatch
```

---

## 🚀 Future Roadmap

- [ ] Audio crossfade transitions
- [ ] Volume normalization across tracks
- [ ] BPM detection and tempo matching
- [ ] Visual waveform display
- [ ] Playlist import from Spotify/Apple Music
- [ ] Docker containerization
- [ ] Environment variable management
- [ ] Multi-format export (WAV, FLAC, OGG)

---

## 💡 Why Local Deployment?

Cloud platforms often impose restrictions on:
- YouTube content scraping
- Large file processing
- SMTP authentication
- Long-running processes

This application is optimized for **local execution** to ensure:
- ✅ Unrestricted access to media sources
- ✅ Full processing control
- ✅ Privacy and data security
- ✅ No rate limiting

---

## 📚 Learning Outcomes

This project demonstrates practical skills in:
- Web scraping and API interaction
- Digital audio signal processing
- Asynchronous task management
- Email protocol implementation
- Modern Python web frameworks

---

## ⚖️ Legal Considerations

**Educational Purpose Statement:**

This tool is developed for academic demonstration and personal learning. Users are responsible for:
- Respecting copyright laws
- Adhering to YouTube's Terms of Service
- Using content within fair use guidelines
- Obtaining proper licenses for commercial use

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

## 📬 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/issues)
- **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/discussions)

---

## 📄 License

Released under the MIT License - see [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with passion for audio engineering and automation** 🎧

⭐ Star this repo if you found it helpful!

</div>
