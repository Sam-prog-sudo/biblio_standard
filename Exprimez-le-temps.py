#--------------------module time--------------------#

import time


time.time()

1297642146.562


time.localtime()

time.struct_time(tm_year=2011,
                 tm_mon=2,
                 tm_mday=14,
                 tm_hour=3,
                 tm_min=22,
                 tm_sec=7,
                 tm_wday=0, #jour de la semaine
                 tm_yday=45, #jour de l'année
                 tm_isdst=0) #changement d'heure local


temps = time.localtime()
ts_debut = time.mktime(temps)
print(ts_debut)

1297642195.0


time.sleep(3.5) # Faire une pause pendant 3,5 secondes


