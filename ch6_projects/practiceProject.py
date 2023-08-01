#! python3

tableData = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose'],
        ]

def printTable(table):
    columns = len(table)
    rows = len(table[0])

    colWidths = [0] * columns

    result = ''

    i = 0
    j = 0
    while i < columns and j < rows:
        if colWidths[i] < len(table[i][j]):
            colWidths[i] = len(table[i][j])
        j += 1
        if j >= rows:
            i += 1
            j = 0

    i = 0
    j = 0
    while i < columns and j < rows:
        result += table[i][j].rjust(colWidths[i]+1)
        i += 1
        if i >= columns:
            result += '\n'
            j += 1
            i = 0
    return result

print(printTable(tableData))
