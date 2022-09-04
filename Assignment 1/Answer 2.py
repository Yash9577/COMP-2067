distance_of_car=440                          # initializing variable of kms travelled by car
time_taken_to_travel=7                       # time taken to travel given kms by car

avgSpeedInKmph = round(distance_of_car/time_taken_to_travel,2)             # round to two decimal places in km/h

avgSpeedInMps = int(avgSpeedInKmph/3.6)             # round to nearest integer in m/h

print(f'Your speed is {avgSpeedInKmph} km/h or {avgSpeedInMps} m/sec.')     #printing answer
