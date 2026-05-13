from IMDB_url_extraction import extract_imdb_id
from OMDB_metadata_extraction import get_omdb_metadata
from dotenv import load_dotenv
from tts import text_to_speech
from ai_script_writer import generate_storyboard
from image_generator import generate_image
import os
from stitcher import stitch_video
from concurrent.futures import ThreadPoolExecutor, as_completed

load_dotenv()

def process_scene(scene):

    # Generate image

    
    image_filename = os.path.join(
        "scene_images",
        f"scene_{scene.scene_number}.jpg"
    )

    generate_image(
        scene.image_prompt,
        image_filename
    )

    scene.image_path = image_filename

    # Generate audio
    

    return scene.scene_number

def main():
    url = input("Enter the IMDB URL: ")
    imdb_id = extract_imdb_id(url)
    print(imdb_id)
    if imdb_id:
        metadata = get_omdb_metadata(imdb_id)
        print(metadata)

        # Stop if metadata retrieval failed or ID doesn't match
        if metadata.get("Response") == "False":
            print(f"OMDB Error: {metadata.get('Error', 'Could not retrieve metadata')}")
            return

        if metadata.get("imdbID") != imdb_id:
            print(f"Security/Match Error: Extracted ID {imdb_id} does not match OMDB ID {metadata.get('imdbID')}")
            return

        storyboard = generate_storyboard(metadata)
        print(storyboard)
        output_dir = "scene_images"
        os.makedirs(output_dir, exist_ok=True)
        

        
        text_to_speech(storyboard)   

        with ThreadPoolExecutor(max_workers = 1) as executor:
            futures = [executor.submit(process_scene, scene)
            

            for scene in storyboard.scenes]

            
        
        print("\n--- Generating Movie Recap Video ---")
        
        # Create video from scenes
        video_path = stitch_video()
        
        print(f"\nSuccess! Movie recap video saved as: {video_path}")
            
            
        


    else:
        print("Invalid IMDB URL")

    

if __name__ == "__main__":
    main()
    