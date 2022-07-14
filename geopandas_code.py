import numpy as np
import geopandas as gpd
import pandas as pd
import shapely.geometry as shp
import matplotlib as plt
oct_2020 = pd.read_csv("27102020.csv")
oct_2020.columns

oct_2020[“price_2”] = oct_2020[“price”].apply(lambda x: str(x).replace(“,”,””).split(“$”)[1]).astype(“float”)
oct_2020[“price”,”price_2"]

oct_2020[‘geometry’]= oct_2020[[‘longitude’,”latitude”]].apply(shp.Point, axis=1)
oct_2020=gpd.GeoDataFrame(oct_2020)
oct_2020.crs={‘init’: ‘epsg:4329’}
oct_2020.sort_values(‘price’).plot(‘price’, cmap=’plasma’, figsize=(15,15));

ist_neigh=gpd.read_file(‘neighbourhoods.geojson’)
ist_neigh.head()

group = gpd.sjoin(oct_2020, ist_neigh, op=’within’, how=’left’)
mean= birlestirilmis.groupby (['neighbourhood_right']).mean()
ist_neigh_merge=ist_neigh.merge(ort,left_on='neighbourhood',right_on='neighbourhood_right')
ax=ist_neigh_merge.plot(figsize=(15,15),column='price_2',scheme='fisher_jenks',k=10,legend=True, cmap='YlGn',edgecolor='black')
ax.set_title("Mean price distribution by districts - Oct-2020")
