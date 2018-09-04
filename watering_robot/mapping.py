from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13)

# Polygon
lats, lons = zip(*[])
gmap.plot(lats, lons, 'cornflowerblue', edge_width=10)

# Scatter points
top_lats, top_lons = zip(*[])
gmap.scatter(top_lats, top_lons, '#3B0B39', size=40, marker=False)

# Marker
hidden_lat, hidden_lon = 37.770776, -122.461689
gmap.marker(hidden_lat, hidden_lon, 'cornflowerblue')

# Draw
gmap.draw("./my_map.html")