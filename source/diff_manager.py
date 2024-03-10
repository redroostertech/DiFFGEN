import os
import subprocess

def get_staged_diff(repo_path):
    """
    Get the diff of staged files in the specified repository.
    """
    original_cwd = os.getcwd()
    os.chdir(repo_path)
    result = subprocess.run(['git', 'diff', '--staged'], stdout=subprocess.PIPE)
    os.chdir(original_cwd)
    return result.stdout.decode('utf-8').strip()

def filter_diff_additions_removals(diff):
    """
    Filters the diff to include only additions and removals.
    """
    filtered_lines = []
    for line in diff.split('\n'):
        if line.startswith('+') or line.startswith('-'):
            filtered_lines.append(line)
    return '\n'.join(filtered_lines)

def split_diff_into_chunks(diff, max_length):
    """
    Splits the diff text into chunks, each with a maximum length of max_length.
    """
    chunks = []
    current_chunk = ""

    for line in diff.split('\n'):
        if len(current_chunk) + len(line) > max_length:
            chunks.append(current_chunk)
            current_chunk = line
        else:
            current_chunk += line + '\n'

    if current_chunk:
        chunks.append(current_chunk)

    return chunks