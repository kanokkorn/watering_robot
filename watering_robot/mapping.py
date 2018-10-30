from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(10.724324, 99.376802, 3)

# Polygon
golden_gate_park_lats, golden_gate_park_lons = zip(*[
    (10.724324, 99.376802),
    (10.724361, 99.376710),
    (10.724410, 99.376525),
    (10.724480, 99.376287),
    (10.724538, 99.376090)
    ])
gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=10)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
    (10.724324, 99.376802),
    (10.724361, 99.376710),
    (10.724410, 99.376525),
    (10.724480, 99.376287),
    (10.724538, 99.376090)
    ])
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)

# Marker
hidden_gem_lat, hidden_gem_lon = 10.724324, 99.376802
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("robo_mapping.html")