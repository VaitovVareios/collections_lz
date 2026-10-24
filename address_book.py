import pandas as pd # I am importing all module

# Creating DataFrame with basic information
DataBase = pd.DataFrame({
    "ФИО": ["Иванов Иван Иванович", "Петровик Ники Вадимович", "Никонов Сергей Шалашников"],
    "Адресс": ["Чайхана 15", "Аляскино 33", "Дедовичи 71"],
    "Телефон": [33131251, 11235321, 98122719],
    "Дата рождения": ["17.01.2000", "15.11.2001", "25.04.2020"]
})

print(DataBase)

action = input("Hello, чтобы ты хотел сделать с адрессным справочником? (Добавить, Удалить, Изменить)")

if action == "Добавить":
    fio, addres, number, dataBirth = map(str, input("Введите ФИО, Адресс, Телефон, Дату рождения (через запятую):  ").split(","))

    # We create a new DataFrame using the information entered by the user.
    addData = {"ФИО": fio, "Адрес": addres, "Телефон": int(number), "Дата рождения": dataBirth}
    new = pd.DataFrame([addData])
    # Adding new info for entered by the user
    newData = pd.concat([new,DataBase], ignore_index=True)

    print(newData)
elif action == "Удалить":
    deleteID = int(input("Введите номер (индекс) строки для удаления: "))
    
    # Deleting user info for ID
    DataBase.drop(deleteID, inplace=True)

    print(DataBase)
elif action == "Изменить":
    dataID = int(input("Введите номер (индекс) строки для изменения: "))
    fio, addres, number, dataBirth = map(str, input("Введите ФИО, Адресс, Телефон, Дату рождения (через запятую):  ").split(","))

    # Changing info about user with take func "loc"
    DataBase.loc[dataID] = [fio, addres, int(number), dataBirth]
    print(DataBase)
else:
    print("Вы ввели не найденное действие...")