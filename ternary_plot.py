import pandas as pd
import ternary
import numpy as np

df=pd.read_csv(r"CSV WITH DATA")

#make a arrays of your data
Y=(np.array(df.Y))*100
X=(np.array(df.X))*100
I=(np.array(df.I))*100

#MAKE TUPLE OF YOUR DATA
points=np.array((X,I,Y)).T


### ternary plot 

#PLOT SET UP
figure, tax = ternary.figure(scale=100)
#tax.set_title("Node types", fontsize=20)
figure.set_size_inches(8, 8)
tax.gridlines(multiple=10, color="lightblue")
tax.boundary(linewidth=1.0)
tax.ax.axis('off')

#DATA
tax.scatter(points, marker='o', edgecolor='k', color='lightcoral', label="nodes")

#LABELS ANF STYLE
tax.legend()
tax.left_corner_label('Y', fontsize=12)
tax.right_corner_label('X', fontsize=12)
tax.top_corner_label('I', fontsize=12)
tax.ticks(axis='lbr', linewidth=1, multiple=10, fontsize=8)
tax.clear_matplotlib_ticks()

#EXPORT AND SHOW PLOT
tax.savefig(r"test.png")
tax.show()

