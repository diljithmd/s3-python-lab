def puzz(heads, legs):
    if legs % 2 != 0:
        print("No solution: number of legs must be even.")
        return
    rabbit = (legs - 2 * heads) // 2
    chicken = heads - rabbit
    if rabbit < 0 or chicken < 0 or 2*heads > legs or 4*heads < legs:
        print("No solution with given heads and legs.")
    else:
        print(f"Number of chickens: {chicken}")
        print(f"Number of rabbits: {rabbit}")
try:
    h = int(input("Enter the number of heads: "))
    l = int(input("Enter the number of legs: "))
    puzz(h, l)
except ValueError:
    print("Please enter valid integers for heads and legs.")
