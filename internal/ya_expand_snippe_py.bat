@echo off
REM 
REM ya_epand_snippe_py.bat python_exe_path snippet_file_name python_path ini_filename command_name args0 args1 ... argsN
REM 
setlocal enabledelayedexpansion

set EXE=%1
set SNIPPET=%2
set PYTHONPATH=%PYTHONPATH%;%3
set YA_HIDEMARU_FILE=%4

set COUNTER=1
set ARGS=
for %%a in (%*) do (
    if "4" LSS "!COUNTER!" (
    	call :join %%a
    )
    set /a COUNTER+=1
)

!EXE! !SNIPPET! !ARGS!
exit /b !errorlevel!


:join
    set ARGS=!ARGS! %1
	exit /b
