import math

def calculateLng( lng1_targetlng, lng1_leafletlng, lng2_targetlng, lng2_leafletlng, extra ):
	divider = 1 / ( lng2_targetlng / lng2_leafletlng );

	# print "lng1 targetlng: " + str( lng1_targetlng )
	# print "lng1 leaflet: " + str( lng1_leafletlng )
	# print "lng2 targetlng: " + str( lng2_targetlng )
	# print "lng2 leaflet: " + str( lng2_leafletlng )

	difference = lng1_targetlng - ( lng1_leafletlng / divider + extra );

	# print "diff1: " + str( difference )

	extra += difference

	# print "diff: " + str( extra )
	# print "divider: " + str( divider )

	if( isEqual( difference, 0 ) ):
		return { 'divider': divider, 'difference': extra }
	else:
		return calculateLng( lng1_targetlng, lng1_leafletlng, convertLng( lng2_targetlng, difference ), lng2_leafletlng, extra )


def convertLng( lng, diff ):
	if( lng < 0 ):
		return lng + diff
	else:
		return lng - diff

def isEqual( val1, val2 ):
	if( val1 == val2 ):
		return 1

	if( abs( val1 - val2 ) < .01 ):
		return 1

	return 0

# def matchingLat( lng1, divider, difference, lng2 ):
# 	if( isEqual( lng1 / divider + difference, lng2 ) ):
# 		return 1

# 	if( isEqual( lng1 / -divider + -difference, lng2 ) ):
# 		return 1

# 	if( isEqual( lng1 / -divider + difference, lng2 ) ):
# 		return 1

# 	if( isEqual( lng1 / divider + -difference, lng2 ) ):
# 		return 1

# 	return 0

lng1_targetlng = float( raw_input( 'Enter the in-game longitude of point 1(n): ' ) )
lng1_leafletlng = float( raw_input( 'Enter the leaflet longitude of point 1(n): ' ) )

lng2_targetlng = float( raw_input( 'Enter the in-game longitude of point 2(s): ' ) )
lng2_leafletlng = float( raw_input( 'Enter the leaflet longitude of point 2(s): ' ) )

print( calculateLng( lng1_targetlng, lng1_leafletlng, lng2_targetlng, lng2_leafletlng, 0 ) )