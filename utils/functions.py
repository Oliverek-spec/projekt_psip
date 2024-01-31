

def main_menu():
    while True:
        print(f'Menu:\n'
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
                print("ok")
            case "2":
                print("ok")
            case "3":
                print("ok")
            case "4":
                print("ok")
            case "5":
                print("ok")
            case "6":
                print("ok")
            case "0":
                exit()
            case _:
                print("Wybór może być tylko z zakresu 0-6")

def choice_1_menu():
    while True:
        print(f'Menu:\n'
            f'1. Dodaj autobus\n'
            f'2. Wyświetl wszystkie autobusy\n'
            f'3. Edytuj autobus\n'
            f'4. Usuń autobus\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                print("ok")
            case "2":
                print("ok")
            case "3":
                print("ok")
            case "4":
                print("ok")
            case "0":
                exit()
            case _:
                print("Wybór może być tylko z zakresu 0-4")

def choice_2_menu():
    while True:
        print(f'Menu:\n'
            f'1. Dodaj kierowcę\n'
            f'2. Wyświetl wszystkich kierowców\n'
            f'3. Edytuj kierowcę\n'
            f'4. Usuń autobus\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                print("ok")
            case "2":
                print("ok")
            case "3":
                print("ok")
            case "4":
                print("ok")
            case "0":
                exit()
            case _:
                print("Wybór może być tylko z zakresu 0-4")

def choice_3_menu():
    while True:
        print(f'Menu:\n'
            f'1. Dodaj kierowcę\n'
            f'2. Wyświetl wszystkich kierowców\n'
            f'3. Edytuj kierowcę\n'
            f'4. Usuń autobus\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                print("ok")
            case "2":
                print("ok")
            case "3":
                print("ok")
            case "4":
                print("ok")
            case "0":
                exit()
            case _:
                print("Wybór może być tylko z zakresu 0-4")

def choice_4_menu():
    while True:
        print(f'Menu:\n'
            f'1. Dodaj pasażera\n'
            f'2. Wyświetl wszystkich pasażerów\n'
            f'3. Edytuj pasażera\n'
            f'4. Usuń pasażera\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                print("ok")
            case "2":
                print("ok")
            case "3":
                print("ok")
            case "4":
                print("ok")
            case "0":
                exit()
            case _:
                print("Wybór może być tylko z zakresu 0-4")

def choice_5_menu():
    while True:
        print(f'Menu:\n'
            f'1. Dodaj pasażera\n'
            f'2. Wyświetl wszystkich pasażerów\n'
            f'3. Edytuj pasażera\n'
            f'4. Usuń pasażera\n'
            f'0. Wyjdź\n')
        choice = input("Podaj numer : ").strip()
        match choice:
            case "1":
                print("ok")
            case "2":
                print("ok")
            case "3":
                print("ok")
            case "4":
                print("ok")
            case "0":
                exit()
            case _:
                print("Wybór może być tylko z zakresu 0-4")

def choice_6_menu():
    while True:
        print(f'Menu:\n'
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
                exit()
            case _:
                print("Wybór może być tylko z zakresu 0-3")




