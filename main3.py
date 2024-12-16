from pathlib import Path

input_dir = 'sorted/'
output_file = 'result/4.txt'

def read_and_process_files(input_dir, output_file):
    files = sorted(Path(input_dir).glob('*.txt'))
    
    text_to_write = ''
    list_to_sorted = []
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().split('\n')
            num_lines = len(text) + 2
            filename = file_path.name

        list_to_sorted.append([text, num_lines, filename])
    list_to_sorted.sort(key=lambda x: x[1])
    for i in list_to_sorted:
        text_to_write = write_text(i, text_to_write)
    
    write_to_file(text_to_write, output_file)

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
    print(f'Текст записан в файл {file_name}')

read_and_process_files(input_dir, output_file)