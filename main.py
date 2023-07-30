from fastapi import FastAPI
from pydantic import BaseModel
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

app = FastAPI()

anthropic = Anthropic(api_key="my api key") # replace with your actual key

class Profile(BaseModel):
    name: str
    interests: str
    location: str
    # add other fields as needed

@app.post("/match")
async def match_profiles(profile: Profile):
    # Here you might want to do some processing on the profile data to formulate a suitable prompt.
    # This is a simplistic example where we just ask Claude-2 for a suitable match based on the interests.
    prompt = f"{HUMAN_PROMPT} Who would be a suitable match for a person interested in {profile.interests}? {AI_PROMPT}"

    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=300,
        prompt=prompt,
    )
    return {"match": completion.completion}
