import sys
import pythoncom
from win32com.client import Dispatch
import os


print ("Этот код меняет текст во всех файлах vsd и первые страницы vsdx файлов")
# Путь к файлу Visio
directory = input("enter dir: ")

# Получаем строку для поиска и строку для замены из аргументов командной строки
old_txt = input("old TXT: ")
new_txt = input("new TXT: ")

# Создаем объект Visio
visio = Dispatch("Visio.Application")

for root, dirs, files in os.walk(directory):
    for file in files:
        # Проверяем расширение файла
        if file.endswith(".vsd") or file.endswith(".vsdx"):
            file_path = os.path.join(root, file)
            # Открываем файл Visio
            doc = visio.Documents.Open(file_path)

            # Получаем коллекцию страниц
            pages = doc.Pages
            # Для каждой страницы получаем текст из всех элементов
            for page in pages:
                shapes = page.Shapes
                for shape in shapes:
                    if shape.Characters.Text != "":
                        shape.Characters.Text = shape.Characters.Text.replace(old_txt, new_txt)

            # Закрываем файл Visio
            doc.Save()
            doc.Close()

# Закрываем приложение Visio
visio.Quit()
