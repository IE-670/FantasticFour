
import math

class Ellipsoid:
    # def __init__(self):
    #
    # def WGS84():
    

    def _oneOverRadiiSquared(cartesian): 
        result = Cartesian3()
        
        if (cartesian.x == 0):
            result.x = 0
        else:
            result.x = 1.0 / (cartesian.x**2)

        if (cartesian.y == 0):
            result.y = 0
        else:
            result.y = 1.0 / (cartesian.y**2)

        if (cartesian.z == 0):
            result.z = 0
        else:
            result.z = 1.0 / (cartesian.z**2)
    
        return result
    
    def geodeticSurfaceNormal(cartesian):
        result = Cartesian3.multiplyComponents(cartesian, Ellipsoid._oneOverRadiiSquared(cartesian))
        return Cartesian3.normalize(result)
     
    def  scaleToGeodeticSurface(cartesian,oneOverRadii,oneOverRadiiSquared, centerToleranceSquared):
        positionX = cartesian.x
        positionY = cartesian.y
        positionZ = cartesian.z
        
        oneOverRadiiX = oneOverRadii.x
        oneOverRadiiY = oneOverRadii.y
        oneOverRadiiZ = oneOverRadii.z
        
        x2 = positionX * positionX * oneOverRadiiX * oneOverRadiiX
        y2 = positionY * positionY * oneOverRadiiY * oneOverRadiiY
        z2 = positionZ * positionZ * oneOverRadiiZ * oneOverRadiiZ
        
        #Compute the squared ellipsoid norm.
        squaredNorm = x2 + y2 + z2
        ratio = Math.sqrt(1.0 / squaredNorm)
        
class CesiumMath:
    EPSILON1 = 0.1
    EPSILON2 = 0.01
    EPSILON3 = 0.001
    EPSILON4 = 0.0001
    EPSILON5 = 0.00001
    EPSILON6 = 0.000001
    EPSILON7 = 0.0000001
    EPSILON8 = 0.00000001
    EPSILON9 = 0.000000001
    EPSILON10 = 0.0000000001
    EPSILON11 = 0.00000000001
    EPSILON12 = 0.000000000001
    
    RADIANS_PER_DEGREE = math.pi / 180.0
    DEGREES_PER_RADIAN = 180.0 / math.pi
    
    def toRadians(degrees):
        return degrees * CesiumMath.RADIANS_PER_DEGREE
    
    def sign(value):
        if (value == 0):
            return 0
        elif (value > 0):
            return 1
        else:
            return -1

class Cartesian3:
    
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        
    def clone(cartesian):
        result = Cartesian3(cartesian.x, cartesian.y, cartesian.z)
        return result
        
    def divideByScalar(cartesian, scalar):
        '''
        Cartesian3.multiplyByScalar = function (cartesian, scalar, result) {
            result.x = cartesian.x * scalar;
            result.y = cartesian.y * scalar;
            result.z = cartesian.z * scalar;
            return result;
            };
        '''
        
        result = Cartesian3()
        result.x = cartesian.x / scalar
        result.y = cartesian.y / scalar
        result.z = cartesian.z / scalar
        return result

    def add(left, right):
        result = Cartesian3()
        result.x = left.x + right.x
        result.y = left.y + right.y
        result.z = left.z + right.z
        return result


    def subtract(left, right):
        result = Cartesian3()
        result.x = left.x - right.x
        result.y = left.y - right.y
        result.z = left.z - right.z
        return result
        
    def multiplyByScalar(cartesian, scalar):
        '''
        Cartesian3.multiplyByScalar = function (cartesian, scalar, result) {
            result.x = cartesian.x * scalar;
            result.y = cartesian.y * scalar;
            result.z = cartesian.z * scalar;
            return result;
            };
        '''
        
        result = Cartesian3()
        result.x = cartesian.x * scalar
        result.y = cartesian.y * scalar
        result.z = cartesian.z * scalar
        return result
        
    def multiplyComponents(left, right):
        result = Cartesian3()
        result.x = left.x * right.x
        result.y = left.y * right.y
        result.z = left.z * right.z
        return result

    def magnitudeSquared(cartesian):
        return (cartesian.x**2 + cartesian.y**2 + cartesian.z**2)

    def magnitude(cartesian):
        return math.sqrt(Cartesian3.magnitudeSquared(cartesian))

    def normalize(cartesian):
        magnitude = Cartesian3.magnitude(cartesian)

        result = Cartesian3()
        result.x = cartesian.x / magnitude
        result.y = cartesian.y / magnitude
        result.z = cartesian.z / magnitude

        return result
        
    def fromDegrees(longitude, latitude, height=0.0, ellipsoid=None):
        longitude = CesiumMath.toRadians(longitude)
        latitude = CesiumMath.toRadians(latitude)
    
        return Cartesian3.fromRadians(longitude, latitude, height)

    def fromRadians(longitude, latitude, height=0.0, ellipsoid=None):
        radiiSquared = wgs84RadiiSquared

        cosLatitude = math.cos(latitude)

        scratchN = Cartesian3()
        scratchN.x = cosLatitude * math.cos(longitude)
        scratchN.y = cosLatitude * math.sin(longitude)
        scratchN.z = math.sin(latitude)
        scratchN = Cartesian3.normalize(scratchN)

        scratchK = Cartesian3()
        scratchK = Cartesian3.multiplyComponents(radiiSquared, scratchN)
        gamma = math.sqrt(Cartesian3.dot(scratchN, scratchK))
        scratchK = Cartesian3.divideByScalar(scratchK, gamma)
        scratchN = Cartesian3.multiplyByScalar(scratchN, height)

        return Cartesian3.add(scratchK, scratchN)
        
    def dot(left, right):
        return left.x * right.x + left.y * right.y + left.z * right.z

Cartesian3.UNIT_X = Cartesian3(1.0, 0.0, 0.0)
Cartesian3.UNIT_Y = Cartesian3(0.0, 1.0, 0.0)
Cartesian3.UNIT_Z = Cartesian3(0.0, 0.0, 1.0)

Cartesian3.UNIT_Z

class IntersectionTests:
    # def __init__(self):
    #     nothing to see here...
    
    def lineSegmentPlane(endPoint0, endPoint1, plane):
        '''
        Find the intersection of the line segment from p0 to p1 and the tangent plane at origin.
        * intersection = IntersectionTests.lineSegmentPlane(p0, p1, plane)
        '''
        
        result = Cartesian3()

        difference = Cartesian3.subtract(endPoint1, endPoint0)
        
        normal = plane.normal
        nDotDiff = Cartesian3.dot(normal, difference)

        # check if the segment and plane are parallel
        if (abs(nDotDiff) < CesiumMath.EPSILON6):
            return None    # FIXME

        nDotP0 = Cartesian3.dot(normal, endPoint0)
        t = -(plane.distance + nDotP0) / nDotDiff

        # intersection only if t is in [0, 1]
        if ((t < 0.0) or (t > 1.0)):
            return None    # FIXME

        # intersection is endPoint0 + t * (endPoint1 - endPoint0)
        result = Cartesian3.multiplyByScalar(difference, t)
        result = Cartesian3.add(endPoint0, result)

        return result

class Plane:
    def __init__(self, normal, distance):
        '''
        A plane in Hessian Normal Form defined by
        * ax + by + cz + d = 0
        where (a, b, c) is the plane's <code>normal</code>, d is the signed
        * <code>distance</code> to the plane, and (x, y, z) is any point on
        * the plane.        
        '''
        
        self.normal = Cartesian3.clone(normal)
        self.distance = distance
        
    def fromPointNormal(point, normal):
        distance = -Cartesian3.dot(normal, point)

        result = Plane(normal, distance)

        result.normal = Cartesian3.clone(normal)
        result.distance = distance
        return result

'''
DON'T NEED THIS, BUT AFRAID TO DELETE JUST YET

class cartesian:
    def __init__(self, x=None, y=None, z=None):
        self.x = x;
        self.y = y;
        self.z = z;        
'''

wgs84OneOverRadii = Cartesian3( 1.0 / 6378137.0, 1.0 / 6378137.0,  1.0 / 6356752.3142451793 )

wgs84RadiiSquared = Cartesian3(6378137.0 * 6378137.0,
                               6378137.0 * 6378137.0,
                               6356752.3142451793 * 6356752.3142451793)
wgs84OneOverRadiiSquared = Cartesian3(
  1.0 / (6378137.0 * 6378137.0),
  1.0 / (6378137.0 * 6378137.0),
  1.0 / (6356752.3142451793 * 6356752.3142451793)
)

wgs84CenterToleranceSquared = CesiumMath.EPSILON1


origin = Cartesian3.fromDegrees(-75.59777, 40.03883, 50)
normal = Ellipsoid.geodeticSurfaceNormal(origin)

plane = Plane.fromPointNormal(origin, normal)

p0 = Cartesian3.fromDegrees(-75.59777, 40.03883, 150)
p1 = Cartesian3.fromDegrees(-75.59777, 40.03883, 0)

# find the intersection of the line segment from p0 to p1 and the tangent plane at origin.
intersection = IntersectionTests.lineSegmentPlane(p0, p1, plane)

print(intersection.x, intersection.y, intersection.z)


'''
var cartographic = 

Cesium.Cartographic.fromCartesian(cartesian);
console.log(
    'lon ' + Cesium.Math.toDegrees(cartographic.longitude) + ', ' +
    'lat ' + Cesium.Math.toDegrees(cartographic.latitude) + ', ' +
    'alt ' + cartographic.height);
'''


def scaleToGeodeticSurface(cartesian, oneOverRadii, oneOverRadiiSquared, centerToleranceSquared):
    
    positionX = cartesian.x
    positionY = cartesian.y
    positionZ = cartesian.z
    
    oneOverRadiiX = oneOverRadii.x
    oneOverRadiiY = oneOverRadii.y
    oneOverRadiiZ = oneOverRadii.z
    
    x2 = positionX * positionX * oneOverRadiiX * oneOverRadiiX
    y2 = positionY * positionY * oneOverRadiiY * oneOverRadiiY
    z2 = positionZ * positionZ * oneOverRadiiZ * oneOverRadiiZ
    
    #Compute the squared ellipsoid norm.
    squaredNorm = x2 + y2 + z2
    ratio = math.sqrt(1.0 / squaredNorm)
    
    #As an initial approximation, assume that the radial intersection is the projection point.
    intersection = Cartesian3.multiplyByScalar(cartesian, ratio)
    
    #If the position is near the center, the iteration will not converge.
    if (squaredNorm < centerToleranceSquared):
        if  math.isfinite(ratio):
            return Cartesian3.clone(intersection)
        else:
            return None
        
    
    oneOverRadiiSquaredX = oneOverRadiiSquared.x
    oneOverRadiiSquaredY = oneOverRadiiSquared.y
    oneOverRadiiSquaredZ = oneOverRadiiSquared.z
    
    #Use the gradient at the intersection point in place of the true unit normal.
    #The difference in magnitude will be absorbed in the multiplier.
    gradient = Cartesian3()
    gradient.x = intersection.x * oneOverRadiiSquaredX * 2.0
    gradient.y = intersection.y * oneOverRadiiSquaredY * 2.0
    gradient.z = intersection.z * oneOverRadiiSquaredZ * 2.0
    
    #Compute the initial guess at the normal vector multiplier, lambda.
    lamda = ((1.0 - ratio) * Cartesian3.magnitude(cartesian)) / (0.5 * Cartesian3.magnitude(gradient))
    correction = 0.0
    
    func = CesiumMath.EPSILON11
    while (abs(func) > CesiumMath.EPSILON12):
        lamda -= correction
        zMultiplier = 1.0 / (1.0 + (lamda * oneOverRadiiSquaredZ))
        yMultiplier = 1.0 / (1.0 + (lamda * oneOverRadiiSquaredY))
        xMultiplier = 1.0 / (1.0 + (lamda * oneOverRadiiSquaredX))
        
        xMultiplier2 = xMultiplier * xMultiplier
        yMultiplier2 = yMultiplier * yMultiplier
        zMultiplier2 = zMultiplier * zMultiplier
        
        xMultiplier3 = xMultiplier2 * xMultiplier
        yMultiplier3 = yMultiplier2 * yMultiplier
        zMultiplier3 = zMultiplier2 * zMultiplier
        
        func = x2 * xMultiplier2 + y2 * yMultiplier2 + z2 * zMultiplier2 - 1.0
        
        #\"denominator\" here refers to the use of this expression in the velocity and acceleration
        #computations in the sections to follow.
        denominator = (x2 * xMultiplier3 * oneOverRadiiSquaredX + y2 * yMultiplier3 * oneOverRadiiSquaredY + z2 * zMultiplier3 * oneOverRadiiSquaredZ)
        
        derivative = -2.0 * denominator
        correction = func / derivative
    
    return Cartesian3(positionX * xMultiplier, positionY * yMultiplier, positionZ * zMultiplier)

class Cartographic:
    def __init__(self, longitude=0.0, latitude=0.0, height=0.0):
        self.longitude = longitude
        self.latitude = latitude
        self.height = height

    def fromCartesian(cartesian, ellipsoid=None):
        # FIXME -- Need to find these values\n"
        oneOverRadii           = wgs84OneOverRadii
        oneOverRadiiSquared    = wgs84OneOverRadiiSquared
        centerToleranceSquared = wgs84CenterToleranceSquared
        
        p = scaleToGeodeticSurface(cartesian, oneOverRadii, oneOverRadiiSquared, centerToleranceSquared)
        
        if p is None:
            return None
        n = Cartesian3.multiplyComponents(p, oneOverRadiiSquared)
        n = Cartesian3.normalize(n)
        
        h = Cartesian3.subtract(cartesian, p)
        
        # lon/lat are in radians
        longitude = math.atan2(n.y, n.x)
        latitude = math.asin(n.z)
        height = CesiumMath.sign(Cartesian3.dot(h, cartesian)) * Cartesian3.magnitude(h)
        
        result = Cartographic()
        result.longitude = longitude
        result.latitude = latitude
        result.height = height
        
        return result
        


# To Do:
# - Need `scaleToGeodeticSurface()` function converted to Python
# 
# - Finish/Fix/Debug `Cartographic.fromCartesian()` function
# 
# - Display plane in Cesium
# - Display line segment in Cesium
# 
# 
# - Verify that our intersection code seems reasonable.
# 
# --- 
# 
# - We need road network data (Thursday installation of pgRouting or OSRM)
#     - Interections