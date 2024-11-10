import cmath  

def solve_quadratic(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    
    
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return root1, root2
print("Quadratic Equation Solver for ax^2 + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:

    print("This is not a quadratic equation (a should not be 0).")
else:
    
    roots = solve_quadratic(a, b, c)
    print(f"The roots are: {roots[0]} and {roots[1]}")
