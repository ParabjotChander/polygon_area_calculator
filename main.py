import math

class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return math.sqrt((self.width*self.width) + (self.height*self.height))

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""

        for i in range(self.height):
                picture += ("*"*self.width)+"\n"
        
        return picture 
    
    def get_amount_inside(self, shape):
        fit_width = self.width // shape.width
        fit_height = self.height // shape.height
        return fit_height * fit_width

class Square(Rectangle):
    
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length
    
    def __str__(self):
        return f"Square(side={self.side_length})"
    
    def set_width(self, new_width):
        self.side_length = new_width

    def set_height(self, new_height):
        self.side_length = new_height 
    
    def set_side(self, side_length):
        self.side_length = side_length
    
    def get_picture(self):
        if self.side_length > 50:
            return "Too big for picture."
        
        picture = ""

        for i in range(self.side_length):
                picture += ("*"*self.side_length)+"\n"
        
        return picture 

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.height = 3
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.height = 8
    rect.width = 16
    print(rect.get_amount_inside(sq))

    print(Rectangle(15,10).get_amount_inside(Square(5)))
    print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))
    print(Rectangle(2,3).get_amount_inside(Rectangle(3, 6)))


