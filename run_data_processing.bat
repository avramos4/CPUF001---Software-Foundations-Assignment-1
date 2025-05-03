@echo off
REM run_data_processing.bat – Script to launch the Data Processing program
REM Usage: run_data_processing.bat input_data.csv output_results.txt

IF "%~1"=="" (
    ECHO Usage: %~nx0 input_data.csv output_results.txt
    EXIT /B 1
)

REM Call Python script with supplied arguments
py data_processing.py "%~1" "%~2"