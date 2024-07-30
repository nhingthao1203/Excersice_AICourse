import math

def is_number(n):
    try:
        float(n) 
    except ValueError:
        return False
    return True

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def elu(x):
    return x if x > 0 else math.exp(x) - 1

def calculate():
    x = int(input("Enter a number: "))
    if not is_number(x):
        print("x must be a number")
        return None
    calculate_type = input("Enter the type of calculation (sigmoid/relu/elu): ")
    if calculate_type.lower() not in ['sigmoid', 'relu', 'elu']:
        print(f"{calculate_type} is not supported!")
        return None
    if calculate_type.lower() == 'sigmoid':
        print(f"Sigmoid of {x} is {sigmoid(x)}")
    elif calculate_type.lower() == 'relu':
        print(f"ReLU of {x} is {relu(x)}")
    else:
        print(f"ELU of {x} is {elu(x)}")
        
        
if __name__ == "__main__":
    calculate()