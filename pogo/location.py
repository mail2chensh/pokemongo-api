from geopy.geocoders import GoogleV3
from s2sphere import CellId, LatLng

geolocator = GoogleV3()

def getLocation(search):
    loc = geolocator.geocode(search)
    return loc

def getCells(loc, radius = 10):
    origin = CellId.from_lat_lng(LatLng.from_degrees(loc.latitude, loc.longitude)).parent(15)
    walk = [origin.id()]
    right = origin.next()
    left = origin.prev()

    # Search around provided radius
    for i in range(radius):
        walk.append(right.id())
        walk.append(left.id())
        right = right.next()
        left = left.prev()

    # Return everything
    return sorted(walk)