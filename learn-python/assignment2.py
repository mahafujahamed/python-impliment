def calculate_area(radius = 1, length = 1, width = 1):
    print("Enter your shape: ")
    print("1 for Circle")
    print("2 for Rectangle")
    print("3 for Triangle")
    shape = int(input("Enter your shape: "))

    if shape == 1:
        radius = float(input("Enter the radius of the circle: "))
    elif shape == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
    elif shape == 3:
        length = float(input("Enter the length of the triangle: "))
        width = float(input("Enter the width of the triangle: "))

    area_of_circle = 3.14 * radius * radius
    area_of_rectangle = length * width
    area_of_triangle = 0.5 * length * width
    
    if shape == 1:
        print("The area of the circle is: ", area_of_circle)
    elif shape == 2:
        print("The area of the rectangle is: ", area_of_rectangle)
    elif shape == 3:
        print("The area of the triangle is: ", area_of_triangle)

calculate_area()