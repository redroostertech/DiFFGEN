import diff_manager
import environment_manager
import openai_service
import prompt_manager
import pyperclip
import utiliities

def generate_commit_message_v1(diff, context):
    """
    Generate a commit message using OpenAI's API based on the diff and a given context.
    """
    if not diff:
        return "No changes staged for commit"
    
    # Filter the diff to include only additions and removals
    filtered_diff = diff_manager.filter_diff_additions_removals(diff)
    
    # Truncate the diff and context if they're too long
    max_diff_length = 4000 - len(context)  # Reserve space for context
    truncated_diff = (filtered_diff[:max_diff_length] + '...') if len(filtered_diff) > max_diff_length else filtered_diff

    # Combine the context with the diff data
    prompt_text = f"{context}\n\nCode Changes:\n{truncated_diff}\n\nCommit message:"

    return openai_service.generate_openai_reponse(prompt_text)

def analyze_diff(diff, context):
    """
    Generate a commit message using OpenAI's API based on the diff and a given context.
    """
    if not diff:
        return "No changes staged for commit"

    # Filter the diff to include only additions and removals
    filtered_diff = diff_manager.filter_diff_additions_removals(diff)

    # Split diff into smaller chunks
    max_chunk_length = 1000  # Adjust as needed
    diff_chunks = diff_manager.split_diff_into_chunks(filtered_diff, max_chunk_length)
    total_chunks = len(diff_chunks)

    print(f"Processing {total_chunks} chunks...")

    summaries = []
    for i, chunk in enumerate(diff_chunks, 1):
        print(f"Processing chunk {i}/{total_chunks}...")
        message = process_chunk(chunk, context)
        chunk_summary = summarize_text(message)
        summaries.append(chunk_summary)

    combined_summary = '\n'.join(summaries)
    return combined_summary

def process_chunk(chunk, context):
    """
    Generate a commit message for a single chunk of diff using OpenAI's API.
    """
    if not chunk:
        return "No changes staged for commit"

    # Create the prompt with specific instructions for the AI
    prompt_text = prompt_manager.prompt_for_chunk_analysis(context, chunk)

    return openai_service.generate_openai_reponse(prompt_text)

def summarize_text(text):
    """
    Summarizes the given text into bullet points using OpenAI's GPT model.
    """
    prompt_text = prompt_manager.prompt_for_summary(text)

    return openai_service.generate_openai_reponse(prompt_text)

def display_commit_message(commit_message): 
    print("""
##############################################################
######                                                  ######
######  DiFFGEN Commit Message Generator                ######	
######                                                  ######        													
######  Author: Michael Westbrooks                      ######				
######  Contact: michael.westbrooks@redroostertec.com   ######	
######                                                  ######
##############################################################
        
Thank you for using this script, a valuable tool 
designed to enhance your development 
workflow. 

This script leverages OpenAI's GPT model to 
automate the creation of meaningful commit 
messages from your staged Git changes. It's a 
time-saving solution that ensures clarity and 
consistency in your project's history, easily 
integrating with your existing version control
tools. 

We appreciate your choice to adopt this script 
and look forward to your valuable feedback as 
we continually strive to improve its effectiveness 
for developers like you.

See the generated message below:

""" + commit_message + """

This message has been copied to your clipboard.   
          """)

def main():
    prompt_path = environment_manager.prompt_path
    context = prompt_manager.load_prompt_from_file(prompt_path)

    if not context:
        return print(f"Prompt '{prompt_path}' not found.")

    dir_name = "sample-repo"
    repo_path = utiliities.find_directory(dir_name)

    if not repo_path:
        return print(f"Directory '{dir_name}' not found.")

    diff = diff_manager.get_staged_diff(repo_path)
    commit_message = analyze_diff(diff, context)

    pyperclip.copy(commit_message)
    display_commit_message(commit_message)

if __name__ == "__main__":
    main()