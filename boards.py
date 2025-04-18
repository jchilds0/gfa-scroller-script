import sys
import pandas as pd
import json
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
c = config['Boards']


def main():
    if len(sys.argv) != 2:
        print("missing file name, expected boards.py <filename>")
        exit(1)

    fileName = sys.argv[1]
    df = pd.read_excel(fileName, sheet_name=c['SheetName']).fillna(0)
    table = create_array(df)

    with open(c['OutputFileName'], "w") as file:
        file.write(json.dumps(table, indent=4))


def rankings(df: pd.DataFrame) -> dict[str, int]:
    """ calculate rank based on the second column of the dataframe """
    ranking = {}
    sortRows = sorted(df.values, key=lambda row: row[1], reverse=True)

    for rank, row in enumerate(sortRows):
        ranking[row[0]] = rank + 1

    return ranking


def create_array(df: pd.DataFrame) -> list:
    """
    create array of id, sort id, first column and
    second column from df
    """
    table = []
    ranking = rankings(df)

    for id, row in enumerate(df.values):
        table.append({
            c["IdentifierName"]: str(id + 1),
            c["SortIdentifierName"]: str(ranking[row[0]]),
            c["FirstColumn"]: row[0],
            c["SecondColumn"]: str(row[1]),
        })

    return table


if __name__ == "__main__":
    main()
