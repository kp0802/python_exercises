class Quadrilateral:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative")
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    @property
    def area(self):
        return self._height*self._width

user_height = int(input("Enter the height of the quadrilateral: "))
user_width = int(input("Enter the width of the quadrilateral: "))

quad = Quadrilateral(user_width,user_height)

print("Area of the said quadrilateral: ", quad.area)

choice = 1

while choice == 1:
    print("\nEnter \n1.To change the height of the quadrilateral \n2.To change the width of the quadrilateral")
    option = int(input("Enter your choice: "))
    if option == 1:
        new_height = int(input("\nEnter the height of the quadrilateral: "))
        quad.height = new_height
        print(f"\nPresent \nHeight = {quad.height} \nWidth = {quad.width}\n")
        print("Area of the new quadrilateral: ", quad.area)
    elif option == 2:
        new_width = int(input("\nEnter the width of the quadrilateral: "))
        quad.width = new_width
        print(f"\nPresent \nHeight = {quad.height} \nWidth = {quad.width}\n")
        print("Area of the new quadrilateral: ",quad.area)
    else:
        print("Invalid choice!!")
    choice = int(input("\nEnter 1 to continue changing the dimensions of the quadrilateral and anything else to Exit: "))
else:
    print("\nExited Successfully!!\n")



