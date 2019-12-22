@echo off
REM #Description: Insert copyright.
REM 
REM #before
REM (c)
REM 
REM #after
REM Copyright (c) YEAR YOURE_NAME. All Rights Reserved.
setlocal
set YEAR=%date:~,4%
set YOURE_NAME=%USERNAME%
set /p X="Copyright (c) %YEAR% %YOURE_NAME%. All Rights Reserved." < NUL
