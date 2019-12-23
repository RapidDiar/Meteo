import pandas as pd
import re

excel_header = ['Дата','средняя','осадков, мм']
list_month = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
word_dict = pd.DataFrame()
excel_read = pd.read_excel('1900-1995.xlsx',sheet_name='Лист1')

for header in excel_header:
    word_dict[header] = [excel_read[header][words] for words in excel_read.index]

for date in word_dict.index:
    for month in range(len(list_month)):
        insert_date = re.sub(r'\D'+list_month[month]+'\D','.'+str(month+1)+'.',word_dict['Дата'][date])
        if re.findall(r'\D[а-я]',insert_date) == []:
            break
    word_dict['Дата'][date] = insert_date

print('input')
date_input = [[input() for i in range(2)]]
date_input.append([next(iter(word_dict[word_dict['Дата'] == date_input[0][index]].index))for index in range(2)])
print(date_input)


print(word_dict.iloc[[index for index in range(int(date_input[1][0]),int(date_input[1][1])+1)]])














