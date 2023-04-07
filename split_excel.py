import pandas as pd
import csv
from os import listdir

inputDir = "C:/Users/joshu/Documents/Projects/gfa-scroller-script/"
outputDir = "//192.168.33.13/ChampionData/ScrollerControl/scrollers/"
#outputDir = "C:/Users/joshu/Documents/Projects/gfa-scroller-script/out/"

scrollerPrefix = "scroller_"
header = ['NAME', 'AMOUNT']

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


df1 = pd.read_excel(inputDir + filename + ".xlsx", sheet_name=None)

for i in range(len(df1)):
    j = current_num()

    if i == 0:
        key = "{}-{}".format(0, 50)
    else:
        key = "{}-{}".format(i * 50 + 1, (i + 1) * 50)

    scrollerName = scrollerPrefix + '0' * (4 - len(str(j))) + str(j) + '.csv'
    print(scrollerName)
    with open(outputDir + scrollerName, "w", newline='') as scrollerFile:
        writer = csv.writer(scrollerFile)
        writer.writerow(header)
        writer.writerows([[name, "$" + str(amount)] for name, amount in df1[key].values[1:][:50]])
