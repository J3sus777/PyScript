import os


path_file = os.chdir(input("path: "))
ld = os.listdir(path_file)


old_file = input("old_file: ")
new_file = input ("new_file: ")

for file_name in ld:
    os.rename(file_name, file_name.replace(old_file, new_file))
print ("save all changes")