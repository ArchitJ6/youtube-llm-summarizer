# 📺 YouTube LLM Summarizer  

### 🚀 AI-powered YouTube Video Summarization with Streamlit  

This project extracts transcripts from YouTube videos using **YouTubeTranscriptAPI** or **Whisper**, then summarizes them using **Groq's LLM**. The app is built with **Streamlit** and runs in a **Dockerized environment** for easy deployment.  

---

## 🚀 Features  
✅ Extracts YouTube transcripts automatically  
✅ Uses **Whisper** for speech-to-text if transcripts are unavailable  
✅ Summarizes content using **Groq LLM**  
✅ Provides a simple **Streamlit UI** for easy interaction  
✅ **Dockerized** for seamless deployment  

---

## 📂 Project Structure  

```
📁 youtube-llm-summarizer  
│── 📄 app.py               # Streamlit UI for summarization  
│── 📄 summarizer.py        # Core logic for transcript extraction & summarization  
│── 📄 Dockerfile           # Docker configuration  
│── 📄 docker-compose.yml   # Docker Compose setup  
│── 📄 .env                 # Environment variables  
│── 📄 requirements.txt     # Python dependencies  
│── 📁 temp/                # Temporary storage for audio files
```

---

## 🛠️ Installation & Setup  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/ArchitJ6/youtube-llm-summarizer.git
cd youtube-llm-summarizer
```

### 2️⃣ **Set Up Environment Variables**  
Create a `.env` file in the root directory and add your API keys:  
```
GROQ_API_KEY=your_groq_api_key
```

### 3️⃣ **Run with Docker Compose**  
```sh
docker-compose up --build
```
This will:
- Pull the necessary dependencies  
- Set up the Streamlit app in a container  
- Run the app on **http://localhost:8501**  

---

## 🎬 How to Use  
1. Open **http://localhost:8501**  
2. Enter a **YouTube video URL**  
3. Click **"Summarize"**  
4. View the **generated summary**  

---

## 📦 Running Without Docker  
If you prefer to run locally:  
```sh
pip install -r requirements.txt
streamlit run app.py
```

---

## 🛠️ Built With  
- **Python** 🐍  
- **Streamlit** 📊  
- **YouTubeTranscriptAPI** 🎥  
- **Whisper** 🎙️  
- **Groq LLM** 🧠  
- **Docker & Docker Compose** 🐳  

---

## 📝 License  
This project is licensed under the [MIT License](LICENSE).