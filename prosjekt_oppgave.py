# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 19:46:42 2025

@author: erikas
"""

#Del A. Program som leser inn filen "support_uke_24.xlsx." og lagrer data i arrayer.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = "support_uke_24.xlsx"  
data = pd.read_excel(file) # lese filen
#print(data)

# Hente ut data frå spesifikke kolonner

u_dag = data["Ukedag"].values             
kl_slett = data["Klokkeslett"].values     
varighet = data["Varighet"].values         
score = data["Tilfredshet"].values             


#Del B. Skrive et program som finner antall henvendelser for hver de 5 ukedagene. Resultatet viser i et søylediagram.
#Antall henvendelser per ukedag

antall_henvendelser_per_dag = data["Ukedag"].value_counts()                    
ukedager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]                
antall_henvendelser_per_dag = antall_henvendelser_per_dag[ukedager].fillna(0)  
                                                                               

plt.bar(antall_henvendelser_per_dag.index, antall_henvendelser_per_dag.values)
plt.xlabel("Ukedag")
plt.ylabel("Antall henvendelser")
plt.title("Antall henvendelser per ukedag")
plt.grid()
plt.show()

#Del C. Skriv et program som finner minste og lengste samtaletid som er loggført for uke 24.

min_tid = np.min(varighet)                                                      
max_tid = np.max(varighet)                                                      


#print(f"Den korteste samtale var {min_tid} minutter.")
#print(f"Den lengste samtale var {max_tid} minutter.")

#Del D. Skriv et program som regner ut gjennomsnitlig samtaletid basert på alle henvendelser i uke 24.

data["Varighet"] = pd.to_timedelta(data["Varighet"], errors="coerce")           # Konverterer tidsverdiene fra formatet hh:mm:ss til timedelta-format.
varighet = data["Varighet"].dt.total_seconds().values                           # Få varigheten i sekunder
gjennomsnitt_tid = np.mean(varighet) / 60                                       # Del på 60 for å få minutter

#print(f"Gjennomsnittling samtaletid for alle henvendelser for hele uke 24 var {gjennomsnitt_tid:.2f} minutter.")

#Del E. Skriv et program som finner det totale antall henvendelser supportavdelingen mottok for hver av tidsrommene 08-10, 10-12, 12-14 og 14-16 
#for uke 24. Resultatet visualiseres ved bruk av et sektordiagram.

data["Klokkeslett"] = pd.to_datetime(data["Klokkeslett"], format="%H:%M:%S")    # Konverter klokkeslett til datetime-format

# Funksjon for å kategorisere tidene i de ønskede tidsintervallene

def kategoriser_tid(tid):                                                       
    if pd.to_datetime("08:00:00", format="%H:%M:%S") <= tid < pd.to_datetime("10:00:00", format='%H:%M:%S'):
        return "08-10"                                                                          
    elif pd.to_datetime("10:00:00", format="%H:%M:%S") <= tid < pd.to_datetime("12:00:00", format='%H:%M:%S'):
        return "10-12"  
    elif pd.to_datetime("12:00:00", format="%H:%M:%S") <= tid < pd.to_datetime("14:00:00", format='%H:%M:%S'):
        return "12-14"  
    elif pd.to_datetime("14:00:00", format="%H:%M:%S") <= tid < pd.to_datetime("16:00:00", format='%H:%M:%S'):
        return "14-16"
    else:
        return "Utenfor tidsintervall"                                          # Hvis det er utenfor de ønskede tidsintervallene
    
    
data["Tidsintervall"] = data["Klokkeslett"].apply(kategoriser_tid)              # Bruk funksjonen på hver rad for å kategorisere klokkeslettene

total_antall_henvendelser_per_bolk = data["Tidsintervall"].value_counts()       # Finn antall henvendelser for hvert tidsintervall

plt.pie(total_antall_henvendelser_per_bolk, labels=total_antall_henvendelser_per_bolk.index, autopct='%1.1f%%', startangle=90)
plt.title("Antall henvendelser per tidsrom (08-16) for uke 24")
plt.show()

#Del F. Lag et program som regner ut supportavdelings NPS og skriver svaret til skjerm.
#Merk: Kunder som ikke har gitt tilbakemelding på tilfredshet, skal utelates fra utregningene


data = data.dropna(subset=["Tilfredshet"])                                     #Fjerne NaN-verdier fra tilfredshetsscoren
data["Tilfredshet"] = data["Tilfredshet"].astype(int)                          #Konvertere data til tilfredshet til heltall

antall_positive = sum((data["Tilfredshet"] >= 9) & (data["Tilfredshet"] <= 10))
antall_noytrale = sum((data["Tilfredshet"] >= 7) & (data["Tilfredshet"] <= 8)) 
antall_negative = sum((data["Tilfredshet"] >= 1) & (data["Tilfredshet"] <= 6)) 

totale_tilbakemeldinger = antall_positive + antall_noytrale + antall_negative   

prosent_positive = (antall_positive / totale_tilbakemeldinger)* 100             # Beregne prosentandel 
prosent_negative =(antall_negative / totale_tilbakemeldinger) * 100  

NPS = prosent_positive - prosent_negative                                       # Beregne NPS

print(f"Net Promoterer  score (NPS) for supportavdelingen er: {NPS:.2f}" )     






