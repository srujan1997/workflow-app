#!/bin/bash

# Get the current working directory
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"


# Create a virtual environment if it doesn't exist
if [ ! -d "$DIR/../venv" ]; then
    python3 -m venv "$DIR/../venv"
    echo "Virtual environment created."
fi

# Activate the virtual environment
source "$DIR/../venv/bin/activate"

# Install the requirements
pip install -r "$DIR/requirements.txt"

exec python3 wsgi.py
