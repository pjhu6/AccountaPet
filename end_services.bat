@echo off

rem Stop running services
taskkill /f /im "webapp.py"
taskkill /f /im "home.py"