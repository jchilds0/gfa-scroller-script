import csv

input_dir = "C:/Users/joshu/Documents/Projects/gfa-scroller-script/"
output_dir = "//192.168.33.13/ChampionData/ScrollerControl/scrollers/"

filename = input("File Name: ")

with open(input_dir + filename + '.csv', "r") as file:
    reader = csv.reader(file)
    lst = []

    i = 0   # Row num
    j = 0   # File num
    header = ['NAME', 'AMOUNT']   # Header Row
    next(reader)
    for row in reader:
        row = row[:2]       # Remove last column
        row[1] = "".join(row[1].split(','))
        if i == 50:
            # Output file
            scrollerName = "scroller_" + str(j) + ".csv"
            with open(output_dir + scrollerName, "w", newline='') as scrollerFile:
                writer = csv.writer(scrollerFile)
                writer.writerow(header)
                writer.writerows(lst)

            # Reset Vars
            lst = []
            i = 0
            j += 1
        else:
            lst += [row]
            i += 1