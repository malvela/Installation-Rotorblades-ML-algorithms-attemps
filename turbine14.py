import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
'''
turbine-14_helihoist-1_tom_acc-vel-pos_hammerhead_2019-11-24-16-42-08_2019-11-24-21-16-51
turbine-14_helihoist-1_tom_geometry_hammerhead_2019-11-24-16-42-08_2019-11-24-21-16-51
turbine-14_sbitroot_tom_acc-vel-pos_hammerhead_2019-11-24-17-36-41_2019-11-24-21-15-48
turbine-14_sbittip_tom_acc-vel-pos_hammerhead_2019-11-24-17-46-36_2019-11-24-21-21-03

turbine-14_helihoist-1_tom_acc-vel-pos_sbi1_2019-11-24-21-16-51_2019-11-25-04-59-18
turbine-14_sbitroot_tom_acc-vel-pos_sbi1_2019-11-24-21-15-48_2019-11-25-04-54-08
turbine-14_sbittip_tom_acc-vel-pos_sbi1_2019-11-24-21-21-04_2019-11-25-04-47-45

turbine-14_helihoist-1_tom_acc-vel-pos_sbi2_2019-11-25-08-27-01_2019-11-25-11-17-00
turbine-14_sbitroot_tom_acc-vel-pos_sbi2_2019-11-25-08-33-35_2019-11-25-11-11-16
turbine-14_sbittip_tom_acc-vel-pos_sbi2_2019-11-25-08-25-08_2019-11-25-10-59-28

turbine-14_helihoist-1_tom_acc-vel-pos_tnhb1_2019-11-25-04-59-18_2019-11-25-08-27-01
turbine-14_helihoist-1_tom_geometry_tnhb1_2019-11-25-04-59-18_2019-11-25-08-27-01
turbine-14_sbitroot_tom_acc-vel-pos_tnhb1_2019-11-25-04-54-09_2019-11-25-08-33-35
turbine-14_sbittip_tom_acc-vel-pos_tnhb1_2019-11-25-04-47-45_2019-11-25-08-25-08

wmb-sued-2019-11-24
wmb-sued-2019-11-25


lidar_2019_11_24
lidar_2019_11_25


'''


#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-14**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-14**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-14**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-14**.csv'))
tnhb2 = sorted(glob('Daten/tnhb2/tnhb2/turbine-14**.csv'))

data = []
helihoist_tele_hammerhead = pd.read_csv(hammerhead[0], delimiter = ',')
helihoist_geo_hammerhead = pd.read_csv(hammerhead[1], delimiter = ',')
sbitroot_hammerhead = pd.read_csv(hammerhead[2], delimiter = ',')
sbitip_hammerhead = pd.read_csv(hammerhead[3], delimiter = ',')
data.append(helihoist_tele_hammerhead) , data.append(helihoist_geo_hammerhead), data.append(sbitroot_hammerhead)  ,data.append(sbitip_hammerhead)

helihoist_sbi1 = pd.read_csv(sbi1[0], delimiter= ',')
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

wmb1= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-24.csv', delimiter = ' ')
wmb2= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-25.csv', delimiter = ' ')

wmb_all = []
wmb_all.append(wmb1), wmb_all.append(wmb2)

lidar1 =pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-24.csv', delimiter = ' ')
lidar2 =pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-25.csv', delimiter = ' ')

data.append(lidar1), data.append(lidar2)
lidar_all = []
lidar_all.append(lidar1),lidar_all.append(lidar2)
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
UTC = []
for k in range(len(wmb)):
    UTC.append(pd.Timestamp.fromtimestamp(wmb.iloc[k, 0]))
wmb['epoch'] = UTC
wmb.index = wmb['epoch']
del wmb['epoch']
wmb = wmb.resample('1S', label='left').mean().pad() / 1800
wmb = wmb


UTC = []
for k in range(len(lidar)):
    UTC.append(pd.Timestamp.fromtimestamp(lidar.iloc[k, 0]))
lidar['epoch'] = UTC
lidar.index = lidar['epoch']
del lidar['epoch']
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
plt.plot(wmb.index, wmb['#Waves'])
plt.title('#Waves')
plt.xlabel('time')
plt.xticks(rotation= 90)
plt.show()
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
#17:46:36  21:15:48
for i in range(4):
    data[i] = data[i]['2019-11-24 17:46:36': '2019-11-24 21:15:48']
transition_wmb =wmb['2019-11-24 17:46:36': '2019-11-24 21:15:48']
transition_lidar = lidar['2019-11-24 17:46:36': '2019-11-24 21:15:48']
result =pd.concat([data[0],data[1],data[2],data[3], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine14/hammerhead_turbine14.csv')

#generating sbi1 file
#21:21:04   04:47:45
for i in range(4,7):
    data[i] = data[i]['2019-11-24 21:21:04': '2019-11-25 04:47:45']
transition_wmb =wmb['2019-11-24 21:21:04': '2019-11-25 04:47:45']
transition_lidar = lidar['2019-11-24 21:21:04': '2019-11-25 04:47:45']
result =pd.concat([data[4],data[5],data[6], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine14/sbi1_turbine14.csv')


#generating sbi2 file
#08:33:35   10:59:28
for i in range(7,10):
    data[i] = data[i]['2019-11-25 08:33:35': '2019-11-25 10:59:28']
transition_wmb =wmb['2019-11-25 08:33:35': '2019-11-25 10:59:28']
transition_lidar = lidar['2019-11-25 08:33:35': '2019-11-25 10:59:28']
result =pd.concat([data[7],data[8],data[9], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine14/sbi2_turbine14.csv')


#generating tnhb1 file
#04:59:18   08:25:08
for i in range(10,14):
    data[i] = data[i]['2019-11-25 04:59:18': '2019-11-25 08:25:08']
transition_wmb =wmb['2019-11-25 04:59:18': '2019-11-25 08:25:08']
transition_lidar = lidar['2019-11-25 04:59:18': '2019-11-25 08:25:08']
result =pd.concat([data[10],data[11],data[12],data[13], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine14/tnhb1_turbine14.csv')