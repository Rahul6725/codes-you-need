import datetime

# sample data
data = [9, 8, 4, 1, 5, 3, 6, 2, 7]
minimum_val_index = None

start_time = datetime.datetime.now()
print("Unsorted data: " + str(data))

# Selection sort
for i in range(len(data)):
    minimum_val_index = i
    for j in range(i+1, len(data)):
        if data[j] < data[minimum_val_index]:    
            minimum_val_index = j
    data[i], data[minimum_val_index] = data[minimum_val_index], data[i]
    minimum_val_index = None

end_time = datetime.datetime.now()

print("Sorted data: " + str(data))
print("Time executed: " + str(end_time-start_time))
