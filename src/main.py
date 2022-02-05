from checkSubnet import checkSubnet
from printResult import printResult

# Check subnet
while True:
    user_Input = checkSubnet()
    printResult(user_Input[0], user_Input[1])
    if (input("Do you want to continue? Y for yes, N for No\n").upper()== "N"):
        break


