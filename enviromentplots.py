import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import seaborn as sn


waves08 = sorted(glob('environment/environment/waves/wmb-sued/wmb-sued_2019-08-**.csv'))
waves09 = sorted(glob('environment/environment/waves/wmb-sued/wmb-sued_2019-09-**.csv'))
waves10 = sorted(glob('environment/environment/waves/wmb-sued/wmb-sued_2019-10-**.csv'))
waves11 = sorted(glob('environment/environment/waves/wmb-sued/wmb-sued_2019-11-**.csv'))
waves12 = sorted(glob('environment/environment/waves/wmb-sued/wmb-sued_2019-12-**.csv'))
waves_all = []
waves_all.append(waves08) , waves_all.append(waves09) , waves_all.append(waves10) , waves_all.append(waves11) , waves_all.append(waves12)
lidar08 = sorted(glob('environment/environment/wind/lidar/lidar_2019-08-**.csv'))
lidar09 = sorted(glob('environment/environment/wind/lidar/lidar_2019-09-**.csv'))
lidar10 = sorted(glob('environment/environment/wind/lidar/lidar_2019-10-**.csv'))
lidar11 = sorted(glob('environment/environment/wind/lidar/lidar_2019-11-**.csv'))
lidar12 = sorted(glob('environment/environment/wind/lidar/lidar_2019-12-**.csv'))
lidar_all = []
lidar_all.append(lidar08), lidar_all.append(lidar09), lidar_all.append(lidar10), lidar_all.append(lidar11), lidar_all.append(lidar12)
'''
for i in range(len(waves_all)):
    for j in range(len(waves_all[i])):
        data = pd.read_csv(waves_all[i][j], delim_whitespace=True)
        data.columns = (
        'epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss',
        'TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav',
        'Eps', '#Waves')
        UTC = []
        for k in range(len(data)):
            UTC.append(pd.Timestamp.fromtimestamp(data.iloc[k, 0]))
        data['epoch'] = UTC
        data.index = data['epoch']
        del data['epoch']
        plt.plot(data.index, data['#Waves'])
        plt.title(f"month{i+8}date{j}corr_wind")
        plt.xticks(rotation=-90)
        plt.savefig(f"environment/environment/waves/#Waves/month{i+8}date{j}wave.png")
        plt.show()
      
        data = pd.read_csv(waves_all[i][j], delim_whitespace=True)
        data.columns = ('epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss', 'TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav', 'Eps', '#Waves')
        data.index = data['epoch']
        del data['epoch']
        sn.heatmap(data.corr())
        plt.title(f"month{i+8}date{j}corr_wave")
        plt.savefig(f"environment/environment/waves/waves_corr/month{i+8}date{j}corr_waves.png")
        plt.show()
       

#Merging all data frames lidar
buffer = []
for i in range(len(waves_all)):
    for j in range(len(waves_all[i])):
        data = pd.read_csv(waves_all[i][j], delim_whitespace=True)
        data.columns = ('epoch', 'Tp', 'Dirp', 'Sprp', 'Tz', 'Hm0', 'TI', 'T1', 'Tc', 'Tdw2', 'Tdw1', 'Tpc', 'nu', 'eps', 'QP', 'Ss', 'TRef', 'TSea', 'Bat', 'Percentage', 'Hmax', 'Tmax', 'H(1/10)', 'T(1/10)', 'H(1/3)', 'T(1/3)', 'Hav', 'Tav', 'Eps', '#Waves')
        buffer.append(data)
waves_all_pd = pd.concat(buffer, axis=0)
UTC = []
for k in range(len(waves_all_pd)):
    UTC.append(pd.Timestamp.fromtimestamp(waves_all_pd.iloc[k, 0]))
waves_all_pd['epoch'] = UTC
waves_all_pd.index = waves_all_pd['epoch']
del waves_all_pd['epoch']
fig = plt.figure(figsize=(14,6), dpi=80)
plt.plot(waves_all_pd.index, waves_all_pd['#Waves'], c='lightblue', label = 'Number of Waves')
#plt.plot(waves_all_pd.index, waves_all_pd['TSea']/30, c= 'blue', label='Average Wave height')
plt.xticks(rotation=-90)
plt.legend()
plt.xlabel('date')
plt.ylabel('count')
plt.title('Waves')
plt.savefig(f'#waves.png')
plt.show()


for i in range(len(lidar_all)):
    for j in range(len(lidar_all[i])):
        data = pd.read_csv(lidar_all[i][j], delim_whitespace=True)
        data.columns = ('epoch', 'wind_speed_0', 'wind_dir_0', 'wind_dir_0_corr', 'height_0', 'wind_speed_1', 'wind_dir_1', 'wind_dir_1_corr', 'height_1', 'wind_speed_2', 'wind_dir_2', 'wind_dir_2_corr', 'height_2', 'wind_speed_3', 'wind_dir_3', 'wind_dir_3_corr', 'height_3', 'wind_speed_4', 'wind_dir_4', 'wind_dir_4_corr', 'height_4', 'wind_speed_5', 'wind_dir_5', 'wind_dir_5_corr', 'height_5', 'wind_speed_6', 'wind_dir_6', 'wind_dir_6_corr', 'height_6', 'wind_speed_7', 'wind_dir_7', 'wind_dir_7_corr', 'height_7', 'wind_speed_8', 'wind_dir_8', 'wind_dir_8_corr', 'height_8', 'wind_speed_9', 'wind_dir_9', 'wind_dir_9_corr', 'height_9', 'wind_speed_10', 'wind_dir_10', 'wind_dir_10_corr', 'height_10', 'heading')
        UTC = []
        for k in range(len(data)):
            UTC.append(pd.Timestamp.fromtimestamp(data.iloc[k, 0]))
        data['epoch'] = UTC
        data.index = data['epoch']
        del data['epoch']
        fig = plt.figure(figsize=(20, 10), dpi=80)
        plt.title(f"month {i + 8} date {j} windspeed")
        plt.xlabel('date')
        plt.ylabel('wind speed in [m/s]')
        #plt.savefig(f"environment/environment/wind/wind_corr/month{i+8}date{j}wave.png")
        plt.plot(data.index, data['wind_speed_0'], c= 'green',linewidth = 0.5, label='wind_speed_0')
        plt.plot(data.index, data['wind_speed_1'], c='red',linewidth = 0.5, label='wind_speed_1')
        plt.plot(data.index, data['wind_speed_2'], c='blue',linewidth = 0.5, label='wind_speed_2')
        plt.plot(data.index, data['wind_speed_3'], c='orange',linewidth = 0.5, label='wind_speed_3')
        plt.plot(data.index, data['wind_speed_4'], c='grey',linewidth = 0.5, label='wind_speed_4')
        plt.plot(data.index, data['wind_speed_5'], c='black',linewidth = 0.5, label='wind_speed_5')
        plt.plot(data.index, data['wind_speed_6'], c='purple',linewidth = 0.5, label='wind_speed_6')
        plt.plot(data.index, data['wind_speed_7'], c='yellow',linewidth = 0.5, label='wind_speed_7')
        plt.plot(data.index, data['wind_speed_8'], c='pink',linewidth = 0.5, label='wind_speed_8')
        plt.plot(data.index, data['wind_speed_9'], c='lightgreen',linewidth = 0.5, label='wind_speed_9')
        plt.plot(data.index, data['wind_speed_10'], c='lightblue', linewidth = 0.5, label='wind_speed_10')
        plt.legend()
        plt.savefig(f"environment/environment/wind/windspeedplots/month{i+8}date{j}windspeed.png")
        plt.show()




data = pd.read_csv(lidar_all[0][0], delim_whitespace=True)
data.columns =  ('epoch', 'wind_speed_0', 'wind_dir_0', 'wind_dir_0_corr', 'height_0', 'wind_speed_1', 'wind_dir_1', 'wind_dir_1_corr', 'height_1', 'wind_speed_2', 'wind_dir_2', 'wind_dir_2_corr', 'height_2', 'wind_speed_3', 'wind_dir_3', 'wind_dir_3_corr', 'height_3', 'wind_speed_4', 'wind_dir_4', 'wind_dir_4_corr', 'height_4', 'wind_speed_5', 'wind_dir_5', 'wind_dir_5_corr', 'height_5', 'wind_speed_6', 'wind_dir_6', 'wind_dir_6_corr', 'height_6', 'wind_speed_7', 'wind_dir_7', 'wind_dir_7_corr', 'height_7', 'wind_speed_8', 'wind_dir_8', 'wind_dir_8_corr', 'height_8', 'wind_speed_9', 'wind_dir_9', 'wind_dir_9_corr', 'height_9', 'wind_speed_10', 'wind_dir_10', 'wind_dir_10_corr', 'height_10', 'heading')
fig = plt.figure(figsize=(2, 8), dpi=80)
data.insert(0, 'filler',0)
plt.plot(data['filler'], data['height_0'],c='blue')
plt.plot(data['filler'], data['height_1'],c='red')
plt.plot(data['filler'], data['height_2'],c='yellow')
plt.plot(data['filler'], data['height_3'],c='green')
plt.plot(data['filler'], data['height_4'],c='orange')
plt.plot(data['filler'], data['height_5'],c='black')
plt.plot(data['filler'], data['height_6'],c='pink')
plt.plot(data['filler'], data['height_7'],c='lightblue')
plt.plot(data['filler'], data['height_8'],c='brown')
plt.plot(data['filler'], data['height_9'],c='purple')
plt.plot(data['filler'], data['height_10'],c='lightgreen')
plt.title('Measure height')
plt.ylabel('height [m]')
plt.xticks(np.arange(0,1,1))
plt.yticks(np.arange(85,145,5))
plt.savefig('measureheight.png')
plt.show()

'''
data = pd.read_csv('lidar_all[0][0]', delim_whitespace=True)
print(len(data.columns))
data.columns =  ('epoch', 'wind_speed_0', 'wind_dir_0', 'wind_dir_0_corr', 'height_0', 'wind_speed_1', 'wind_dir_1', 'wind_dir_1_corr', 'height_1', 'wind_speed_2', 'wind_dir_2', 'wind_dir_2_corr', 'height_2', 'wind_speed_3', 'wind_dir_3', 'wind_dir_3_corr', 'height_3', 'wind_speed_4', 'wind_dir_4', 'wind_dir_4_corr', 'height_4', 'wind_speed_5', 'wind_dir_5', 'wind_dir_5_corr', 'height_5', 'wind_speed_6', 'wind_dir_6', 'wind_dir_6_corr', 'height_6', 'wind_speed_7', 'wind_dir_7', 'wind_dir_7_corr', 'height_7', 'wind_speed_8', 'wind_dir_8', 'wind_dir_8_corr', 'height_8', 'wind_speed_9', 'wind_dir_9', 'wind_dir_9_corr', 'height_9', 'wind_speed_10', 'wind_dir_10', 'wind_dir_10_corr', 'height_10', 'heading')
#plt.plot(data['epoch'],data['heading'],c='blue')
#plt.show()
'''
fig = plt.figure(figsize=(8, 8), dpi=80)
ax = plt.subplot(111, projection='polar')
ax.plot(data["wind_dir_0_corr"][0:1000], data["wind_speed_0"][0:1000], color = 'green', linewidth = 0.1)
plt.title('Wind Direction')
plt.xlabel('wind speed [m/s]')
ax.set_rmax(10)
plt.savefig('winddirection0.png')
plt.show()
'''
