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
gmap.plot(watering_lats, watering_lons, 'cornflowerblue', edge_width=10)
watering_lat1, watering_lon1 = 10.724324, 99.376802
gmap.marker(watering_lat1, watering_lon1, 'cornflowerblue')

watering_lat2, watering_lon2 = 10.724361, 99.376710
gmap.marker(watering_lat2, watering_lon2, 'cornflowerblue')

watering_lat3, watering_lon3 = 10.724410, 99.376525
gmap.marker(watering_lat3, watering_lon3, 'cornflowerblue')

watering_lat4, watering_lon4 = 10.724480, 99.376287
gmap.marker(watering_lat4, watering_lon4, 'cornflowerblue')

watering_lat5, watering_lon5 = 10.724538, 99.376090
gmap.marker(watering_lat5, watering_lon5, 'cornflowerblue')

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