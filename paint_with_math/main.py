from paint_with_math.canvas import Canvas
from paint_with_math.shapes import Square, Rectangle

# Get Height and Width of the canvas
canvas_height = int(input("Enter the height of canvas: "))
canvas_width = int(input("Enter the width of canvas: "))

# Getting the colour of the canvas
colors = {"white": [255, 255, 255], "black": [0, 0, 0]}
canvas_color = input("Enter your option for canvas colour (black or white): ").lower()
if canvas_color not in colors:
    print("WARNING: We did not recognize your input, Making the canvas WHITE by default!")
    canvas_color = "white"

# Creating a Canvas
canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])

# A Counter acts as condition for exiting the loop
invalid_input_counter = 0
while True:
    shape_choice = input("What do you like to draw Rectangle or Square? Enter 'quit' to stop: ")
    if shape_choice.lower() not in ['rectangle', 'square', 'quit']:
        invalid_input_counter += 1
        print("WARNING: We did not recognize your input! Try again")
        if invalid_input_counter >= 3:
            print("Too many invalid attempts! Let's quit the loop")
            break

    elif shape_choice.lower() == "rectangle":
        rec_x = int(input("Enter x for the rectangle: "))
        rec_y = int(input("Enter y for the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        print("Okay! Let's decide with the colors, Enter the values of RGB (0-255)")
        red = int(input("Red: "))
        green = int(input("Green: "))
        blue = int(input("Blue: "))

        # Create and draw rectangle
        rectangle = Rectangle(rec_x, rec_y, rec_height, rec_width, (red,green,blue))
        rectangle.draw(canvas)

    elif shape_choice.lower() == "square":
        sq_x = int(input("Enter x for the square: "))
        sq_y = int(input("Enter y for the square: "))
        sq_side = int(input("Enter the length of the side of square"))
        print("Okay! Let's decide with the colors, Enter the values of RGB (0-255)")
        red = int(input("Red: "))
        green = int(input("Green: "))
        blue = int(input("Blue: "))

        # Create and draw rectangle
        square = Square(sq_x, sq_y, sq_side, (red, green, blue))
        square.draw(canvas)

    elif shape_choice.lower() == 'quit':
        break


print("Creating Canvas for your input ... ")
canvas.create("canvas.png")
