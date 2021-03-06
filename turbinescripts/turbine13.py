import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
'''
turbine-13_helihoist-1_tom_geometry_hammerhead_2019-11-09-12-22-51_2019-11-10-12-59-19
turbine-13_sbitroot_tom_acc-vel-pos_hammerhead_2019-11-09-12-12-04_2019-11-09-15-25-59
turbine-13_sbittip_tom_acc-vel-pos_hammerhead_2019-11-09-12-13-17_2019-11-10-13-04-29

turbine-13_helihoist-1_tom_acc-vel-pos_sbi1_2019-11-10-12-59-20_2019-11-10-13-33-08

turbine-13_helihoist-1_tom_acc-vel-pos_tnhb1_2019-11-10-13-33-08_2019-11-16-05-29-59
turbine-13_helihoist-1_tom_geometry_tnhb1_2019-11-10-13-33-08_2019-11-16-05-29-59
turbine-13_sbitroot_tom_acc-vel-pos_tnhb1_2019-11-15-17-14-58_2019-11-16-05-36-40
turbine-13_sbittip_tom_acc-vel-pos_tnhb1_2019-11-10-13-31-42_2019-11-15-22-27-35

wmb-sued-2019-11-09
wmb-sued-2019-11-10
wmb-sued-2019-11-11
wmb-sued-2019-11-12
wmb-sued-2019-11-13
wmb-sued-2019-11-14
wmb-sued-2019-11-15
wmb-sued-2019-11-16

lidar_2019_11_09
lidar_2019_11_10
lidar_2019_11_11
lidar_2019_11_12
lidar_2019_11_13
lidar_2019_11_14
lidar_2019_11_15

lidar_2019_11_16 is missing



'''



#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-13**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-13**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-13**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-13**.csv'))


data = []
helihoist_tele_hammerhead = pd.read_csv(hammerhead[0], delimiter = ',')
helihoist_geo_hammerhead = pd.read_csv(hammerhead[1], delimiter = ',')
sbitroot_hammerhead = pd.read_csv(hammerhead[2], delimiter = ',')
sbitip_hammerhead = pd.read_csv(hammerhead[3], delimiter = ',')
data.append(helihoist_tele_hammerhead) , data.append(helihoist_geo_hammerhead), data.append(sbitroot_hammerhead)  ,data.append(sbitip_hammerhead)

helihoist_sbi1 = pd.read_csv(sbi1[0], delimiter = ',')

data.append(helihoist_sbi1)

helihoist_tnhb1 = pd.read_csv(tnhb1[0], delimiter = ',')
helihoist_geo_tnhb1 = pd.read_csv(tnhb1[1], delimiter = ',')
sbiroot_tnhb1 = pd.read_csv(tnhb1[2], delimiter = ',')
sbitip_tnhb1 = pd.read_csv(tnhb1[3], delimiter = ',')

data.append(helihoist_tnhb1) ,data.append(helihoist_geo_tnhb1) ,data.append(sbiroot_tnhb1),data.append(sbitip_tnhb1)

wmb1= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-09.csv', delimiter = ' ')
wmb2= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-10.csv', delimiter = ' ')
wmb3= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-11.csv', delimiter = ' ')
wmb4= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-12.csv', delimiter = ' ')
wmb5= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-13.csv', delimiter = ' ')
wmb6= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-14.csv', delimiter = ' ')
wmb7= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-15.csv', delimiter = ' ')
wmb8= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-11-16.csv', delimiter = ' ')
#besonders auf 11/12 und 15 achten **TODO** entfernen

data.append(wmb1), data.append(wmb2), data.append(wmb3), data.append(wmb4), data.append(wmb5), data.append(wmb6), data.append(wmb7), data.append(wmb8)
wmb_all = []
wmb_all.append(wmb1), wmb_all.append(wmb2), wmb_all.append(wmb3), wmb_all.append(wmb4)

lidar1= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-09.csv', delimiter = ' ')
lidar2= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-10.csv', delimiter = ' ')
lidar3= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-11.csv', delimiter = ' ')
lidar4= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-12.csv', delimiter = ' ')
lidar5= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-13.csv', delimiter = ' ')
lidar6= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-14.csv', delimiter = ' ')
lidar7= pd.read_csv('environment/environment/wind/lidar/lidar_2019-11-15.csv', delimiter = ' ')

lidar_all =[]
lidar_all.append(lidar1), lidar_all.append(lidar2), lidar_all.append(lidar3), lidar_all.append(lidar4), lidar_all.append(lidar5), lidar_all.append(lidar6), lidar_all.append(lidar7),
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
#12:22:51   15:25:59
for i in range(4):
    data[i] = data[i]['2019-11-09 12:22:51': '2019-11-09 15:25:59']
transition_wmb =wmb['2019-11-09 12:22:51': '2019-11-09 15:25:59']
transition_lidar = lidar['2019-11-09 12:22:51': '2019-11-09 15:25:59']
result =pd.concat([data[0],data[1],data[2],data[3], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine13/hammerhead_turbine13.csv')

#generating sbi1 file
#12:59:20   13:33:08
for i in range(4,5):
    data[i] = data[i]['2019-11-10 12:59:20': '2019-11-10 13:33:08']
transition_wmb =wmb['2019-11-10 12:59:20': '2019-11-10 13:33:08']
transition_lidar = lidar['2019-11-10 12:59:20': '2019-11-10 13:33:08']
result =pd.concat([data[4], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine13/sbi1_turbine13.csv')


#generating sbi2 file
#05:36:40   06:31:29
for i in range(5,7):
    data[i] = data[i]['2019-11-16 05:36:40': '2019-11-16 06:31:29']
transition_wmb =wmb['2019-11-16 05:36:40': '2019-11-16 06:31:29']
transition_lidar = lidar['2019-11-16 05:36:40': '2019-11-16 06:31:29']
result =pd.concat([data[5],data[6], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine13/sbi2_turbine13.csv')


#generating tnhb1 file
#17:14:58   22:27:35
for i in range(7,11):
    data[i] = data[i]['2019-11-15 17:14:58': '2019-11-15 22:27:35']
transition_wmb =wmb['2019-11-15 17:14:58': '2019-11-15 22:27:35']
transition_lidar = lidar['2019-11-15 17:14:58': '2019-11-15 22:27:35']
result =pd.concat([data[7],data[8],data[9],data[10], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine13/tnhb1_turbine13.csv')
'''

'''
files to extract:
09.11.2019	12:22:51	10.11.2019	12:59:19
10.11.2019	13:33:08	16.11.2019	05:29:59
'''
print(data[1].index[0])
print(data[1].index[-1])
data[1] = data[1]['2019-11-09 13:22:52': '2019-11-10 13:59:14']
transition_wmb =wmb['2019-11-09 13:22:52': '2019-11-10 13:59:14']
transition_lidar = lidar['2019-11-09 13:22:52': '2019-11-10 13:59:14']
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
result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine13.csv')
print(data[6].index[0])
print(data[6].index[-1])
data[6] = data[6]['2019-11-10 14:33:09': '2019-11-16 06:29:54']
transition_wmb =wmb['2019-11-10 14:33:09': '2019-11-16 06:29:54']
transition_lidar = lidar['2019-11-10 14:33:09': '2019-11-16 06:29:54']
result = pd.concat([data[6], transition_lidar, transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb1_turbine13.csv')