import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

#imputs



df=pd.read_excel(r"LOCATION", sheet_name="Sheet1")


#Group data
x=df['Ga_ppm_m69']
y=df['Ge_ppm_m72']
s=50

fig = plt.figure(figsize=(10,10))

#plot 1
ax = plt.subplot(111, facecolor='lightgrey')
ax.scatter(x,y, s=s, c='lightcoral', edgecolor='k', marker='o', label='1')

#Tailor plot 1
plt.xlabel('Ga')
plt.xlim()
plt.ylabel('Ge')
plt.ylim()
plt.title('HF_Br_05_sph', size=12)
#plt.legend(facecolor='white', edgecolor='k', framealpha =1.0)
plt.grid(False)

#export
plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=1.0)
plt.savefig(file_name, dpi= 500, transparent=False)
plt.show()
