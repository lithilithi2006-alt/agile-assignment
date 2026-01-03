

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = int(input("Enter choice: "))
    temp = float(input("Enter temperature: "))
    
    if choice == 1:
        print("Result:", c_to_f(temp), "F")
    elif choice == 2:
        print("Result:", f_to_c(temp), "C")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()