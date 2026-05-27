import json


def update_transcript(full_talk, splitted_transcript):
    for talk, transcript in zip(full_talk, splitted_transcript):
        # Tokenize the sentence while keeping punctuation
        words = [w.strip() for w in talk["message"].split()]
        trans_words = transcript["transcript"]
        
        # Correct capitalization and punctuation
        for word_obj, word_talk in zip(trans_words, words):
            word_obj["word"] = word_talk

    return splitted_transcript

with open(f"talk.json", "r") as file:
    full_talk = json.load(file)
with open(f"talk_voices.json", "r") as file:
    splitted_transcript = json.load(file)
    

# Update the transcript based on full_talk
updated_splitted_transcript = update_transcript(full_talk, splitted_transcript)

#print(json.dumps(updated_splitted_transcript, indent=2))


# Save the updated dialogues to a new JSON file
with open("talk_voices_refined.json", "w") as json_file:
    json.dump(updated_splitted_transcript, json_file, indent=2)