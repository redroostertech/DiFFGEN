#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Please install Python."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null
then
    echo "pip is not installed. Please install pip."
    exit 1
fi

# Install requirements using pip
if [ -f "requirements.txt" ]; then
    echo "Uninstalling Python dependencies for a fresh install..."
    pip3 uninstall openai pyperclip python-dotenv python-docx
    echo "Installing Python dependencies from requirements.txt..."
    pip3 install -r requirements.txt
    echo "Dependencies installed successfully."
else
    echo "requirements.txt not found. Please ensure it is in the same directory as this script."
    exit 1
fi