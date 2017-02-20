# Given 2 points p1(x1,y1) and p2(x2,y2)
# Show the equation of the bisector line 

print("-"*95)
print("This program shows the equation for a line that intersects two given points, and its bisector.")

# Formats the point as x,y and checks for input format for point 1
pointInput1 = "(10,2)" #input("Please enter the coordinates for point 1 in the following format: (x,y) ")

pointCoords1 = pointInput1

if "(" and ")" in pointCoords1:
    pointCoords1 = pointCoords1.replace( "(" , "")
    pointCoords1 = pointCoords1.replace( ")" , "")
    pointCoords1 = pointCoords1.replace( " " , "")
    print(pointCoords1)
else:
    print("The input was not formatted correctly. Please try again.")

# Does the same for point 2
pointInput2 = "(20,50)" # input("Please enter the coordinates for point 2 on the line: ")

pointCoords2 = pointInput2

if "(" and ")" in pointCoords2:
    pointCoords2 = pointCoords2.replace( "(" , "")
    pointCoords2 = pointCoords2.replace( ")" , "")
    pointCoords2 = pointCoords2.replace( " " , "")
    print(pointCoords2)
else:
    print("The input was not formatted correctly. Please try again.")

print("-"*95)
# Time to separate the values into two variables
pointCoords1 = pointCoords1.split(",")

pointX1 = float(pointCoords1[0])
pointY1 = float(pointCoords1[1])

pointCoords2 = pointCoords2.split(",")

pointX2 = float(pointCoords2[0])
pointY2 = float(pointCoords2[1])

# Time to make an equation for the two points

slope = (pointY2 - pointY1) / (pointX2 - pointX1)

inverseSlope = -1 / slope

# Time to get the midpoint and the coordinates for the original equation
midPointX = (pointX1 + pointX2) / 2
midPointY = (pointY1 + pointY2) / 2
midPoint = str(midPointX) + "," + str(midPointY)
midPoint = midPoint.split(",")
midPointX = float(midPoint[0])
midPointY = float(midPoint[1])

# Time to get the y-intercept of the original equation
yInt = (pointY1 - slope * pointX1)

# Time to get the y intercept of the bisector
yIntBisector = (midPointY - inverseSlope * midPointX)

# Now for hte grand finale
print( "The equation for the line that intersects the two given points is: y = (%.2f) x + (%.2f)" % (slope ,yInt) )
print( "The equation for the bisector line of the two given points is: y = (%.2f) x + (%.2f)" % (inverseSlope ,yIntBisector) ) 




















