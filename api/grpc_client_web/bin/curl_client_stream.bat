@echo off
@setlocal
rem Read common env vars from file
for /F "usebackq tokens=*" %%A in ("../../env_vars_common.txt") do set %%A
@echo on
curl --insecure --no-buffer -X POST "https://localhost:%GRPC_REST_PORT%/api/StartLongProcessStreaming" ^
-H  "accept: application/json" -H  "Content-Type: application/json" ^
-d "{  \"sequence\": \"Three Rings for the Elven-kings under the sky, Seven for the Dwarf-lords in ^
their halls of stone, Nine for Mortal Men doomed to die, One for the Dark Lord on his dark throne In ^
the Land of Mordor where the Shadows lie. One Ring to rule them all, One Ring to find them, One Ring to ^
bring them all, and in the darkness bind them, In the Land of Mordor where the Shadows lie.\"}"
@endlocal
pause