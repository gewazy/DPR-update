GRUPA = 'PL-186'

# pliki
## pliki wejsciowe
MDB = r"c:\PL-186_Zapalow_3D\01_database\Pl-186_Zapalow_3D.mdb"
DRILL_RAPORT = r"c:\PL-186_Zapalow_3D\09_wiertnictwo\Raport wiertnictwa PL186.xls"

## pliki wyjściowe
DPR = r"c:\PL-186_Zapalow_3D\08_raport_geodezyjny\PL_186_Raport_geodezyjny_DPR.xlsx"
JSON_FILE = r'.\output\line_station.json'
QC_DOMIAR_GPS = rf'.\output\{GRUPA}_QC_Domiar_GPS.csv'
QC_DOMIAR_ZUPT = rf'.\output\{GRUPA}_QC_Domiar_ZUPT.txt'
WZNAWIANIE_FILE = rf'.\output\{GRUPA}_max_indeks.txt'

# zakresy linii punktów strzałowych i geofonów
SOURCES_TRACK = "2064 And 2424"
RECEIVERS_TRACK = "3001 And 3761"

# w zależności kiedy robimy raport, domyślnie ddiff = 0
DDIFF = 0

# połączenie/łącznik do bazy danych
CONN_STR = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'  # sterownik mdb
            fr'DBQ={MDB};')



# descriptory
VIBRATORY_DSC = "('x40', 'x45', 'x30', 'x35', 'x20', 'x25', 'x10', 'x15', 'xm', 'xm5')"
DYNAMITY_DSC = "('xt', 'xr')"
