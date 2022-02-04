import ipaddress

def checkSubnet():
    # Get IP address input
    while True:
        try:
            # Check if valid input
            get_Input = input("Please enter the IPv4 address with its subnet\nExample: 192.168.0.0/28\n")
            myip = ipaddress.IPv4Network(get_Input)
            break
        except ipaddress.AddressValueError: # If ip address is invalid
            print("The ip address is invalid")
        except ipaddress.NetmaskValueError: # If subnet mask is invalid
            print("The subnet mask is invalid")
        except ValueError: # If the input is invalid
            print("Input is invalid")
    return get_Input,myip