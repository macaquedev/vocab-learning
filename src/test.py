import random
from fractions import Fraction

def generate_equation():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    return a, b, c

def complete_the_square(a, b, c):
    h = Fraction(-b, 2*a)
    k = -Fraction(b*b,4*a)+c
    return h, k

def quiz():
    print(complete_the_square(1,2,1))
    a, b, c = generate_equation()
    print(f"Complete the square for the equation {a}x^2 + {b}x + {c} = 0")
    user_h = input("Enter the value of h (in the form 'numerator/denominator'): ")
    user_k = input("Enter the value of k (in the form 'numerator/denominator'): ")
    h, k = complete_the_square(a, b, c)
    if Fraction(user_h) == h and Fraction(user_k) == k:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is h={h}, k={k}")

if __name__ == "__main__":
    quiz()