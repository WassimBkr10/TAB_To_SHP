@echo off
set /p Folder=Enter Your Input Folder's Path: 
echo %Folder%


REM MIGRATION ARCS
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" scripts\FMEPython_runner.py %Folder% 
pause