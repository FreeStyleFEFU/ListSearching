import csv

def circle(id):
        csv_path = "res_1.csv"
        with open(csv_path) as f_obj:
        #if name in f_obj:
            #csv_reader(f_obj)
            file_reader = csv.reader(f_obj, delimiter = ",")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            l=[];
            for row in file_reader:
                if count == 0:
                    for column in row:
                        l.append(str(column))
            # Вывод строки, содержащей заголовки для столбцов
                    print("")
                
                else:
                    st = str(row[id-1])
                    index = st.find(n)
                    if index > -1:
                        li=[];
                        coun = 0
                        print(csv_path + " "+str(count)+" строка")
                        for column in l:
                            s = column + " - " + row[coun] + "; "
                            li.append(s)
                            coun+=1
                            print(s)  
                        print("")
                count += 1
                #print(f'{count} строка')
            print(f'Всего в файле {count} строк.')


if __name__ == "__main__":
    while True:
        print("Что ищем?")
        name = input()
        n = str(name)
        index = 0

        print("Где ищем?")
        print("1 - begin; 2 - end; 3 - time interval;	4 - login; 5 - mac ab; 6 - ULSK1; 7 - BRAS ip; 8 - start count; 9 - alive count; 10 - stop count; 11 - incoming; 12 - outcoming")
        number = input()
        try:
            circle(int(number))
        except:
            continue

 
        



