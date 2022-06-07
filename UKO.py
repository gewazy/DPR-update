import pyodbc
from datetime import datetime
import init
import kury

'''Przygotowanie pliku UKO'''

cnxn = pyodbc.connect(init.CONN_STR)
crsr = cnxn.cursor()

uko = crsr.execute(kury.UKO).fetchall()

cnxn.commit()
cnxn.close()

print("Tworzę plik UKO!")

# Zapisanie pliku UKO, gdy jest wymiana, zakomentuj i użyj następnego kawałka kodu
with open(f".\\output\\uko\\{str(datetime.now().strftime('%Y%m%d_%H%M'))}.uko", 'w') as file:
    for item in uko:
        file.write(
            f'{item[0]}{item[1]}{13 * " "}{item[2]}{25 * " "}{round(float(item[3]), 1)} {round(float(item[4]), 1)}  {round(float(item[5]), 1)} {item[6] if len(item[6]) > 1 else str(item[6]) + "  "}   {int(item[7])}\n')

'''
# odkomentować jak już vbędzie wymiana..
try:
    with open(f"\\\\192.168.46.92\\Public\\!!!_Geodezja\\UKO\\{str(datetime.now().strftime('%Y%m%d_%H%M'))}.uko", 'w') as file:
        for item in uko:
            file.write(f'{item[0]}{item[1]}{13*" "}{item[2]}{25*" "}{round(float(item[3]), 1)} {round(float(item[4]), 1)}  {round(float(item[5]), 1)} {item[6] if len(item[6]) > 1 else str(item[6])+"  " }   {int(item[7])}\n')
except FileNotFoundError:
    with open(f".\\output\\uko\\{str(datetime.now().strftime('%Y%m%d_%H%M'))}.uko", 'w') as file:
        for item in uko:
            file.write(f'{item[0]}{item[1]}{13*" "}{item[2]}{25*" "}{round(float(item[3]), 1)} {round(float(item[4]), 1)}  {round(float(item[5]), 1)} {item[6] if len(item[6]) > 1 else str(item[6])+"  " }   {int(item[7])}\n')
'''

input("Uko gotowe\nEnter by zakończyć")
