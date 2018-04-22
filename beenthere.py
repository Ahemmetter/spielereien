from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

# lat = float(raw_input("Latitude: "))
# long = float(raw_input("Longitude: "))

lat = float(59.906459)
long = float(30.479903)

latd = 5340     # 89*60
longd = 10740   # 179*60

def find_square(lat, long):
    if lat < 0:
        ys = int(lat)*60 - int(abs(lat - int(lat))*60)
    else:
        ys = int(lat)*60 + int(abs(lat - int(lat))*60)

    if long < 0:
        xs = int(long)*60 - int(abs(long - int(long))*60)
    else:
        xs = int(long)*60 + int(abs(long - int(long))*60)

    return xs, ys

xs, ys = find_square(lat, long)

map = Basemap(projection='merc', lat_0=0, lon_0=0, resolution='l', llcrnrlon=-180, llcrnrlat=-70, urcrnrlon=180, urcrnrlat=85)
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.fillcontinents(color='darkgrey',lake_color='lightsteelblue')
map.drawmapboundary(fill_color='lightsteelblue')
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))

x, y = map(long, lat)
map.plot(x, y, 'bo', markersize=1)
res = 100

def draw_screen_poly(lats, lons, map):
    toplat, toplon = map(lons, np.full(res, top))
    bottomlat, bottomlon = map(lons, np.full(res, bottom))
    rightlat, rightlon = map(np.full(res, right), lats)
    leftlat, leftlon = map(np.full(res, left), lats)
    xy = zip(toplat, toplon) + zip(bottomlat, bottomlon) + zip(rightlat, rightlon) + zip(leftlat, leftlon)
    poly = Polygon(xy, facecolor='red', alpha=0.4 )
    plt.gca().add_patch(poly)

top = (ys+1)/60.0
bottom = ys/60.0
right = (xs+1)/60.0
left = xs/60.0

print top
print right
lats = np.linspace(bottom, top, res)
lons = np.linspace(left, right, res)

draw_screen_poly(lats, lons, map )

plt.show()
