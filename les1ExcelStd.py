import pandas as pd
import numpy as np

print("hello")
'''
les1VoorbeeldExcel.xlsx


'''
filenaam='les1VoorbeeldExcel.xlsx'
  # linker kant van het = teken  staat waar iets wordt bewaard in dit geval in df
                            # df is een afkorting van DataFrame
  # nu krijg je 8 regels te zien , als je niets opgeeft krijg je de eerste 5 regels te zien,  (of een error)

# kolomnamen

print(kolomnamen)
# de eerste kolom begint met index waarde =0 (bij programmeren tellen we meestal vanaf nul)
print(kolomnamen[0])

#
#  kolom selectie
#
# inhoud van een kolom bekijken
kolomnr=2

print(df2.head())
# wat ook kan (raad het niet aan)
 # df.kolomnaam (je hebt een probleem als er een spatie in zit
print(df2.head())
 # hier kan je wel rekening houden met spaties , ja mag geen tikfouten maken
print(df2.head(8))
#  df[kolomnamen[2] kolom selectie

#
# rij selectie
#
#print(df[??])  #  geeft de eerste 3 rijen (index 0 t/m 2  [vanaf:tot:step]  step is standaard =1
#print(df[?])  # geeft vanaf index=1  tot index=4 step=1
#print(df[??]) # omgekeerd vanaf index=4 tot index=1 -1 geeft aan omgekeerd (zonder -1 werkt mhet niet
#
#  bekijken van de inhoud van df
#
#print() #aantal, gemiddelde, standaard deviatie, minimum, Quartile : 25%,50% en 75%, maximum
#w=df.
#aantal=w[??][0]  # nr is kolomnaam , 0 is de index er van
print("aantal=",aantal)

#waarde=df[kolomnamen[2]]  # waarden die in de kolom staan
print(waarde)
print("minimum=",min(waarde))
print("maximum=",max(waarde))
#waarde[??]=??  # het vervangen dan nan door 0.  MAG NIET in bij DataMining !!!!
             # let op ook in de df wordt de nan vervangen door een nul
print("som= ",sum(waarde))
print("lengte=",len(waarde)) # lengte = aantal
# let op geen  count alleen zonder nan sum,
arr=np.asarray(waarde)
print(sum(arr))

#
#  Het verwijderen van NaN  (lege velden Not a Number
# nan means "not a number", a float value that you get if you perform a calculation whose result can't be expressed as a number.
# Any calculations you perform with NaN will also result in NaN
#
#
print("====== tonen van de lijst =========")
print(df.head(10))
waarde[4]='nan' # terug in de dataframe zetten van de nan
print(df.head(10))
#print(df.)  # opzoek naar of er niet ingevulde waarden zijn

#df=df.   # verwijderen van rijen met niet ingevulde waarden
print(df.head(10))
# je verliest een aantal rijen. Echter als het goed is dan niet veel
# let op : onderzoek waarom er NaN zijn

#
#
#  selectie
#
print(kolomnamen[2]) # O1

#df3=df[] # df[kolomnamen[2]]>6.0 lezen als  df['O1]>6.0
#print(df3.head())







