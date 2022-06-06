
new_dataset = []

with open("dataset.csv", "r") as file:
    
    for row in file.readlines():

        row_data = row.rstrip().split(",")

        r = int(row_data[3])
        g = int(row_data[4])
        b = int(row_data[5])
        if .8 * (g + b) <= r and r + g + b >= 120 and (g * 75 <= b or g + b < 50):
            row_new = row_data[1] + "," + "\"Piros\"" + "," + row_data[2] + "," + str(r) + "," + str(g) + "," + str(b)
            new_dataset.append(row_new)
        elif .7 * (r + b) <= g and r + g + b >= 100 and  r <= g - 40:
            row_new = row_data[1] + "," + "\"Zöld\"" + "," + row_data[2] + "," + str(r) + "," + str(g) + "," + str(b)
            new_dataset.append(row_new)
        elif .8 * (r + g) <= b and r + g + b >= 80:
            row_new = row_data[1] + "," + "\"Kék\"" + "," + row_data[2] + "," + str(r) + "," + str(g) + "," + str(b)
            new_dataset.append(row_new)
        else:
            row_new = row_data[1] + "," + "\"Ismeretlen\"" + "," + row_data[2] + "," + str(r) + "," + str(g) + "," + str(b)
            new_dataset.append(row_new)

with open("dataset_new.txt", "w", encoding="utf-8") as newFile:

    for i in new_dataset:
        newFile.write(f"{i}\n")

