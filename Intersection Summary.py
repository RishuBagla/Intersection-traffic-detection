# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:50:55 2020

@author: hp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

af = pd.read_excel('E:\\Yolo\\Traffic Detection\\Multi-type_vehicles_flow_statistics-master\\Multi-type_vehicles_flow_statistics-master\\mydata.xlsx')
def f(x):
    a = {}
    a['First Frame'] = x['C'].min()
    a['Last Frame'] = x['C'].max()
    a['Number of Frame'] = (x['C'].max()-x['C'].min())
    a['Start Coordinate (X)'] = (x['D'].head(1)).iloc[0]
    a['Start Coordinate (Y)'] = (x['E'].head(1)).iloc[0]
    a['Last Coordinate (X)'] = (x['D'].tail(1)).iloc[0]
    a['Last Coordinate (Y)'] = (x['E'].tail(1)).iloc[0]
    #a['Start Coordinate (X)'] = x.loc[x['C'] == x['C'].head(1), 'D'].iloc[0]
    #a['Start Coordinate (Y)'] = x.loc[x['C'] == x['C'].min(), 'E'].iloc[0]
    #a['Last Coordinate (X)'] = x.loc[x['C'] == x['C'].max(), 'D'].iloc[0]
    #a['Last Coordinate (Y)'] = x.loc[x['C'] == x['C'].max(), 'E'].iloc[0]
    return pd.Series(a, index=['First Frame', 'Last Frame', 'Number of Frame', 'Start Coordinate (X)','Start Coordinate (Y)','Last Coordinate (X)','Last Coordinate (Y)'])
af1 = af.groupby(['A', 'B']).apply(f) # Reaing first and last coordinate
af1=pd.DataFrame(af1)
#df2 = df.groupby(['A', 'B'])['C'].min(),['D']
#df = df1-df2
print(af1)
af1.to_excel("summary"+".xlsx")

BC=pd.read_excel('Boundary Coordinate.xlsx') # BC represent boundary coordinate, estimated from app2 code
dataset=pd.read_excel('summary.xlsx') # Containing the information of vechile type, first, last coordinate, nuber of frame and time required
Y_start=dataset.iloc[:, 5:7].values #Extracting vechile starting coordinte coordinate
Y_end = dataset.iloc[:, 7:9].values #Extracting vechile lst coordinate
V = dataset.iloc[:, :2].values # Vechile ctegory
V=pd.DataFrame(V) 
V = V.set_axis(['Number','Type'], axis=1, inplace=False) #Adding header
#V=V.rename({'0': 'Vechile Class'}, axis=1)
d1={}
d2={}
#n= BC.count
for i in range (1,5):
    p1=BC.iloc[i-1:i,:].values # Represent line first coordinate
    p2=BC.iloc[i:i+1,:].values # Rpresent line second coordinate
    #c=Y-p1
    #Y=dataset.iloc[:, 2:3].values
    #print(X(1))
    d1[i]=abs(np.cross(p2-p1,Y_start-p1)/np.linalg.norm(p2-p1)) # Calculting minimum distance of point from line of starting line
    d2[i]=abs(np.cross(p2-p1,Y_end-p1)/np.linalg.norm(p2-p1)) # Calculting minimum distance of point from line of end line
    d1=pd.DataFrame(d1)
    d11=d1.idxmin(axis=1) # Finding minimum distance of starting point of vechile from all identified line
    d2=pd.DataFrame(d2)
    d22=d2.idxmin(axis=1) # Finding minimum distance of end point of vechile from all identified line
    combine=pd.concat([V,d11,d22,d1,d2], axis=1) # Combining vechile type, minimum distance of from starting point, minimum distance of from end point
    d=pd.concat([V,d11,d22], axis=1)
    d = d.set_axis(['Vechile Type','Vechile Class', 'Starting point', 'End Point'], axis=1, inplace=False) # Adding header
    d=pd.DataFrame(d)
    dt=d.pivot_table(index=['Vechile Class', 'Starting point', 'End Point'], aggfunc='size') # Calculting summary using piviot
    d.to_excel("Distance from line"+".xlsx")
    dt.to_excel("Final Summary"+".xlsx")
    #d.iloc[:,i:]=d
    print(dt,BC)
