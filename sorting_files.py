# with open('data_3.txt', 'a') as f:
#     f.write('Первая строка! \n')
# with open('data_3.txt', 'a') as f:
#     f.write('Вторая строка! \n')
#
#
# /home/tatyanix/py-homeworks-basic/sorted/
#
# Подключаем модуль
import os

#Каталог из которого будем брать файлы
directory = '/home/tatyanix/py-homeworks-basic/sorted/'

#Получаем список файлов в переменную files
files = os.listdir(directory)


#print(files)
def abs_path_file_def(file):
    abs_path_file = directory + file
    return abs_path_file


def len_file(file):
    abs_path_file = abs_path_file_def(file)
    # print(abs_path_file)
    with open(abs_path_file) as myfile:
        count = sum(1 for line in myfile)
    return count

def sorting_files(files):
    for_sort_list = []
    for file in files:
        for_sort_list.append({'len': len_file(file), 'filename': file})
    sort_list = (sorted(for_sort_list, key=lambda l: l['len']))
    return sort_list

# print(sorting_files(files))

def write_sorted_files(sorted_list):
    with open('sorting_files.txt', 'w') as f:
        f.close()
    for file_line in sorted_list:
        abs_path_file = abs_path_file_def(file_line['filename'])
        with open(abs_path_file) as fread:
            file_content = fread.read()
        with open('sorting_files.txt', 'a') as f:
            f.write(file_line['filename'] + '\n' + str(file_line['len']) + '\n' + file_content + '\n')
            f.close()


sorting_files = (sorting_files(files))
write_sorted_files(sorting_files)

