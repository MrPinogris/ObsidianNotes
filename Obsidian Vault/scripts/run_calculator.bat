@echo off
set input=%1
for /f "delims=" %%i in ('python "C:\Users\alexa\Desktop\Obsidian\Obsidian Vault\scripts\latex_calculator.py" %input%') do set result=%%i
echo %result% | clip
echo Resultaat is gekopieerd naar het klembord: %result%
pause

