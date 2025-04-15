from os import listdir
import pandas as pd
import configparser

# Config
config = configparser.ConfigParser()
config.read('ticker.ini')
c = config['GFA']


def main():
    rows = []

    while True:
        filename = input("File Name: ")

        try:
            if c['InputFormat'] == "full":
                df = convert_full_excel(filename)
            elif c['InputFormat'] == "split":
                df = convert_split_excel(filename)
            else:
                raise ValueError("Unknown Format")

            rows.append(format_table(df))
            rows = write_output_file(rows)
        except Exception as e:
            print(e)


def current_num() -> int:
    """
    Find the last number of the scrollers
    currently in the output dir
    """

    lst = [string.lstrip(c['ScrollerPrefix']).rstrip(".xlsx")
           for string in listdir(c['OutputDirectory'])]
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
    """
    Get data from an excel sheet consisting
    of one sheet with two header rows
    """

    return pd.read_excel(c['InputDirectory'] + fname + ".xlsx").values[1:]


def convert_split_excel(fname: str):
    """
    Get data from an excel sheet consisting
    of multiple sheets with two header rows
    """

    df1 = pd.read_excel(c['InputDirectory'] + fname + ".xlsx", sheet_name=None)
    retval = []
    print(f"Found Sheets {list(df1.keys())}")
    for df in df1.values():
        for row in df.values[1:]:
            retval.append(row)

    return retval


def format_row(row) -> list[str]:
    """ Format a row """

    return [row[0], str(int(row[1])), ""]


def format_table(df) -> list[list[str]]:
    """ Format a data frame using format row """

    formatted = []
    for row in df:
        try:
            newRow = format_row(row)
            formatted.append(newRow)
        except Exception as e:
            print(e)
            print("Row: ", row)

    return formatted


def write_output_file(array) -> list[list[str]]:
    """
    Write the data in array to output files,
    and return remaining rows
    """
    header = [c['HeaderCol1'], c['HeaderCol2'], c['HeaderCol3']]

    j = current_num()  # File num
    i = 0
    while (len(array) > c['OutputNumRows']):
        data = array[:c['OutputNumRows']]
        array = array[c['OutputNumRows']:]

        scrollerName = c['ScrollerPrefix']
        scrollerName += '0' * (3 - len(str(j + i))) + str(j + i)
        scrollerName += ".xlsx"
        print(scrollerName)

        df = pd.DataFrame(data, columns=header)
        df.to_excel(
            c['OutputDirectory'] + scrollerName,
            index=False,
            sheet_name=c['SheetName']
        )

        i += 1

    return array


if __name__ == "__main__":
    main()
