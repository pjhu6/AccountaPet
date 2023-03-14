#!/bin/bash

# Stop running services
pkill -f "webapp.py"
pkill -f "home.py"
pkill -f "shop.py"
pkill -f "pet_status.py"
pkill -f "settings.py"