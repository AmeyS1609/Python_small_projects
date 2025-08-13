def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid+1
            else:
                high = mid-1

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root
print("Choice 1:Calculate approx square root of a number")
print("Choice 2:Exit")
def main(i):
    try:
        N=int(input("Enter a number:"))
        T=float(input("Enter tolerence:"))
        M=int(input("Enter max iterations:"))
        square_root_bisection(N,T,M)
    except Exception:
        print("Enter valid Integer")
        return main(i)
def error():
    try:
        i=int(input("Enter a choice:"))
        return i
    except Exception:
        print("INVALID!! Enter valid choice")
        return error()
while True:
    s=error()
    if s==1:
        main(s)
    elif s==2:
        break
    else:
        print("Choice not available")

