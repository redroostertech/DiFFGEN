import openai
import utiliities

def generate_openai_reponse(prompt):
    """
    Generate a OpenAI response.
    """
        
    openai.api_key = utiliities.openai_api_key
    response = openai.Completion.create(
        engine = utiliities.openai_engine,
        prompt = prompt,
        max_tokens = 60
    )

    return response.choices[0].text.strip()
