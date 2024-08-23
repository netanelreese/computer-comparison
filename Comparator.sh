#!/bin/bash
# This script runs the Python program located at src/main.py

# Activate a virtual environment if needed
# source path/to/your/venv/bin/activate

export PYTHONPATH="${PYTHONPATH}:/home/nreese/workspace/python/computer-comparison"
python3 src/main.py

# Deactivate the virtual environment if it was activated
# deactivate