#!/usr/bin/env python2
import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots()

#Give x and y samples to plot
ax1.plot([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120],[0,2.8200802976190475,2.466606490909091,2.3999369824324326,2.3648651001540832,2.458179808939096,2.4821249836679145,2.5234428494596632,2.6830654715384616,2.883369433008526,3.038450470125,3.3519350329999997,3.81234939775,4.739969011625,5.147480070625,5.965252448625,6.894743129375,6.947494894875001,7.550845669,7.723081675375,7.360268077375,7.627367698875,7.2231915785,7.209323506625,9.916057593875001,13.551432447625,14.722236867000001,14.056013838125,16.409578264875,13.366630341625,8.795811968374998,6.963216885875,9.533213402875,10.111435217875,11.915416877875,10.58307006025,11.2988304365,8.6237939445,11.406732999125,15.520516409,19.453140517125,21.308459306375,23.4550921915,13.12923864525,14.075912965,11.382815145,15.843184612125,30.271631102375,35.173471702,41.45916271275,39.139799506125,46.392753186875,60.2568160295,24.141920157625,23.10473447275,22.755046473,21.742383727375,29.497785803625,43.8110739615,54.399312426125,32.378404650625,13.940002832000001,37.23962533175,38.846183034999996,42.42276019187501,37.296984303,32.13546649425,45.00626074625001,54.978963652500006,57.240005337875004,55.197403687875,70.64772568012499,30.247484871,48.257725760750006,65.78336894525,63.032139648000005,55.312042851499996,68.531325122875,67.037718416875,70.252255796125,70.51047155575,80.95314374275,66.91091948225,72.9064212225,61.881587442000004,79.50947370575,78.1367016335,83.548202483875,89.904093662625,88.452223560875,84.44367597925,92.350222746125,71.43503609462499,94.03864067225,65.39841764075,102.460765834,99.6729611145,100.48724089775,113.28096876075,97.59060814300001,105.672540701125,108.954105581,108.571423139125,102.4263034245,98.445340526625,102.942393255,115.39410289575,125.582196055375,119.22068564037501,101.914786774375,119.01507572837501,119.72277964075,132.798807252375,115.22924984562499,120.5311717255,119.676170044125,139.644232739,111.148275699875,135.037867578875,127.87164965424999,139.57698109362502],color='blue')

#Set labels
ax1.set_ylabel('Response Time in milliseconds', fontsize=20,color='blue')
ax1.set_xlabel('Time', fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue',labelsize=15)
ax1.tick_params(axis='x',labelsize=15)

#Set xlimit and ylimits
plt.ylim((0,300))
plt.xlim((0,120))

#Customize x axis values using xticks
x=["0","10S","20S","30S","40S","50S","60S","70S","80S","90S","10S","110S","120S"]
l=[00,10,20,30,40,50,60,70,80,90,100,110,120]
plt.xticks(l,x)

#Take another subplot
ax2 = ax1.twinx()
#Give x and y samples to plot
ax2.plot([0,15,30,45,60,75,90,105,120],[0,250,500,750,1000,1250,1500,1750,2000],color='red')
ax2.tick_params(axis='y', labelcolor='red', pad=1,labelsize=15)

#Set labels
ax2.set_ylabel('Users', fontsize=20,color='red')
ax2.set_ylim(0,2100)

plt.show()