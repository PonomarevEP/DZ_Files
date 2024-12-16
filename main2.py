from pathlib import Path

file_path1 = 'sorted/1.txt'
file_path2 = 'sorted/2.txt'
file_path3 = 'sorted/3.txt'
file_name  = 'result/4.txt'

def write_text(list_text, text_to_write):
    for k in range(list_text[1]):
                if k == 0:
                    text_to_write += list_text[2] + "\n"
                elif k == 1:
                    text_to_write += str(list_text[1] - 2) + "\n"
                else:
                    if list_text[0][k - 2] != "":
                        text_to_write += list_text[0][k - 2] + "\n"
    return text_to_write

def write_to_file(text_to_write, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text_to_write)
    print(f'Текст записан в файл {file_name}')

with open(file_path1, 'r', encoding='utf-8') as file1, open(file_path2, 'r', encoding='utf-8') as file2, open(file_path3, 'r', encoding='utf-8') as file3:
    text1 = file1.read()
    text2 = file2.read()
    text3 = file3.read()

    list_text1 = [text1.split('\n'), len(text1.split('\n')) + 2, "1.txt"]
    list_text2 = [text2.split('\n'), len(text2.split('\n')) + 2, "2.txt"]
    list_text3 = [text3.split('\n'), len(text3.split('\n')) + 2, "3.txt"]

    list_numbers = [list_text1[1], list_text2[1], list_text3[1]]
    list_numbers.sort()

    text_to_write = ""
     
    for i in list_numbers:
        if i == list_text1[1]:
            text_to_write = write_text(list_text1, text_to_write)
        elif i == list_text2[1]:
            text_to_write = write_text(list_text2, text_to_write)
        elif i == list_text3[1]:
            text_to_write = write_text(list_text3, text_to_write)

    write_to_file(text_to_write, file_name)