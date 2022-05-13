@echo off
rem Read common env vars from file
for /F "usebackq tokens=*" %%A in ("../../env_vars_common.txt") do set %%A
set "PYTHONPATH=..;..\proto_compiled"
call %_PYTHON% "..\client.py"
pause
