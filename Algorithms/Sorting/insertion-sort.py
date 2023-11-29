import datetime

# sample data
data = [9, 8, 4, 1, 5, 3, 6, 2, 7]
new_data = []

start_time = datetime.datetime.now()
print("Unsorted data: " + str(data))

# Insertion sort
for i in range(len(data)):
    if len(new_data) == 0:
        new_data.append(data[i])
    else:
        for j in range(len(new_data)):
            if data[i] < new_data[j]:
                new_data.insert(j, data[i])
                break

end_time = datetime.datetime.now()

print("Sorted data: " + str(new_data))
print("Time executed: " + str(end_time-start_time))