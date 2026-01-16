class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    def set_width(self,new_width):
        self._width=new_width
    def set_height(self,new_height):
        self._height=new_height
    def get_area(self):
        return (self._width*self._height)
    def get_perimeter(self):
        return 2*(self._width+self._height)
    def get_picture(self):
        if self._width>50 or self._height>50:
            return "Too big for picture."
        result=""
        result1="*"*(self._width)
        for _ in range(self._height):
            result+=result1+"\n"
        return result
    def get_diagonal(self):
        return ((self._width)**2+(self._height)**2)**(0.5)
    def get_amount_inside(self,obj):
        return (self._width // obj._width) * (self._height // obj._height)
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    def set_width(self,new_width):
        self._width=new_width
        self._height=new_width
    def set_height(self,new_height):
        self._height=new_height
        self._width=new_height
    def set_side(self,new_side):
        self._height=new_side
        self._width=new_side
    def __str__(self):
        return f"Square(side={self._width})"
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))