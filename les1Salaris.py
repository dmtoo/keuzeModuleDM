import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

filenaam='Salaries.csv'
scheidingsteken=','
df=pd.read_csv(filenaam,sep=scheidingsteken)
print(df.head())
dfman=df[df['sex']=='Male']
print(dfman.head())
dfvrouw=df[df['sex']=='Female']
print(dfvrouw.head())

'''


ax=dfman['salary'].plot.hist(color='blue')
# https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.plot.html

plt.title("Man")
plt.xlabel("salary")


plt.show() # zoek op het verschil tussen deze regel voorzien van een #

ax=dfvrouw['salary'].plot.hist(color='red',label="V")  # hier mag ook title
#plt.title("Vrouw")
ax.set_title("vrouw")
# ax.set_xlabel("x label")
# ax.set_ylabel("y label")
ax.legend()
plt.xlabel("salary")
plt.show()
'''



kolnm=list(df)

#print(kolnm[0])
xw=dfman[kolnm[0]].values # Unnamed: 0 tbv indexen  aantaly = aantal mannen aantaly=len(ym)  xw=range(0,aantaly) niet ivm verkeerde index
aantalx=len(xw)
#print("aantal x=",aantalx)

ym=dfman['salary'].values

#aantalx=len(xw)
#print("aantal x=",aantalx)

yv=dfvrouw['salary'].values
aantalxv=len(yv)
xv=dfvrouw[kolnm[0]] # niet xv=range(0,aantalxv) ivm passende index

plt.scatter(xw,ym,c="Blue")
plt.scatter(xv,yv,c="Red")
plt.show()
