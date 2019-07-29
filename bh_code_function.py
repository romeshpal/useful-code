def coded_bh(x, column):
	''' Number of BH's coded, x= dataframe, column=coded columns'''
	x2=x.loc[:, ['bgs_id', column]]
	x3=x2.dropna(axis=0)
	bgs_id=np.array(x3.bgs_id)
	x4=np.unique(bgs_id)
	result=len(x4)
	print(result)

