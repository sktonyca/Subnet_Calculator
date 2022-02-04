import ipaddress

def printResult(ip, thisNetwork):
    # Print result
    print("Information for {0} network".format(ip))
    print("{0}".format("-"*75))
    print("Network Address | Broadcast Address | Total Addresses | Usable Addresses\n{0:<15} | {1:<17} | {2:<15} | {3}\n".format(str(thisNetwork.network_address),str(thisNetwork.broadcast_address), thisNetwork.num_addresses, len(list(thisNetwork.hosts()))))
    if (len(list(thisNetwork.hosts()))>5):
        print("Printing first 5 usable addresses")
    for count, host in enumerate(list(thisNetwork.hosts())):
        if count <5:
            print(host)
