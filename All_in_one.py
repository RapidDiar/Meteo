import pandas as pd
import os, glob
import matplotlib.pyplot as plt
path = os.getcwd()
word_list = ['Дата','средняя','осадков, мм',]
words = [[],[],[]]
word_dict = {}
excel_read = pd.read_excel('Диана Петропавл темп123.xlsx',sheet_name='Лист1')


for z in range(len(word_list)):
    for x in excel_read.index:
        words[z].append(excel_read[word_list[z]][x])

for i in range(len(word_list)):
    word_dict[word_list[i]] = words[i]

datf = pd.DataFrame(word_dict)




