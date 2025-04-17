# Good Friday Appeal Scripts

Converts scroller .xlsx with rows constiting of name and amount
to multiple .xlsx with 50 lines per file.
Converts boards .xlsx into a json.

## Quickstart

Clone repo.

```
git clone https://github.com/jchilds0/gfa-scroller-script
cd gfa-scroller-script
```

Configure options in `default.ini` and rename to `config.ini`

Setup python virtual environment and install dependencies.
```
python -m venv venv
source venv/bin/activate # ./venv/Scripts/activate.bat on Windows
pip install -r requirements.txt
```

Run script 
```
python scroller.py
python boards.py <filename>
```

## Formats

### 2024 Update

- Config File: Duplicate default.ini and rename to ticker.ini
- Outputs an xlsx file with a single sheet.

### Dropbox from Ch7 (Correct 2023)

- Two header rows
- One xlsx file with all data on one sheet (can handle multiple sheets with a config change)
- Amount is a float
- No dolar sign prefix

```
Good Friday Appeal Donations 2023, 12:00pm
Name, Amount
John Smith, 1000.05
...
```

### Scroll Control

- Header must be NAME, AMOUNT
- Max 50 names per file
- Amount is an integer, with a dollar sign prefix
- Amount contains no commas

```
NAME, AMOUNT
John Smith, $1000
...
```
