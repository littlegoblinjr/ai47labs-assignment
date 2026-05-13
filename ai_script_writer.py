from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from typing import List
import os 

class Scene(BaseModel):
    scene_number: int
    narration: str
    image_prompt: str
    duration: int
    image_path: str = ""

class StoryBoard(BaseModel):
    scenes: List[Scene]

client = ChatOpenAI(
    model = "gpt-5-nano",
    api_key = os.getenv("OPENAI_API_KEY"),
    
)

def generate_storyboard(metadata):

    structured_llm = client.with_structured_output(StoryBoard)
    response = structured_llm.invoke(f"""
You are an expert cinematic storyboard writer.

Create a storyboard for a 2-minute AI-generated movie recap video.

Movie metadata:
{metadata}

STRICT REQUIREMENTS:
- Output EXACTLY 10 scenes.
- Each scene must represent a major cinematic moment from the movie.
- Each narration must be approximately 25-35 words long.
- Narration should consist of 1-2 concise cinematic sentences.
- Narration must sound engaging, emotional, and trailer-like.
- The pacing should feel like a professional, high-energy movie recap.
- Each scene should last approximately 12 seconds.
- The total video duration MUST be 2 minutes.

IMAGE PROMPT REQUIREMENTS:
- Each image_prompt must be extremely cinematic and visually detailed.
- Describe:
  - environment
  - atmosphere
  - lighting
  - mood
  - composition
  - colors
  - cinematic style
- Focus on cinematic scenery, architecture, lighting, and atmosphere.
- Prompts should work well for AI image generation.
- Maintain visual consistency across all scenes.
- Avoid mentioning subtitles, text, logos, narration, or watermarks.
- Avoid close-up facial expressions with extreme emotions.
- Prefer wide cinematic shots over intense character closeups.
- Keep visuals visually dramatic but emotionally safe.

SAFETY REQUIREMENTS:
- Avoid graphic violence, horror, gore, blood, injury, or suffering.
- Avoid disturbing, terrifying, or psychologically intense imagery.
- Avoid words such as:
  - fear
  - despair
  - pain
  - horror
  - shock
  - eerie
  - chaotic destruction
  - disturbing
  - blinding explosion
- Use cinematic alternatives like:
  - dramatic tension
  - surreal atmosphere
  - emotional intensity
  - mysterious ambiance
  - cinematic energy
- Maintain a kids friendly cinematic movie trailer tone.
- Keep all image prompts safe for AI image generation systems.

Return ONLY structured storyboard data.

Example image_prompt:
"A surreal futuristic dream city at night, towering curved skyscrapers glowing with blue neon light, fog drifting through the streets, cinematic atmosphere, ultra detailed sci-fi movie still, dramatic lighting, wide angle composition"
""")
    return response