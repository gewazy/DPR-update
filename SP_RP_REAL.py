import pyodbc

# Plik RP_REAL i SP_REAL (csv)

print("\nŁączę z bazą danych")
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=..\01_database\PL-182 HUSOW.mdb;'  # ścieżka do bazy danych, do zmiany jeśli potrzeba
    )

postplot_s = "Select [POSTPLOT].`Station (value)`, " \
             "[POSTPLOT].`Local Easting`, " \
             "[POSTPLOT].`Local Northing`, " \
             "[POSTPLOT].`WGS84 Latitude`, " \
             "[POSTPLOT].`WGS84 Longitude`, " \
             "[POSTPLOT].`Local Height`," \
             "[POSTPLOT].`Descriptor`, " \
             "[POSTPLOT].`Indeks` " \
             "From [POSTPLOT] " \
             "Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between 4060 And 4550 And [POSTPLOT].`Status` >= 0  " \
             "Order By [POSTPLOT].`Station (value)`"
postplot_r = "Select [POSTPLOT].`Station (value)`, " \
             "[POSTPLOT].`Local Easting`, " \
             "[POSTPLOT].`Local Northing`, " \
             "[POSTPLOT].`WGS84 Latitude`, " \
             "[POSTPLOT].`WGS84 Longitude`, " \
             "[POSTPLOT].`Local Height`, " \
             "[POSTPLOT].`Indeks` " \
             "From [POSTPLOT] " \
             "Where  [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between 1175 And 1930  And [POSTPLOT].`Status` >=0 " \
             "Order By [POSTPLOT].`Station (text)`"

cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

crsr.execute(postplot_s)
postplot_s = crsr.fetchall()
crsr.execute(postplot_r)
postplot_r = crsr.fetchall()

cnxn.commit()
cnxn.close()

print(f'Punktów wzbudzania + SKIP: {len(postplot_s)}')
print(f'Punktów odbioru + SKIP: {len(postplot_r)}')

with open('.\\output\\SP_REAL_PL182.csv', 'w') as file:
    for row in postplot_s:
        file.write(f"{int(row[0])}-{row[7]},{format(round(row[1], 2), '.2f')},{format(round(row[2], 2), '.2f')},{format(round(row[5], 2), '.2f')},{row[6]}\n")
with open('.\\output\\RP_REAL_PL182.csv', 'w') as file:
    for row in postplot_r:
        file.write(f"{int(row[0])}-{row[6]},{format(round(row[1], 2), '.2f')},{format(round(row[2], 2), '.2f')},{format(round(row[5], 2), '.2f')},{row[6]}\n")

print('\nPliki SP i RP REAL gotowe!')
