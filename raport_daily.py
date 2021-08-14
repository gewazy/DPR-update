import openpyxl
import pyodbc
from datetime import date

'''Generowanie raportu z 'dniówką' '''

print(f"Raport dniówkowy z dnia:"
      f"{str(date.today().strftime('%Y%m%d'))}"
      f"\n\nTworzę połaczenie z bazą danych\n"
      f"\nwysyłam zapytanie o dane\n")

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=..\01_database\PL-182 HUSOW.mdb;'  # ścieżka do bazy danych, do zmiany jeśli potrzeba
    )

cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

# dane z bazy, jak trzeba popraw kwerendę
qra = "Select " \
      "`Station (text)`, `Station (value)`, " \
      "`Track`, `Bin`, " \
      "`Descriptor`, `Description1`, `Description2`, `Comment`, " \
      "`Survey Time (Local)`, `Survey Mode (text)`, `Surveyor` " \
      "From [POSTPLOT] " \
      "Where " \
      "(datediff ('d', `Survey Time (Local)`,Now()) = 0) And " \
      "(" \
      "(`Station (value)` > 0 and `Station (text)` Not Like '88%') " \
      "OR `Station (text)` Like 'cp%' " \
      "OR `Station (text)` Like '?88%'" \
      ")  " \
      "Order By `Surveyor`,`Survey Time (Local)`"

crsr.execute(qra)
std = crsr.fetchall()

crsr.close()
cnxn.close()

print('\nTworzę plik Excel')

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['Station (text)', 'Station (value)', 'Track', 'Bin', 'Descriptor',
           'Description1', 'Description2', 'Comment', 'Survey Time (Local)',
           'Survey Mode (text)', 'Surveyor'])

for row in std:
    ws.append(item for item in row)

print(f"Zapisałem {len(std)} wierszy do pliku {str(date.today().strftime('%Y%m%d'))}.xlsx")


wb.save(f"./output/dniowki/{str(date.today().strftime('%Y%m%d'))}.xlsx")

print('\nGotowe')
input("\nEnter by zakończyć")
