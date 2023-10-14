import math  

class Rectangle:

    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'


    # >> setting new shape sizes
    def set_width(self, newWidth):
        self.width = newWidth

    def set_height(self, newHeight):
        self.height = newHeight

    # >> getting shape sizes
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height)*2

    def get_diagonal(self):
        return (math.sqrt((self.width ** 2) + (self.height ** 2)))

    def get_picture(self):
        result = ""
        if self.width > 50:
            return "Too big for picture."
        else:
            for line in range(0, self.height): 
                    result = f'{"*"*self.width}\n'*self.height
            #print (result)
            return result
                        
    def get_amount_inside(self, insertedShape):
        testShape = "testShape\n"
        for line in range(0, insertedShape.height): 
            testShape = testShape + (f'{"*"*insertedShape.width}\n')
        #print(testShape)

        ourShape = "ourShape\n"
        for line in range(0, self.height): 
            ourShape = ourShape + (f'{"*"*self.width}\n')
        #print(ourShape)

        testWidth = self.width / insertedShape.width
        testHeight = self.height / insertedShape.height
        result = testWidth * testHeight
        #print('result', math.floor(result))
        return math.floor(result)


class Square(Rectangle):
    def __init__(self, side):
        #super().__init__(width, height)
        self.side = side
        self.width = side
        self.height = side
    
    def __str__(self):
        return f'{self.__class__.__name__}(side={self.side})'
    
    def set_side(self, side):
        self.width = side
        self.height = side
        self.side = side
        return self.height * self.width

    def set_width(self, newWidth):
        self.side = newWidth

    def set_height(self, newHeight):
        self.side = newHeight



        