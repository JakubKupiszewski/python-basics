user_choice = -1

tasks = []

def show_tasks():
    tasks_index = 0
    for task in tasks:
        print(task + " [" + str(tasks_index) + "]")
        tasks_index += 1

def add_task():
    task = input("Dodaj zadanie: ")
    tasks.append(task)
    print("Dodane!")

def delete_task():
    task_index = int(input("Podaj indeks zadania które chcesz usunąć: "))

    if task_index < 0 or task_index > len(tasks) -1:
        print("Nie ma zadania z danym indeksem")
        return
    
    tasks.pop(task_index)
    print("Usunięto zadanie!")

def save_tasks_to_file():
    file = open("tasks.txt", "w", encoding="utf-8")
    for task in tasks:
        file.write(task+"\n")
    file.close()

def load_tasks_from_file():
    try:
        file = open("tasks.txt", "r", encoding="utf-8")

        for line in file.readlines():
            tasks.append(line.strip()) 
        
        file.close()
    except FileNotFoundError:
        return

load_tasks_from_file()
print(tasks)
while user_choice != 5:
    if user_choice == 1:
        show_tasks()
    
    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_tasks_to_file()

    print()
    print("1.Pokaż zadania")
    print("2.Dodaj zadania")
    print("3.Usuń zadania")
    print("4.Zapisz zmiany do pliku")
    print("5.Wyjdź")

    user_choice = int(input("Jaką liczbe wybrać?: "))

    print()
    print()