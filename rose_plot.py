import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl



data = pd.read_csv(r"DATA")
data2 = pd.read_csv(r"DATA")

#Create right hand side of rose plot
data['Orient'] = data['Orient'].where(data['Orient']<180, data['Orient']-180, axis = 0)

data['Orient'] = data['Orient'] + 180

#creat left hand side of rose plot
data2['Orient'] = data2['Orient'].where(data2['Orient']<180, data2['Orient']-180, axis = 0)

#apped two half od rose plot
df = data.append(data2)



BIN_COUNT = 20
width = 2 * np.pi / BIN_COUNT
range = (0, 2*np.pi)

area_1 = df.loc[df['Circle id'] == 1]
area_2 = df.loc[df['Circle id'] == 2]

                                    #plot
fig = plt.figure(figsize=(16,10))
                             
strikes = area_1['Orient']

strikes_rad = np.deg2rad(strikes)
# hist is like radii, bin_edges is like theta
hist, bin_edges = np.histogram(strikes_rad, bins=BIN_COUNT, range=(0, 2*np.pi))

theta1 = bin_edges
radii1 = hist

#Calculating average length for coloring each bar
sort=area_1.sort_values('Orient', ascending=True)
sort['Orient_radons']= sort['Orient']*(np.pi/180)
Group_orient=sort.groupby(pd.cut(sort['Orient_radons'], theta1))
len_mean=Group_orient['Length'].mean()
len_mean_array=np.array(len_mean)
len_mean_array=np.nan_to_num(len_mean_array)
RGB=len_mean_array/len_mean_array.max()
RGB_round=np.round(RGB, 2)


ax1 = plt.subplot(111, projection='polar')
bars = ax1.bar(theta1[:-1], radii1, width=width, edgecolor='k')
ax1.set_theta_zero_location('N')
ax1.set_theta_direction(-1)
#plt.axis('off')
#ax1.grid(False)
fig.patch.set_alpha(0.)
ax1.set_thetagrids(np.arange(0, 360, 90), labels=np.arange(0, 360, 90), fontsize=8)
ax1.set_title('Upper circle', y=1.10, fontsize=12)


#Colour bar for plot 1
for r, bar in zip(len_mean_array, bars):
    bar.set_facecolor(plt.cm.PiYG(r))
    bar.set_alpha(1)
    
axis = fig.add_axes([0.15, 0.1, 0.3, 0.04])
cmap = mpl.cm.PiYG
norm = mpl.colors.Normalize(vmin=len_mean_array.min(), vmax=len_mean_array.max())
cb1 = mpl.colorbar.ColorbarBase(axis, cmap=cmap,
                                norm=norm,
                                orientation='horizontal', 
                                spacing='uniform')
cb1.set_label('Length (m)')
    
#plt.show()
plt.savefig('test.png', dpi= 300)