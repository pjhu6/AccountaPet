@echo off

rem clear current user table
start /B python clearcurrentuser.py

rem Start pet_status.py on port 5004
start /B python pet_status.py 5004

rem Start pet_status.py on port 5003
start /B python settings.py 5003

rem Start pet_status.py on port 5002
start /B python shop.py 5002

rem Start home.py on port 5001
start /B python home.py 5001

rem Start webapp.py on port 5000
start /B python webapp.py 5000