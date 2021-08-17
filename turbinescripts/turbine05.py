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