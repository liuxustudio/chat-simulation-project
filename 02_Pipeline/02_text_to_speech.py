import json
import os

# Assuming the JSON data is loaded into a variable `dialogues`
dialogues = []
try:
    with open('talk.json', 'r') as file:
        dialogues = json.load(file)
    # print(file_content)
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")
    
from pathlib import Path
import openai
import requests







#speech_file_path = Path(__file__).parent / "speech.mp3"
#response = openai.audio.speech.create(
  # model="tts-1",
 #  voice="alloy",
 #  input="The quick brown fox jumped over the lazy dog."
# )
#response.stream_to_file(speech_file_path)
#response.with_streaming_response.method()




from openai import OpenAI
client = OpenAI()





#curl https://api.openai.com/v1/audio/transcriptions \
#-H "Authorization: Bearer $OPENAI_API_KEY" \
#   -H "Content-Type: multipart/form-data" \
# -F file="@/path/to/file/audio.mp3" \
# -F "timestamp_granularities[]=word" \
# -F model="whisper-1" \
#-F response_format="verbose_json"

# Path to save audio files
os.makedirs("../03_UI/voice", exist_ok=True)

# List to hold updated dialogue info with voice file paths
updated_dialogues = []

for index, dialogue in enumerate(dialogues):
    voice = 'onyx' if dialogue["name"] == "Salesman" else 'shimmer'
    audio_path = f"../03_UI/voice/{index:03}.wav"  # Zero-padded file numbering
    
    

    # Replace 'your_openai_api_key' with your actual OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    url = 'https://api.openai.com/v1/audio/speech'

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    data = {
        "model": "tts-1",
        "input": dialogue["message"],
        "voice": voice
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
         # Save the audio to a file
        with open(audio_path, 'wb') as file:
             file.write(response.content)
    #     print(f"Audio ({audio_path}) saved successfully.")
    else:
        print("Failed to generate audio. Status code:", response.status_code)
    #     print("Response:", response.text)

    
    # Generate word position info from audio file
    transcript = client.audio.transcriptions.create(
        file=open(audio_path, "rb"),
        model="whisper-1",
        response_format="verbose_json",
        timestamp_granularities=["word"]#jedes Wort einkommen
    )
    updated_dialogue = {
        "name": dialogue["name"],
        "voice_file": audio_path,
        "transcript": transcript.words
    }
    with open(f"../03_UI/voice/{index:03}.json", "w") as json_file:
        json.dump(updated_dialogue, json_file, indent=2)
        
        
    # Append the updated information to the list
    __dialogue = {**dialogue, "voice_file": audio_path}
    updated_dialogues.append(updated_dialogue)
    # if index == 0:
    #     break

# Save the updated dialogues to a new JSON file
with open("talk_voices.json", "w") as json_file:
    json.dump(updated_dialogues, json_file, indent=2)
