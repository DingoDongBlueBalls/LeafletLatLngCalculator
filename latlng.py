import math

def calculateLat( lat1_targetlat, lat1_leafletlat, lat2_targetlat, lat2_leafletlat, extra ):
	divider = 1 / ( lat2_targetlat / lat2_leafletlat );

	difference = lat1_targetlat - ( -lat1_leafletlat / -divider + extra );

	extra += difference

	if( isEqual( difference, 0 ) ):
		return { 'divider': divider, 'difference': extra }
	else:
		return calculateLat( lat1_targetlat, lat1_leafletlat, convertLat( lat2_targetlat, difference ), lat2_leafletlat, extra )


def calculateLng( lng1_targetlng, lng1_leafletlng, lng2_targetlng, lng2_leafletlng, extra ):
	divider = 1 / ( lng2_targetlng / lng2_leafletlng );

	difference = lng1_targetlng - ( lng1_leafletlng / divider + extra );

	extra += difference

	if( isEqual( difference, 0 ) ):
		return { 'divider': divider, 'difference': extra }
	else:
		return calculateLng( lng1_targetlng, lng1_leafletlng, convertLng( lng2_targetlng, difference ), lng2_leafletlng, extra )


def convertLat( lat, diff ):
	if( lat < 0 ):
		return lat + diff
	else:
		return lat - diff

def convertLng( lng, diff ):
	if( lng < 0 ):
		return lng + diff
	else:
		return lng - diff

def isEqual( val1, val2 ):
	if( val1 == val2 ):
		return 1

	if( abs( val1 ) < 0.001 ):
		return 1

	return 0




lat1_targetlat = abs( float( raw_input( 'Enter the in-game latitude of point 1(n): ' ) ) )
lng1_targetlng = float( raw_input( 'Enter the in-game longitude of point 1(n): ' ) )

lat1_leafletlat = abs( float( raw_input( 'Enter the leaflet latitude of point 1(n): ' ) ) )
lng1_leafletlng = float( raw_input( 'Enter the leaflet longitude of point 1(n): ' ) )

lat2_targetlat = abs( float( raw_input( 'Enter the in-game latitude of point 2(s): ' ) ) )
lng2_targetlng = float( raw_input( 'Enter the in-game longitude of point 2(s): ' ) )

lat2_leafletlat = abs( float( raw_input( 'Enter the leaflet latitude of point 2(s): ' ) ) )
lng2_leafletlng = float( raw_input( 'Enter the leaflet longitude of point 2(s): ' ) )




latresult = calculateLat( lat1_targetlat, lat1_leafletlat, lat2_targetlat, lat2_leafletlat, 0 )
lngresult = calculateLng( lng1_targetlng, lng1_leafletlng, lng2_targetlng, lng2_leafletlng, 0 )

print '[ [ ' + str( latresult[ 'divider' ] ) + ', ' + str( latresult[ 'difference' ] ) + ' ], [ ' + str( lngresult[ 'divider' ] ) + ', ' + str( lngresult[ 'difference' ] ) + ' ] ]';