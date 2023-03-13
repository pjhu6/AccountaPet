#!/bin/bash

#clear current user table
python clearcurrentuser.py

#Start home.py on port 5001
python home.py 5001 &

#Start shop.py on port 5002
python shop.py 5002 &

#Start webapp.py on port 5000
export FLASK_APP=webapp.py
flask run --port 5000
