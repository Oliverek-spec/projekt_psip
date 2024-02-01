import orm.dml as dml

def main_menu():
    while True:
        print(f'\n Menu:\n'
            f'1. Przejdź do menu autobusów\n'
            f'2. Przejdź do menu kierowców autobusów\n'
            f'3. Przejdź do menu kierowców autobusów wybranej linii autobusowej\n'
            f'4. Przejdź do menu pasażerów\n'
            f'5. Przejdź do menu pasażerów wybranej linii autobusowej\n'
            f'6. Przejdź do menu generowania map\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                choice_1_menu()
            case "2":
                choice_2_menu()
            case "3":
                choice_3_menu()
            case "4":
                choice_4_menu()
            case "5":
                choice_5_menu()
            case "6":
                choice_6_menu()
            case "0":
                exit()
            case _:
                print("Wybór może być tylko z zakresu 0-6")

def choice_1_menu():
    while True:
        print(f'\nMenu:\n'
            f'1. Dodaj autobus\n'
            f'2. Wyświetl wszystkie autobusy\n'
            f'3. Edytuj autobus\n'
            f'4. Usuń autobus\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                dml.create_bus()
            case "2":
                dml.read_bus()
            case "3":
                dml.update_bus()
            case "4":
                dml.delete_bus()
            case "0":
                break
            case _:
                print("Wybór może być tylko z zakresu 0-4")

def choice_2_menu():
    while True:
        print(f'\nMenu:\n'
            f'1. Dodaj kierowcę\n'
            f'2. Wyświetl wszystkich kierowców\n'
            f'3. Edytuj kierowcę\n'
            f'4. Usuń kierowcę\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                dml.create_driver()
            case "2":
                dml.read_driver()
            case "3":
                dml.update_driver()
            case "4":
                dml.delete_driver()
            case "0":
                break
            case _:
                print("Wybór może być tylko z zakresu 0-4")

def choice_3_menu():
    while True:
        print(f'\nMenu:\n'
            f'1. Dodaj kierowcę do wybranej linii\n'
            f'2. Wyświetl wszystkich kierowców do wybranej linii\n'
            f'3. Edytuj kierowcę wybranej linii\n'
            f'4. Usuń kierowcę wybranej linii\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                dml.create_driver_by_line()
            case "2":
                dml.read_driver_by_line()
            case "3":
                dml.update_driver_by_line()
            case "4":
                dml.delete_driver_by_line()
            case "0":
                break
            case _:
                print("Wybór może być tylko z zakresu 0-4")

def choice_4_menu():
    while True:
        print(f'\nMenu:\n'
            f'1. Dodaj pasażera\n'
            f'2. Wyświetl wszystkich pasażerów\n'
            f'3. Edytuj pasażera\n'
            f'4. Usuń pasażera\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                dml.create_passenger()
            case "2":
                dml.read_passenger()
            case "3":
                dml.update_passenger()
            case "4":
                dml.delete_passenger()
            case "0":
                break
            case _:
                print("Wybór może być tylko z zakresu 0-4")

def choice_5_menu():
    while True:
        print(f'\nMenu:\n'
            f'1. Dodaj pasażera\n'
            f'2. Wyświetl wszystkich pasażerów\n'
            f'3. Edytuj pasażera\n'
            f'4. Usuń pasażera\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                dml.create_passenger_by_line()
            case "2":
                dml.read_passenger_by_line()
            case "3":
                dml.update_passenger_by_line()
            case "4":
                dml.delete_passenger_by_line()
            case "0":
                break
            case _:
                print("Wybór może być tylko z zakresu 0-4")

def choice_6_menu():
    while True:
        print(f'\nMenu:\n'
            f'1. Utwórz mapę autobusów\n'
            f'2. Utwórz mapę kierowców\n'
            f'3. Utwórz mapę pasażerów\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                print("ok")
            case "2":
                print("ok")
            case "3":
                print("ok")
            case "0":
                break
            case _:
                print("Wybór może być tylko z zakresu 0-3")




