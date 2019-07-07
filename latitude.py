import math

def calculateLat( lat1_targetlat, lat1_leafletlat, lat2_targetlat, lat2_leafletlat, extra ):
	divider = 1 / ( lat2_targetlat / lat2_leafletlat );

	difference = lat1_targetlat - ( -lat1_leafletlat / -divider + extra );

	extra += difference

	if( isEqual( difference, 0 ) ):
		return { 'divider': divider, 'difference': extra }
	else:
		return calculateLat( lat1_targetlat, lat1_leafletlat, convertLat( lat2_targetlat, difference ), lat2_leafletlat, extra )


def convertLat( lat, diff ):
	if( lat < 0 ):
		return lat - diff
	else:
		return lat + diff

def isEqual( val1, val2 ):
	if( val1 == val2 ):
		return 1

	if( abs( val1 - val2 ) < .01 ):
		return 1

	return 0

# def matchingLat( lat1, divider, difference, lat2 ):
# 	if( isEqual( lat1 / divider + difference, lat2 ) ):
# 		return 1

# 	if( isEqual( lat1 / -divider + -difference, lat2 ) ):
# 		return 1

# 	if( isEqual( lat1 / -divider + difference, lat2 ) ):
# 		return 1

# 	if( isEqual( lat1 / divider + -difference, lat2 ) ):
# 		return 1

# 	return 0

lat1_targetlat = float( raw_input( 'Enter the in-game latitude of point 1(n): ' ) )
lat1_leafletlat = float( raw_input( 'Enter the leaflet latitude of point 1(n): ' ) )

lat2_targetlat = float( raw_input( 'Enter the in-game latitude of point 2(s): ' ) )
lat2_leafletlat = float( raw_input( 'Enter the leaflet latitude of point 2(s): ' ) )

print( calculateLat( lat1_targetlat, lat1_leafletlat, lat2_targetlat, lat2_leafletlat, 0 ) )