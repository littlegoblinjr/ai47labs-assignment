# ✨ AI Movie Recap Generator (AI47 Labs)

An automated production pipeline that transforms any IMDB URL into a high-quality, cinematic 2-minute movie recap video. 

This project orchestrates local LLMs, AI image generation, and offline Text-to-Speech to create professional-grade content with minimal human intervention.

## 🚀 Overview

The **AI Movie Recap Generator** handles the entire creative process:
1. **Scraping & Metadata**: Extracts movie details from IMDB/OMDB.
2. **Scripting**: Uses GPT-5-Nano to write a 10-scene cinematic storyboard.
3. **Visuals**: Generates high-fidelity images based on AI-generated prompts.
4. **Audio**: Converts the script into narration using stable offline TTS.
5. **Editing**: Stitches all assets into a final `.mp4` with cinematic zooms and transitions.

## 🛠️ Tech Stack

- **Orchestration**: Python (ThreadPoolExecutor for parallel processing)
- **Intelligence**: 
  - **Scripting**: GPT-5-Nano (State-of-the-art Storyboard Generation)
  - **Image Generation**: OpenAI-compatible local/cloud API (gpt-image-1)
- **Media Processing**: 
  - **Video**: MoviePy (v2.0+)
  - **Audio**: pyttsx3 (SAPI5 for Windows)
- **Metadata**: OMDB API
- **Workflow**: LangChain, Pydantic, Dotenv

## 📂 Project Structure

```text
AI47Labs/
├── main.py                    # Main pipeline orchestrator
├── ai_script_writer.py        # LLM logic for storyboard & narration
├── image_generator.py         # AI image generation client
├── tts.py                     # Offline text-to-speech engine
├── stitcher.py                # MoviePy video editing logic
├── OMDB_metadata_extraction.py# Movie data fetching
├── IMDB_url_extraction.py     # URL parsing utilities
├── scene_images/              # Generated visuals (artifacts)
├── scene_audios/              # Generated narrations (artifacts)
└── movie_recap.mp4            # Final output 🎬
```

## ⚙️ Setup & Installation

### 1. Prerequisites
- **Python 3.9+**
- **FFmpeg** (Required by MoviePy)
- **Local LLM Server** (Optional: LM Studio or Ollama running on `http://127.0.0.1:1234`)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/your-repo/ai47labs.git
cd ai47labs

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory:
```env
OMDB_API_KEY=your_omdb_key_here
OPENAI_API_KEY=your_api_key_here
```

## 📽️ Usage

1. **Start your local LLM server** (e.g., LM Studio) ensure it's hosting the model on Port 1234.
2. **Run the main pipeline**:
   ```bash
   python main.py
   ```
3. **Follow the prompt**: Enter a valid IMDB movie URL when requested.
4. **Check the output**: The final video will be saved as `movie_recap.mp4`.

## 🎨 Creative Constraints
The pipeline is pre-configured with strict cinematic requirements:
- **Exactly 10 Scenes**: Ensuring a consistent runtime of 2 minutes.
- **Visual Consistency**: Prompts are engineered for cinematic wide shots and atmospheric lighting.
- **Safety**: Built-in prompt filters for "kids-friendly" content (avoiding gore/violence).
- **Cinematic Pacing**: Each scene includes a subtle digital zoom (Ken Burns effect) and 1-second cross-fades.

## 📝 License
Proprietary - Developed for AI47 Labs.

---

