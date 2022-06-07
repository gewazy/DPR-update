import xlrd
import pyodbc
from datetime import date
from time import sleep
import init


plik = xlrd.open_workbook(init.DRILL_RAPORT)
raport = plik.sheet_by_index(-1)

print('Pobieram dane z raportu wiertnictwa')
sleep(1)

input("\nOstatni dzien w rapocie to: {} "
      "\nOdwiercili: {} otworów"
      "\nNaciśnij ENTER by kontynuować lub zamknij okno by anulować".format(raport.name, raport.nrows - 3))


sleep(0.3)

print("\nPrzetwarzam dane do wgrania?")
data = "{}-{}-{}".format('0' + raport.name.split('.')[0] if len(raport.name.split('.')[0]) == 1
                         else raport.name.split('.')[0], raport.name.split('.')[1], date.today().year)
print()

params = []
# formatowanie danych z raportu do prawidłowej postaci
for rw in range(3, raport.nrows):
    params.append((int(str(int(raport.row(rw)[1].value)) + str(int(raport.row(rw)[2].value))), raport.row(rw)[4].value,
                   raport.row(rw)[8].value, raport.row(rw)[9].value.upper(), data, None, ''))
sleep(0.2)
print('Wgrywam do tabeli Drilling_Tab dane:\n')
sleep(0.5)
for p in params:
    print(p)
    sleep(0.3)
sleep(1.5)

# łaczenie z bazą danych i wgranie danych

cnxn = pyodbc.connect(init.CONN_STR)  # łączenie z bazą danych
crsr = cnxn.cursor()
crsr.executemany("INSERT INTO Drilling_Tab (station, depth, dr_name, dr_eq, dr_date, status, Uwagi_Biuro) "
                 "VALUES (?, ?, ?, ?, ?, ?, ?);", params)
crsr.close()
cnxn.commit()
cnxn.close()

print('Gotowe! '
      '\nSprawdź czy baza danych została zaktualizowana!\n'
      '\nPamiętaj by skontrolować dane i zrobić update postplotu.\n')

input('Enter by zakończyć!')
