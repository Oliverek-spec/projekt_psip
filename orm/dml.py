from orm.ddl import engine, Base, Bus, Driver, Passenger
import sqlalchemy.orm as orm


Session = orm.sessionmaker(bind=engine)
session = Session()

###Funkcje menu nr 1###

def create_bus():
    create_registration = input('Podaj rejestracje ')
    create_line = input('Podaj nr linii ')
    north = input('Podaj współrzędną X ')
    east = input('Podaj współrzędną Y ')
    bus_to_create = Bus(
        registration = create_registration,
        line = create_line,
        location = f'POINT({north} {east})')
    session.add(bus_to_create)
    session.commit()

def read_bus():
    buses = session.query(Bus).all()
    if len(buses) == 0:
        print('Brak autobusów do wyświetlenia')
    print('Lista autobusów:')
    for bus in buses:
        print(f'Nr rejestracyjny: {bus.registration}    nr linii: {bus.line}')
    session.commit()

def update_bus():
    bus_to_update = input('Podaj nr rejestracyjny autobusu do zmodyfikowania ')
    bus = session.query(Bus).filter(Bus.registration == bus_to_update).first()
    if bus is None:
        print('Nie ma autobusu o takiej rejestracji')
    elif bus.registration == bus_to_update:
        while True:
            new_registration = input('Podaj nową rejestrację ')
            registtration_check = session.query(Bus).filter(Bus.registration == new_registration).all()
            if len(registtration_check) != 0:
                print('Rejestracja zajęta')
            elif new_registration == '':
                break
            else:
                bus.registration = new_registration
                break 
        new_line = input('Podaj nowy nr linii ')
        if new_line != "":
            bus.line = new_line
        new_north = input('Podaj nową współrzędną X ')
        new_east = input('Podaj nową współrzędną Y ')
        if new_north !="" and new_east != "":
            bus.location = f'POINT({new_north} {new_east})'
    session.commit()
    
def delete_bus():
    bus_to_delete = input('Podaj nr rejestracyjny autobusu do usunięcia ')
    bus = session.query(Bus).filter(Bus.registration == bus_to_delete).first()
    if bus is None:
        print('Nie ma autobusu o takiej rejestracji')
    elif bus.registration == bus_to_delete:
        session.delete(bus)
    session.commit()

### Funkcje menu nr 2 ###

def create_driver():
    create_bus = input('Podaj rejestrację prowadzonego autobusu ')
    create_line = session.query(Bus).filter(Bus.registration == create_bus).first()
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
        print('Brak kierowców do wyświetlenia')
    print('Lista kierowców:')
    for driver in drivers:
        print(f'Nr rejestracyjny: {driver.bus}    nr linii: {driver.line}   imię: {driver.name} {driver.surname}')
    session.commit()

def update_driver():
    driver_to_update = input('Podaj nr rejestracyjny autobusu który prowadzi kierowca ')
    driver = session.query(Driver).filter(Driver.bus == driver_to_update).first()
    if driver is None:
        print('Nie ma kierowcy takiego autobusu lub takiej rejestracji')
    elif driver.bus == driver_to_update:
        while True:
            new_registration = input('Podaj nową rejestrację ')
            registtration_check = session.query(Driver).filter(Driver.bus == new_registration).all()
            if len(registtration_check) != 0:
                print('Autobus zajęty')
            elif new_registration == '':
                break
            else:
                driver.bus = new_registration
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
    while True:
        choice = input('Podaj nr linii ')
        check = session.query(Bus).filter(Bus.line == choice).all()
        if len(check) != 0:
            break
        else:
            print('Nie ma takiej linii, wybierz istniejącą ') 
    create_bus = session.query(Bus).filter(Bus.line == choice).first()
    create_name = input('Podaj imię kierowcy ')
    create_surname = input('Podaj nazwisko kierowcy ')
    north = input('Podaj współrzędną X ')
    east = input('Podaj współrzędną Y ')
    driver_to_create = Driver(
        bus = create_bus.registration,
        line = choice, 
        name = create_name,
        surname = create_surname,
        location = f'POINT({north} {east})')
    session.add(driver_to_create)
    session.commit()


def read_driver_by_line():
    while True:
        choice = input('Podaj nr linii ')
        check = session.query(Bus).filter(Bus.line == choice).all()
        if len(check) != 0:
            break
        else:
            print('Nie ma takiej linii, wybierz istniejącą ') 
    drivers = session.query(Driver).filter(Driver.line == choice).all()
    if len(drivers) == 0:
        print('Brak kierowców do wyświetlenia')
    print('Lista kierowców:')
    for driver in drivers:
        print(f'Nr rejestracyjny: {driver.bus}    nr linii: {driver.line}   imię: {driver.name} {driver.surname}')
    session.commit()

def update_driver_by_line():
    while True:
        choice = input('Podaj nr linii ')
        check = session.query(Bus).filter(Bus.line == choice).all()
        if len(check) != 0:
            break
        else:
            print('Nie ma takiej linii, wybierz istniejącą ') 
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
    while True:
        choice = input('Podaj nr linii ')
        check = session.query(Bus).filter(Bus.line == choice).all()
        if len(check) != 0:
            break
        else:
            print('Nie ma takiej linii, wybierz istniejącą ')
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
        print('Brak pasażerów do wyświetlenia')
    print('Lista pasażerów:')
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
    
def delete_passenger():
    passenger_to_delete = input('Podaj nr biletu ')
    passenger = session.query(Passenger).filter(Passenger.ticket == passenger_to_delete).first()
    if passenger is None:
        print('Nie ma takiego biletu')
    elif passenger.ticket == passenger_to_delete:
        session.delete(passenger)
    session.commit()
    