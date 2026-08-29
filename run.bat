@echo off

cd /d "%~dp0"

echo Starting Django backend...
start "Django Backend" cmd /k "call .venv\Scripts\activate.bat && python manage.py runserver"

echo Starting frontend...
start "Frontend" cmd /k "cd /d "%~dp0frontend" && npm run dev"

exit