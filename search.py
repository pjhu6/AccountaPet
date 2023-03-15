import sqlite3
import weather
import datetime

def perform_search(balance, weather_id, timestamp):
    
    weather_class = weather_id//100
    weather_key = {2:3, 3:4, 5:5, 6:6, 7:7, 8:8}

    dt_object = datetime.datetime.fromtimestamp(timestamp)
    time_component = dt_object.time()
    seconds_since_midnight = time_component.hour * 3600 + time_component.minute * 60 + time_component.second


    conn = sqlite3.connect('db/accountapet.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pet_shop')
    

    # search algorithm
    # - filter balance
    # - calcilate weather factor
    # - calculate time factor
    # - adjust effect score
    # - sort by effect/cost ratio

    rows = [row for row in c.fetchall() if row[2] <= balance]
    conn.close()

    new_pet_shop_list = []

    for row in rows:
        original_effect = row[3]
        weather_factor = row[weather_key[weather_class]]

        key_time = row[10]
        time_difference = seconds_since_midnight - key_time
        if time_difference < 0:
            time_difference += 24*60*60
        time_factor = 1.15-(time_difference/(24*60*60)*0.3)

        adjusted_effect = int(round(original_effect*weather_factor*time_factor, 0))

        # index, item_name, cost, adjusted_effect, 
        new_pet_shop_list.append((row[0], row[1], row[2], adjusted_effect))

    

    return sorted(new_pet_shop_list, key=(lambda x: -x[3]/x[2]))

if __name__ == "__main__":
    time, weather_data = weather.get_weather()
    weather_id = weather_data[0]['id']
    new_pet_shop_list = perform_search(50, weather_id, time)
    for i in new_pet_shop_list:
        print(f'{i[3]/i[2]}: {i}')