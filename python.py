from collections import Counter
import csv

with open("HeightWeight.csv", newline = "" ) as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

y = len(new_data)
total = 0
for x in new_data:
    total += x

mean = total / x

print(str(mean))

n = len(new_data)
new_data.sort()
if n%2 == 0:
    median1 = float(new_data[n/2])
    median2 = float(new_data[n/2-1])
    median = (median1 + median2)/2
else:
    median = new_data[n/2]
    print(n)
    
print(str(median))

data = Counter(new_data)
mode_data_for_range = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}

for height, occurrence in data.items():
    if 50 < float(height) < 85:
        mode_data_for_range["75-85"] += occurrence
    elif 60 < float(height) < 95:
        mode_data_for_range["85-95"] += occurrence
    elif 60 < float(height) < 105:
        mode_data_for_range["95-105"] += occurrence
    elif 60 < float(height) < 115:
        mode_data_for_range["105-115"] += occurrence
    elif 60 < float(height) < 125:
        mode_data_for_range["115-125"] += occurrence
    elif 60 < float(height) < 135:
        mode_data_for_range["125-135"] += occurrence
    elif 60 < float(height) < 145:
        mode_data_for_range["135-145"] += occurrence
    elif 60 < float(height) < 155:
        mode_data_for_range["145-155"] += occurrence
    elif 60 < float(height) < 165:
        mode_data_for_range["155-165"] += occurrence
    elif 60 < float(height) < 175:
        mode_data_for_range["165-175"] += occurrence

mode_range, mode_occurrence = 0, 0
for range, occurrence in mode_data_for_range.items():
    if occurrence > mode_occurrence:
        mode_range, mode_occurrence = [int(range.split("-")[0]), int(range.split("-")[1])]
mode = float((mode_range[0] + mode_range[1])/2)
print(f"Mode Is -> {mode:2f}")