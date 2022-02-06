from checkSubnet import checkSubnet
from printResult import printResult

# Check subnet
while True:
    user_Input = checkSubnet()
    printResult(user_Input[0], user_Input[1])
    while True:
        # Ask if continue
        if (input("Do you want to continue? Y for yes, N for No\n").upper()== "N"):
            exit()
        else:
            print("Invalid Input")