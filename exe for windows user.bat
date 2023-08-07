@echo off
setlocal

rem Check if Python is installed
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b
)

rem Get the directory of the batch file
set "batch_dir=%~dp0"

rem Change to the batch file directory
cd /d "%batch_dir%"

rem Execute the Python script
python -u main.py

endlocal
