from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(10.725359, 99.375334, 3)

# Polygon
golden_gate_park_lats, golden_gate_park_lons = zip(*[
    (10.725359, 99.375334),
    (10.725499, 99.375376),
    (10.725635, 99.375414),
    (10.725771, 99.375461),
    (10.725940, 99.375502)
    ])
gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=10)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
    (10.725359, 99.375334),
    (10.725499, 99.375376),
    (10.725635, 99.375414),
    (10.725771, 99.375461),
    (10.725940, 99.375502)
    ])
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)

# Marker
hidden_gem_lat, hidden_gem_lon = 10.725359, 99.375334
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("robo_mapping.html")