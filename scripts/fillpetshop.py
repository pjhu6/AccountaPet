import sqlite3
import csv
import os

conn = sqlite3.connect('db/accountapet.db')

c = conn.cursor()

# insert some data into the pet_shop table
current_dir = os.getcwd()
filename = "tables/pet_shop.csv"
with open(filename, "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t")
    # Convert each row into a tuple and add it to the list
    data = [(row["item_name"], 
             row["cost"], 
             row["effect"], 
             row["weather_2xx"], 
             row["weather_3xx"], 
             row["weather_5xx"], 
             row["weather_6xx"], 
             row["weather_7xx"], 
             row["weather_8xx"], 
             row["ideal_time"]) for row in reader]



c.executemany('INSERT INTO pet_shop (item_name, cost, effect, weather_2xx, weather_3xx, weather_5xx, weather_6xx, weather_7xx, weather_8xx, ideal_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data)

conn.commit()

c.close()
conn.close()
