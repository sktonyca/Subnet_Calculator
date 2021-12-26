import ipaddress

def printResult(ip, thisNetwork):
    # Print result
    print("Information for {0} network".format(ip))
    print("{0}".format("-"*75))
    print("Network Address | Broadcast Address | Total Addresses | Usable Addresses\n{0:<15} | {1:<17} | {2:<15} | {3}\n".format(str(thisNetwork.network_address),str(thisNetwork.broadcast_address), thisNetwork.num_addresses, len(list(thisNetwork.hosts()))))
    print("Printing usable addresses")
    for host in list(thisNetwork.hosts()):
        print(host)
