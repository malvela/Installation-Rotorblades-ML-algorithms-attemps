import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
'''
turbine-11_helihoist-1_tom_acc-vel-pos_hammerhead_2019-10-31-04-18-02_2019-10-31-10-41-13
turbine-11_helihoist-1_tom_geometry_hammerhead_2019-10-31-04-18-02_2019-10-31-10-41-13
turbine-11_sbitroot_tom_acc-vel-pos_hammerhead_2019-10-31-05-10-55_2019-10-31-10-38-59
turbine-11_sbittip_tom_acc-vel-pos_hammerhead_2019-10-31-05-17-56_2019-10-31-10-23-54

turbine-11_helihoist-1_tom_acc-vel-pos_sbi1_2019-10-31-10-41-13_2019-10-31-12-54-16
turbine-11_sbitroot_tom_acc-vel-pos_sbi1_2019-10-31-10-39-00_2019-10-31-12-54-35
turbine-11_sbittip_tom_acc-vel-pos_sbi1_2019-10-31-10-23-54_2019-10-31-13-06-39

turbine-11_helihoist-1_tom_acc-vel-pos_sbi2_2019-10-31-15-30-44_2019-10-31-18-52-53
turbine-11_sbitroot_tom_acc-vel-pos_sbi2_2019-10-31-15-37-45_2019-10-31-18-49-33
turbine-11_sbittip_tom_acc-vel-pos_sbi2_2019-10-31-15-23-09_2019-10-31-19-02-46

turbine-11_helihoist-1_tom_acc-vel-pos_tnhb1_2019-10-31-12-54-16_2019-10-31-15-30-44
turbine-11_helihoist-1_tom_geometry_tnhb1_2019-10-31-12-54-16_2019-10-31-15-30-44
turbine-11_sbitroot_tom_acc-vel-pos_tnhb1_2019-10-31-12-54-35_2019-10-31-15-37-45
turbine-11_sbittip_tom_acc-vel-pos_tnhb1_2019-10-31-13-06-40_2019-10-31-15-23-09


wmb missing


lidar_2019_10_31


'''

#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-11**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-11**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-11**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-11**.csv'))

data = []
helihoist_tele_hammerhead = pd.read_csv(hammerhead[0], delimiter = ',')
helihoist_geo_hammerhead = pd.read_csv(hammerhead[1], delimiter = ',')
sbitroot_hammerhead = pd.read_csv(hammerhead[2], delimiter = ',')
sbitip_hammerhead = pd.read_csv(hammerhead[3], delimiter = ',')
data.append(helihoist_tele_hammerhead) , data.append(helihoist_geo_hammerhead), data.append(sbitroot_hammerhead)  ,data.append(sbitip_hammerhead)

helihoist_sbi1 = pd.read_csv(sbi1[0], delimiter = ',')
sbiroot_sbi1 = pd.read_csv(sbi1[1], delimiter = ',')
sbitip_sbi1 = pd.read_csv(sbi1[2], delimiter = ',')

data.append(helihoist_sbi1) ,data.append(sbiroot_sbi1) ,data.append(sbitip_sbi1)

helihoist_sbi2 = pd.read_csv(sbi2[0], delimiter = ',')
sbiroot_sbi2 = pd.read_csv(sbi2[1], delimiter = ',')
sbitip_sbi2 = pd.read_csv(sbi2[2], delimiter = ',')

data.append(helihoist_sbi2) ,data.append(sbiroot_sbi2) ,data.append(sbitip_sbi2)

helihoist_tnhb1 = pd.read_csv(tnhb1[0], delimiter = ',')
helihoist_geo_tnhb1 = pd.read_csv(tnhb1[1], delimiter = ',')
sbiroot_tnhb1 = pd.read_csv(tnhb1[2], delimiter = ',')
sbitip_tnhb1 = pd.read_csv(tnhb1[3], delimiter = ',')

data.append(helihoist_tnhb1) ,data.append(helihoist_geo_tnhb1) ,data.append(sbiroot_tnhb1),data.append(sbitip_tnhb1)

lidar=pd.read_csv('environment/environment/wind/lidar/lidar_2019-10-31.csv', delimiter = ' ')
lidar.columns = ( 'epoch', 'wind_speed_0', 'wind_dir_0', 'wind_dir_0_corr', 'height_0', 'wind_speed_1', 'wind_dir_1', 'wind_dir_1_corr', 'height_1', 'wind_speed_2', 'wind_dir_2', 'wind_dir_2_corr', 'height_2', 'wind_speed_3', 'wind_dir_3', 'wind_dir_3_corr', 'height_3', 'wind_speed_4', 'wind_dir_4', 'wind_dir_4_corr', 'height_4', 'wind_speed_5', 'wind_dir_5', 'wind_dir_5_corr', 'height_5', 'wind_speed_6', 'wind_dir_6', 'wind_dir_6_corr', 'height_6', 'wind_speed_7', 'wind_dir_7', 'wind_dir_7_corr', 'height_7', 'wind_speed_8', 'wind_dir_8', 'wind_dir_8_corr', 'height_8', 'wind_speed_9', 'wind_dir_9', 'wind_dir_9_corr', 'height_9', 'wind_speed_10', 'wind_dir_10', 'wind_dir_10_corr', 'height_10', 'heading')
data.append(lidar)

UTC = []
for k in range(len(lidar)):
    UTC.append(pd.Timestamp.fromtimestamp(lidar.iloc[k, 0]))
lidar['epoch'] = UTC
lidar.index = lidar['epoch']
del lidar['epoch']
lidar = lidar.resample('1S', label='left').mean().pad()
lidar = lidar

#generating timestamps for every dataframe
counter = 0
for df in data:
    UTC = []
    for k in range(len(df)):
        UTC.append(pd.Timestamp.fromtimestamp(df.iloc[k, 0]))
    df['epoch'] = UTC
    df.index = df['epoch']
    del df['epoch']
    df = df.resample('1S', label = 'left').mean().pad()
    data[counter] = df
    counter = counter+1
'''
#Plotting 
plt.plot(lidar.index, lidar['wind_speed_7'])
plt.title('wind_speed_7')
plt.xlabel('time')
plt.xticks(rotation= 90)
plt.show()
plt.plot(lidar.index, lidar['wind_dir_7_corr'])
plt.title('wind_dir_7_corr')
plt.xlabel('time')
plt.xticks(rotation= 90)
plt.show()

'''

# generating hammerhead file
#05:17:56   10:23:54
for i in range(4):
    data[i] = data[i]['2019-10-31 05:17:56': '2019-10-31 10:23:54']
transition_lidar = lidar['2019-10-31 05:17:56': '2019-10-31 10:23:54']
result =pd.concat([data[0],data[1],data[2],data[3], transition_lidar], axis=1 )
result.to_csv('Results_preprocessing/turbine11/hammerhead_turbine11.csv')

#generating sbi1 file
#10:41:13   21:54:16
for i in range(4,7):
    data[i] = data[i]['2019-10-31 10:41:13': '2019-10-31 12:54:16']
transition_lidar = lidar['2019-10-31 10:41:13': '2019-10-31 12:54:16']
result =pd.concat([data[4],data[5],data[6], transition_lidar], axis=1 )
result.to_csv('Results_preprocessing/turbine11/sbi1_turbine11.csv')

#generating sbi2 file
#15:37:45   18:49:33
for i in range(7,10):
    data[i] = data[i]['2019-10-31 15:37:45': '2019-10-31 18:49:33']
transition_lidar = lidar['2019-10-31 15:37:45': '2019-10-31 18:49:33']
result =pd.concat([data[7],data[8],data[9], transition_lidar], axis=1 )
result.to_csv('Results_preprocessing/turbine11/sbi2_turbine11.csv')

#generating tnhb1 file
#13:06:40   15:23:09
for i in range(10,14):
    data[i] = data[i]['2019-10-31 13:06:40': '2019-10-31 15:23:09']
transition_lidar = lidar['2019-10-31 13:06:40': '2019-10-31 15:23:09']
result =pd.concat([data[10],data[11],data[12],data[13], transition_lidar], axis=1 )
result.to_csv('Results_preprocessing/turbine11/tnhb1_turbine11.csv')



