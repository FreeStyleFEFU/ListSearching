import csv

def circle(name):
    path = "1.txt"
    with open(path, "r", encoding="utf8") as file:
        contents = file.readlines()
        count = 0
        # Считывание данных из CSV файла
        l=[];
        find = 0
        for row in contents:
            index = row.find(n)
            if index > -1:
                find+=1
                li=[];
                coun = 0
                print(path + " "+str(count)+" строка")                  
                print(row)
            count += 1
        if find == 0:
            print("Нет такого")
        #print(f'{count} строка')
        print(f'Всего в файле {count} строк.\nКанетс')


if __name__ == "__main__":
    while True:
        print("Что ищем?")
        name = input()
        n = str(name)
        index = 0
        print("")
        try:
            circle(n)
        except:
            continue

 
        



