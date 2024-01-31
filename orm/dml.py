from ddl import engine, Base, Bus, Driver, Passenger
import sqlalchemy.orm as orm


Session = orm.sessionmaker(bind=engine)
session = Session()

###Funkcje menu nr 1###

def create_bus():
    create_registration = input('Podaj rejestracje ')
    create_line = input('Podaj nr linii ')
    north = input('Podaj współrzędną X')
    east = input('Podaj współrzędną Y')
    bus_to_create = Bus(
        registration = create_registration,
        line = create_line,
        location = f'POINT({north} {east})')
    session.add(bus_to_create)
    session.commit()

def read_bus():
    buses = session.query(Bus).all()
    if buses == None:
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
    north = input('Podaj współrzędną X')
    east = input('Podaj współrzędną Y')
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
    if drivers == None:
        print('Brak kierowców do wyświetlenia')
    print('Lista kierowców:')
    for driver in drivers:
        print(f'Nr rejestracyjny: {driver.bus}    nr linii: {driver.line}   imię: {driver.name} nazwisko: {driver.surname}')
    session.commit()

def update_driver():
    driver_to_update = input('Podaj nr rejestracyjny autobusu do zmodyfikowania ')
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
        driver.line = new_line
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
