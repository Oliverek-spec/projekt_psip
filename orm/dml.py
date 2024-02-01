from orm.ddl import engine, Base, Bus, Driver, Passenger
import sqlalchemy.orm as orm


Session = orm.sessionmaker(bind=engine)
session = Session()

###Funkcje menu nr 1###

def create_bus():
    registration_query = registration_insert()
    if registration_query == False: 
        return
    line_query = input('Podaj nr linii ')
    lines = session.query(Bus).filter(Bus.line == line_query).first()
    if lines is not None:
        print('\n!Taka linia już istnieje!\n')
        return
    elif registration_query == "":
        print('\n!Linia musi mieć znaki!\n')
        return
    north = input('Podaj współrzędną X ')
    east = input('Podaj współrzędną Y ')
    bus_to_create = Bus(
        registration = registration_query,
        line = line_query,
        location = f'POINT({north} {east})')
    session.add(bus_to_create)
    session.commit()

def read_bus():
    buses = session.query(Bus).all()
    if len(buses) == 0:
        print('\n!Brak autobusów do wyświetlenia!\n')
    print('\nLista autobusów:\n')
    for bus in buses:
        print(f'Nr rejestracyjny: {bus.registration}    nr linii: {bus.line}')
    session.commit()

def update_bus():
    bus_to_update = input('Podaj rejestracje autobusu do zmodyfikowania ')
    bus = session.query(Bus).filter(Bus.registration == bus_to_update).first()
    if bus is None:
        print('Nie ma autobusu o takiej rejestracji')
        return
    while True:
        new_registration = input('Podaj nową rejestrację ')
        registrations = session.query(Bus).filter(Bus.registration == new_registration).first()
        if registrations is None:
            print('Taka rejestracja już istnieje ')
        elif new_registration != "":
            bus.registration = new_registration
            break
        else:
            print('@Brak zmian')
            break 
    while True:
        new_line = input('Podaj nowy nr linii ')
        lines = session.query(Bus).filter(Bus.line == new_line).first()
        if lines is None:
            print('\n!Taka linia już istnieje!\n')
        elif new_line != "":
            bus.line = new_line
            break
        else:
            print('@Brak zmian')
            break 
    new_north = input('Podaj nową współrzędną X ')
    new_east = input('Podaj nową współrzędną Y ')
    if new_north !="" and new_east != "":
        bus.location = f'POINT({new_north} {new_east})'
    session.commit()
    
def delete_bus():
    bus_to_delete = input('Podaj nr rejestracyjny autobusu do usunięcia ')
    bus = session.query(Bus).filter(Bus.registration == bus_to_delete).first()
    if bus is None:
        print('\n!Nie ma autobusu o takiej rejestracji!\n')
    elif bus.registration == bus_to_delete:
        session.delete(bus)
    session.commit()

### Funkcje menu nr 2 ###

def create_driver():
    registration_query = registration_insert()
    if registration_query == False: 
        return
    create_line = session.query(Bus).filter(Bus.registration == registration_query).first()
    create_name = input('Podaj imię kierowcy ')
    create_surname = input('Podaj nazwisko kierowcy ')
    north = input('Podaj współrzędną X ')
    east = input('Podaj współrzędną Y ')
    driver_to_create = Driver(
        bus = create_bus,
        line = create_line.line,
        name = create_name,
        surname = create_surname,
        location = f'POINT({north} {east})')
    session.add(driver_to_create)
    session.commit()

def read_driver():
    drivers = session.query(Driver).all()
    if len(drivers) == 0:
        print('\n!Brak kierowców do wyświetlenia!\n')
    print('\nLista kierowców:\n')
    for driver in drivers:
        print(f'Nr rejestracyjny: {driver.bus}    nr linii: {driver.line}   imię: {driver.name} {driver.surname}')
    session.commit()

def update_driver():
    driver_to_update = input('Podaj nr rejestracyjny autobusu który prowadzi kierowca ')
    driver = session.query(Driver).filter(Driver.bus == driver_to_update).first()
    if driver is None:
        print('Nie ma kierowcy takiego autobusu lub takiej rejestracji')
        return
    while True:
        new_registration = input('Podaj nową rejestrację ')
        buses = session.query(Bus).filter(Bus.registration == new_registration).first()
        registrations = session.query(Driver).filter(Driver.bus == new_registration).first()
        if buses is None:
            print('\n!Nie ma takiej rejestracji!\n')
        elif registrations is not None:
            print('\n!Autobus zajęty!\n')
        elif new_registration != '':
            driver.bus = new_registration
            break
        else:
            print('@Brak zmian')
            break 
    new_line = session.query(Bus).filter(Bus.registration == new_registration).first()
    driver.line = new_line.line
    new_name = input('Podaj nowe imię ')
    if new_name != "":
        driver.name = new_name
    new_surname = input('Podaj nowe nazwisko ')
    if new_name != "":
        driver.surname = new_surname
    new_north = input('Podaj nową współrzędną X ')
    new_east = input('Podaj nową współrzędną Y ')
    if new_north !="" and new_east != "":
        driver.location = f'POINT({new_north} {new_east})'
    session.commit()
    
def delete_driver():
    driver_to_delete = input('Podaj nr rejestracyjny autobusu który prowadzi kierowca ')
    driver = session.query(Driver).filter(Driver.bus == driver_to_delete).first()
    if driver is None:
        print('Nie ma kierowcy prowadzącego ten autobus lub takiego kierowcy')
    elif driver.bus == driver_to_delete:
        session.delete(driver)
    session.commit()
    
### Funkcje menu nr 3 ###

def create_driver_by_line():
    choice = line_checker() 
    create_bus = input('Podaj rejestracyję prowadzonego autobusu ')
    create_name = input('Podaj imię kierowcy ')
    create_surname = input('Podaj nazwisko kierowcy ')
    north = input('Podaj współrzędną X ')
    east = input('Podaj współrzędną Y ')
    driver_to_create = Driver(
        bus = create_bus,
        line = choice, 
        name = create_name,
        surname = create_surname,
        location = f'POINT({north} {east})')
    session.add(driver_to_create)
    session.commit()


def read_driver_by_line():
    choice = line_checker() 
    drivers = session.query(Driver).filter(Driver.line == choice).all()
    if len(drivers) == 0:
        print('\nBrak kierowców do wyświetlenia\n')
    print('\nLista kierowców:\n')
    for driver in drivers:
        print(f'Nr rejestracyjny: {driver.bus}    nr linii: {driver.line}   imię: {driver.name} {driver.surname}')
    session.commit()

def update_driver_by_line():
    choice = line_checker() 
    driver_to_update = input('Podaj nr rejestracyjny autobusu który prowadzi kierowca ').upper
    driver = session.query(Driver).filter(Driver.line == choice, Driver.bus == driver_to_update).first()
    if driver is None:
        print('Nie ma kierowcy takiego autobusu lub takiej rejestracji')
    elif driver.bus == driver_to_update:
        while True:
            new_registration = input('Podaj nową rejestrację ').upper
            registtration_check = session.query(Driver).filter(Driver.bus == new_registration).all()
            if len(registtration_check) != 0:
                print('Autobus zajęty')
            elif new_registration == '':
                break
            else:
                driver.bus = new_registration
                break 
        new_name = input('Podaj nowe imię ')
        if new_name != "":
            driver.name = new_name
        new_surname = input('Podaj nowe nazwisko ')
        if new_name != "":
            driver.surname = new_surname
        new_north = input('Podaj nową współrzędną X ')
        new_east = input('Podaj nową współrzędną Y ')
        if new_north !="" and new_east != "":
            driver.location = f'POINT({new_north} {new_east})'
    session.commit()
    
def delete_driver_by_line():
    choice = line_checker()
    driver_to_delete = input('Podaj nr rejestracyjny autobusu który prowadzi kierowca ')
    driver = session.query(Driver).filter(Driver.line == choice, Driver.bus == driver_to_delete).first()
    if driver is None:
        print('Nie ma kierowcy prowadzącego ten autobus lub takiego kierowcy')
    elif driver.bus == driver_to_delete:
        session.delete(driver)
    session.commit()
    
### Funkcje menu 4 ###

def create_passenger():
    create_ticket = input('Podaj nr biletu ')
    create_line = input('Podaj nr linii ')
    create_name = input('Podaj imię pasażera ')
    create_surname = input('Podaj nazwisko pasażera ')
    north = input('Podaj współrzędną X ')
    east = input('Podaj współrzędną Y ')
    passenger_to_create = Passenger(
        ticket = create_ticket,
        line = create_line,
        name = create_name,
        surname = create_surname,
        location = f'POINT({north} {east})')
    session.add(passenger_to_create)
    session.commit()

def read_passenger():
    passengers = session.query(Passenger).all()
    if len(passengers) == 0:
        print('\nBrak pasażerów do wyświetlenia\n')
    print('\nLista pasażerów:\n')
    for passenger in passengers:
        print(f'Nr biletu: {passenger.ticket}    nr linii: {passenger.line}   imię: {passenger.name} {passenger.surname}')
    session.commit()

def update_passenger():
    passanger_to_update = input('Podaj nr biletu do zmodyfikowania ')
    passanger = session.query(Passenger).filter(Passenger.ticket == passanger_to_update).first()
    if passanger is None:
        print('Nie ma takiego biletu')
    elif passanger.ticket == passanger_to_update:
        while True:
            new_ticket = input('Podaj nowy bilet ')
            ticket_check = session.query(Passenger).filter(Passenger.ticket == new_ticket).all()
            if len(ticket_check) != 0:
                print('Taki bilet już istnieje')
            elif new_ticket == '':
                break
            else:
                passanger.ticket = new_ticket
                break 
    while True:
        choice = input('Podaj nr linii ')
        check = session.query(Bus).filter(Bus.line == choice).all()
        if len(check) != 0:
            break
        else:
            print('Nie ma takiej linii, wybierz istniejącą ')
    passanger.line = choice
    new_name = input('Podaj nowe imię ')
    if new_name != "":
        passanger.name = new_name
    new_surname = input('Podaj nowe nazwisko ')
    if new_name != "":
        passanger.surname = new_surname
    new_north = input('Podaj nową współrzędną X ')
    new_east = input('Podaj nową współrzędną Y ')
    if new_north !="" and new_east != "":
        passanger.location = f'POINT({new_north} {new_east})'
    session.commit()
    
def delete_passenger():
    passenger_to_delete = input('Podaj nr biletu ')
    passenger = session.query(Passenger).filter(Passenger.ticket == passenger_to_delete).first()
    if passenger is None:
        print('Nie ma takiego biletu')
    elif passenger.ticket == passenger_to_delete:
        session.delete(passenger)
    session.commit()
    
### Funkcje menu nr 5 ###

def create_passenger_by_line():
    choice = line_checker()
    create_ticket = input('Podaj nr biletu ')
    create_name = input('Podaj imię pasażera ')
    create_surname = input('Podaj nazwisko pasażera ')
    north = input('Podaj współrzędną X ')
    east = input('Podaj współrzędną Y ')
    passenger_to_create = Passenger(
        ticket = create_ticket,
        line = choice,
        name = create_name,
        surname = create_surname,
        location = f'POINT({north} {east})')
    session.add(passenger_to_create)
    session.commit()

def read_passenger_by_line():
    choice = line_checker()
    passengers = session.query(Passenger).filter(Passenger.line == choice).all()
    if len(passengers) == 0:
        print('\nBrak pasażerów do wyświetlenia\n')
    print('\nLista pasażerów:\n')
    for passenger in passengers:
        print(f'Nr biletu: {passenger.ticket}    nr linii: {passenger.line}   imię: {passenger.name} {passenger.surname}')
    session.commit()

def update_passenger_by_line():
    choice = line_checker()
    passanger_to_update = input('Podaj nr biletu do zmodyfikowania ')
    passanger = session.query(Passenger).filter(Passenger.ticket == passanger_to_update, Passenger.line == choice).first()
    if passanger is None:
        print('Nie ma takiego biletu')
    elif passanger.ticket == passanger_to_update:
        while True:
            new_ticket = input('Podaj nowy bilet ')
            ticket_check = session.query(Passenger).filter(Passenger.ticket == new_ticket).all()
            if len(ticket_check) != 0:
                print('Taki bilet już istnieje')
            elif new_ticket == '':
                break
            else:
                passanger.ticket = new_ticket
                break 
    while True:
        new_line = input('Podaj nowy nr linii ')
        line_check = session.query(Bus).filter(Bus.line == new_line).all()
        if line_check is None:
            print('Taki bilet już istnieje')
        elif new_ticket != "":
            passanger.ticket = new_ticket
            break
        else:
            break 
    new_name = input('Podaj nowe imię ')
    if new_name != "":
        passanger.name = new_name
    new_surname = input('Podaj nowe nazwisko ')
    if new_name != "":
        passanger.surname = new_surname
    new_north = input('Podaj nową współrzędną X ')
    new_east = input('Podaj nową współrzędną Y ')
    if new_north !="" and new_east != "":
        passanger.location = f'POINT({new_north} {new_east})'
    session.commit()
    
def delete_passenger_by_line():
    choice = line_checker()
    passenger_to_delete = input('Podaj nr biletu ')
    passenger = session.query(Passenger).filter(Passenger.ticket == passenger_to_delete, Passenger.line == choice).first()
    if passenger is None:
        print('Nie ma takiego biletu')
    elif passenger.ticket == passenger_to_delete:
        session.delete(passenger)
    session.commit()

### DODATKOWE FUNKCJE ###

def line_checker():
    """_summary_
    loop function asking for input with line number to use then checks if the input exists in Bus(table) if True returns value
    Returns:
        _type_: string 
    """
    while True:
        choice = input('Podaj nr linii ')
        check = session.query(Bus).filter(Bus.line == choice).all()
        if len(check) != 0:
            break
        else:
            print('Nie ma takiej linii, wybierz istniejącą ')
    return choice

def registration_insert():
    registration_query = input('Podaj rejestracje ')
    registrations = session.query(Bus).filter(Bus.registration == registration_query).first()
    if registrations is not None:
        print('\n!Taka rejestracja już istnieje!\n')
        return False
    elif registration_query == "":
        print('\n!Rejestracja musi mieć znaki!\n')
        return False
    else:
        return registration_query