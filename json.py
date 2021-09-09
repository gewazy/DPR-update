import pyodbc

'''Przygotowanie pliku json dla transcribera'''

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=..\01_database\PL-182 HUSOW.mdb;'  # ścieżka do bazy danych, do zmiany jeśli potrzeba
    )

cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

# dane dzienne z bazy jak trzeba popraw kwerendę
qra = "Select " \
      "`Track`, `Bin`, `WGS84 Longitude`, `WGS84 Latitude`" \
      "From [POSTPLOT] " \
      "Where " \
      "([POSTPLOT].`Track`>=1175) And ([POSTPLOT].`Track`<=1930) " \
      "And ([POSTPLOT].`Station (value)`>0 And [POSTPLOT].`Status` > 0 ) " \
      "Order By [POSTPLOT].`Station (value)`, [POSTPLOT].`Survey Time (Local)`"

qc_s = "Select [POSTPLOT].`Station (value)`, " \
       "IIF (([POSTPLOT].`Status` = 3 or [POSTPLOT].`Status` =4 or [POSTPLOT].`Status` =5) ,[POSTPLOT].`COG Local Easting`,[POSTPLOT].`Local Easting`) AS `Easting`," \
       "IIF (([POSTPLOT].`Status` = 3 or [POSTPLOT].`Status` =4 or [POSTPLOT].`Status` =5),[POSTPLOT].`COG Local Northing`,[POSTPLOT].`Local Northing`) AS `Northing`, " \
       "IIF (([POSTPLOT].`Status` = 3 or [POSTPLOT].`Status` =4 or [POSTPLOT].`Status` =5),[POSTPLOT].`COG WGS Latitude`, [POSTPLOT].`WGS84 Latitude`) AS `Latitude`," \
       "IIF (([POSTPLOT].`Status` = 3 or [POSTPLOT].`Status` =4 or [POSTPLOT].`Status` =5),[POSTPLOT].`COG WGS Longitude`,[POSTPLOT].`WGS84 Longitude`) AS `Longitude`," \
       "[POSTPLOT].`Local Height`," \
       "[POSTPLOT].`Descriptor`, " \
       "[POSTPLOT].`Indeks` " \
       "From [POSTPLOT] " \
       "Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between 4060 And 4550 And (([POSTPLOT].`Status` IN (2,4) And [POSTPLOT].`Survey Mode (value)` Not In (3,5,6)) Or ([POSTPLOT].`Status` IN (2,4)  And  [POSTPLOT].`Survey Mode (value)` In (3) And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3) )  or [POSTPLOT].`Status` = 5 or [POSTPLOT].`Status` = 6 ) " \
       "Order By [POSTPLOT].`Station (value)`"

qc_r = "Select [POSTPLOT].`Station (value)`, [POSTPLOT].`Local Easting`, [POSTPLOT].`Local Northing`, [POSTPLOT].`WGS84 Latitude`, [POSTPLOT].`WGS84 Longitude`, [POSTPLOT].`Local Height`, [POSTPLOT].`Indeks`" \
       " From [POSTPLOT] " \
       "Where  [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between 1175 And 1930  And [POSTPLOT].`Status` >=1 And [POSTPLOT].`Status` <= 11 And (( [POSTPLOT].`Survey Mode (value)` Not In (3,5,6) ) Or ( [POSTPLOT].`Survey Mode (value)` = 3 And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3) ))  " \
       "Order By [POSTPLOT].`Station (text)`"

wzn = "Select [POSTPLOT].`Station (value)`, [POSTPLOT].`Local Easting`, [POSTPLOT].`Local Northing` " \
      "From [POSTPLOT], " \
      "(Select [POSTPLOT].`Station (value)` as `Station` , Count(*) as `ilosc`  From [POSTPLOT] Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between 1175 And 1930 Group by [POSTPLOT].`Station (value)` ) as MxInd " \
      "Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between 1175 And 1930 AND [POSTPLOT].`Station (value)` = MxInd.`Station` AND [POSTPLOT].`Indeks` = MxInd.`ilosc` Order By [POSTPLOT].`Station (value)`"


# Listy z dnymi z zapytań
dane = crsr.execute(qra).fetchall()
qc_s = crsr.execute(qc_s).fetchall()
qc_r = crsr.execute(qc_r).fetchall()
wzn = crsr.execute(wzn).fetchall()


cnxn.commit()
cnxn.close()

with open('.\\output\\line_station.json', 'w') as file:
    file.write('{"locations":[\n')
    for row in dane[:-1]:
        file.write('{' + f'"line":{row[0]}.0,"station":{row[1]}.0,"longitude":{format(row[2], ".8f")},"latitude":{format(row[3], ".9f")}' + '},\n')
    file.write('{' + f'"line":{dane[-1][0]}.0,"station":{dane[-1][1]}.0,"longitude":{format(dane[-1][2], ".8f")},"latitude":{format(dane[-1][3], ".9f")}' + '}]}')
print('\nPlik Json gotowy')
print("Tworzę pliki do domiaru:")
print(f'-Punktów wzbudzania do domiaru: {len(qc_s)}')
print(f'-Punktów odbioru do domiaru: {len(qc_r)}')

with open('.\\output\\PL182_QC_Domiar_GPS.csv', 'w') as file:
    for row in qc_s:
        file.write(f"{int(row[0])}-{row[7]},{format(round(row[1], 2), '.2f')},{format(round(row[2], 2), '.2f')},{format(round(row[5], 2), '.2f')},{row[6]}\n")
    for row in qc_r:
        file.write(f"{int(row[0])}-{row[6]},{format(round(row[1], 2), '.2f')},{format(round(row[2], 2), '.2f')},{format(round(row[5], 2), '.2f')},{row[6]}\n")

print('\nPlik PL182_QC_Domiar_GPS.csv gotowy!')

# ZUPT
try:
    with open('.\\output\\PL182_QC_Domiar_ZUPT.txt', 'w') as file:
        for row in qc_s:
            file.write(f"{int(row[0])}-{row[7]} {format(round(row[3], 8), '.8f')} {format(round(row[4], 8), '.8f')} 0.00 0 7 1 0 \n")
        for row in qc_r:
            file.write(f"{int(row[0])}-{int(row[6])} {format(round(row[3], 8), '.8f')} {format(round(row[4], 8), '.8f')} 0.00 0 7 1 0 \n")
except TypeError:
    print('\nCHYBA ZAPOMNIAŁEŚ POLICZYĆ COG WGS!!')
else:
    print('\nPlik PL182_QC_Domiar_ZUPT.txt gotowy!')


# Do wznawiania csv
with open('.\\output\\PL182_max_indeks.csv', 'w') as file:
    for row in wzn:
        file.write(f"{int(row[0])},{format(round(row[1], 2), '.2f')},{format(round(row[2], 2), '.2f')}\n")

print('Plik PL182_max_indeks.csv gotowy')
