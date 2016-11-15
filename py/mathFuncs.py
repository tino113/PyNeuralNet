from math import exp
from colorsys import hsv_to_rgb

def sigmoid(x):
    return 1 / (1 + exp(-x))

def decTohex(d):
    return "%02X" % d

def rgbTohex(r,g,b):
    return '#%02x%02x%02x' % (r,g,b)

def hsvTohex(h,s,v):
    rgb = hsvTorgb(h,s,v)
    return rgbTohex(rgb[0],rgb[1],rgb[2])

def hsvTorgb(h,s,v):
    return tuple(int(i * 255) for i in hsv_to_rgb(h,s,v))
