import openai
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Authenticate OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def jsonBuilder(speaker_name, content):
    members = ["jeff", "elon", "jobs"]

    prompt = "Return a json with following 4 parts\n"
    prompt += f"Speaker: {speaker_name}\n"
    prompt += f"Content: {content}\n"
    prompt += f"lookAt : Which member of the podcast should the speaker direct their gaze towards based on the Content value? Members present: {' '.join([m for m in members if m != speaker_name])}. just one word response\n"
    prompt += f"animation: Which animation should be played based on the Content value, out of the following sitting, idle, pointing, angry, sad? Just one word response."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        stop=None,
        temperature=0.5,
    )

    data = response.choices[0].text.strip()

    with open("podcast.json", "w") as outfile:
        json.dump(data, outfile)

    # Return the JSON data
    return data

print(jsonBuilder("jeff", "what are your thoughts on spaceX"))