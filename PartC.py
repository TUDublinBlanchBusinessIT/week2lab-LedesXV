#Part C
#Ledes Ajuonoma B00164804
#10/02/2025
#A Program to Print Steps 1 to 10 to the Screen

def printSteps(a, b):
    for i in range(a, b +1):
        print(f"Step {i}")


def main():
    a = int(input("Insert first step "))
    b = int(input("Insert last step "))
    printSteps(a, b)




main()