import sympy as sp

# Define the input equation as a string
equation_str = input("Enter an equation (e.g., '3*x + 2 = 7'): ")

# Define a symbolic variable
x = sp.symbols('x')

try:
    # Split the input into left and right sides using the equal sign
    sides = equation_str.split('=')

    if len(sides) == 2:
        left_side = sp.sympify(sides[0].strip())  # Parse and clean the left side
        right_side = sp.sympify(sides[1].strip())  # Parse and clean the right side

        equation = sp.Eq(left_side, right_side) # Insert equation sides as params

        solutions = sp.solve(equation, x)
        if solutions:
            print("Solutions for x:", solutions)
    else:
        print("No solutions found for x in this equation.")

except sp.SympifyError:
    print("Invalid input. Please enter a valid equation.")