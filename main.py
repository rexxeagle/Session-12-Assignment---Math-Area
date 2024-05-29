from area import circle, square, triangle
from volume import ball, cubic, trapezoid

print("Welcome to the program!")
def menu():
    print("Here's the available menu:")
    print("1. Circle Area")
    print("2. Square Area")
    print("3. Triangle Area")
    print("4. Ball Volume")
    print("5. Cube Volume")
    print("6. Trapezoid Volume")
    print("7. Exit")
    print()
    menus = range(1, 8)
    decision = int(input("Choose the number of the menu: "))

    if decision not in menus:
        print("Invalid menu")
        is_repeat_program()
    else:
        if decision == 1:
            print("You choose Circle Area")
            radius = float(input("Enter the radius: "))
            result = circle.circle_area(radius)
            print(f"The area of the circle is {result}")
            is_repeat_program()
        elif decision == 2:
            print("You choose Square Area")
            side_length = float(input("Enter the side length: "))
            result = square.square_area(side_length)
            print(f"The area of the square is {result}")
            is_repeat_program()
        elif decision == 3:
            print("You choose Triangle Area")
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            result = triangle.triangle_area(base, height)
            print(f"The area of the triangle is {result}")
            is_repeat_program()
        elif decision == 4:
            print("You choose Ball Volume")
            radius = float(input("Enter the radius: "))
            result = round(ball.ball_volume(radius), 2)
            print(f"The volume of the ball is {result}")
            is_repeat_program()
        elif decision == 5:
            print("You choose Cube Volume")
            side_length = float(input("Enter the side length: "))
            result = cubic.cubic_volume(side_length)
            print(f"The volume of the cube is {result}")
            is_repeat_program()
        elif decision == 6:
            print("You choose Trapezoid Volume")
            base1 = float(input("Enter the first base: "))
            base2 = float(input("Enter the second base: "))
            height = float(input("Enter the height: "))
            result = trapezoid.trapezoid_volume(base1, base2, height)
            print(f"The volume of the trapezoid is {result}")
            is_repeat_program()
        elif decision == 7:
            print("Thank you for using this program!")
            exit()

def is_repeat_program():
    print()
    repeat = input("Do you want to repeat the program? (y/n) ")
    if repeat == "y":
        menu()
    elif repeat == "n":
        print("Thank you for using this program!")
        exit()
    else:
        print("Invalid input. Please input 'y' or 'n'")
        is_repeat_program()

menu()