import csv
from os import listdir
import pandas as pd

# Config
format = "full"
inputDir = "./"
outputDir = "./out/"
scrollerPrefix = "scroller_"
header = ['NAME', 'AMOUNT']  # Header Row
outputNumRows = 50


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


def format_row(row):
    """ Convert the formatting of data rows"""
    return [row[0], "$" + str(round(row[1]))]


def convert_full_excel(fname: str):
    """ Get data from an excel sheet consisting of one sheet with two header rows"""
    return pd.read_excel(inputDir + fname + ".xlsx").values[1:]


def convert_split_excel(fname: str):
    """ Get data from an excel sheet consisting of multiple sheets with two header rows"""
    df1 = pd.read_excel(inputDir + fname + ".xlsx", sheet_name=None)
    retval = []
    array = list(df1.values())
    for df in array:
        for row in df.values[1:]:
            retval.append(row)

    return retval


def write_output_file(array):
    """ Write the data in array to output files"""
    j = current_num()  # File num
    for i in range(len(array) // outputNumRows):
        data = array[i * outputNumRows: (i + 1) * outputNumRows + 1]
        scrollerName = scrollerPrefix + '0' * (4 - len(str(j + i))) + str(j + i) + '.csv'
        print(scrollerName)

        # Output File
        with open(outputDir + scrollerName, "w", newline='') as scrollerFile:
            writer = csv.writer(scrollerFile)
            writer.writerow(header)
            writer.writerows([format_row(row) for row in data])


if __name__ == "__main__":
    filename = input("File Name: ")

    if format == "full":
        df = convert_full_excel(filename)
    elif format == "split":
        df = convert_split_excel(filename)
    else:
        raise ValueError("Unknown Format")

    write_output_file(df)