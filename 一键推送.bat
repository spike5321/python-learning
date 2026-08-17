@echo off
chcp 65001 >nul
cd /d "D:\Project_spike\python-1"

echo === 正在推送 python-1 ===
echo.

git add -A

:: 检查是否有要提交的内容
git diff --cached --quiet
if %errorlevel% == 0 (
    echo.
    echo 没有改动，无需提交。
    pause
    exit /b
)

git commit -m "update"
git push origin main

echo.
echo === 推送完成！===
pause
