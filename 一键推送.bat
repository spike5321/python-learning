@echo off
cd /d "D:\Project_spike\python-1"

echo [1] Adding files...
git add -A

git diff --cached --quiet
if %errorlevel% == 0 (
    echo No changes to push.
    pause
    exit /b
)

echo [2] Committing...
git commit -m "update"

echo [3] Pushing to GitHub...
git push origin main

echo [Done]
pause
