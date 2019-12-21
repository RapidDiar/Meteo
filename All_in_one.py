import pandas as pd

excel_header = ['Дата','средняя','осадков, мм',]
word_dict = pd.DataFrame()
excel_read = pd.read_excel('Диана Петропавл темп123.xlsx',sheet_name='Лист1')

for header in excel_header:
    word_dict[header] = [excel_read[header][words] for words in excel_read.index]







