

def calculateSleepStateScore(sleepGoal): #calculates pet state based on inputted goals-sample: sleep Goal
    SLEEP_SENSOR_DATA = 6 #REPLACE WITH REFERENCE TO ACTUAL DATA
    if SLEEP_SENSOR_DATA > sleepGoal + 3: #significantly passed sleep goal
        return -1
    elif SLEEP_SENSOR_DATA  < sleepGoal -1:
        return -1
    else:
        return 1
    
