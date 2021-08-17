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
    df = df.resample('3S', label = 'left').mean().pad()
    data[counter] = df
    counter = counter+1

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
#generating csv files
'''
# generating hammerhead file
#04:48:53	07:12:46

for i in range(0,4):
    data[i] = data[i]['2019-09-07 04:48:53': '2019-09-07 07:12:46']
transition_wmb =wmb['2019-09-07 04:48:53': '2019-09-07 07:12:46']
transition_lidar = lidar['2019-09-07 04:48:53': '2019-09-07 07:12:46']
result =pd.concat([data[0],data[1],data[2],data[3], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine04/hammerhead_turbine04.csv')

#generating sbi1 file
#07: 19:27  12: 34:23

for i in range(4,7):
    data[i] = data[i]['2019-09-07 07:25:10': '2019-09-07 12:34:23']
transition_wmb =wmb['2019-09-07 07:25:10': '2019-09-07 12:34:23']
transition_lidar = lidar['2019-09-07 07:25:10': '2019-09-07 12:34:23']
result = pd.concat([data[4], data[5], data[6], transition_lidar, transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine04/sbi1_turbine4.csv')


#generating tnhb1 file
#12:34:23	04:43:15

for i in range(7,11):
    data[i] = data[i]['2019-09-07 12:40:14': '2019-09-07 21:49:58']
transition_wmb =wmb['2019-09-07 12:40:14': '2019-09-07 21:49:58']
transition_lidar = lidar['2019-09-07 12:40:14': '2019-09-07 21:49:58']
result = pd.concat([data[10], data[11], data[12], data[13], transition_lidar, transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine04/tnhb1_turbine4.csv')
'''

'''
files to extract:
01.09.2019	10:20:45	07.09.2019	07:19:26 /data[1]
07.09.2019	12:40:14	07.09.2019	21:49:58 /data[8]
'''
print(data[1].index[0])
print(data[1].index[-1])
data[1] = data[1]['2019-09-01 12:20:45': '2019-09-07 09:19:26']
transition_wmb =wmb['2019-09-01 12:20:45': '2019-09-07 09:19:26']
transition_lidar = lidar['2019-09-01 12:20:45': '2019-09-07 09:19:26']
print(transition_lidar)
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
del result['wind_speed_3']
del result['wind_dir_3']
del result['wind_dir_3_corr']
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
result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine04.csv')
print(data[8].index[0])
print(data[8].index[-1])
data[8] = data[8]['2019-09-07 14:40:14': '2019-09-07 23:49:58']
transition_wmb =wmb['2019-09-07 14:40:14': '2019-09-07 23:49:58']
transition_lidar = lidar['2019-09-07 14:40:14': '2019-09-07 23:49:58']
print(transition_lidar)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb1_turbine04.csv')

#turbine05
import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt

'''
turbine-05_helihoist-1_tom_acc-vel-pos_hammerhead_2019-09-10-16-04-47_2019-09-20-02-53-43
turbine-05_helihoist-1_tom_geometry_hammerhead_2019-09-10-16-04-47_2019-09-20-02-53-43

turbine-05_helihoist-1_tom_acc-vel-pos_sbi1_2019-09-20-02-53-43_2019-09-20-07-42-54
turbine-05_sbitroot_tom_acc-vel-pos_sbi1_2019-09-20-02-34-11_2019-09-20-07-33-33
turbine-05_sbittip_tom_acc-vel-pos_sbi1_2019-09-20-02-47-05_2019-09-20-07-43-54

turbine-05_sbittip_tom_acc-vel-pos_sbi2_2019-09-20-12-07-46_2019-09-20-13-00-55
turbine-05_sbitroot_tom_acc-vel-pos_sbi2_2019-09-20-12-03-56_2019-09-20-12-58-11
turbine-05_helihoist-1_tom_acc-vel-pos_sbi2_2019-09-20-12-01-12_2019-09-20-12-51-37

turbine-05_sbittip_tom_acc-vel-pos_tnhb1_2019-09-20-07-43-54_2019-09-20-12-07-46
turbine-05_sbitroot_tom_acc-vel-pos_tnhb1_2019-09-20-07-33-33_2019-09-20-12-03-56
turbine-05_helihoist-1_tom_geometry_tnhb1_2019-09-20-07-42-54_2019-09-20-12-01-11
turbine-05_helihoist-1_tom_acc-vel-pos_tnhb1_2019-09-20-07-42-54_2019-09-20-12-01-11

turbine-05_helihoist-1_tom_acc-vel-pos_tnhb2_2019-09-20-12-51-37_2019-09-20-16-14-47
turbine-05_helihoist-1_tom_geometry_tnhb2_2019-09-20-12-51-37_2019-09-20-16-14-47
turbine-05_sbitroot_tom_acc-vel-pos_tnhb2_2019-09-20-12-58-11_2019-09-20-16-36-36
turbine-05_sbittip_tom_acc-vel-pos_tnhb2_2019-09-20-13-00-55_2019-09-20-16-11-16

wmb-sued-2019-9-10
wmb-sued-2019-9-11
wmb-sued-2019-9-12
wmb-sued-2019-9-13
wmb-sued-2019-9-14
wmb-sued-2019-9-15
wmb-sued-2019-9-16
wmb-sued-2019-9-17
wmb-sued-2019-9-18
wmb-sued-2019-9-19
wmb-sued-2019-9-20

keine winddaten



'''
#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-05**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-05**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-05*.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-05**.csv'))
tnhb2 = sorted(glob('Daten/tnhb2/tnhb2/turbine-05**.csv'))


data = []
helihoist_tele_hammerhead = pd.read_csv(hammerhead[0], delimiter = ',')
helihoist_geo_hammerhead = pd.read_csv(hammerhead[1], delimiter = ',')

data.append(helihoist_tele_hammerhead) , data.append(helihoist_geo_hammerhead)

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

wmb1= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-10.csv', delimiter = ' ')
wmb2= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-11.csv', delimiter = ' ')
wmb3= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-12.csv', delimiter = ' ')
wmb4= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-13.csv', delimiter = ' ')
wmb5= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-14.csv', delimiter = ' ')
wmb6= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-15.csv', delimiter = ' ')
wmb7= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-16.csv', delimiter = ' ')
wmb8= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-17.csv', delimiter = ' ')
wmb9= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-18.csv', delimiter = ' ')
wmb10= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-19.csv', delimiter = ' ')
wmb11= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-09-20.csv', delimiter = ' ')

wmb_all = []
wmb_all.append(wmb1), wmb_all.append(wmb2), wmb_all.append(wmb3), wmb_all.append(wmb4),wmb_all.append(wmb5), wmb_all.append(wmb6), wmb_all.append(wmb7), wmb_all.append(wmb8),wmb_all.append(wmb9), wmb_all.append(wmb10), wmb_all.append(wmb11)

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

UTC = []
for k in range(len(wmb)):
    UTC.append(pd.Timestamp.fromtimestamp(wmb.iloc[k, 0]))
wmb['epoch'] = UTC
wmb.index = wmb['epoch']
del wmb['epoch']
wmb = wmb.resample('3S', label='left').mean().pad() / 1800
wmb = wmb




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
'''
'''
# generating hammerhead file
#17:29:33       02:34:11
for i in range(0,4):
    data[i] = data[i]['2019-09-20 17:29:33': '2019-09-20 02:34:11']
transition_wmb =wmb['2019-09-20 17:29:33': '2019-09-20 02:34:11']

result =pd.concat([data[0],data[1],data[2],data[3], transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine05/hammerhead_turbine05.csv')

#generating sbi1 file
#02:53:43  07:33:33

for i in range(4,7):
    data[i] = data[i]['2019-09-20 02:53:43': '2019-09-20 07:33:33']
transition_wmb =wmb['2019-09-20 02:53:43': '2019-09-20 07:33:33']

result = pd.concat([data[4], data[5], data[6],  transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine05/sbi1_turbine5.csv')


#generating sbi2 file
#12:07:46	12:51:37
for i in range(7,10):
    data[i] = data[i]['2019-09-20 12:07:46': '2019-09-20 12:51:37']
transition_wmb =wmb['2019-09-20 12:07:46': '2019-09-20 12:51:37']

result = pd.concat([data[7], data[8], data[9], transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine05/sbi2_turbine5.csv')


#generating tnhb1 file
#07:43:54	12:01:11

for i in range(10,14):
    data[i] = data[i]['2019-09-20 07:43:54': '2019-09-20 12:01:11']
transition_wmb =wmb['2019-09-20 07:43:54': '2019-09-20 12:01:11']

result = pd.concat([data[10], data[11], data[12], data[13], transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine05/tnhb1_turbine5.csv')

#generating tnhb2 file
#13:00:55    16:11:16

for i in range(14,16):
    data[i] = data[i]['2019-09-20 13:00:55': '2019-09-20 16:11:16']
transition_wmb = wmb['2019-09-20 13:00:55': '2019-09-20 16:11:16']

result = pd.concat([data[14], data[15], data[16], data[17], transition_wmb], axis=1)
result.to_csv('Results_preprocessing/turbine05/tnhb2_turbine5.csv')
'''


'''
files to extract
10.09.2019	16:04:47	20.09.2019	02:53:43
20.09.2019	07:42:54	20.09.2019	12:01:11
20.09.2019	12:51:37	20.09.2019	16:14:47

'''
print(data[1].index[0])
print(data[1].index[-1])
data[1] = data[1]['2019-09-10 18:04:48': '2019-09-20 04:53:39']
transition_wmb =wmb['2019-09-10 18:04:48': '2019-09-20 04:53:39']
result = pd.concat([data[1], transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine05.csv')
print(data[9].index[0])
print(data[9].index[-1])
data[9] = data[9]['2019-09-20 09:42:54': '2019-09-20 14:01:07']
transition_wmb =wmb['2019-09-20 09:42:54': '2019-09-20 14:01:07']
result = pd.concat([data[9], transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb1_turbine05.csv')
print(data[13].index[0])
print(data[13].index[-1])
data[13] = data[13]['2019-09-20 14:51:37': '2019-09-20 18:14:40']
transition_wmb =wmb['2019-09-20 14:51:37': '2019-09-20 18:14:40']
result = pd.concat([data[13], transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb2_turbine05.csv')

#turbine06
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
wmb = wmb.resample('3S', label = 'left').mean().pad() / 1800

#same with lidar data
UTC = []
for k in range(len(lidar)):
    UTC.append(pd.Timestamp.fromtimestamp(lidar.iloc[k, 0]))
lidar['epoch'] = UTC
lidar.index = lidar['epoch']
del lidar['epoch']
lidar = lidar.resample('3S', label='left').mean().pad()
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
    df = df.resample('3S', label = 'left').mean().pad()
    data[counter] = df
    counter = counter+1

'''
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

'''
#generating correlation matrix
sbi1_turbine6 = pd.read_csv('Results_preprocessing/turbine06/sbi1_turbine6.csv', delimiter = ',')
corrMatrix = sbi1_turbine6.corr() #coolwarm
sn.heatmap(corrMatrix, annot=False)
plt.show()

'''


'''
files to extract
22.09.2019	03:14:43	22.09.2019	12:05:47
22.09.2019	12:41:45	22.09.2019	22:11:22
23.09.2019	00:30:45	23.09.2019	00:42:54
'''
print(data[1].index[0])
print(data[1].index[-1])
data[1] = data[1]['2019-09-22 05:14:43': '2019-09-22 14:05:42']
transition_wmb =wmb['2019-09-22 05:14:43': '2019-09-22 14:05:42']
transition_lidar = lidar['2019-09-22 05:14:43': '2019-09-22 14:05:42']
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
del result['wind_speed_3']
del result['wind_dir_3']
del result['wind_dir_3_corr']
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
result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine06.csv')
print(data[11].index[0])
print(data[11].index[-1])
data[11] = data[11]['2019-09-22 14:41:45': '2019-09-22 23:30:03']
transition_wmb =wmb['2019-09-22 14:41:45': '2019-09-22 23:30:03']
transition_lidar = lidar['2019-09-22 14:41:45': '2019-09-22 23:30:03']
result = pd.concat([data[11], transition_lidar, transition_wmb], axis=1)
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
del result['wind_speed_3']
del result['wind_dir_3']
del result['wind_dir_3_corr']
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
result.to_csv('Results_preprocessing/geometry_files/tnhb1_turbine06.csv')
print(data[15].index[0])
print(data[15].index[-1])
data[15] = data[15]['2019-09-23 02:30:46': '2019-09-23 00:42:47']
transition_wmb =wmb['2019-09-23 02:30:46': '2019-09-23 00:42:47']
transition_lidar = lidar['2019-09-23 02:30:46': '2019-09-23 00:42:47']
result = pd.concat([data[15], transition_lidar, transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb2_turbine06.csv')

#turbine07
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

#turbine08
import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt

'''
turbine-08_helihoist-1_tom_acc-vel-pos_hammerhead_2019-10-14-07-55-52_2019-10-15-06-10-33
turbine-08_helihoist-1_tom_geometry_hammerhead_2019-10-14-07-55-52_2019-10-15-06-10-33
turbine-08_sbitroot_tom_acc-vel-pos_hammerhead_2019-10-14-10-49-53_2019-10-15-06-18-48
turbine-08_sbittip_tom_acc-vel-pos_hammerhead_2019-10-14-10-45-39_2019-10-15-06-08-27

turbine-08_helihoist-1_tom_acc-vel-pos_sbi1_2019-10-15-06-10-33_2019-10-15-07-30-26
turbine-08_sbitroot_tom_acc-vel-pos_sbi1_2019-10-15-06-18-48_2019-10-15-07-40-56
turbine-08_sbittip_tom_acc-vel-pos_sbi1_2019-10-15-06-08-27_2019-10-15-07-57-03

turbine-08_helihoist-1_tom_acc-vel-pos_sbi2_2019-10-15-14-21-36_2019-10-15-15-13-04
turbine-08_sbitroot_tom_acc-vel-pos_sbi2_2019-10-15-14-10-47_2019-10-15-15-05-07
turbine-08_sbittip_tom_acc-vel-pos_sbi2_2019-10-15-14-17-49_2019-10-15-15-09-25

turbine-08_helihoist-1_tom_acc-vel-pos_tnhb1_2019-10-15-07-30-26_2019-10-15-14-21-36
turbine-08_helihoist-1_tom_geometry_tnhb1_2019-10-15-07-30-26_2019-10-15-14-21-36
turbine-08_sbitroot_tom_acc-vel-pos_tnhb1_2019-10-15-07-40-56_2019-10-15-14-10-47
turbine-08_sbittip_tom_acc-vel-pos_tnhb1_2019-10-15-07-57-03_2019-10-15-14-17-49

turbine-08_helihoist-1_tom_acc-vel-pos_tnhb2_2019-10-15-15-13-04_2019-10-15-22-19-59

wmb-sued-2019-10-14
wmb-sued-2019-10-15

lidar_2019_10_14
lidar_2019_10_15

komplett
'''


#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-08**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-08**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-08**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-08**.csv'))
tnhb2 = sorted(glob('Daten/tnhb2/tnhb2/turbine-08**.csv'))
#wmb =  "wmb-sued-2019-9-22"
#lidar =  "lidar_2019_09_22"
data = []
helihoist_tele_hammerhead = pd.read_csv(hammerhead[0], delimiter = ',')
helihoist_geo_hammerhead = pd.read_csv(hammerhead[1], delimiter = ',')
sbitroot_hammerhead = pd.read_csv(hammerhead[2], delimiter = ',')
sbitip_hammerhead = pd.read_csv(hammerhead[3], delimiter = ',')
data.append(helihoist_tele_hammerhead) , data.append(helihoist_geo_hammerhead), data.append(sbitroot_hammerhead)  ,data.append(sbitip_hammerhead)

helihoist_sbi1 = pd.read_csv(sbi1[0], delimiter= ',')
sbiroot_sbi1 = pd.read_csv(sbi1[1], delimiter = ',')
sbitip_sbi1 = pd.read_csv(sbi1[2], delimiter = ',')

data.append(helihoist_sbi1) ,data.append(sbiroot_sbi1), data.append(sbitip_sbi1)

helihoist_sbi2 = pd.read_csv(sbi2[0], delimiter = ',')
sbiroot_sbi2 = pd.read_csv(sbi2[1], delimiter = ',')
sbitip_sbi2 = pd.read_csv(sbi2[2], delimiter = ',')

data.append(helihoist_sbi2) ,data.append(sbiroot_sbi2), data.append(sbitip_sbi2)

helihoist_tnhb1 = pd.read_csv(tnhb1[0], delimiter = ',')
helihoist_geo_tnhb1 = pd.read_csv(tnhb1[1], delimiter = ',')
sbiroot_tnhb1 = pd.read_csv(tnhb1[2], delimiter = ',')
sbitip_tnhb1 = pd.read_csv(tnhb1[3], delimiter = ',')
data.append(helihoist_tnhb1) ,data.append(helihoist_geo_tnhb1) ,data.append(sbiroot_tnhb1), data.append(sbitip_tnhb1)

helihoist_tnhb2 = pd.read_csv(tnhb2[0], delimiter = ',')


data.append(helihoist_tnhb2)

wmb1= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-10-14.csv', delimiter = ' ')
wmb2= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-10-15.csv', delimiter = ' ')

wmb_all = []
wmb_all.append(wmb1), wmb_all.append(wmb2)

lidar1 =pd.read_csv('environment/environment/wind/lidar/lidar_2019-10-14.csv', delimiter = ' ')
lidar2 =pd.read_csv('environment/environment/wind/lidar/lidar_2019-10-15.csv', delimiter = ' ')

data.append(lidar1), data.append(lidar2)
lidar_all = []
lidar_all.append(lidar1), lidar_all.append(lidar2)


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
#10:49:53   06:08:27
for i in range(4):
    data[i] = data[i]['2019-10-14 10:49:53': '2019-10-15 06:08:27']
transition_wmb =wmb['2019-10-14 10:49:53': '2019-10-15 06:08:27']
transition_lidar = lidar['2019-10-14 10:49:53': '2019-10-15 06:08:27']
result =pd.concat([data[0],data[1],data[2],data[3], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine08/hammerhead_turbine08.csv')

#generating sbi1 file
#06:18:48   07:30:26
for i in range(4,7):
    data[i] = data[i]['2019-10-15 06:18:48': '2019-10-15 07:30:26']
transition_wmb =wmb['2019-10-15 06:18:48': '2019-10-15 07:30:26']
transition_lidar = lidar['2019-10-15 06:18:48': '2019-10-15 07:30:26']
result =pd.concat([data[4],data[5],data[6], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine08/sbi1_turbine08.csv')

#generating sbi2 file
#14:21:36   15:05:07
for i in range(7,10):
    data[i] = data[i]['2019-10-15 14:21:36': '2019-10-15 15:05:07']
transition_wmb =wmb['2019-10-15 14:21:36': '2019-10-15 15:05:07']
transition_lidar = lidar['2019-10-15 14:21:36': '2019-10-15 15:05:07']
result =pd.concat([data[7],data[8],data[9], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine08/sbi2_turbine08.csv')

#generating tnhb1 file
#07:57:03   14:10:47
for i in range(10,14):
    data[i] = data[i]['2019-10-15 07:57:03': '2019-10-15 14:10:47']
transition_wmb =wmb['2019-10-15 07:57:03': '2019-10-15 14:10:47']
transition_lidar = lidar['2019-10-15 07:57:03': '2019-10-15 14:10:47']
result =pd.concat([data[10],data[11],data[12],data[13], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine08/tnhb1_turbine08.csv')

#generating tnhb2 file
#15:13:04   22:19:59
for i in range(14,15):
    data[i] = data[i]['2019-10-15 15:13:04': '2019-10-15 22:19:59']
transition_wmb =wmb['2019-10-15 15:13:04': '2019-10-15 22:19:59']
transition_lidar = lidar['2019-10-15 15:13:04': '2019-10-15 22:19:59']
result =pd.concat([data[14], transition_lidar, transition_wmb], axis=1 )
result.to_csv('Results_preprocessing/turbine08/tnhb2_turbine08.csv')
'''


'''
files to extract
14.10.2019	07:55:52	15.10.2019	06:10:33
15.10.2019	07:30:26	15.10.2019	14:21:36
'''
print(data[1].index[0])
print(data[1].index[-1])
data[1] = data[1]['2019-10-14 09:55:53': '2019-10-15 08:10:27']
transition_wmb =wmb['2019-10-14 09:55:53': '2019-10-15 08:10:27']
transition_lidar = lidar['2019-10-14 09:55:53': '2019-10-15 08:10:27']
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
result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine08.csv')
print(data[11].index[0])
print(data[11].index[-1])
data[11] = data[11]['2019-10-15 09:30:27': '2019-10-15 16:21:31']
transition_wmb =wmb['2019-10-15 09:30:27': '2019-10-15 16:21:31']
transition_lidar = lidar['2019-10-15 09:30:27': '2019-10-15 16:21:31']
result = pd.concat([data[11], transition_lidar, transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb1_turbine08.csv')

#turbine09
import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt


'''
turbine-09_helihoist-1_tom_acc-vel-pos_hammerhead_2019-10-04-12-59-44_2019-10-08-01-41-05
turbine-09_helihoist-1_tom_geometry_hammerhead_2019-10-04-12-59-44_2019-10-08-01-41-05
turbine-09_sbitroot_tom_acc-vel-pos_hammerhead_2019-10-17-00-43-06_2019-10-17-06-47-39
turbine-09_sbittip_tom_acc-vel-pos_hammerhead_2019-10-17-00-50-54_2019-10-17-06-49-19

wmb-sued-2019-10-04
wmb-sued-2019-10-05
wmb-sued-2019-10-06
wmb-sued-2019-10-07
wmb-sued-2019-10-08

lidar fehlt



sonst keine weiteren daten vorhanden
'''



#loading data and filling it into an array of all dataframes
hammerhead = sorted(glob('Daten/hammerhead/hammerhead/turbine-09**.csv'))
sbi1 = sorted(glob('Daten/sbi1/sbi1/turbine-09**.csv'))
sbi2 = sorted(glob('Daten/sbi2/sbi2/turbine-09**.csv'))
tnhb1 = sorted(glob('Daten/tnhb1/tnhb1/turbine-09**.csv'))
tnhb2 = sorted(glob('Daten/tnhb2/tnhb2/turbine-09**.csv'))
#wmb =  "wmb-sued-2019-9-22"
#lidar =  "lidar_2019_09_22"
data = []
helihoist_tele_hammerhead = pd.read_csv(hammerhead[0], delimiter = ',')
helihoist_geo_hammerhead = pd.read_csv(hammerhead[1], delimiter = ',')
sbitroot_hammerhead = pd.read_csv(hammerhead[2], delimiter = ',')
sbitip_hammerhead = pd.read_csv(hammerhead[3], delimiter = ',')
data.append(helihoist_tele_hammerhead) , data.append(helihoist_geo_hammerhead), data.append(sbitroot_hammerhead)  ,data.append(sbitip_hammerhead)

wmb1= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-10-04.csv', delimiter = ' ')
wmb2= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-10-05.csv', delimiter = ' ')
wmb3= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-10-06.csv', delimiter = ' ')
wmb4= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-10-07.csv', delimiter = ' ')
wmb5= pd.read_csv('environment/environment/waves/wmb-sued/wmb-sued_2019-10-08.csv', delimiter = ' ')

data.append(wmb1), data.append(wmb2), data.append(wmb3), data.append(wmb4) , data.append(wmb5)
wmb_all = []
wmb_all.append(wmb1), wmb_all.append(wmb2), wmb_all.append(wmb3), wmb_all.append(wmb4) , wmb_all.append(wmb5)

buffer = []

for i in wmb_all:
    i.columns = (
    'epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss',
    'TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav', 'Eps',
    '#Waves')
    buffer.append(i)
    wmb = pd.concat(buffer, axis=0)
    wmb.columns = (
    'epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss',
    'TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav', 'Eps',
    '#Waves')
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
UTC = []
for k in range(len(wmb)):
    UTC.append(pd.Timestamp.fromtimestamp(wmb.iloc[k, 0]))
wmb['epoch'] = UTC
wmb.index = wmb['epoch']
del wmb['epoch']
wmb = wmb.resample('3S', label='left').mean().pad() / 1800
wmb = wmb

#plotting
'''

fig = plt.figure(figsize=(14,6), dpi=80)
plt.plot(wmb.index, wmb['#Waves'])
plt.title('#Waves')
plt.ylabel('number of waves')

plt.xlabel('time')
plt.xticks(rotation= 90)
plt.show()
'''
'''
files to extract
04.10.2019	12:59:44	08.10.2019	01:41:05
'''
print(data[1].index[0])
print(data[1].index[-1])
data[1] = data[1]['2019-10-4 14:59:45': '2019-10-8 03:41:00']
transition_wmb =wmb['2019-10-4 14:59:45': '2019-10-8 03:41:00']
result = pd.concat([data[1], transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine09.csv')

#turbine10
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
result = pd.concat([data[1],transition_wmb], axis=1)
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

#turbine11

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
'''
'''
files to extract
31.10.2019	04:18:02	31.10.2019	10:41:13
31.10.2019	12:54:16	31.10.2019	15:30:44
'''
print(data[1].index[0])
print(data[1].index[-1])
data[1] = data[1]['2019-10-31 05:18:03': '2019-10-31 11:41:08']
transition_lidar = lidar['2019-10-31 05:18:03': '2019-10-31 11:41:08']
result = pd.concat([data[1], transition_lidar], axis=1)
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

result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine11.csv')
print(data[11].index[0])
print(data[11].index[-1])
data[11] = data[11]['2019-10-31 13:54:18': '2019-10-31 16:30:41']
transition_lidar = lidar['2019-10-31 13:54:18': '2019-10-31 16:30:41']
result = pd.concat([data[11], transition_lidar], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb1_turbine11.csv')

#turbine12
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

#turbine13
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

#turbine14
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
'''

'''
files to extract:
24.11.2019	16:42:08	24.11.2019	21:16:51
25.11.2019	04:59:18	25.11.2019	08:27:01
'''

print(data[1].index[0])
print(data[1].index[-1])
data[1] = data[1]['2019-11-24 17:42:09': '2019-11-24 22:16:47']
transition_wmb =wmb['2019-11-24 17:42:09': '2019-11-24 22:16:47']
transition_lidar = lidar['2019-11-24 17:42:09': '2019-11-24 22:16:47']
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
result.to_csv('Results_preprocessing/geometry_files/hammerhead_turbine14.csv')
print(data[11].index[0])
print(data[11].index[-1])
data[11] = data[11]['2019-11-25 05:59:19': '2019-11-25 09:26:55']
transition_wmb =wmb['2019-11-25 05:59:19': '2019-11-25 09:26:55']
transition_lidar = lidar['2019-11-25 05:59:19': '2019-11-25 09:26:55']
result = pd.concat([data[11], transition_lidar, transition_wmb], axis=1)
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
result.to_csv('Results_preprocessing/geometry_files/tnhb1_turbine14.csv')

#turbine16

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
