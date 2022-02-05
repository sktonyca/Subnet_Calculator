import ipaddress

def printResult(ip, thisNetwork):
    # Print result
    print("Information for {0} network".format(ip))
    print("{0}".format("-"*105))
    print("Network Address | Broadcast Address | Total Addresses | Usable Addresses | First Address | Last Address \n{0:<15} | {1:<17} | {2:<15} | {3:<16} | {4:<13} | {5}\n".format(str(thisNetwork.network_address),str(thisNetwork.broadcast_address), thisNetwork.num_addresses, len(list(thisNetwork.hosts())),str(list(thisNetwork.hosts())[0]),str(list(thisNetwork.hosts())[-1])),end="")

    
    
