import math

# Equation needed to solve problem: method= surface: t = (d * kpd)v, method=chord: t2= (2*R/vp)sin(theta/2)
# t= travel time, d = ANGULAR distance in degrees, kpd= km to degree conversion, v= avg velocity in km/s

# Choose a method
method = 'chord'
# method= 'surface'

# Constants
R = 3390.0  # km

# Equation variables
kpd = math.pi*R/180
rpd = math.pi/180

# Compute distance and time for surface and P waves
d = 0
dstep = 1

if method == 'surface':
    v = 4  # km/s
    while d < 101:
        dist = d * kpd
        t = dist/v
        print('Distance in degrees: {:d} Travel time in seconds: {:10.1f}'.format(d, t))
        d += dstep

if method == 'chord':
    vp = 11  # km/s
    while d <= 100:
        theta = d * rpd
        halftheta = 0.5 * theta
        a = 2 * R * math.sin(halftheta)
        t2 = a/vp
        print('Distance in degrees: {:d} Travel time in seconds: {:10.1f}'.format(d, t2))
        d = d + dstep
