import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
'''
turbine-10_helihoist-1_tom_acc-vel-pos_hammerhead_2019-10-23-11-32-59_2019-10-23-19-42-22
turbine-10_helihoist-1_tom_geometry_hammerhead_2019-10-23-11-32-59_2019-10-23-19-42-22
turbine-10_sbitroot_tom_acc-vel-pos_hammerhead_2019-10-23-11-48-51_2019-10-23-19-45-30
turbine-10_sbittip_tom_acc-vel-pos_hammerhead_2019-10-23-11-40-32_2019-10-23-19-55-12

turbine-10_helihoist-1_tom_acc-vel-pos_sbi1_2019-10-23-19-42-31_2019-10-23-20-29-21
turbine-10_sbitroot_tom_acc-vel-pos_sbi1_2019-10-23-19-45-31_2019-10-23-22-00-39
turbine-10_sbittip_tom_acc-vel-pos_sbi1_2019-10-23-19-55-12_2019-10-23-22-05-43


wmb-sued-2019-10-23

lidar_2019_10_23

mehr haben wir hier auch nicht



'''

#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-10**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-10**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-10**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-10**.csv'))
tnhb2 = sorted(glob('Daten/tnhb2/tnhb2/turbine-10**.csv'))

data = []
helihoist_tele_hammerhead = pd.read_csv(hammerhead[0], delimiter = ',')
helihoist_geo_hammerhead = pd.read_csv(hammerhead[1], delimiter = ',')
sbitroot_hammerhead = pd.read_csv(hammerhead[2], delimiter = ',')
sbitip_hammerhead = pd.read_csv(hammerhead[3], delimiter = ',')
data.append(helihoist_tele_hammerhead) , data.append(helihoist_geo_hammerhead), data.append(sbitroot_hammerhead)  ,data.append(sbitip_hammerhead)
helihoist_sbi1 = pd.read_csv(sbi1[0], delimiter= ',')
sbiroot_sbi1 = pd.read_csv(sbi1[1], delimiter = ',')
sbitip_sbi1 = pd.read_csv(sbi1[2], delimiter = ',')

data.append(helihoist_sbi1) ,data.append(sbiroot_sbi1)

wmb= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-10-23.csv', delimiter = ' ')
lidar=pd.read_csv('environment/environment/wind/lidar/lidar_2019-10-23.csv', delimiter = ' ')
data.append(wmb), data.append(lidar)

wmb.columns = ('epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss', 'TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav', 'Eps', '#Waves')
lidar.columns = ( 'epoch', 'wind_speed_0', 'wind_dir_0', 'wind_dir_0_corr', 'height_0', 'wind_speed_1', 'wind_dir_1', 'wind_dir_1_corr', 'height_1', 'wind_speed_2', 'wind_dir_2', 'wind_dir_2_corr', 'height_2', 'wind_speed_3', 'wind_dir_3', 'wind_dir_3_corr', 'height_3', 'wind_speed_4', 'wind_dir_4', 'wind_dir_4_corr', 'height_4', 'wind_speed_5', 'wind_dir_5', 'wind_dir_5_corr', 'height_5', 'wind_speed_6', 'wind_dir_6', 'wind_dir_6_corr', 'height_6', 'wind_speed_7', 'wind_dir_7', 'wind_dir_7_corr', 'height_7', 'wind_speed_8', 'wind_dir_8', 'wind_dir_8_corr', 'height_8', 'wind_speed_9', 'wind_dir_9', 'wind_dir_9_corr', 'height_9', 'wind_speed_10', 'wind_dir_10', 'wind_dir_10_corr', 'height_10', 'heading')
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
print(lidar)
lidar = lidar.resample('3S', label='left').mean().pad()
lidar = lidar
print(lidar)

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
'''
# generating hammerhead file
#11:48:51   19:42:22


for i in range(4):
    data[i] = data[i]['2019-10-23 11:48:51': '2019-10-23 19:42:22']
transition_wmb =wmb['2019-10-23 11:48:51': '2019-10-23 19:42:22']


result =pd.concat([data[0],data[1],data[2],data[3], transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine10/hammerhead_turbine10.csv')

#generating sbi1 file
#19:55:12   20:29:21
for i in range(4,7):
    data[i] = data[i]['2019-10-23 19:55:12': '2019-10-23 20:29:21']
transition_wmb =wmb['2019-10-23 19:55:12': '2019-10-23 20:29:21']
result =pd.concat([data[4],data[5],data[6], transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine10/sbi1_turbine10.csv')
'''

'''
files to extract
23.10.2019	11:32:59	23.10.2019	19:42:22
'''
print(lidar.columns)
print(wmb.columns)
data[1] = data[1]['2019-10-23 13:33:00': '2019-10-23 21:42:15']
transition_wmb =wmb['2019-10-23 13:33:00': '2019-10-23 21:42:15']
transition_lidar = lidar['2019-10-23 13:33:00': '2019-10-23 21:42:15']
result = pd.concat([data[1],transition_lidar, transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine10.csv')