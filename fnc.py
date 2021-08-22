import numpy as np
import cv2
import gpsd

def getPositionData(gps):
	nx = gpsd.next()
    if nx['class'] == 'TPV':
        latitude = getattr(nx, 'lat', "Unknown")
        longitude = getattr(nx, 'lon', "Unknown")
        return str(latitude), str(longitude)


