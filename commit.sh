#!/bin/bash

# Define the path to the Python script
PYTHON_SCRIPT_PATH="source/commit_generator.py"

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT_PATH" ]; then
    echo "Python script not found at $PYTHON_SCRIPT_PATH. Please check the path."
    exit 1
fi

# Run the Python script
python3 "$PYTHON_SCRIPT_PATH"