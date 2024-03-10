import environment_manager
import os

def load_prompt_from_file(file_path):
    """
    Loads the prompt text from a specified file.
    """
    with open(file_path, 'r') as file:
        return file.read()
    
def prompt_for_chunk_analysis(context, chunk):
    return (f"{context}\n\n"
            "Analyze the following code changes. Generate a concise, informative commit message that "
            "summarizes these key changes.\n\n"
            "Code Changes:\n"
            f"{chunk}\n\n"
            "Commit message:")

def prompt_for_summary(context):
    return (f"Based on the detailed analyses of code changes, please consolidate the key findings into a summarized commit message. The summary should be presented in a bulleted list, "
            "capturing the essence of the changes in a clear and concise manner. Focus on highlighting the most significant aspects of the changes, including their purpose and impact. "
            f"Analyses:\n\n{context}"
            "Generate a summarized commit message in bullet points:")