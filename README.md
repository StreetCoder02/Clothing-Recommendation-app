# 👗 StyleMe AI – Personalized Clothing Recommendations

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Gradio](https://img.shields.io/badge/Gradio-4.44.0+-orange.svg)](https://gradio.app/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-red.svg)](https://ai.google.dev/)

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-FF7C00?style=flat&logo=huggingface)](https://huggingface.co/spaces/StreetCoder02/StyleMe-AI)

A modern Gradio web application that leverages **Google Gemini AI** to generate personalized clothing recommendations based on user profile data. The app analyzes body shape, height, gender, and clothing size to provide actionable styling advice with outfit suggestions, fit tips, color guidance, and quick styling tricks.

---

## ✨ Key Features

- **AI-Powered Recommendations**: Uses Google Gemini 2.5 Flash model for intelligent, context-aware styling advice
- **Light & Dark Mode**: Fully responsive UI with automatic theme detection and manual toggle
- **Real-Time Generation**: Instant clothing recommendations with structured advice sections
- **Example Profiles**: Pre-loaded sample inputs for quick testing and exploration
- **Input Validation**: Graceful error handling with user-friendly feedback messages
- **Production-Ready**: Environment-based configuration for secure API key management
- **Modern UI/UX**: Clean, intuitive interface with gradient styling and smooth interactions
- **Cross-Platform**: Works on Windows, macOS, and Linux

---

## 🎯 What It Does

Input your profile:
- 👤 Gender (Male, Female, Non-binary)
- 👗 Body Shape (Hourglass, Pear, Rectangle, Apple, Inverted Triangle, Athletic, Round)
- 📏 Height (cm or feet format)
- 📐 Clothing Size (XS to XXL)

Get personalized styling guidance:
1. **Best Outfit Ideas** - Tailored suggestions matching your body type
2. **Fit & Silhouette Tips** - How to flatter your unique shape
3. **Color & Pattern Suggestions** - Shades and prints that enhance your look
4. **Quick Styling Tip** - One actionable advice you can use immediately

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Gradio 4.44.0+ |
| **Backend** | Python 3.11 |
| **AI Model** | Google Gemini 2.5 Flash |
| **API Client** | google-generativeai 0.3.2+ |
| **Web Framework** | Gradio Blocks |

---

## 📋 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.11+** installed on your system
- **pip** or **conda** package manager
- **Google Gemini API Key** ([Get one free here](https://ai.google.dev/))

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/StreetCoder02/Clothing-Recommendation-app.git
cd Clothing-Recommendation-app
```

### 2. Create and Activate Virtual Environment (Recommended)

#### On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key

Create a `.env` file in the project root (use `.env.example` as a template):

```bash
cp .env.example .env
```

Then edit `.env` and add your Google Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

**Alternatively**, set it as an environment variable:

```bash
export GEMINI_API_KEY="your_api_key_here"  # macOS/Linux
set GEMINI_API_KEY=your_api_key_here      # Windows CMD
```

---

## 🎨 Running the Application

### Local Development

```bash
python Clothing_Gradio.py
```

The app will start at **http://127.0.0.1:7860**

### Custom Port

```bash
GRADIO_SERVER_PORT=8080 python Clothing_Gradio.py
```

### With Virtual Environment (Complete Setup)

```bash
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
python Clothing_Gradio.py
```

---

## 📱 Usage Guide

1. **Fill Your Profile**: Select or enter your gender, body shape, height, and clothing size
2. **Click "Generate Recommendations"**: Wait for AI to process your profile
3. **Read Your Styling Tips**: Get personalized outfit and color suggestions
4. **Try Examples**: Click the example profiles to see how the app works
5. **Toggle Theme**: Use the 🌙 Dark Mode button to switch between light/dark modes

### Example Profiles Included:
- ✨ Female, Hourglass, 168 cm, Size M
- 💼 Male, Rectangle, 5'10", Size L
- 🎭 Non-binary, Pear, 160 cm, Size S

---

## 🔐 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | ✅ Yes | Your Google Gemini API key |
| `GRADIO_SERVER_PORT` | ❌ Optional | Port number (default: 7860) |
| `PORT` | ❌ Optional | Alternative port variable for deployment |

---

## 🌐 Deployment

### Deploy to Hugging Face Spaces

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces)
2. Select **Gradio** as the Space SDK
3. Upload your repository files
4. Add `GEMINI_API_KEY` to **Repository Secrets**
5. Set `Clothing_Gradio.py` as the entry point
6. Your app will deploy automatically!

### Deploy to Other Platforms

The app works on any Python hosting platform:
- **Railway.app** - Set environment variables in dashboard
- **Heroku** - Add `Procfile` with `web: python Clothing_Gradio.py`
- **Render** - Add deploy configuration in dashboard
- **AWS Lambda** - Package with serverless framework
- **Docker** - See Docker deployment section below

---

## 🐳 Docker Deployment

### Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV GEMINI_API_KEY=""
ENV GRADIO_SERVER_PORT=7860

EXPOSE 7860

CMD ["python", "Clothing_Gradio.py"]
```

### Build and Run

```bash
docker build -t styleme-ai .
docker run -e GEMINI_API_KEY="your_key" -p 7860:7860 styleme-ai
```

---

## 📁 Project Structure

```
Clothing-Recommendation-app/
├── Clothing_Gradio.py       # Main application entry point
├── requirements.txt          # Python dependencies
├── runtime.txt              # Python version specification
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

---

## 🎯 How It Works

### AI Prompting Strategy

The app uses a sophisticated system prompt that:

1. **Establishes Context**: Frames the AI as an expert fashion stylist
2. **Profiles the User**: Analyzes body type, height, and size data
3. **Structures Output**: Requests specific sections (outfits, fit, colors, tips)
4. **Ensures Tone**: Keeps advice respectful, practical, and actionable

### Code Flow

```
User Input → Validation → Prompt Generation → Gemini API Call → Response Processing → Display Output
```

---

## 🔧 Customization

### Change AI Model

Edit line 13 in `Clothing_Gradio.py`:

```python
MODEL_NAME = "gemini-2.5-flash"  # Change to other models
```

Available models: `gemini-pro`, `gemini-1.5-flash`, `gemini-1.5-pro`

### Modify Body Shape Options

Edit the body shape dropdown in `Clothing_Gradio.py`:

```python
body_shape = gr.Dropdown(
    ["Your", "Custom", "Shapes", "Here"],
    label="Body Shape"
)
```

### Adjust App Title & Subtitle

```python
APP_TITLE = "Your Custom Title"
APP_SUBTITLE = "Your custom subtitle here"
```

---

## ⚠️ Limitations & Known Issues

- **API Rate Limiting**: Google Gemini has usage limits (check your plan)
- **Deprecated Library**: `google-generativeai` is deprecated; consider migrating to `google-genai` in future
- **Cold Start**: First request may take 2-3 seconds
- **Internet Required**: Cannot work offline (requires API connection)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙋 Support & Questions

- 📖 **Gradio Docs**: https://gradio.app/docs
- 🤖 **Google Gemini API**: https://ai.google.dev/
- 🐛 **Report Issues**: Open an issue on GitHub
- 💬 **Discussions**: Start a discussion for questions

---

## 🌟 Acknowledgments

- [Gradio](https://gradio.app/) - Beautiful web UI framework
- [Google AI Studio](https://ai.google.dev/) - Gemini API access
- [Python](https://www.python.org/) - Amazing programming language

---

<div align="center">

**Made with ❤️ for fashion enthusiasts and tech lovers**

[⭐ Star this repo](https://github.com/StreetCoder02/Clothing-Recommendation-app) if you found it helpful!

</div>
