@echo off
chcp 65001 >nul
set "game=%~dp0辰辉.html"
if not exist "%game%" goto missing
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" (
    start "" "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" "%game%"
    if not errorlevel 1 exit /b 0
)
start "" "%game%"
if not errorlevel 1 exit /b 0
echo 无法启动浏览器，请用浏览器打开同目录的辰辉.html。
goto failed
:missing
echo 找不到辰辉.html。请先完整解压游戏 ZIP，再运行开始游戏.bat。
:failed
pause
exit /b 1
