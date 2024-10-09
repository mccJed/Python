from math_operations import calculator

result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result:", result)

from math_operations import geometry

def main():
    #rectangle
    length = 16
    width = 4
    rectangle_area = geometry.area_of_rectangle(length, width)
    print(f"Area of the rectangle: {rectangle_area}")
    
    #triangle
    base = 2
    height = 7
    triangle_area = geometry.area_of_triangle(base, height)
    print(f"Area of the triangle: {triangle_area}")
    
    #circle
    radius = 8
    circle_area = geometry.area_of_circle(radius)
    print(f"Area of the circle: {circle_area}")

if __name__ == "__main__":
    main()
