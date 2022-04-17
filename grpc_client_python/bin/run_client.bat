@echo off
set "THIS_FOLDER=%~dp0"
set "PYTHONPATH=..\..;..\proto_compiled"
call C:\Python388\python.exe "%THIS_FOLDER%\..\client.py"
pause
