import pyodbc
import shapefile
import time

import init
import kury


start = time.perf_counter()

# pola do shp:
pola_post = ["w.field('Stationtex', 'C', size=16)", "w.field('Stationval', 'N', size=16, decimal=3)",
             "w.field('Track', 'N', size=16)", "w.field('Bin', 'N', size=16)", "w.field('Descriptor', 'C', size=32)",
             "w.field('SurveyMode', 'C', size=16)", "w.field('SurveyMod0', 'C', size=5)",
             "w.field('HI', 'N', size=16, decimal=3)", "w.field('OffsetInli', 'N', size=16, decimal=3)",
             "w.field('OffsetCros', 'N', size=16, decimal=3)", "w.field('NumberofSa', 'C', size=5)",
             "w.field('PDOP', 'N', size=16,decimal=3)", "w.field('JulianDate', 'N', size=16, decimal=0)",
             "w.field('SurveyTime', 'C', size=8)", "w.field('SurveyTim1', 'C',size=8)",
             "w.field('Comment', 'C', size=32)", "w.field('DownloadFi', 'C', size=32)",
             "w.field('ReceiverTy', 'C', size=32)", "w.field('ReceiverSN', 'C', size=32)",
             "w.field('NumberOfEp', 'N', size=16, decimal=3)", "w.field('Occupation', 'N', size=16,decimal=3)",
             "w.field('AcquiredJu', 'N', size=16,decimal=0)", "w.field('Indeks', 'N', size=8, decimal=0)",
             "w.field('Status', 'N', size=8, decimal=0)", "w.field('IsDuplicat', 'N', size=8,decimal=0)",
             "w.field('Surveyor', 'C', size=16)", "w.field('Descriptio', 'C', size=32)",
             "w.field('Descripti2', 'C', size=32)", "w.field('depth', 'C', size=8)",
             "w.field('drname', 'C', size=16)", "w.field('dreq', 'C', size=16)", "w.field('drdate', 'C', size=16)",
             "w.field('UwagiBiuro', 'C', size=64)", "w.field('PPV', 'C', size=10)",
             "w.field('IsNNjoin', 'N', size=8,decimal=0)"]

pola_pre = ["w.field('Stationtex', 'C', size=16)", "w.field('Stationval', 'N', size=16, decimal=3)",
            " w.field('Track', 'N', size=16)", "w.field('Bin', 'N', size=16)"]

pola_post_kr = ["w.field('Stationtex', 'C', size=16)", "w.field('Stationval', 'N', size=16, decimal=3)",
                "w.field('Track', 'N', size=16)", "w.field('Bin', 'N', size=16)", "w.field('Descriptor', 'C', size=32)",
                "w.field('JulianDate', 'N', size=16, decimal=0)", "w.field('Comment', 'C', size=32)",
                "w.field('Indeks', 'N', size=8, decimal=0)", "w.field('Status', 'N', size=8, decimal=0)",
                "w.field('IsDuplicat', 'N', size=8,decimal=0)", "w.field('Descriptio', 'C', size=32)",
                "w.field('Descripti2', 'C', size=32)", "w.field('UwagiBiuro', 'C', size=64)"]

pola_qc_domiar_s = ["w.field('Stationtex', 'C', size=16)",  "w.field('Stationval', 'N', size=16, decimal=3)",
               "w.field('Track', 'N', size=16)", "w.field('Bin', 'N', size=16)", "w.field('UwagiBiuro', 'C', size=64)",
               "w.field('Descriptor', 'C', size=32)", "w.field('SurveyMode', 'C', size=16)",
               "w.field('Status', 'N', size=8, decimal=0)", "w.field('Indeks', 'N', size=8, decimal=0)"]

pola_otg_t = ["w.field('id', 'N', size=32, decimal=3)", "w.field('Nazwa', 'C', size=16)"]


cnxn = pyodbc.connect(init.CONN_STR)  # łączenie z bazą danych
crsr = cnxn.cursor()

# tworzenie list z danymi
postplot_s = crsr.execute(kury.POSTPLOT_S).fetchall()
postplot_r = crsr.execute(kury.POSTPLOT_R).fetchall()
do_tyczenia_sp = crsr.execute(kury.DO_TYCZENIA_SP).fetchall()
do_tyczenia_rp = crsr.execute(kury.DO_TYCZENIA_RP).fetchall()
skipy_s = crsr.execute(kury.SKIP_S).fetchall()
skipy_r = crsr.execute(kury.SKIP_R).fetchall()
qc_domiar_r = crsr.execute(kury.QC_DOMIAR_R_SHP).fetchall()
qc_domiar_s = crsr.execute(kury.QC_DOMIAR_R_SHP).fetchall()
uwagi_geodetow = crsr.execute(kury.UWAGI_GEODEZJA).fetchall()
wystawki_all = crsr.execute(kury.WYSTAWKI).fetchall()
vibratory = crsr.execute(kury.VIBRATORY).fetchall()
dynamity = crsr.execute(kury.DYNAMITY).fetchall()

crsr.close()
cnxn.close()


# tworzenie szejfilow:
with shapefile.Writer('shp_files/Postplot (source)', shapeType=1) as w:
    for i in pola_post:
        eval(i)

    for item in postplot_s:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3], Descriptor=item[4],
                 SurveyMode=item[16], SurveyMod0=item[17], HI=item[18],  OffsetInli=item[23], OffsetCros=item[24],
                 NumberofSa=item[30], PDOP=item[31], JulianDate=item[34], SurveyTime=item[35], SurveyTim1=item[36],
                 Comment=item[45], DownloadFi=item[46], ReceiverTy=item[48], ReceiverSN=item[49], NumberOfEp=item[50],
                 Occupation=item[55], AcquiredJu=item[74], Indeks=item[75], Status=item[76], IsDuplicat=item[77],
                 Surveyor=item[79], Descriptio=item[80], Descripti2=item[81], depth=item[82], drname=item[83],
                 dreq=item[84], drdate=item[85], UwagiBiuro=item[87], PPV=item[88], IsNNjoin=item[90])


with shapefile.Writer('shp_files/Vibratory', shapeType=1) as w:
    for i in pola_post:
        eval(i)

    for item in postplot_s:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3], Descriptor=item[4],
                 SurveyMode=item[16], SurveyMod0=item[17], HI=item[18],  OffsetInli=item[23], OffsetCros=item[24],
                 NumberofSa=item[30], PDOP=item[31], JulianDate=item[34], SurveyTime=item[35], SurveyTim1=item[36],
                 Comment=item[45], DownloadFi=item[46], ReceiverTy=item[48], ReceiverSN=item[49], NumberOfEp=item[50],
                 Occupation=item[55], AcquiredJu=item[74], Indeks=item[75], Status=item[76], IsDuplicat=item[77],
                 Surveyor=item[79], Descriptio=item[80], Descripti2=item[81], depth=item[82], drname=item[83],
                 dreq=item[84], drdate=item[85], UwagiBiuro=item[87], PPV=item[88], IsNNjoin=item[90])


with shapefile.Writer('shp_files/Dynamity', shapeType=1) as w:
    for i in pola_post:
        eval(i)

    for item in dynamity:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3], Descriptor=item[4],
                 SurveyMode=item[16], SurveyMod0=item[17], HI=item[18],  OffsetInli=item[23], OffsetCros=item[24],
                 NumberofSa=item[30], PDOP=item[31], JulianDate=item[34], SurveyTime=item[35], SurveyTim1=item[36],
                 Comment=item[45], DownloadFi=item[46], ReceiverTy=item[48], ReceiverSN=item[49], NumberOfEp=item[50],
                 Occupation=item[55], AcquiredJu=item[74], Indeks=item[75], Status=item[76], IsDuplicat=item[77],
                 Surveyor=item[79], Descriptio=item[80], Descripti2=item[81], depth=item[82], drname=item[83],
                 dreq=item[84], drdate=item[85], UwagiBiuro=item[87], PPV=item[88], IsNNjoin=item[90])


with shapefile.Writer('shp_files/Postplot (receiver)', shapeType=1) as w:
    for i in pola_post:
        eval(i)

    for item in postplot_r:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3], Descriptor=item[4],
                 SurveyMode=item[16], SurveyMod0=item[17], HI=item[18], OffsetInli=item[23], OffsetCros=item[24],
                 NumberofSa=item[30], PDOP=item[31], JulianDate=item[34], SurveyTime=item[35], SurveyTim1=item[36],
                 Comment=item[45], DownloadFi=item[46], ReceiverTy=item[48], ReceiverSN=item[49], NumberOfEp=item[50],
                 Occupation=item[55], AcquiredJu=item[74], Indeks=item[75], Status=item[76], IsDuplicat=item[77],
                 Surveyor=item[79], Descriptio=item[80], Descripti2=item[81], depth=item[82], drname=item[83],
                 dreq=item[84], drdate=item[85], UwagiBiuro=item[87], PPV=item[88], IsNNjoin=item[90])


with shapefile.Writer('shp_files/Do tyczenia RP', shapeType=1) as w:
    for i in pola_pre:
        eval(i)

    for item in do_tyczenia_rp:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3])


with shapefile.Writer('shp_files/Do tyczenia SP', shapeType=1) as w:
    for i in pola_pre:
        eval(i)

    for item in do_tyczenia_sp:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3])


with shapefile.Writer('shp_files/SKIP S', shapeType=1) as w:
    for i in pola_post_kr:
        eval(i)

    for item in skipy_s:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3], Descriptor=item[4],
                 JulianDate=item[34], Comment=item[45], Indeks=item[75], Status=item[76], IsDuplicat=item[77],
                 Descriptio=item[80], Descripti2=item[81], UwagiBiuro=item[87])


with shapefile.Writer('shp_files/SKIP R', shapeType=1) as w:
    for i in pola_post_kr:
        eval(i)

    for item in skipy_r:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3], Descriptor=item[4],
                 JulianDate=item[34], Comment=item[45], Indeks=item[75], Status=item[76], IsDuplicat=item[77],
                 Descriptio=item[80], Descripti2=item[81], UwagiBiuro=item[87])


with shapefile.Writer('shp_files/QC_DOMIAR_RP', shapeType=1) as w:
    for i in pola_post_kr:
        eval(i)

    for item in qc_domiar_r:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3], Descriptor=item[4],
                 JulianDate=item[34], Comment=item[45], Indeks=item[75], Status=item[76], IsDuplicat=item[77],
                 Descriptio=item[80], Descripti2=item[81], UwagiBiuro=item[87])


with shapefile.Writer('shp_files/QC_DOMIAR_VP', shapeType=1) as w:
    for i in pola_qc_domiar_s:
        eval(i)

    for item in qc_domiar_s:
        w.point(item[4], item[5])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3], UwagiBiuro=item[6],
                 Descriptor=item[7], SurveyMode=item[8], Status=item[9], Indeks=item[10])


with shapefile.Writer('shp_files/UWAGI_GEODEZJA', shapeType=1) as w:
    for i in pola_post_kr:
        eval(i)

    for item in uwagi_geodetow:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3], Descriptor=item[4],
                 JulianDate=item[34], Comment=item[45], Indeks=item[75], Status=item[76], IsDuplicat=item[77],
                 Descriptio=item[80], Descripti2=item[81], UwagiBiuro=item[87])


with shapefile.Writer('shp_files/WYSTAWKI_all', shapeType=1) as w:
    for i in pola_post:
        eval(i)

    for item in wystawki_all:
        w.point(item[9], item[10])
        w.record(Stationtex=item[0], Stationval=item[1], Track=item[2], Bin=item[3], Descriptor=item[4],
                 SurveyMode=item[16], SurveyMod0=item[17], HI=item[18],  OffsetInli=item[23], OffsetCros=item[24],
                 NumberofSa=item[30], PDOP=item[31], JulianDate=item[34], SurveyTime=item[35], SurveyTim1=item[36],
                 Comment=item[45], DownloadFi=item[46], ReceiverTy=item[48], ReceiverSN=item[49], NumberOfEp=item[50],
                 Occupation=item[55], AcquiredJu=item[74], Indeks=item[75], Status=item[76], IsDuplicat=item[77],
                 Surveyor=item[79], Descriptio=item[80], Descripti2=item[81], depth=item[82], drname=item[83],
                 dreq=item[84], drdate=item[85], UwagiBiuro=item[87], PPV=item[88], IsNNjoin=item[90])


end = time.perf_counter()
run_time = end - start

print(f'Wykonano pliki SHP w: {run_time:.4f} sekund\n')