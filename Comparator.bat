@echo off
REM This script runs the Python program located at src/main.py

REM Activate a virtual environment if needed
REM call path\to\your\venv\Scripts\activate

venv\Scripts\activate
pip install -q -r requirements.txt
python src\main.py

REM Deactivate the virtual environment if it was activated
REM deactivate

pause