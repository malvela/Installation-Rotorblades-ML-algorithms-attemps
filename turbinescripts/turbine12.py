import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt

'''
turbine-12_helihoist-1_tom_acc-vel-pos_sbi1_2019-11-05-04-33-05_2019-11-05-06-55-15
turbine-12_sbitroot_tom_acc-vel-pos_sbi1_2019-11-05-04-18-04_2019-11-05-06-32-41
turbine-12_sbittip_tom_acc-vel-pos_sbi1_2019-11-05-04-11-07_2019-11-05-06-53-50

gehen teilweise länger ->
turbine-12_helihoist-1_tom_acc-vel-pos_tnhb1_2019-11-05-06-55-15_2019-11-07-01-33-43
turbine-12_helihoist-1_tom_geometry_tnhb1_2019-11-05-06-55-15_2019-11-07-01-33-43
turbine-12_sbitroot_tom_acc-vel-pos_tnhb1_2019-11-05-06-32-42_2019-11-07-01-05-50
turbine-12_sbittip_tom_acc-vel-pos_tnhb1_2019-11-05-06-53-50_2019-11-05-23-27-03

wmb-sued-2019-11-04
wmb-sued-2019-11-05
wmb-sued-2019-11-06
wmb-sued-2019-11-07

lidar_2019_11_04
lidar_2019_11_05
lidar_2019_11_06
lidar_2019_11_07

'''


#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-12**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-12**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-12**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-12**.csv'))


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
data.append(helihoist_tnhb1) ,data.append(helihoist_geo_tnhb1) ,data.append(sbiroot_tnhb1), data.append(sbitip_tnhb1)

wmb1= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-04.csv', delimiter = ' ')
wmb2= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-05.csv', delimiter = ' ')
wmb3= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-06.csv', delimiter = ' ')
wmb4= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-07.csv', delimiter = ' ')


wmb_all = []
wmb_all.append(wmb1), wmb_all.append(wmb2), wmb_all.append(wmb3), wmb_all.append(wmb4)

lidar1= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-04.csv', delimiter = ' ')
lidar2= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-05.csv', delimiter = ' ')
lidar3= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-06.csv', delimiter = ' ')
lidar4= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-07.csv', delimiter = ' ')

data.append(lidar1), data.append(lidar2), data.append(lidar3), data.append(lidar4),
lidar_all =[]
lidar_all.append(lidar1), lidar_all.append(lidar2), lidar_all.append(lidar3), lidar_all.append(lidar4),
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
'''
# generating hammerhead file
#23:44:46   04:11:07
for i in range(4):
    data[i] = data[i]['2019-11-04 23:44:46': '2019-11-05 04:11:07']
transition_wmb =wmb['2019-11-04 23:44:46': '2019-11-05 04:11:07']
transition_lidar = lidar['2019-11-04 23:44:46': '2019-11-05 04:11:07']
result =pd.concat([data[0],data[1],data[2],data[3], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine12/hammerhead_turbine12.csv')

#generating sbi1 file
#04:33:05   06:32:41
for i in range(4,7):
    data[i] = data[i]['2019-11-05 04:33:05': '2019-11-05 06:32:41']
transition_wmb =wmb['2019-11-05 04:33:05': '2019-11-05 06:32:41']
transition_lidar = lidar['2019-11-05 04:33:05': '2019-11-05 06:32:41']
result =pd.concat([data[4],data[5],data[6], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine12/sbi1_turbine12.csv')


#generating tnhb1 file
#06:55:15   23:27:03
for i in range(7,11):
    data[i] = data[i]['2019-11-05 06:55:15': '2019-11-05 23:27:03']
transition_wmb =wmb['2019-11-05 06:55:15': '2019-11-05 23:27:03']
transition_lidar = lidar['2019-11-05 06:55:15': '2019-11-05 23:27:03']
result =pd.concat([data[7],data[8],data[9],data[10], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine12/tnhb1_turbine12.csv')
'''

'''
files to extract
04.11.2019	23:16:25	05.11.2019	04:33:05
05.11.2019	06:55:15	07.11.2019	01:33:43
'''

print(data[1].index[0])
print(data[1].index[-1])
data[1] = data[1]['2019-11-05 00:16:25': '2019-11-05 05:32:57']
transition_wmb =wmb['2019-11-05 00:16:25': '2019-11-05 05:32:57']
transition_lidar = lidar['2019-11-05 00:16:25': '2019-11-05 05:32:57']
result = pd.concat([data[1], transition_lidar, transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine12.csv')
print(data[8].index[0])
print(data[8].index[-1])
data[8] = data[8]['2019-11-05 07:55:15': '2019-11-07 02:33:38']
transition_wmb =wmb['2019-11-05 07:55:15': '2019-11-07 02:33:38']
transition_lidar = lidar['2019-11-05 07:55:15': '2019-11-07 02:33:38']
result = pd.concat([data[8], transition_lidar, transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb1_turbine12.csv')