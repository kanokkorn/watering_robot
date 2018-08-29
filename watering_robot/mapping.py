from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13)

# Polygon
lats, lons = zip(*[
    (37.771269, -122.511015),
    (37.773495, -122.464830),
    (37.774797, -122.454538),
    (37.771988, -122.454018),
    (37.773646, -122.440979),
    (37.772742, -122.440797),
    (37.771096, -122.453889),
    (37.768669, -122.453518),
    (37.766227, -122.460213),
    (37.764028, -122.510347),
    (37.771269, -122.511015)
    ])
gmap.plot(lats, lons, 'cornflowerblue', edge_width=10)

# Scatter points
top_lats, top_lons = zip(*[
    (37.769901, -122.498331),
    (37.768645, -122.475328),
    (37.771478, -122.468677),
    (37.769867, -122.466102),
    (37.767187, -122.467496),
    (37.770104, -122.470436)
    ])
gmap.scatter(top_lats, top_lons, '#3B0B39', size=40, marker=False)

# Marker
hidden_lat, hidden_lon = 37.770776, -122.461689
gmap.marker(hidden_lat, hidden_lon, 'cornflowerblue')

# Draw
gmap.draw("./my_map.html")