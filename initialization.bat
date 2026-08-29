@echo off
setlocal

echo ========================================
echo      Cafe Website - Initialization
echo ========================================
echo.

cd /d "%~dp0"

echo [1/5] Creating Python virtual environment...

if not exist ".venv" (
    python -m venv .venv
) else (
    echo .venv already exists. Skipping...
)

echo.

echo [2/5] Installing Python dependencies...

call .venv\Scripts\activate.bat

python -m pip install --upgrade pip
pip install django-cors-headers
pip install -r requirements.txt

echo.

echo [3/5] Applying database migrations...

python manage.py migrate

echo.

echo [4/5] Installing Node dependencies...

cd /d "%~dp0frontend"

call npm install

echo.

echo [5/5] Initialization complete!

echo.
echo You can now run the project using run.bat
echo.

pause