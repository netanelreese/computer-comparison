#!/bin/bash
# This script runs the Python program located at src/main.py

# Activate a virtual environment if needed
# source path/to/your/venv/bin/activate

source venv/Scripts/activate
pip install -r requirements.txt
python3 src/main.py

# Deactivate the virtual environment if it was activated
# deactivate