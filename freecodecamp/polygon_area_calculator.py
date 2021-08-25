
 # Area = 1/2 x Perimeter x Apothem
 # !!! SUCCESS !!!
 # Probably Contains Bugs / Needs Tuned and Cleaned


class Rectangle:
    """A Class Representing a Rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
            self.height = height
            return self.height

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_area(self):
        area = self.width * self.height
        return area

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        """Prints picture of the Rectangle"""
        line = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        if self.width <= 50:
            line_width = "*" * self.width
            for i in range(0, self.height):
                line += line_width + "\n"
            return line
        elif self.height <= 50:
            line_width = "*" * self.width
            for i in range(0, self.height):
                line += line_width + "\n"
            return line

    def get_amount_inside(self, shape):
        self.shape = shape

        inside_area = shape.get_area()
        outside_area = self.get_area()
        num_times = outside_area // inside_area
        return int(num_times)


class Square(Rectangle):
    """Class Representing a Square"""

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side
        return self.width, self.height

    def set_width(self, side):
        self.width = side
        self.height = side
        return self.width, self.height

    def set_height(self, side):
        self.height = side
        self.width = side
        return self.height, self.width

    def get_area(self):
        area = self.width * self.height
        return area


# Inputs to Test and Print Functions
rect = Rectangle(50, 50)
print(rect.get_area())
rect.set_height(50)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
 
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
 
rect.set_height(50)
rect.set_width(50)
print(rect.get_amount_inside(sq))