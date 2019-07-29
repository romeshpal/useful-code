def bh_fil(df, minx, maxx, miny, maxy):
	r=df[(df.x >= minx) & (df.x <= maxx)]
	r=r[(r.y >= miny) & (r.y <= maxy)]
	return r