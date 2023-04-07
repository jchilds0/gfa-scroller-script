import csv
from os import listdir
import pandas as pd

format = "full"
inputDir = "./"
outputDir = "./out/"
scrollerPrefix = "scroller_"
header = ['NAME', 'AMOUNT']  # Header Row


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


def convert_full_excel(fname: str):
    """ Converts an excel file with all data in one sheet"""
    df1 = pd.read_excel(inputDir + fname + ".xlsx")
    lst = []

    i = 0  # Row num
    j = current_num()  # File num
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


def convert_split_excel(fname: str):
    """ Converts an excel file with data split into sheets labelled x-x+50"""
    df1 = pd.read_excel(inputDir + fname + ".xlsx", sheet_name=None)
    j = current_num()

    for i in range(len(df1)):
        # Format dict key (corresponds to sheet name)
        if i == 0:
            key = "{}-{}".format(0, 50)
        else:
            key = "{}-{}".format(i * 50 + 1, (i + 1) * 50)

        # output file name
        scrollerName = scrollerPrefix + '0' * (4 - len(str(j))) + str(j) + '.csv'
        print(scrollerName)
        with open(outputDir + scrollerName, "w", newline='') as scrollerFile:
            writer = csv.writer(scrollerFile)
            writer.writerow(header)
            writer.writerows([[name, "$" + str(amount)] for name, amount in df1[key].values[1:][:50]])


filename = input("File Name: ")

if format == "full":
    convert_full_excel(filename)
elif format == "split":
    convert_split_excel(filename)
else:
    print("Error: Unknown Format")