# with manage.py shell
# from trail_maker import trail_maker
# from fiona import collection
# with collection("BSP_Trails_2014Jan2.shp", "r") as input:
#	for trail in input:
#		t = trail_maker(trail)
#		db.session.add(t)
#		db.session.commit(t)

from baxter.models import Trail
from shapely.geometry import mapping, shape, MultiLineString
from geoalchemy2.shape import from_shape
# coding: utf-8
def trail_maker(trail):
    if trail['properties']['SkiTrail'] == 'Y':
        skitrail = True
    else:
        skitrail = False

    if trail['properties']['Display1'] == 'Y':
        display = True
    else:
        display = False

    if trail['properties']['PubShare'] == 'Y':
        pubshare = True
    else:
        pubshare = False

    if trail['properties']['Display_WU'] == 'Y':
        display_wu = True
    else:
        display_wu = False

    if trail['properties']['Display_WN'] == 'Y':
        display_wn = True
    else:
        display_wn = False
        
    if trail['geometry']['type'] == 'LineString':
    	geom = MultiLineString([shape(trail['geometry'])])
    else:
    	geom = shape(trail['geometry'])
    t = Trail(geom=from_shape(geom, srid=926919),
              use_type=trail['properties']['USE_TYPE'],
              comments=trail['properties']['COMMENTS'],
              tid=trail['properties']['TID'],
              skitrail=skitrail,
              name=trail['properties']['TName'],
              length_mi=trail['properties']['TLength_mi'],
              status=trail['properties']['TStatus'],
              display=display,
              pubshare=pubshare,
              gpsupdate=trail['properties']['GPSUpDate'],
              gpsunit=trail['properties']['GPSUnit'],
              gpsuser=trail['properties']['GPSUser'],
              bspaid=trail['properties']['BSPAID'],
              tsid=trail['properties']['TSID'],
              display_wu=display_wu,
              display_wn=display_wn,
              ttype=trail['properties']['TType'],
              season=trail['properties']['TSeason'],
              shape_leng=trail['properties']['Shape_Leng'],
              tclass=trail['properties']['TClass'],
              maintclass=trail['properties']['MaintClass'],
              slength=trail['properties']['SLength'],
              min_slope=trail['properties']['Min_Slope'],
              max_slope=trail['properties']['Max_Slope'],
              avg_slope=trail['properties']['Avg_Slope'],
              length_ft=trail['properties']['TLength_ft'])
    return t
