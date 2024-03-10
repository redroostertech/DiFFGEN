import openai
import os
import pyperclip
import re
import subprocess

def get_recent_commits(branch_name, max_commits=5):
    cmd = ["git", "log", f"--max-count={max_commits}", "--oneline", branch_name]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

def generate_pr_description(commits, context):
    # Modify your existing generator function to handle PR description generation
    # ...
    return "OK'"

def main():
    branch_name = "your-feature-branch"
    context = "High-level context for the PR"
    recent_commits = get_recent_commits(branch_name)
    
    pr_description = generate_pr_description(recent_commits, context)
    print("Generated PR Description:")
    print(pr_description)

if __name__ == "__main__":
    main()