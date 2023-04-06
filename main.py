import csv

input_dir = "C:/Users/joshu/Documents/Projects/gfa-scroller-script/"
output_dir = "C:/Users/joshu/Documents/Projects/gfa-scroller-script/out/"

filename = input("File Name: ")

with open(input_dir + filename + '.csv', "r") as file:
    reader = csv.reader(file)
    lst = []

    i = 0   # Row num
    j = 0   # File num
    header = next(reader)[:2]   # Header Row
    for row in reader:
        row = row[:2]       # Remove last column

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