# Good Friday Appeal Scroller Script

Converts a .csv with rows constiting of name and amount
to multiple .csv with 50 lines per file

**To Run:** Set input and output directories

## Formats

### Dropbox from Ch7 (Correct 2023)

- Two header rows
- One xlsx file with all data on one sheet
- Amount is a float
- No dolar sign prefix

```
Good Friday Appeal Donations 2023, 12:00pm
Name, Amount
John Smith, 1000.05
...
```

### GFA Scroller Script

- Two header rows
- One xlsx file with all data on one sheet (can also handle split into pages with 50 names by changing format)
- Amount is a float.
- No dollar sign prefix

```
Header 1
Header 2
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
