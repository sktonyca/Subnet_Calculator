import ipaddress

def checkSubnet():
    # Get IP address input
    while True:
        try:
            # Check if valid input
            get_Input = input("Please enter the IPv4 address with its subnet\nExample: 192.168.0.0/28\n")
            myip = ipaddress.IPv4Network(get_Input)
            break
        except ValueError:
            print("Input is invalid")
        except ipaddress.AddressValueError:
            print("The ip address is invalid")
        except ipaddress.NetmaskValueError:
            print("The subnet mask is invalid")
    return get_Input,myip