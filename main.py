import csv
from os import listdir
import pandas as pd

# Config
format = "full"
inputDir = "./"
outputDir = "./out/"
scrollerPrefix = "scroller_"
sheetName = "PLEDGES"
header = ['t_text_1', 't_text_2', 't_text_3']  # Header Row
outputNumRows = 50


def current_num():
    """ Find the last number of the scrollers currently in the output dir """
    lst = [string.lstrip(scrollerPrefix).rstrip(".xlsx") for string in listdir(outputDir)]
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
    return [row[0], round(float(row[1])), ""]


def format_table(df):
    formatted = []
    for row in df:
        formatted.append(format_row(row))

    return formatted


def convert_full_excel(fname: str):
    """ Get data from an excel sheet consisting of one sheet with two header rows"""
    return pd.read_excel(inputDir + fname + ".xlsx").values[1:]


def convert_split_excel(fname: str):
    """ Get data from an excel sheet consisting of multiple sheets with two header rows"""
    df1 = pd.read_excel(inputDir + fname + ".xlsx", sheet_name=None)
    retval = []
    array = list(df1.values())
    for df in array:
        for row in df.values[2:]:
            retval.append(row)

    return retval


def write_output_file(array):
    """ Write the data in array to output files"""
    j = current_num()  # File num
    for i in range(len(array) // outputNumRows):
        start = i * outputNumRows
        end = (i + 1) * outputNumRows + 1

        data = array[start : end]

        scrollerName = scrollerPrefix + '0' * (3 - len(str(j + i))) + str(j + i) + ".xlsx"
        print(scrollerName)
        df = pd.DataFrame(data, columns=header)
        df.to_excel(outputDir + scrollerName, index=False, sheet_name=sheetName)


if __name__ == "__main__":
    while True:
        filename = input("File Name: ")

        try:
            if format == "full":
                df = convert_full_excel(filename)
            elif format == "split":
                df = convert_split_excel(filename)
            else:
                raise ValueError("Unknown Format")

            new = format_table(df)
            write_output_file(new)
        except Exception as e:
            print(e)

