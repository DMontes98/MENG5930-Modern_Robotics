# Reading Files
with open("python/sensor_data.txt", "r") as file:  # Open File
    # now iterate over each line
    for line in file:
        # split the line into timestamp and temprature:
        timestamp, temperature = line.strip().split(", ")

        # now we can process the data
        print("Timestamp: ", timestamp)
        print("Temperature: ", temperature)