import csv
import math
from os import listdir

inputDir = "C:/Users/joshu/Documents/Projects/gfa-scroller-script/"
outputDir = "//192.168.33.13/ChampionData/ScrollerControl/scrollers/"

scrollerPrefix = "scroller_"
filename = input("File Name: ")


def current_num():
    """ Find the last number of the scrollers currently in the output dir """
    lst = [string.lstrip(scrollerPrefix).rstrip(".csv") for string in listdir(outputDir)]
    retval = []

    for string in lst:
        try:
            retval += [int(string)]
        except ValueError:
            pass

    if len(retval) == 0:
        return 1
    else:
        return max(retval) + 1


with open(inputDir + filename + '.csv', "r") as file:
    reader = csv.reader(file)
    lst = []

    i = 0   # Row num
    j = current_num()   # File num
    header = ['NAME', 'AMOUNT']   # Header Row
    next(reader)
    for row in reader:
        row = row[:2]       # Remove last column
        row[1] = "".join(row[1].split(','))
        if i == 50:
            # Output file

            # Filename
            scrollerName = scrollerPrefix + '0' * (3 - math.floor(math.log(j, 10))) + str(j) + '.csv'

            with open(outputDir + scrollerName, "w", newline='') as scrollerFile:
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