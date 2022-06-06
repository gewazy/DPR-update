import initial_data

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
         f"And [POSTPLOT].`Track` Between {initial_data.RECEIVERS_TRACK} " \
         f"And datediff('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {initial_data.DDIFF} " \
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
         f"And  [POSTPLOT].`Track` Between {initial_data.SOURCES_TRACK}" \
         f"And datediff ('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {initial_data.DDIFF} " \
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
       f"And  [POSTPLOT].`Track` Between {initial_data.RECEIVERS_TRACK}" \
       f"And datediff ('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {initial_data.DDIFF} " \
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
       f"And  [POSTPLOT].`Track` Between {initial_data.SOURCES_TRACK}" \
       f"And datediff ('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {initial_data.DDIFF} " \
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
       f"And  [REMEASURE].`Track` Between {initial_data.SOURCES_TRACK} " \
       f"And datediff ('d',[REMEASURE].`Survey Time (Local)`,Now()) = {initial_data.DDIFF} " \
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
       f"And [REMEASURE].`Track` Between {initial_data.RECEIVERS_TRACK} " \
       f"And datediff('d',[REMEASURE].`Survey Time (Local)`,Now()) = {initial_data.DDIFF} " \
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
      f"And datediff('d',[OTG].`Survey Time (Local)`,Now()) = {initial_data.DDIFF} " \
      "Group By " \
      "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 9),'GPS',''))), " \
      "[OTG].`Surveyor`, " \
      "[OTG].`Julian Date (Local)`, " \
      "[Ludziki].`Nr_auta`"

QC_R = "Select [POSTPLOT].* " \
       "From [POSTPLOT] " \
       f"Where  [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {initial_data.RECEIVERS_TRACK}  " \
       "And [POSTPLOT].`Status` >=1 And [POSTPLOT].`Status` <= 11 " \
       "And (( [POSTPLOT].`Survey Mode (value)` Not In (3,5,6) ) Or ( [POSTPLOT].`Survey Mode (value)` = 3 And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3) ))  " \
       "Order By [POSTPLOT].`Station (text)`"

QC_S = "Select [POSTPLOT].* " \
       "From [POSTPLOT] " \
       f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {initial_data.SOURCES_TRACK}  " \
       "And ( ([POSTPLOT].`Status` IN (2,4) And  [POSTPLOT].`Survey Mode (value)` Not In (3,5,6))  Or ( [POSTPLOT].`Status` = 5  And  [POSTPLOT].`Survey Mode (value)` In (3) And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3) )  or [POSTPLOT].`Status` = 5 or [POSTPLOT].`Status` = 6 ) " \
       "Order By [POSTPLOT].`Station (value)`"

VIB = "Select [POSTPLOT].* From [POSTPLOT] " \
      f"Where  [POSTPLOT].`Status` <> 0 And  [POSTPLOT].`Track` Between {initial_data.SOURCES_TRACK}  And [POSTPLOT].`Station (value)`>0 " \
      f"And (([POSTPLOT].`Descriptor` in ({initial_data.VIBRATORY_DSC}) OR ([POSTPLOT].`Descriptor` in ({initial_data.DYNAMITY_DSC}) and [POSTPLOT].`Status`  in (3,4,5)))) " \
      "Order By [POSTPLOT].`Station (value)`"

XR = f"Select [POSTPLOT].* From [POSTPLOT] Where [POSTPLOT].`Status` <> 0 And [POSTPLOT].`Track` Between {initial_data.SOURCES_TRACK}  " \
     "And [POSTPLOT].`Station (value)`<>0 And (([POSTPLOT].`Descriptor` Like 'xr' And [POSTPLOT].`dr_date` is NULL) OR ([POSTPLOT].`dr_date` is not NULL And ([POSTPLOT].`dr_eq` Like 'EMCI' Or [POSTPLOT].`dr_eq` Like  'Emci' Or [POSTPLOT].`dr_eq` Like  'LPHB'))) And [POSTPLOT].`Status` not in (3,4,5) Order By [POSTPLOT].`Station (value)`"

XT = "Select [POSTPLOT].* From [POSTPLOT] " \
     f"Where [POSTPLOT].`Status` <> 0 And [POSTPLOT].`Track` Between {initial_data.SOURCES_TRACK} And [POSTPLOT].`Station (value)`<>0 And( ([POSTPLOT].`Descriptor` Like 'xt' " \
     "And [POSTPLOT].`dr_date` is NULL) OR ([POSTPLOT].`dr_date` is not NULL And ([POSTPLOT].`dr_eq` Like 'PAT' Or [POSTPLOT].`dr_eq` Like  'Pat' ))) And [POSTPLOT].`Status` not in (3,4,5) " \
     "Order By [POSTPLOT].`Station (value)`"

SKIP = "Select [POSTPLOT].* From [POSTPLOT] " \
       "Where [POSTPLOT].`Status` = 0 And [POSTPLOT].`Station (value)` > 0 " \
       f"And [POSTPLOT].`Track` Between {initial_data.SOURCES_TRACK} Order By [POSTPLOT].`Station (value)`"


