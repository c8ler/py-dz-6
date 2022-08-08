# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def ZipText(lst):
    lists = list(lst)
    count = 1
    zip_text = []
    for i in range(1, len(lists)):
        if lists[i] == lists[i-1]:
            count += 1
        else:
            zip_text.append(lists[i-1])
            zip_text.append(count)
            count = 1
    zip_text.append(lists[-1])
    zip_text.append(count)
    result = "".join(map(str, zip_text))
    return result


def UnzipText(lst):
    unzip_text = []
    unzip_text.append(lst[0])
    for i in range(1, len(lst)):
        if type(lst[i]) == int:
            for j in range(lst[i]):
                unzip_text.append(lst[i-1])
        else:
            unzip_text.append(lst[i])
    result = "".join(map(str, unzip_text))
    return result


with open('initial_text.txt') as f:
    text = f.read()
print("Данные успешно прочитаны из файла 'initial_text.txt'")
zip_text = ZipText(text)
with open("zip_text.txt", "w") as f:
        f.write(zip_text)
print("Данные успешно записаны в файл 'zip_text.txt'")
unzip_text = UnzipText(text)
with open("unzip_text.txt", "w") as f:
        f.write(unzip_text)
print("Данные успешно записаны в файл 'unzip_text.txt'")