import os

def note_creation():
    #Создание заметки
    note_to_text = input("Введите текст заметки: ")
    id_of_note = id_note_generation()
    note_saving(id_of_note, note_to_text)


def id_note_generation():
    #Генерация уникального идентификатора заметки
    #Использование модуля ниже для генерации глобального идентификатора(нашёл в интернете) 
    return str(uuid.uuid4())


def note_saving():
    #Сохранение заметки
    with open(id_of_note + ".txt", "w") as file:
        file.write(note_to_text)


def notes_reading():
    #Чтение заметок
    #os.listdir возвращает список, содержащий имена файлов и директорий в каталоге
    file_for_notes = [f for f in os.listdir() if f.endswith(".txt")] #Получение списка файлов заметок
    for note_file in file_for_notes:
        with open(note_file, "r") as file:
            print(f"{note_file}: {file.read()}")


def note_editting():
    #Заполнение заметок
    id_of_note = input("Введите идентификатор заметки для редактирования: ")
    if os.path.exists(id_of_note + ".txt"):
        note_to_text = input("Введите текст заметки: ")
        note_saving(id_of_note, note_to_text)#Обновление заметки
    else:
        print("Заметка с таким идентификатором не найдена")


def note_deleting():
    #Удаление заметок
    id_of_note = input("Введите идентификатор заметки для удаления: ")  
    if os.path.exists(id_of_note + ".txt"):
        os.remove(id_of_note + ".txt")
    else:
        print("Заметка с таким идентификатором не найдена")

    
def main():

    while True:

        print("1. Создать заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            note_creation()
        elif choice == "2":
            notes_reading()
        elif choice == "3":
            note_editting()
        elif choice == "4":
            note_deleting()
        elif choice == "0":
            break
        else:
            print("Некорректный выбор")



if __name__ == "__main__":
        main()
        
    







