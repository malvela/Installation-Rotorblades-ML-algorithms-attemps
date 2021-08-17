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