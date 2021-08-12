import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
'''
turbine-04_helihoist-1_tom_acc-vel-pos_hammerhead_2019-09-01-10-20-45_2019-09-07-07-19-26
turbine-04_helihoist-1_tom_geometry_hammerhead_2019-09-01-10-20-45_2019-09-07-07-19-26
turbine-04_sbitroot_tom_acc-vel-pos_hammerhead_2019-09-07-04-48-53_2019-09-07-07-12-46
turbine-04_sbittip_tom_acc-vel-pos_hammerhead_2019-09-07-04-41-36_2019-09-07-07-25-10

turbine-04_helihoist-1_tom_acc-vel-pos_sbi1_2019-09-07-07-19-27_2019-09-07-12-40-14
turbine-04_sbitroot_tom_acc-vel-pos_sbi1_2019-09-07-07-12-47_2019-09-07-12-39-30
turbine-04_sbittip_tom_acc-vel-pos_sbi1_2019-09-07-07-25-10_2019-09-07-12-34-23

turbine-04_helihoist-1_tom_acc-vel-pos_tnhb1_2019-09-07-12-40-14_2019-09-07-21-49-58
turbine-04_helihoist-1_tom_geometry_tnhb1_2019-09-07-12-40-14_2019-09-07-21-49-58
turbine-04_sbitroot_tom_acc-vel-pos_tnhb1_2019-09-07-12-39-30_2019-09-08-04-43-15
turbine-04_sbittip_tom_acc-vel-pos_tnhb1_2019-09-07-12-34-23_2019-09-08-04-49-49

wmb-sued-2019-9-1
wmb-sued-2019-9-2
wmb-sued-2019-9-3
wmb-sued-2019-9-4
wmb-sued-2019-9-5
wmb-sued-2019-9-6
wmb-sued-2019-9-7

lidar_2019_09_01
lidar_2019_09_03
lidar_2019_09_04
lidar_2019_09_05
lidar_2019_09_06
lidar_2019_09_07


'''
#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-04**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-04**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-04**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-04**.csv'))
tnhb2 = sorted(glob('Daten/tnhb2/tnhb2/turbine-04**.csv'))
#wmb =  "wmb-sued-2019-9-22"
#lidar =  "lidar_2019_09_22"
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

helihoist_tnhb1 = pd.read_csv(tnhb1[0], delimiter = ',')
helihoist_geo_tnhb1 = pd.read_csv(tnhb1[1], delimiter = ',')
sbiroot_tnhb1 = pd.read_csv(tnhb1[2], delimiter = ',')
sbitip_tnhb1 = pd.read_csv(tnhb1[3], delimiter = ',')

data.append(helihoist_tnhb1) ,data.append(helihoist_geo_tnhb1) ,data.append(sbiroot_tnhb1),data.append(sbitip_tnhb1)

wmb1= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-01.csv', delimiter = ' ')
wmb2= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-02.csv', delimiter = ' ')
wmb3= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-03.csv', delimiter = ' ')
wmb4= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-04.csv', delimiter = ' ')
wmb5= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-05.csv', delimiter = ' ')
wmb6= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-06.csv', delimiter = ' ')
wmb7= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-07.csv', delimiter = ' ')

data.append(wmb1), data.append(wmb2), data.append(wmb3), data.append(wmb4), data.append(wmb5), data.append(wmb6), data.append(wmb7)
wmb_all = []
wmb_all.append(wmb1), wmb_all.append(wmb2), wmb_all.append(wmb3), wmb_all.append(wmb4), wmb_all.append(wmb5), wmb_all.append(wmb6), wmb_all.append(wmb7)

lidar1= pd.read_csv('environment/environment/wind/lidar/lidar_2019-09-01.csv', delimiter = ' ')
lidar2= pd.read_csv('environment/environment/wind/lidar/lidar_2019-09-03.csv', delimiter = ' ')
lidar3= pd.read_csv('environment/environment/wind/lidar/lidar_2019-09-04.csv', delimiter = ' ')
lidar4= pd.read_csv('environment/environment/wind/lidar/lidar_2019-09-05.csv', delimiter = ' ')
lidar5= pd.read_csv('environment/environment/wind/lidar/lidar_2019-09-06.csv', delimiter = ' ')
lidar6= pd.read_csv('environment/environment/wind/lidar/lidar_2019-09-07.csv', delimiter = ' ')



data.append(lidar1), data.append(lidar2), data.append(lidar3), data.append(lidar4), data.append(lidar5), data.append(lidar6),
lidar_all =[]
lidar_all.append(lidar1), lidar_all.append(lidar2), lidar_all.append(lidar3), lidar_all.append(lidar5), data.append(lidar6)
buffer1 = []

for i in wmb_all:
    i.columns = (
    'epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss',
    'TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav', 'Eps',
    '#Waves')
    buffer1.append(i)
    wmb = pd.concat(buffer1, axis=0)
    wmb.columns = (
    'epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss',
    'TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav', 'Eps',
    '#Waves')
buffer2 = []
for j in lidar_all:
    j.columns = ('epoch', 'wind_speed_0', 'wind_dir_0', 'wind_dir_0_corr', 'height_0', 'wind_speed_1', 'wind_dir_1',
                    'wind_dir_1_corr', 'height_1', 'wind_speed_2', 'wind_dir_2', 'wind_dir_2_corr', 'height_2',
                    'wind_speed_3', 'wind_dir_3', 'wind_dir_3_corr', 'height_3', 'wind_speed_4', 'wind_dir_4',
                    'wind_dir_4_corr', 'height_4', 'wind_speed_5', 'wind_dir_5', 'wind_dir_5_corr', 'height_5',
                    'wind_speed_6', 'wind_dir_6', 'wind_dir_6_corr', 'height_6', 'wind_speed_7', 'wind_dir_7',
                    'wind_dir_7_corr', 'height_7', 'wind_speed_8', 'wind_dir_8', 'wind_dir_8_corr', 'height_8',
                    'wind_speed_9', 'wind_dir_9', 'wind_dir_9_corr', 'height_9', 'wind_speed_10', 'wind_dir_10',
                    'wind_dir_10_corr', 'height_10', 'heading')
    buffer2.append(j)

    lidar = pd.concat(buffer2, axis=0)
    lidar.columns = ('epoch', 'wind_speed_0', 'wind_dir_0', 'wind_dir_0_corr', 'height_0', 'wind_speed_1', 'wind_dir_1',
                    'wind_dir_1_corr', 'height_1', 'wind_speed_2', 'wind_dir_2', 'wind_dir_2_corr', 'height_2',
                    'wind_speed_3', 'wind_dir_3', 'wind_dir_3_corr', 'height_3', 'wind_speed_4', 'wind_dir_4',
                    'wind_dir_4_corr', 'height_4', 'wind_speed_5', 'wind_dir_5', 'wind_dir_5_corr', 'height_5',
                    'wind_speed_6', 'wind_dir_6', 'wind_dir_6_corr', 'height_6', 'wind_speed_7', 'wind_dir_7',
                    'wind_dir_7_corr', 'height_7', 'wind_speed_8', 'wind_dir_8', 'wind_dir_8_corr', 'height_8',
                    'wind_speed_9', 'wind_dir_9', 'wind_dir_9_corr', 'height_9', 'wind_speed_10', 'wind_dir_10',
                    'wind_dir_10_corr', 'height_10', 'heading')
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
lidar = lidar.resample('1S', label='left').mean().pad()
lidar = lidar
'''
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

# generating hammerhead file
#04:48:53	07:12:46

for i in range(0,4):
    data[i] = data[i]['2019-09-07 06:48:53': '2019-09-07 09:12:46']
transition_wmb =wmb['2019-09-07 06:48:53': '2019-09-07 09:12:46']
transition_lidar = lidar['2019-09-07 06:48:53': '2019-09-07 09:12:46']
result =pd.concat([data[0],data[1],data[2],data[3], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine04/hammerhead_turbine04.csv')

#generating sbi1 file
#07: 19:27  12: 34:23

for i in range(4,7):
    data[i] = data[i]['2019-09-07 09:19:27': '2019-09-07 14:34:23']
transition_wmb =wmb['2019-09-07 09:19:27': '2019-09-07 14:34:23']
transition_lidar = lidar['2019-09-07 09:19:27': '2019-09-07 14:34:23']
result = pd.concat([data[4], data[5], data[6], transition_lidar, transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine04/sbi1_turbine4.csv')


#generating tnhb1 file
#12:34:23	04:43:15

for i in range(7,11):
    data[i] = data[i]['2019-09-07 14:34:23': '2019-09-07 21:49:58']
transition_wmb =wmb['2019-09-07 14:34:23': '2019-09-07 21:49:58']
transition_lidar = lidar['2019-09-07 14:34:23': '2019-09-07 21:49:58']
result = pd.concat([data[10], data[11], data[12], data[13], transition_lidar, transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine04/tnhb1_turbine4.csv')

