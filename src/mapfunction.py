# get maps api key and initialize
import gmaps
from ipywidgets.embed import embed_minimal_html


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
    embed_minimal_html('/Users/granttostenrud/Desktop/RestaurantAventure/templates/rmap.html', views=[fig])