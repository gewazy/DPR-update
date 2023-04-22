import pyodbc


def comment(a):
    '''Zapytanie o komentarz do raportu DPR'''
    return a + input(f"\nWprowadź komentarz: \n{a}")


def ddiff():
    '''Zapytanie  o dzień, z którego chemy zrobić raport'''
    return int(input('Wpisz Daydiff:\n 0 -> dzisiejsze dane, 1-> dane wczorajsze:\n'))

# Dane podstawowe:
GRUPA = 'PL192'
GEODETA = "Dominik Jurkowski"
ZUPT_BRYG = '[Goleń, Szatkowski], [Krawczyk, Dyja], [Istal, Nizioł]\n'
KOMENTARZ = 'Mało dróg, istniejące drogi trudne i niebezpieczne, długie przejścia. Bardzo dalekie dojazdy (ponad 1h) '
DDIFF = ddiff()
## ************************* PLIKI *********************************************

## pliki wejsciowe
MDB = r"c:\PL-192_Dylagowa_3D\05_database\PL-192_DYLAGOWA_3D.mdb"
DRILL_RAPORT = r"c:\PL-192_Dylagowa_3D\09_wiertnictwo\Raport wiertnictwa PL192.xls"

## pliki wyjściowe
DPR = (r'c:\PL-192_Dylagowa_3D\06_raporty\\PL-192_Raport_geodezyjny_dzienny.xlsx',
       r'c:\PL-192_Dylagowa_3D\06_raporty\\2023 PL-192 raport geodezja.xlsm')
JSON_FILE = r'.\output\line_station.json'
QC_DOMIAR_GPS = rf'.\output\{GRUPA}_QC_Domiar_GPS.csv'
QC_DOMIAR_ZUPT = rf'.\output\{GRUPA}_QC_Domiar_ZUPT.txt'
WZNAWIANIE_FILE = rf'.\output\{GRUPA}_max_indeks.txt'


# ***********************ZMIENNE PODSTAWOWE ************************************

# zakresy linii punktów strzałowych i geofonów
SOURCES_TRACK = "2210 And 2980"
RECEIVERS_TRACK = "1001 And 1505"


# descriptory
VIBRATORY_DSC = "('x40', 'x45', 'x30', 'x35', 'x20', 'x25', 'x10', 'x15', 'xm', 'xm5')"
DYNAMITY_DSC = "('xt', 'xr')"

# redukcja wysokości dla wibratorów
REDUKCJA = 2.75

# *********************** STEROWNIK MDB oraz łączenie z bazą danych ************

sterownik = [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]

if not sterownik:
    print('Brak zainstalowanych sterowników do MDB,\n'
          '- zainstaluj lub zaktualizuj MS Office do wersji 64 bit.\n'
          '- możesz również zainstalować Microsoft Access Database Engine 2010 Redistributable:\n'
          '  https://www.microsoft.com/en-US/download/details.aspx?id=13255')
    input('Enter by zakończyć')
else:
    CONN_STR = (r'DRIVER={' + sterownik[0] + '};' + fr'DBQ={MDB};')  # sterownik mdb


# *********************** ADRESY EMAIL *****************************************

SENDER = f"{GRUPA}surveyor@geofizyka.pl"
SUPERVISOR = 'ibort@o2.pl'
RECIPIENT_DPR = (f"{GRUPA}partychief@geofizyka.pl",
                 "Wojciech.Burczynski@geofizyka.pl", "maciej.gruza@geofizyka.pl",
                 "tomasz.stankiewicz@geofizyka.pl", "ryszard.kolacz@geofizyka.pl", "renata.ciechanska@geofizyka.pl",
                 "andrzej.czemerzynski@geofizyka.pl", f"{GRUPA}geophysicist@geofizyka.pl")
RECIP_JSON = (f"{GRUPA}transcriber@geofizyka.pl", f"{GRUPA}lineboss@geofizyka.pl", "Slawomir.Bloniarz@geofizyka.pl")


if __name__ == "__main__":
    print('Plik przechowuje podstawowe parametry')
