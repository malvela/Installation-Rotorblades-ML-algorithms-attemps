import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
'''
turbine-16_helihoist-1_tom_acc-vel-pos_sbi1_2019-12-17-03-56-11_2019-12-17-04-22-54

turbine-16_helihoist-1_tom_acc-vel-pos_sbi2_2019-12-22-06-09-43_2019-12-22-18-47-25	22.12.2019	06:09:43	22.12.2019	18:47:25
turbine-16_sbitroot_tom_acc-vel-pos_sbi2_2019-12-22-06-15-57_2019-12-22-18-47-00	22.12.2019	06:15:57	22.12.2019	18:47:00
turbine-16_sbittip_tom_acc-vel-pos_sbi2_2019-12-22-06-18-23_2019-12-22-18-35-19	22.12.2019	06:18:23	22.12.2019	18:35:19

turbine-16_helihoist-1_tom_acc-vel-pos_tnhb1_2019-12-17-04-22-54_2019-12-22-06-09-32
turbine-16_helihoist-1_tom_geometry_tnhb1_2019-12-17-04-22-54_2019-12-22-06-09-32
turbine-16_sbitroot_tom_acc-vel-pos_tnhb1_2019-12-21-12-47-53_2019-12-22-06-15-57
turbine-16_sbittip_tom_acc-vel-pos_tnhb1_2019-12-21-12-44-57_2019-12-22-06-18-23

wmb-sued-2019-12-17
wmb-sued-2019-12-18
wmb-sued-2019-12-19
wmb-sued-2019-12-20
wmb-sued-2019-12-21

lidar_2019_12_17
lidar_2019_12_18
lidar_2019_12_19
lidar_2019_12_20
lidar_2019_12_21
'''

#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-16**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-16**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-16**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-16**.csv'))


data = []

helihoist_sbi1 = pd.read_csv(sbi1[0], delimiter = ',')


data.append(helihoist_sbi1) ,

helihoist_sbi2 = pd.read_csv(sbi2[0], delimiter = ',')
sbiroot_sbi2 = pd.read_csv(sbi2[1], delimiter = ',')
sbitip_sbi2 = pd.read_csv(sbi2[2], delimiter = ',')


data.append(helihoist_sbi2) ,data.append(sbiroot_sbi2) ,data.append(sbitip_sbi2)

helihoist_tnhb1 = pd.read_csv(tnhb1[0], delimiter = ',')
helihoist_geo_tnhb1 = pd.read_csv(tnhb1[1], delimiter = ',')
sbiroot_tnhb1 = pd.read_csv(tnhb1[2], delimiter = ',')
sbitip_tnhb1 = pd.read_csv(tnhb1[3], delimiter = ',')

data.append(helihoist_tnhb1) ,data.append(helihoist_geo_tnhb1) ,data.append(sbiroot_tnhb1),data.append(sbitip_tnhb1)

wmb1= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-12-17.csv', delimiter = ' ')
wmb2= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-12-18.csv', delimiter = ' ')
wmb3= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-12-19.csv', delimiter = ' ')
wmb4= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-12-20.csv', delimiter = ' ')
wmb5= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-12-21.csv', delimiter = ' ')

wmb_all = []
wmb_all.append(wmb1), wmb_all.append(wmb2), wmb_all.append(wmb3), wmb_all.append(wmb4), wmb_all.append(wmb5)

lidar1= pd.read_csv('environment/environment/wind/lidar/lidar_2019-12-17.csv', delimiter = ' ')
lidar2= pd.read_csv('environment/environment/wind/lidar/lidar_2019-12-18.csv', delimiter = ' ')
lidar3= pd.read_csv('environment/environment/wind/lidar/lidar_2019-12-19.csv', delimiter = ' ')
lidar4= pd.read_csv('environment/environment/wind/lidar/lidar_2019-12-20.csv', delimiter = ' ')
lidar5= pd.read_csv('environment/environment/wind/lidar/lidar_2019-12-21.csv', delimiter = ' ')

data.append(lidar1), data.append(lidar2), data.append(lidar3), data.append(lidar4),data.append(lidar5),
lidar_all =[]
lidar_all.append(lidar1), lidar_all.append(lidar2), lidar_all.append(lidar3), lidar_all.append(lidar4), lidar_all.append(lidar5),
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
wmb = wmb.resample('3S', label='left').mean().pad() / 1800
wmb = wmb

UTC = []
for k in range(len(lidar)):
    UTC.append(pd.Timestamp.fromtimestamp(lidar.iloc[k, 0]))
lidar['epoch'] = UTC
lidar.index = lidar['epoch']
del lidar['epoch']
lidar = lidar.resample('3S', label='left').mean().pad()
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
#generating timestamps for every dataframe
counter = 0
for df in data:
    UTC = []
    for k in range(len(df)):
        UTC.append(pd.Timestamp.fromtimestamp(df.iloc[k, 0]))
    df['epoch'] = UTC
    df.index = df['epoch']
    del df['epoch']
    df = df.resample('3S', label = 'left').mean().pad()
    data[counter] = df
    counter = counter+1
'''    
#generating sbi1 file
#03:56:11   04:22:54
for i in range(1):
    data[i] = data[i]['2019-12-17 03:56:11': '2019-12-17 04:22:54']
transition_wmb =wmb['2019-12-17 03:56:11': '2019-12-17 04:22:54']
transition_lidar = lidar['2019-12-17 03:56:11': '2019-12-17 04:22:54']
result =pd.concat([data[0], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine16/sbi1_turbine16.csv')


#generating sbi2 file
#06:18:23   18:35:19
for i in range(1,4):
    data[i] = data[i]['2019-12-22 06:18:23': '2019-12-22 18:35:19']
transition_wmb =wmb['2019-12-22 06:18:23': '2019-12-22 18:35:19']
transition_lidar = lidar['2019-12-22 06:18:23': '2019-12-22 18:35:19']
result =pd.concat([data[1],data[2],data[3], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine16/sbi2_turbine16.csv')


#generating tnhb1 file
#12:47:53   06:09:32
for i in range(4,8):
    data[i] = data[i]['2019-12-21 12:47:53': '2019-12-22 06:09:32']
transition_wmb =wmb['2019-12-21 12:47:53': '2019-12-22 06:09:32']
transition_lidar = lidar['2019-12-21 12:47:53': '2019-12-22 06:09:32']
result =pd.concat([data[4],data[5],data[6],data[7], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine16/tnhb1_turbine16.csv')
'''
'''
files to extract:
17.12.2019	04:22:54	22.12.2019	06:09:32
'''
print(data[5].index[0])
print(data[5].index[-1])
data[5] = data[5]['2019-12-17 05:22:54': '2019-12-22 07:09:32']
transition_wmb =wmb['2019-12-17 05:22:54': '2019-12-22 07:09:32']
transition_lidar = lidar['2019-12-17 05:22:54': '2019-12-22 07:09:32']
result = pd.concat([data[5], transition_lidar, transition_wmb], axis=1)
del result['max_deflection_i']
del result['ddt_max_deflection']
del result['eccentricity']
del result['ddt_axis_ratio']
del result['ddt_eccentricity']
del result['axis_angle_signed']
del result['axis_angle_unsigned']
del result['axis_azimuth']
del result['ddt_axis_angle_signed']
del result['ddt_axis_angle_unsigned']
del result['p2p_angle_unsigned']
del result['p2p_angle_signed']
del result['p2p_azimuth']
del result['ddt_p2p_azimuth_unwrapped']
del result['ddt_p2p_azimuth']
del result['ddt_p2p_angle_unsigned']
del result['ddt_p2p_angle_signed']
del result['wind_speed_0']
del result['wind_dir_0']
del result['wind_dir_0_corr']
del result['height_0']
del result['wind_speed_1']
del result['wind_dir_1']
del result['wind_dir_1_corr']
del result['height_1']
del result['wind_speed_2']
del result['wind_dir_2']
del result['wind_dir_2_corr']
del result['height_2']
del result['wind_dir_3']
del result['height_3']
del result['wind_speed_4']
del result['wind_dir_4']
del result['wind_dir_4_corr']
del result['height_4']
del result['wind_speed_5']
del result['wind_dir_5']
del result['wind_dir_5_corr']
del result['height_5']
del result['wind_speed_6']
del result['wind_dir_6']
del result['wind_dir_6_corr']
del result['height_6']
del result['wind_speed_7']
del result['wind_dir_7']
del result['wind_dir_7_corr']
del result['height_7']
del result['wind_speed_8']
del result['wind_dir_8']
del result['wind_dir_8_corr']
del result['height_8']
del result['wind_speed_9']
del result['wind_dir_9']
del result['wind_dir_9_corr']
del result['height_9']
del result['wind_speed_10']
del result['wind_dir_10']
del result['wind_dir_10_corr']
del result['height_10']
del result['heading']
del result['Tp']
del result['Sprp']
del result['Tz']
del result['Hm0']
del result['TI']
del result['T1']
del result['Tc']
del result['Tdw2']
del result['Tdw1']
del result['Tpc']
del result['nu']
del result['eps']
del result['QP']
del result['Ss']
del result['TRef']
del result['Bat']
del result['Percentage']
del result['H(1/10)']
del result['T(1/10)']
del result['H(1/3)']
del result['T(1/3)']
del result['Eps']
del result['#Waves']
result.to_csv('Results_preprocessing/geometry_files/tnhb1_turbine16.csv')