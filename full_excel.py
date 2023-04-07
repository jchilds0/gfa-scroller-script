import csv
from os import listdir

import pandas as pd

inputDir = "C:/Users/joshu/Documents/Projects/gfa-scroller-script/"
outputDir = "//192.168.33.13/ChampionData/ScrollerControl/scrollers/"
#outputDir = "C:/Users/joshu/Documents/Projects/gfa-scroller-script/out/"

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


df1 = pd.read_excel(inputDir + filename + ".xlsx")
lst = []

i = 0   # Row num
j = current_num()   # File num
header = ['NAME', 'AMOUNT']   # Header Row

for row in df1.values[1:]:
    row = [row[0], "$" + str(round(row[1]))]
    if i == 50:
        # Output file

        # Filename
        scrollerName = scrollerPrefix + '0' * (4 - len(str(j))) + str(j) + '.csv'
        print(scrollerName)
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