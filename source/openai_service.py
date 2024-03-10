from openai import OpenAI
import environment_manager
import prompt_manager

client = OpenAI()

def generate_openai_reponse(prompt):
    """
    Generate a OpenAI response.
    """
    prompt_path = "source/role_description.txt"
    system_content = prompt_manager.load_prompt_from_file(prompt_path)

    if not system_content:
        return print(f"Prompt '{prompt_path}' not found.")
    
    response = client.chat.completions.create(
        model= environment_manager.openai_engine,
        temperature = 0.2,
        messages = [
            {
                "role": "system",
                "content": system_content
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
