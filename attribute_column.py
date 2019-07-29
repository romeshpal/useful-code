
conda install -c conda-forge geopandas
import geopandas as gpd
df=gpd.read_file(r"")


def f(row):
    '''
    Given a column value, set the value of the column to a new value
    '''
    if row['GRID_CODE'] == 0:
        val = 7
    elif row['GRID_CODE'] ==  1:
        val = 3
    elif row['GRID_CODE'] ==  2:
        val = 1  
    else:
        val = 0 

    return val

# Apply function to each row
df['thick']=df.apply(f, axis=1)

#set projection
df.crs={'init':'epsg:27700'}

#write to file
df.to_file(r"")

