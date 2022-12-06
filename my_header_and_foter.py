import os
import openpyxl
from openpyxl.workbook import Workbook



print("Программа обрабатывает только xlsx файлы")
direct=os.chdir(r"\\path\\to\\file")
list_directory = os.listdir(direct)
print (list_directory)

for i in list_directory:
    print('Начинаем обработку файла:', i)
    if i.endswith('.xlsx'):
        wb = openpyxl.load_workbook(i) 
        ws = wb.active
        for sheet in wb:
            sheet.oddHeader.left.text = ""
            sheet.oddHeader.center.text = ""
            sheet.oddHeader.right.text = ""
            sheet.oddFooter.left.text = ""
            sheet.oddFooter.center.text = ""
            sheet.oddFooter.right.text = ""
        print('save all changes')
        wb.save(i)
        wb.close()
    else:
        print ("это не xlsx")

for i in list_directory:
    wb = openpyxl.load_workbook(i) 
    wb.save(i)
    wb.close()
