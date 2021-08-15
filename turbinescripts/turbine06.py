import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import jinja2
import seaborn as sn

# every data name that keeps data for turbine6
'''
turbine-06_helihoist-1_tom_acc-vel-pos_hammerhead_2019-09-22-03-14-43_2019-09-22-12-05-47
turbine-06_helihoist-1_tom_geometry_hammerhead_2019-09-22-03-14-43_2019-09-22-12-05-47
turbine-06_sbitroot_tom_acc-vel-pos_hammerhead_2019-09-22-03-11-49_2019-09-22-12-15-43
turbine-06_sbittip_tom_acc-vel-pos_hammerhead_2019-09-22-03-16-30_2019-09-22-12-12-21

turbine-06_helihoist-1_tom_acc-vel-pos_sbi1_2019-09-22-12-05-48_2019-09-22-12-41-45
turbine-06_sbitroot_tom_acc-vel-pos_sbi1_2019-09-22-12-15-43_2019-09-22-12-42-48
turbine-06_sbittip_tom_acc-vel-pos_sbi1_2019-09-22-12-12-21_2019-09-22-12-39-12

turbine-06_helihoist-1_tom_acc-vel-pos_sbi2_2019-09-22-22-11-22_2019-09-23-00-30-45
turbine-06_sbitroot_tom_acc-vel-pos_sbi2_2019-09-22-22-13-32_2019-09-23-00-29-28
turbine-06_sbittip_tom_acc-vel-pos_sbi2_2019-09-22-22-04-11_2019-09-23-00-19-04

turbine-06_helihoist-1_tom_acc-vel-pos_tnhb1_2019-09-22-12-41-45_2019-09-22-22-11-22
turbine-06_helihoist-1_tom_geometry_tnhb1_2019-09-22-12-41-45_2019-09-22-22-11-22
turbine-06_sbitroot_tom_acc-vel-pos_tnhb1_2019-09-22-12-42-48_2019-09-22-22-13-32
turbine-06_sbittip_tom_acc-vel-pos_tnhb1_2019-09-22-12-39-13_2019-09-22-22-04-11

turbine-06_helihoist-1_tom_acc-vel-pos_tnhb2_2019-09-23-00-30-45_2019-09-23-00-42-54
turbine-06_helihoist-1_tom_geometry_tnhb2_2019-09-23-00-30-45_2019-09-23-00-42-54
turbine-06_sbitroot_tom_acc-vel-pos_tnhb2_2019-09-23-00-29-28_2019-09-23-11-16-27
turbine-06_sbittip_tom_acc-vel-pos_tnhb2_2019-09-23-00-19-04_2019-09-23-11-22-22

wmb-sued-2019-9-22
lidar_2019_09_22

everthing available
'''
#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-06**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-06**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-06**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-06**.csv'))
tnhb2 = sorted(glob('Daten/tnhb2/tnhb2/turbine-06**.csv'))

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

helihoist_tnhb2 = pd.read_csv(tnhb2[0], delimiter = ',')
helihoist_geo_tnhb2 = pd.read_csv(tnhb2[1], delimiter = ',')
sbiroot_tnhb2 = pd.read_csv(tnhb2[2], delimiter = ',')
sbitip_tnhb2 = pd.read_csv(tnhb2[3], delimiter = ',')

data.append(helihoist_tnhb2) ,data.append(helihoist_geo_tnhb2) ,data.append(sbiroot_tnhb2),data.append(sbitip_tnhb2)

wmb1= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-22.csv', delimiter = ' ')

wmb_all = []
wmb_all.append(wmb1)

lidar1= pd.read_csv('environment/environment/wind/lidar/lidar_2019-09-22.csv', delimiter = ' ')
data.append(lidar1)
lidar_all =[]
lidar_all.append(lidar1)
buffer1 = []

for j in wmb_all:
    j.columns = (
    'epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss',
    'TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav', 'Eps',
    '#Waves')
    buffer1.append(j)
    wmb = pd.concat(buffer1, axis=0)
    wmb.columns = (
    'epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss',
    'TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav', 'Eps',
    '#Waves')
buffer2 = []
for i in lidar_all:
    i.columns = ('epoch', 'wind_speed_0', 'wind_dir_0', 'wind_dir_0_corr', 'height_0', 'wind_speed_1', 'wind_dir_1',
                    'wind_dir_1_corr', 'height_1', 'wind_speed_2', 'wind_dir_2', 'wind_dir_2_corr', 'height_2',
                    'wind_speed_3', 'wind_dir_3', 'wind_dir_3_corr', 'height_3', 'wind_speed_4', 'wind_dir_4',
                    'wind_dir_4_corr', 'height_4', 'wind_speed_5', 'wind_dir_5', 'wind_dir_5_corr', 'height_5',
                    'wind_speed_6', 'wind_dir_6', 'wind_dir_6_corr', 'height_6', 'wind_speed_7', 'wind_dir_7',
                    'wind_dir_7_corr', 'height_7', 'wind_speed_8', 'wind_dir_8', 'wind_dir_8_corr', 'height_8',
                    'wind_speed_9', 'wind_dir_9', 'wind_dir_9_corr', 'height_9', 'wind_speed_10', 'wind_dir_10',
                    'wind_dir_10_corr', 'height_10', 'heading')
    buffer2.append(i)

    lidar = pd.concat(buffer2, axis=0)
    lidar.columns = ('epoch', 'wind_speed_0', 'wind_dir_0', 'wind_dir_0_corr', 'height_0', 'wind_speed_1', 'wind_dir_1',
                    'wind_dir_1_corr', 'height_1', 'wind_speed_2', 'wind_dir_2', 'wind_dir_2_corr', 'height_2',
                    'wind_speed_3', 'wind_dir_3', 'wind_dir_3_corr', 'height_3', 'wind_speed_4', 'wind_dir_4',
                    'wind_dir_4_corr', 'height_4', 'wind_speed_5', 'wind_dir_5', 'wind_dir_5_corr', 'height_5',
                    'wind_speed_6', 'wind_dir_6', 'wind_dir_6_corr', 'height_6', 'wind_speed_7', 'wind_dir_7',
                    'wind_dir_7_corr', 'height_7', 'wind_speed_8', 'wind_dir_8', 'wind_dir_8_corr', 'height_8',
                    'wind_speed_9', 'wind_dir_9', 'wind_dir_9_corr', 'height_9', 'wind_speed_10', 'wind_dir_10',
                    'wind_dir_10_corr', 'height_10', 'heading')

#Plotting and generating UTC Timestamps
'''
UTC = []
for k in range(len(wmb)):
    UTC.append(pd.Timestamp.fromtimestamp(wmb.iloc[k, 0]))
wmb['epoch'] = UTC
wmb.index = wmb['epoch']
del wmb['epoch']
#wmb = wmb.resample('1S', label='left').mean().pad() / 1800
wmb = wmb

UTC = []
for k in range(len(lidar)):
    UTC.append(pd.Timestamp.fromtimestamp(lidar.iloc[k, 0]))
lidar['epoch'] = UTC
lidar.index = lidar['epoch']
del lidar['epoch']
#wmb = wmb.resample('1S', label='left').mean().pad() / 1800
lidar = lidar

#Plotting:
fig = plt.figure(figsize=(14,6), dpi=80)
plt.plot(wmb.index, wmb['#Waves'])
plt.title('#Waves')
plt.ylabel('number of waves')
plt.xlabel('time')
plt.xticks(rotation= 90)
plt.show()
fig = plt.figure(figsize=(14,6), dpi=80)
plt.plot(lidar.index, lidar['wind_speed_7'])
plt.title('wind_speed_7')
plt.xlabel('time')
plt.xticks(rotation= 90)
plt.show()
fig = plt.figure(figsize=(14,6), dpi=80)
plt.plot(lidar.index, lidar['wind_dir_7_corr'])
plt.title('wind_dir_7_corr')
plt.xlabel('time')
plt.xticks(rotation= 90)
plt.show()
'''




#merging dataframes together:
#by manuel analysing the data we foung following intervalls with constant enviroment circumstances
#Installation im Zeitraum vom 22.9/23.9
#4-12 Uhr
#17-18 Uhr
#19-24 Uhr
'''
hammerhead
03:16:30	12:05:47
sbi1
14:15:43	12:39:12
sbi2	
22:13:32	00:19:04
tnhb1	
12:39:13	22:04:11
tnhb2	
00:30:45	00:42:54

'''

#for boje data resampling and then adding to sampleframes
wmb.columns = ('epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss','TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav', 'Eps', '#Waves')
UTC = []
for k in range(len(wmb)):
    UTC.append(pd.Timestamp.fromtimestamp(wmb.iloc[k, 0]))
wmb['epoch'] = UTC

wmb.index = wmb['epoch']
wmb.pop('epoch')
wmb = wmb.resample('1S', label = 'right', closed = 'right').mean().pad() / 1800

#same with lidar data
UTC = []
for k in range(len(lidar)):
    UTC.append(pd.Timestamp.fromtimestamp(lidar.iloc[k, 0]))
lidar['epoch'] = UTC
lidar.index = lidar['epoch']
del lidar['epoch']
lidar = lidar.resample('1S', label='left').mean().pad()
lidar = lidar


#helping method to get the beginning and end time for a dataframe, inclusive the duration
def getduration(df):
    start = df.index[0]
    ende = df.index[-1]
    print(start, ende)
    return ende-start
counter = 0
#generating timestamps for every dataframe
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


# generating hammerhead file
for i in range(4):
    data[i] = data[i]['2019-09-22 03:16:30': '2019-09-22 12:05:47']
transition_wmb =wmb['2019-09-22 03:16:30': '2019-09-22 12:05:47']
transition_lidar = lidar['2019-09-22 03:16:30': '2019-09-22 12:05:47']
result =pd.concat([data[0],data[1],data[2],data[3], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine06/hammerhead_turbine06.csv')

#generating sbi1 file

for i in range(4,7):
    data[i] = data[i]['2019-09-22 12:15:43': '2019-09-22 12:39:12']
transition_wmb =wmb['2019-09-22 12:15:43': '2019-09-22 12:39:12']
transition_lidar = lidar['2019-09-22 12:15:43': '2019-09-22 12:39:12']
result = pd.concat([data[4], data[5], data[6], transition_lidar, transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine06/sbi1_turbine6.csv')

#generating sbi2 file
#22:13:32	00:19:04
for i in range(7,10):
    data[i] = data[i]['2019-09-22 22:13:32': '2019-09-23 00:19:04']
transition_wmb =wmb['2019-09-22 22:13:32': '2019-09-23 00:19:04']
transition_lidar = lidar['2019-09-22 22:13:32': '2019-09-23 00:19:04']
result = pd.concat([data[7], data[8], data[9], transition_lidar, transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine06/sbi2_turbine6.csv')

#generating tnhb1 file
#12:39:13	22:04:11
for i in range(10,14):
    data[i] = data[i]['2019-09-22 12:41:44': '2019-09-22 22:04:11']
transition_wmb =wmb['2019-09-22 12:41:44': '2019-09-22 22:04:11']
transition_lidar = lidar['2019-09-22 12:41:44': '2019-09-22 22:04:11']
result = pd.concat([data[10], data[11], data[12], data[13], transition_lidar, transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine06/tnhb1_turbine6.csv')

#generating tnhb2 file
#00:30:45	00:42:54
for i in range(14,18):
    data[i] = data[i]['2019-09-23 00:30:45': '2019-09-23 00:42:54']
transition_wmb =wmb['2019-09-23 00:30:45': '2019-09-23 00:42:54']
transition_lidar = lidar['2019-09-23 00:30:45': '2019-09-23 00:42:54']
result = pd.concat([data[14], data[15], data[16], data[17],transition_lidar, transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine06/tnhb2_turbine6.csv')

'''
sbi1_turbine6 = pd.read_csv('Results_preprocessing/turbine06/sbi1_turbine6.csv', delimiter = ',')
corrMatrix = sbi1_turbine6.corr() #coolwarm
sn.heatmap(corrMatrix, annot=False)
plt.show()

'''