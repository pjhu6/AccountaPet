@echo off

rem Start home.py on port 5001
start /B python home.py 5001

rem Start webapp.py on port 5000
start /B python webapp.py 5000