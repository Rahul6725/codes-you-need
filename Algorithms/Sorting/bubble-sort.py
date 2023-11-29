import datetime

# sample data
data = [9, 8, 4, 1, 5, 3, 6, 2, 7]

start_time = datetime.datetime.now()
print("Unsorted data: " + str(data))

# Bubble sort
for i in range(len(data)-1):
    for j in range(len(data)-i-1):
        if data[j] > data[j+1]:    
            data[j], data[j+1] = data[j+1], data[j]

end_time = datetime.datetime.now()

print("Sorted data: " + str(data))
print("Time executed: " + str(end_time-start_time))