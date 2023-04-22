import openai
import json
import os
from dotenv import load_dotenv
from update_Json_Array import add_to_json_array

load_dotenv()

# Authenticate OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")


# Define the function
def generate_json(speaker_name, content):

    # Define the members present in the podcast
    jeff = "Jeff Bezoz"
    elon = "Elon Musk"
    jobs = "Steve Jobs"
    members = ["Jeff Bezoz", "Elon Musk", "Steve Jobs"]

    # Use OpenAI to determine the appropriate look_at value
    prompt = f"Speaker: {speaker_name}\nContent: {content}\n"
    prompt += f"Which member of the podcast should the speaker direct their gaze towards? based on the statement: {content} "
    prompt += f"Members present: {' '.join([m for m in members if m != speaker_name])}\n"
    prompt += "Just five the name of the Member"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        stop=None,
        temperature=0.5,
    )
    look_at = response.choices[0].text.strip()

    # Use OpenAI to determine the appropriate animation
    prompt = f"Speaker: {speaker_name}\nContent: {content}\n"
    prompt += f"Who should the speaker look at while saying this: {look_at}\n"
    prompt += "Which animation should be played from among sitting, idle, pointing, angry, sad?"
    prompt += "give the response in one word"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    animation = response.choices[0].text.strip()

    # Create the JSON file
    data = {
        "speaker": speaker_name,
        "content": content,
        "lookAt": look_at,
        "animation": animation
    }



    # Return the JSON data
    return data
