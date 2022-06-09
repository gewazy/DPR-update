import init

'''Zapytania SQL'''

# muszę sprawdzić czy jest potrzeba rozbijac kwerendy qcS i qcR

''' Zapytania do raportu DPR '''
TYCZ_R = f"Select " \
         "[Ludziki].`Nr_auta`,  " \
         "'1', " \
         "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))) & ' ' & [POSTPLOT].`Surveyor`, " \
         "Count (*) " \
         "From " \
         "[POSTPLOT] Left Join [Ludziki] on [POSTPLOT].`Surveyor`=[Ludziki].`Surveyor` " \
         "Where " \
         "[POSTPLOT].`Offset (North)` is not NULL " \
         "and `IsDuplicate` is NULL " \
         "And [POSTPLOT].`Station (value)` > 0 " \
         f"And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} " \
         f"And datediff('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
         "Group By " \
         "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))), " \
         "[POSTPLOT].`Surveyor`, " \
         "[POSTPLOT].`Julian Date (Local)`, " \
         "[Ludziki].`Nr_auta`"

TYCZ_S = f"Select " \
         "[Ludziki].`Nr_auta`, " \
         " '1', " \
         "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))) & ' ' & [POSTPLOT].`Surveyor`, " \
         "Count (*) " \
         "From " \
         "[POSTPLOT] Left Join [Ludziki] on [POSTPLOT].`Surveyor`=[Ludziki].`Surveyor` " \
         "Where " \
         "[POSTPLOT].`Offset (North)` is not NULL " \
         "and `IsDuplicate` is NULL " \
         "And [POSTPLOT].`Station (value)` > 0 " \
         f"And  [POSTPLOT].`Track` Between {init.SOURCES_TRACK}" \
         f"And datediff ('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
         "Group By " \
         "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))), " \
         "[POSTPLOT].`Surveyor`, " \
         "[POSTPLOT].`Julian Date (Local)`, " \
         "[Ludziki].`Nr_auta`"

ZM_R = f"Select " \
       "[Ludziki].`Nr_auta`,  " \
       "'1' , " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))) & ' ' & [POSTPLOT].`Surveyor` , " \
       "Count (*) " \
       "From " \
       "[POSTPLOT] Left Join [Ludziki] on [POSTPLOT].`Surveyor`=[Ludziki].`Surveyor` " \
       "Where " \
       "[POSTPLOT].`Offset (North)` is not NULL " \
       "and `IsDuplicate` is not NULL " \
       "And [POSTPLOT].`Station (value)` > 0 " \
       f"And  [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK}" \
       f"And datediff ('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
       "Group By " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))), " \
       "[POSTPLOT].`Surveyor`, " \
       "[POSTPLOT].`Julian Date (Local)`, " \
       "[Ludziki].`Nr_auta`"

ZM_S = f"Select " \
       "[Ludziki].`Nr_auta`,  " \
       "'1', " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))) & ' ' & [POSTPLOT].`Surveyor`, " \
       "Count (*) " \
       "From " \
       "[POSTPLOT] Left Join [Ludziki] on [POSTPLOT].`Surveyor`=[Ludziki].`Surveyor` " \
       "Where " \
       "[POSTPLOT].`Offset (North)` is not NULL " \
       "and `IsDuplicate` is not NULL " \
       "And [POSTPLOT].`Station (value)` > 0 " \
       f"And  [POSTPLOT].`Track` Between {init.SOURCES_TRACK}" \
       f"And datediff ('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
       "Group By " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))), " \
       "[POSTPLOT].`Surveyor`, " \
       "[POSTPLOT].`Julian Date (Local)`, " \
       "[Ludziki].`Nr_auta`"

RE_S = "Select " \
       "[Ludziki].`Nr_auta`, " \
       " '1' , " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))) & ' ' & [REMEASURE].`Surveyor` , " \
       "Count (*) " \
       "From " \
       "[REMEASURE] Left Join [Ludziki] on [REMEASURE].`Surveyor`=[Ludziki].`Surveyor` " \
       "Where " \
       "[REMEASURE].`Offset (North)` is not NULL " \
       "and `IsDuplicate` is NULL " \
       "And [REMEASURE].`Station (value)` > 0 " \
       f"And  [REMEASURE].`Track` Between {init.SOURCES_TRACK} " \
       f"And datediff ('d',[REMEASURE].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
       "Group By " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))), " \
       "[REMEASURE].`Surveyor`, " \
       "[REMEASURE].`Julian Date (Local)`, " \
       "[Ludziki].`Nr_auta`"

RE_R = "Select " \
       "[Ludziki].`Nr_auta`,  " \
       "'1', " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))) & ' ' & [REMEASURE].`Surveyor`, " \
       "Count (*) " \
       "From " \
       "[REMEASURE] Left Join [Ludziki] on [REMEASURE].`Surveyor`=[Ludziki].`Surveyor` " \
       "Where " \
       "[REMEASURE].`Offset (North)` is not NULL " \
       "and `IsDuplicate` is NULL " \
       "And [REMEASURE].`Station (value)` > 0 " \
       f"And [REMEASURE].`Track` Between {init.RECEIVERS_TRACK} " \
       f"And datediff('d',[REMEASURE].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
       "Group By " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))), " \
       "[REMEASURE].`Surveyor`, " \
       "[REMEASURE].`Julian Date (Local)`, " \
       "[Ludziki].`Nr_auta`"

OTG = "Select " \
      "[Ludziki].`Nr_auta`,  " \
      "'1', " \
      "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))) & ' ' & [OTG].`Surveyor`, " \
      "Count (*) " \
      "From " \
      "[OTG] Left Join [Ludziki] on [OTG].`Surveyor`=[Ludziki].`Surveyor` " \
      "Where " \
      "[OTG].`Station (value)` > 0 " \
     f"And datediff('d',[OTG].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
      "Group By " \
      "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))), " \
      "[OTG].`Surveyor`, " \
      "[OTG].`Julian Date (Local)`, " \
      "[Ludziki].`Nr_auta`"

QC_R = "Select [POSTPLOT].`Station (value)`, [POSTPLOT].`Local Easting`, [POSTPLOT].`Local Northing`, [POSTPLOT].`WGS84 Latitude`, [POSTPLOT].`WGS84 Longitude`, [POSTPLOT].`Local Height`, [POSTPLOT].`Indeks`" \
       "From [POSTPLOT] " \
      f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} And [POSTPLOT].`Status` >=1 And [POSTPLOT].`Status` <= 11 And (([POSTPLOT].`Survey Mode (value)` Not In (3,5,6)) Or ([POSTPLOT].`Survey Mode (value)` = 3 And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3)))" \
       "Order By [POSTPLOT].`Station (text)`"

QC_S = "Select [POSTPLOT].`Station (value)`, " \
       "IIF ([POSTPLOT].`Status` in (3, 4, 5), [POSTPLOT].`COG Local Easting`, [POSTPLOT].`Local Easting`) AS `Easting`," \
       "IIF ([POSTPLOT].`Status` in (3, 4, 5), [POSTPLOT].`COG Local Northing`, [POSTPLOT].`Local Northing`) AS `Northing`," \
       "IIF ([POSTPLOT].`Status` in (3, 4, 5), [POSTPLOT].`COG WGS Latitude`, [POSTPLOT].`WGS84 Latitude`) AS `Latitude`," \
       "IIF ([POSTPLOT].`Status` in (3, 4, 5), [POSTPLOT].`COG WGS Longitude`, [POSTPLOT].`WGS84 Longitude`) AS `Longitude`," \
       "[POSTPLOT].`Local Height`," \
       "[POSTPLOT].`Descriptor`, " \
       "[POSTPLOT].`Indeks` " \
       "From [POSTPLOT] " \
      f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK} And (([POSTPLOT].`Status` IN (2,4) And [POSTPLOT].`Survey Mode (value)` Not In (3,5,6)) Or ([POSTPLOT].`Status` IN (2,4) And [POSTPLOT].`Survey Mode (value)` In (3) And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3)) or [POSTPLOT].`Status` in (5, 6))" \
       "Order By [POSTPLOT].`Station (value)`"

VIB = "Select [POSTPLOT].* From [POSTPLOT] " \
     f"Where  [POSTPLOT].`Status` <> 0 And  [POSTPLOT].`Track` Between {init.SOURCES_TRACK}  And [POSTPLOT].`Station (value)` > 0 " \
     f"And (([POSTPLOT].`Descriptor` in {init.VIBRATORY_DSC} OR ([POSTPLOT].`Descriptor` in {init.DYNAMITY_DSC} and [POSTPLOT].`Status` in (3,4,5)))) " \
      "Order By [POSTPLOT].`Station (value)`"

XR = f"Select [POSTPLOT].* From [POSTPLOT] Where [POSTPLOT].`Status` <> 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK}  " \
      "And [POSTPLOT].`Station (value)`<> 0 And (([POSTPLOT].`Descriptor` Like 'xr' And [POSTPLOT].`dr_date` is NULL) OR ([POSTPLOT].`dr_date` is not NULL And ([POSTPLOT].`dr_eq` Like 'EMCI' Or [POSTPLOT].`dr_eq` Like  'LPHB'))) And [POSTPLOT].`Status` not in (3,4,5) Order By [POSTPLOT].`Station (value)`"

XT = "Select [POSTPLOT].* From [POSTPLOT] " \
    f"Where [POSTPLOT].`Status` <> 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK} And [POSTPLOT].`Station (value)`<>0 And (([POSTPLOT].`Descriptor` Like 'xt' " \
     "And [POSTPLOT].`dr_date` is NULL) OR ([POSTPLOT].`dr_date` is not NULL And [POSTPLOT].`dr_eq` Like 'PAT')) And [POSTPLOT].`Status` not in (3,4,5) " \
     "Order By [POSTPLOT].`Station (value)`"

PATERNY = f"Select [POSTPLOT].* From [POSTPLOT] " \
          f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK} And [POSTPLOT].`Descriptor` in {init.DYNAMITY_DSC} and [POSTPLOT].`depth` like '%x%'" \
          f"Order By [POSTPLOT].`Station (value)`"


'''zapytania do bazy danych (SHP, UKOOA, JSON, etc)'''
UKO = "Select " \
     f"IIF (([PREPLOT].`Track` Between {init.RECEIVERS_TRACK}), 'G', 'S')," \
      "[PREPLOT].`Track`," \
      "([PREPLOT].`Bin`), " \
      "IIF (([POSTPLOT].`Station (value)` not like '%' Or [POSTPLOT].`Status`=0),[PREPLOT].`Local Easting`, IIF([POSTPLOT].`Status` in (1, 2, 6, 12, 22), [POSTPLOT].`Local Easting`, [POSTPLOT].`COG Local Easting`))," \
      "IIF (([POSTPLOT].`Station (value)` not like '%' Or [POSTPLOT].`Status`=0),[PREPLOT].`Local Northing`, IIF([POSTPLOT].`Status` in (1, 2, 6, 12, 22), [POSTPLOT].`Local Northing`, [POSTPLOT].`COG Local Northing`))," \
      "IIF (([POSTPLOT].`Station (value)` not like '%' OR [POSTPLOT].`Status`=0), [PREPLOT].`NMT`, IIF([POSTPLOT].`Status` In (3,5) ,[POSTPLOT].`COG Local Height`, IIF ([POSTPLOT].`Status` in (1, 2, 4, 6), [POSTPLOT].`Local Height`, IIF([POSTPLOT].`Status` in (12, 22), [POSTPLOT].`NMT`, [POSTPLOT].`COG NMT`))))," \
     f"IIF ([POSTPLOT].`Station (value)` not like '%', '1', IIF(( [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK}),[POSTPLOT].`Indeks` & '  ', IIF((([POSTPLOT].`Descriptor` like 'xt') or ([POSTPLOT].`Descriptor` like 'xz') or ([POSTPLOT].`Descriptor` like 'xr')), [POSTPLOT].`Indeks` & ' ' &'D',IIF (([POSTPLOT].`Descriptor` like 'x%'),([POSTPLOT].`Indeks` & ' ' & 'V'), ([POSTPLOT].`Indeks` & '  ')))))," \
     f"IIF ([POSTPLOT].`Status` in (1, 12), 1, IIF ([POSTPLOT].`Status`>1 , IIF([PREPLOT].`Track` Between {init.RECEIVERS_TRACK}, 1, 2), IIF ([POSTPLOT].`Status`= 0, '0', '10')))" \
      "From " \
      "[POSTPLOT] Right Join [PREPLOT] On [POSTPLOT].`Station (value)`=[PREPLOT].`Station (value)` " \
      "Where " \
     f"([PREPLOT].`Track` Between {init.RECEIVERS_TRACK}  ) Or (([PREPLOT].`Track` Between {init.SOURCES_TRACK}) And [POSTPLOT].`Status` > 0 ) " \
      "Order By [PREPLOT].`Track`, [PREPLOT].`Bin`, [POSTPLOT].`Indeks`"

# kwerendy json i wznawianie wybierają z bazy danych punkty z najwyższym indeksem
JSON = "Select " \
       "`Track`, `Bin`, `WGS84 Longitude`, `WGS84 Latitude`" \
      f"From [POSTPLOT], (Select [POSTPLOT].`Station (value)` as `Station` , Count(*) as `ilosc`  From [POSTPLOT] Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} Group by [POSTPLOT].`Station (value)`) as MxInd " \
      f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} AND [POSTPLOT].`Station (value)` = MxInd.`Station` AND [POSTPLOT].`Indeks` = MxInd.`ilosc` Order By [POSTPLOT].`Station (value)`"

WZNAWIANIE = "Select [POSTPLOT].`Station (value)`, [POSTPLOT].`Local Easting`, [POSTPLOT].`Local Northing` " \
             "From [POSTPLOT], " \
            f"(Select [POSTPLOT].`Station (value)` as `Station` , Count(*) as `ilosc`  From [POSTPLOT] Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} Group by [POSTPLOT].`Station (value)` ) as MxInd " \
            f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} AND [POSTPLOT].`Station (value)` = MxInd.`Station` AND [POSTPLOT].`Indeks` = MxInd.`ilosc` Order By [POSTPLOT].`Station (value)`"


'''Kwerendy potrzebne do robienia plików shp'''
POSTPLOT_S = "Select [POSTPLOT].* From [POSTPLOT] " \
             f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK}"

POSTPLOT_R = "Select [POSTPLOT].* From [POSTPLOT] " \
             f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK}"

DO_TYCZENIA_SP = "Select [PREPLOT].* From [PREPLOT] " \
                f"Where ([PREPLOT].`Track` Between {init.SOURCES_TRACK}) And [PREPLOT].`IsSurveyed` = 0"

DO_TYCZENIA_RP = "Select [PREPLOT].* From [PREPLOT] " \
                f"Where ([PREPLOT].`Track` Between {init.RECEIVERS_TRACK})  And [PREPLOT].`IsSurveyed` = 0"

SKIP_S = "Select [POSTPLOT].* From [POSTPLOT] " \
        f"Where [POSTPLOT].`Status` = 0 And [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK}"


SKIP_R = "Select [POSTPLOT].* From [POSTPLOT] " \
        f"Where [POSTPLOT].`Status` = 0 And [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK}"

QC_DOMIAR_S_SHP = "Select " \
                  "[POSTPLOT].`Station (text)`," \
                  "[POSTPLOT].`Station (value)`, " \
                  "[POSTPLOT].`Track`, [POSTPLOT].`Bin`, " \
                  "IIF ([POSTPLOT].`Status` in (3, 4, 5),[POSTPLOT].`COG Local Easting`,[POSTPLOT].`Local Easting`)," \
                  "IIF ([POSTPLOT].`Status` in (3, 4, 5),[POSTPLOT].`COG Local Northing`,[POSTPLOT].`Local Northing`)," \
                  "[POSTPLOT].`Uwagi_Biuro`, " \
                  "[POSTPLOT].`Descriptor`, " \
                  "[POSTPLOT].`Survey Mode (value)`," \
                  "[POSTPLOT].`Status`," \
                  "[POSTPLOT].`Indeks` " \
                  "From [POSTPLOT] " \
                  "Where " \
                 f"[POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK}  And (([POSTPLOT].`Status` IN (2,4) And  [POSTPLOT].`Survey Mode (value)` Not In (3,5,6))  Or ( [POSTPLOT].`Status` = 5  And  [POSTPLOT].`Survey Mode (value)` In (3) And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3) )  or [POSTPLOT].`Status` = 5 or [POSTPLOT].`Status` = 6 )"

QC_DOMIAR_R_SHP = "Select [POSTPLOT].* From [POSTPLOT] " \
                 f"Where  [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK}  And [POSTPLOT].`Status` >=1 And [POSTPLOT].`Status` <= 11 And (([POSTPLOT].`Survey Mode (value)` Not In (3,5,6) ) Or ( [POSTPLOT].`Survey Mode (value)` = 3 And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3))) Order By [POSTPLOT].`Station (text)`"

UWAGI_GEODEZJA = "Select [POSTPLOT].* From [POSTPLOT] Where [POSTPLOT].`Station (text)` Like '@%'"

WYSTAWKI = "Select [POSTPLOT].* From POSTPLOT " \
           "Where " \
           "([POSTPLOT].`Station (text)` Like '88_______' or " \
               "[POSTPLOT].`Station (text)` Like '99_______' or " \
               "[POSTPLOT].`Station (text)` Like '88________' or " \
               "[POSTPLOT].`Station (text)` Like 'PP*') " \
           "And [POSTPLOT].`Survey Mode (value)` IN (3,6) " \
           "Order By [POSTPLOT].`Station (text)`"


VIBRATORY = "Select [POSTPLOT].* From POSTPLOT " \
           f"Where [POSTPLOT].`Status` <> 0 And  [POSTPLOT].`Track` Between {init.SOURCES_TRACK} And [POSTPLOT].`Station (value)`> 0 And ([POSTPLOT].`Descriptor` IN {init.VIBRATORY_DSC} OR ([POSTPLOT].`Descriptor` IN {init.DYNAMITY_DSC} and [POSTPLOT].`Status` in (3,4,5)))"

DYNAMITY = "Select [POSTPLOT].* From POSTPLOT " \
          f"Where [POSTPLOT].`Status` <> 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK} And [POSTPLOT].`Station (value)`<>0 And [POSTPLOT].`Descriptor` IN {init.DYNAMITY_DSC} And [POSTPLOT].`Status` not in (3,4,5)"


