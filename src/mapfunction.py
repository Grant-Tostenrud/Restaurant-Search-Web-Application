# get maps api key and initialize
import gmaps
from ipywidgets.embed import embed_minimal_html


#map function
def mapfunction(lat_long):
    mapsApiKey = 'AIzaSyALZd_zEydRGrv4Fk3tQqUH5R19Y8aykYc'
    gmaps.configure(api_key=mapsApiKey)
    # markers on the map are the locations of each business
    marker_locations = lat_long
    fig = gmaps.figure()
    markers = gmaps.marker_layer(marker_locations)
    # add markers
    fig.add_layer(markers)
    # export to html
<<<<<<< HEAD
    embed_minimal_html('rmap.html', views=[fig])
=======
    embed_minimal_html('/Users/granttostenrud/Desktop/RestaurantAventure/templates/rmap.html', views=[fig])
>>>>>>> f5b8e3e5b728e37ba454e883dbc2c85f71a34e82
