
import matplotlib.pyplot as plt

fig, ax=plt.subplots(figsize=(10,10))
ax.set_aspect('equal')
circle.plot(ax=ax, color='white', edgecolor='grey', markersize=20, label='circle')
plt.legend()
plt.ylim()
plt.xlim()
#plt.savefig(r"", dpi= 500)
plt.show()


def shape_plot(df):
	fig, ax=plt.subplots(figsize=(10,10))
	ax.set_aspect('equal')
	df.plot(ax=ax, color='k')
	plt.show()