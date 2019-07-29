
import numpy as np
import mplstereonet
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(r"CSV")
azimuth=np.array(df['AZIMUTH'])
dips=np.array(df['DIP'])
strikes=azimuth-90



fig = plt.figure(figsize=(8,8))
ax= fig.add_subplot(111, projection='stereonet')
ax.plane(strikes, dips, c='g')
ax.pole(strikes, dips, c='r')


ax.grid()

#plt.savefig('NAME', dpi= 300, transparent=True)
