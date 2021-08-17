import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
'''
turbine-07_helihoist-1_tom_acc-vel-pos_hammerhead_2019-09-24-11-38-50_2019-09-25-12-01-27
turbine-07_helihoist-1_tom_geometry_hammerhead_2019-09-24-11-38-50_2019-09-25-12-01-27
turbine-07_sbitroot_tom_acc-vel-pos_hammerhead_2019-09-24-11-56-08_2019-09-25-11-58-23
turbine-07_sbittip_tom_acc-vel-pos_hammerhead_2019-09-24-11-59-00_2019-09-25-00-25-15

turbine-07_helihoist-1_tom_acc-vel-pos_sbi1_2019-09-25-12-01-27_2019-09-25-13-49-58
turbine-07_sbitroot_tom_acc-vel-pos_sbi1_2019-09-25-11-58-23_2019-09-25-13-48-10

turbine-07_helihoist-1_tom_acc-vel-pos_sbi2_2019-09-25-18-30-36_2019-09-25-21-28-56
turbine-07_sbitroot_tom_acc-vel-pos_sbi2_2019-09-25-18-15-46_2019-09-25-21-25-41

turbine-07_helihoist-1_tom_acc-vel-pos_tnhb1_2019-09-25-13-49-58_2019-09-25-18-30-35
turbine-07_helihoist-1_tom_geometry_tnhb1_2019-09-25-13-49-58_2019-09-25-18-30-35
turbine-07_sbitroot_tom_acc-vel-pos_tnhb1_2019-09-25-13-48-10_2019-09-25-18-15-46

turbine-07_helihoist-1_tom_acc-vel-pos_tnhb2_2019-09-25-21-28-57_2019-09-26-01-04-54
turbine-07_helihoist-1_tom_geometry_tnhb2_2019-09-25-21-28-57_2019-09-26-01-04-54
turbine-07_sbitroot_tom_acc-vel-pos_tnhb2_2019-09-25-21-25-41_2019-09-26-00-37-22

wmb-sued-2019-9-24
wmb-sued-2019-9-25

lidar_2019_09_24
lidar_2019_09_25

alles vorhanden

'''

#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-07**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-07**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-07**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-07**.csv'))
tnhb2 = sorted(glob('Daten/tnhb2/tnhb2/turbine-07**.csv'))

data = []
helihoist_tele_hammerhead = pd.read_csv(hammerhead[0], delimiter = ',')
helihoist_geo_hammerhead = pd.read_csv(hammerhead[1], delimiter = ',')
sbitroot_hammerhead = pd.read_csv(hammerhead[2], delimiter = ',')
sbitip_hammerhead = pd.read_csv(hammerhead[3], delimiter = ',')
data.append(helihoist_tele_hammerhead) , data.append(helihoist_geo_hammerhead), data.append(sbitroot_hammerhead)  ,data.append(sbitip_hammerhead)

helihoist_sbi1 = pd.read_csv(sbi1[0], delimiter= ',')
sbiroot_sbi1 = pd.read_csv(sbi1[1], delimiter = ',')

data.append(helihoist_sbi1) ,data.append(sbiroot_sbi1)

helihoist_sbi2 = pd.read_csv(sbi2[0], delimiter = ',')
sbiroot_sbi2 = pd.read_csv(sbi2[1], delimiter = ',')


data.append(helihoist_sbi2) ,data.append(sbiroot_sbi2)

helihoist_tnhb1 = pd.read_csv(tnhb1[0], delimiter = ',')
helihoist_geo_tnhb1 = pd.read_csv(tnhb1[1], delimiter = ',')
sbiroot_tnhb1 = pd.read_csv(tnhb1[2], delimiter = ',')

data.append(helihoist_tnhb1) ,data.append(helihoist_geo_tnhb1) ,data.append(sbiroot_tnhb1)

helihoist_tnhb2 = pd.read_csv(tnhb2[0], delimiter = ',')
helihoist_geo_tnhb2 = pd.read_csv(tnhb2[1], delimiter = ',')
sbiroot_tnhb2 = pd.read_csv(tnhb2[2], delimiter = ',')

data.append(helihoist_tnhb2) ,data.append(helihoist_geo_tnhb2) ,data.append(sbiroot_tnhb2),

wmb1= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-24.csv', delimiter = ' ')
wmb2= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-25.csv', delimiter = ' ')

wmb_all =[]
wmb_all.append(wmb1), wmb_all.append(wmb2)

lidar1 =pd.read_csv('environment/environment/wind/lidar/lidar_2019-09-24.csv', delimiter = ' ')
lidar2 =pd.read_csv('environment/environment/wind/lidar/lidar_2019-09-25.csv', delimiter = ' ')

data.append(lidar1), data.append(lidar2)

lidar_all = []
lidar_all.append(lidar1), lidar_all.append(lidar2)

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

counter = 0
#generating timestamps for every dataframe
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
# generating hammerhead file
#11:59:00   00:25:15
for i in range(4):
    data[i] = data[i]['2019-09-24 11:59:00': '2019-09-25 00:25:15']
transition_wmb =wmb['2019-09-24 11:59:00': '2019-09-25 00:25:15']
transition_lidar = lidar['2019-09-24 11:59:00': '2019-09-25 00:25:15']
result =pd.concat([data[0],data[1],data[2],data[3], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine07/hammerhead_turbine07.csv')

#generating sbi1 file
#12:01:27   13:48:10
for i in range(4,6):
    data[i] = data[i]['2019-09-25 12:01:27': '2019-09-25 13:48:10']
transition_wmb =wmb['2019-09-25 12:01:27': '2019-09-25 13:48:10']
transition_lidar = lidar['2019-09-25 12:01:27': '2019-09-25 13:48:10']
result =pd.concat([data[4],data[5], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine07/sbi1_turbine07.csv')

#generating sbi2 file
#18:30:36   21:25:41
for i in range(6,8):
    data[i] = data[i]['2019-09-25 18:30:36': '2019-09-25 21:25:41']
transition_wmb =wmb['2019-09-25 18:30:36': '2019-09-25 21:25:41']
transition_lidar = lidar['2019-09-25 18:30:36': '2019-09-25 21:25:41']
result =pd.concat([data[6],data[7], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine07/sbi2_turbine07.csv')

#generating tnhb1 file
#13:49:58   18:15:46
for i in range(8,11):
    data[i] = data[i]['2019-09-25 13:49:58': '2019-09-25 18:15:46']
transition_wmb =wmb['2019-09-25 13:49:58': '2019-09-25 18:15:46']
transition_lidar = lidar['2019-09-25 13:49:58': '2019-09-25 18:15:46']
result =pd.concat([data[8],data[9],data[10], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine07/tnhb1_turbine07.csv')

#generating tnhb2 file
#21:28:57   00:37:22
for i in range(11,14):
    data[i] = data[i]['2019-09-25 21:28:57': '2019-09-26 00:37:22']
transition_wmb =wmb['2019-09-25 21:28:57': '2019-09-26 00:37:22']
transition_lidar = lidar['2019-09-25 21:28:57': '2019-09-26 00:37:22']
result =pd.concat([data[11],data[12],data[13], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine07/tnhb2_turbine07.csv')
'''


'''
files to extract
24.09.2019	11:38:50	25.09.2019	12:01:27
25.09.2019	13:49:58	25.09.2019	18:30:35
25.09.2019	21:28:57	26.09.2019	01:04:54

'''
print(data[1].index[0])
print(data[1].index[-1])
data[1] = data[1]['2019-09-24 13:38:51': '2019-09-25 14:01:23']
transition_wmb =wmb['2019-09-24 13:38:51': '2019-09-25 14:01:23']
transition_lidar = lidar['2019-09-24 13:38:51': '2019-09-25 14:01:23']
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
result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine07.csv')

print(data[9].index[0])
print(data[9].index[-1])
data[9] = data[9]['2019-09-25 15:49:59': '2019-09-25 20:30:32']
transition_wmb =wmb['2019-09-25 15:49:59': '2019-09-25 20:30:32']
transition_lidar = lidar['2019-09-25 15:49:59': '2019-09-25 20:30:32']
result = pd.concat([data[9], transition_lidar, transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb1_turbine07.csv')

print(data[12].index[0])
print(data[12].index[-1])
data[12] = data[12]['2019-09-25 23:28:57': '2019-09-26 03:04:49']
transition_wmb =wmb['2019-09-25 23:28:57': '2019-09-26 03:04:49']
transition_lidar = lidar['2019-09-25 23:28:57': '2019-09-26 03:04:49']
result = pd.concat([data[12], transition_lidar, transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb2_turbine07.csv')