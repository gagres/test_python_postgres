# -*- coding: utf8 -*-
from xlrd import open_workbook
from postgres import selectAll, addNew

wb = open_workbook('teste_python.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []
    rows = []

    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = int(value) if isinstance(value, float) else str(value)
            except ValueError:
                pass
            finally:
                values.append(value)
        items.append(values)

listPersons = selectAll()

for item in items:
    if tuple(item) not in listPersons:
        addNew(item[0], item[1])
        print '%s adicionado com sucesso!' % (item[1])
    else:
        print 'Usuário #%s: %s' % (item[0], item[1])