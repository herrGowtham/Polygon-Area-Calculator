class Rectangle(object):

  def __init__(self,width = 0,height = 0):
    self.width = width
    self.height = height

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return (self.height*self.width)

  def get_perimeter(self):
    return ((2*self.height) + (2*self.width))

  def get_diagonal(self):
    return (((self.width**2) + (self.height**2))**0.5)

  def get_picture(self):
    list_1 = []
    if self.width > 50 or self.height > 50:
      return f"Too big for picture."

    else:
      for i in range(0,self.height):
          for j in range(0,self.width):
            list_1.append("*")
          list_1.append("\n")
      return (''.join(list_1))  
  
  def get_amount_inside(self,shape):
    self.shape = shape
    self.shape_area = shape.get_area()

    return (int((self.height*self.width)/self.shape_area))

   #if self.shape == "sq":
      
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

  def __init__(self,side_length):
    self.height = side_length
    self.width = side_length

  def set_side(self,side_length):
    self.height = side_length
    self.width = side_length

  def __str__(self):
    return f"Square(side={self.width})"
