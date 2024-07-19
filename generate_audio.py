from gtts import gTTS
import os

def text_to_speech(text, lang='en', output_file='output/audio.mp3'):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    print(f"Audio saved to {output_file}")

if __name__ == "__main__":
    with open('scripts/video_script.txt', 'r') as file:
        script = file.read()

    text_to_speech(script)
