import os

def batch_rename(files_folder):
  new_name = input("Введите желаемое имя файлов: ")
  digits = int(input("Введите количество цифр в номере: "))
  old_ext = input("Введите расширение исходных файлов: ")
  new_ext = input("Введите расширение результирующих файлов: ")
  start, end = map(int, input("Введите диапазон сохраняемых символов [x,y]: ").split(","))
  
  counter = 1
  for filename in os.listdir(files_folder):
    if filename.endswith(old_ext):
      name_part = filename[start-1:end]
      new_filename = new_name + str(counter).zfill(digits) + name_part + '.' + new_ext
      os.rename(os.path.join(files_folder, filename), os.path.join(files_folder, new_filename))
      counter += 1

files_folder = '/path/to/files/'
batch_rename(files_folder)