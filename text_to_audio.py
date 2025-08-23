
import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs


 
client = ElevenLabs(
    api_key="sk_c36f0a0c1b6833573358c9a8fdfcd751d5e526182f6cb92b",
)


def text_to_speech_file(text: str, folder: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_v3", # use the turbo model for low latency
        # Optional voice settings that allow you to customize the output
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    # uncomment the line below to play the audio back
    # play(response)

    # Generating a unique file name for the output MP3 file
    save_file_path = os.path.join(f"user_uploads/{folder}", "audio.mp3")

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path


#text_to_speech_file("Hey I am a good boy and its the python course", "24fff8d4-7de9-11f0-a8ad-fc349796c5ae")