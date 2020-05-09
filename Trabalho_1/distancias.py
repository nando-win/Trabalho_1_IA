import csv

# read flash.dat to a list of lists
datContent = [i.strip().split() for i in open("./iris_log.dat").readlines()]

# write it as a new CSV file
with open("./iris_log.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)