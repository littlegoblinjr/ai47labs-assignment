import pyttsx3
import os
import time

def text_to_speech(storyboard):
    """Generates audio for each scene in the storyboard and saves them as separate files."""
    
    # Create a directory for scene audios
    output_dir = "scene_audios"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("\n--- Generating Scene-wise Audio ---")
    
    # Safety limit: only process the first 10 scenes
    for i, scene in enumerate(storyboard.scenes[:10], 1):
        scene_id = getattr(scene, 'scene_number', i)
        # Using .wav instead of .mp3 as it's often significantly faster and more stable for SAPI5
        filename = os.path.join(output_dir, f"scene_{scene_id}.wav")
        
        # Clean text to ensure no weird characters confuse the engine
        clean_text = scene.narration.encode('ascii', 'ignore').decode('ascii')
        
        print(f"Processing Scene {scene_id} ({len(clean_text.split())} words)...")
        
        try:
            # Explicitly use sapi5 for Windows stability
            engine = pyttsx3.init('sapi5')
            engine.setProperty('rate', 150)
            
            engine.save_to_file(clean_text, filename)
            engine.runAndWait()
            
            # Explicitly force destruction of the engine object
            del engine
            
            print(f"Done! Saved Scene {scene_id} as WAV.")
            
            # Small delay to allow the OS to release the file and audio driver
            time.sleep(1.5)
            
        except Exception as e:
            print(f"Error on Scene {scene_id}: {e}")

    print(f"\nSuccess! All audio files saved in the '{output_dir}' directory as WAV files.")
    

