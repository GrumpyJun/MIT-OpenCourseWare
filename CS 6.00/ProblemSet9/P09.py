# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 9
# Student: May Pongpitpitak
# August 13, 2011

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    """
    DESC:   This is a sub-class of Shape [Shape -> Triangle]
    INPUT:  Triangle(base, height)
            where:
            base is the dimension of the triangle's base
            height is the dimension of the triangle's height
    """

    def __init__(self, base, height):
        """
        DESC:   To initialize the triangle object, we requrie
                the base and the height of the triangle

        base:   the base of the triangle
        height: the height of the triangle
        """
        self.base   = float(base)
        self.height = float(height)

    def area(self):
        """
        return: the area of the triangle using the formula (1/2 * base * height)
        """
        return (0.5 * self.base * self.height)

    def __str__(self):
        """
        return: the base and height dimension of the triangle
        """
        return ("Triangle with base %0.2f and height %0.2f" % (self.base, self.height))

    def __eq__(self, other):
        """
        DESC:   Two triangles are equal if they have the same radius.

        other:  another triangle object to check for equality

        return:     
        """
        return (type(other) == Triangle and \
                self.base == other.base and self.height == other.height) 
                



#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    """
    Return the string representation for a set, which consists of
    the string representation of each shape, categorized by type
    (circles, then squares, then triangles)
    """
    
    def __init__(self):
        """
        Initialize any needed variables
        """

        self.shapeList  = []
        self.shapeIndex = None
        
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """

        assert type(sh) == Circle or type(sh) == Square or type(sh) == Triangle, \
               "Input shape is not supported"
        assert sh not in self.shapeList, \
               "Shape already existed"
        
        self.shapeList.append(sh)
        
                
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        self.shapeIndex = 0
        return (self)

    def next(self):
        """
        DESC:   increase the index position of the current iteration by 1
                for the next iteration and return the current object
        
        return: object at current index
        """
        if self.shapeIndex >= len(self.shapeList):
            raise StopIteration
        self.shapeIndex += 1
        return (self.shapeList[self.shapeIndex - 1])

    def __str__(self):
        """
        DESC:   creating a string representation of the set by assembling
                the object's own string representation organized in the order of
                Circle, Square and Triangle

        return: lines of string representation of all supported objects in the set
        """
        
        allCircles      = ''
        allSquares      = ''
        allTriangles    = ''

        # Group the string representation of the same shapes together
        for eachShape in self.shapeList:
            if type(eachShape) is Circle:      allCircles   += str(eachShape) + '\n'
            elif type(eachShape) is Square:    allSquares   += str(eachShape) + '\n'
            elif type(eachShape) is Triangle:  allTriangles += str(eachShape) + '\n'

        # Combine all the string representation
        allShape = allCircles + allSquares + allTriangles
        
        # Return the string representation
        return (allShape)


        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapeSet):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    shapeAreaList   = []
    largestShape    = []
    
    for shape in shapeSet.shapeList:
        shapeAreaList.append(shape.area())
    
    largestArea = max(shapeAreaList)
    for shape in shapeSet.shapeList:
        if shape.area() == largestArea:
            largestShape.append(shape)
            
    return (tuple(largestShape))



#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    
    inputFile = open(filename, 'r', 1)

    createShapesCmd = []
    shapesCreated   = ShapeSet()
    
    for line in inputFile:
        nextCmd = line.strip().split(',', 1)
        createShapesCmd.append(nextCmd[0].title() + \
                               '(' + nextCmd[1] + ')')

    for eachCmd in createShapesCmd:
        shapesCreated.addShape(eval(eachCmd))
        
    return(shapesCreated)
            

        


