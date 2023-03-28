from dns import resolver

def input_values_dns():
    dns = input("DNS: ")
    typeData = input("TYPE: ")
    return dns, typeData

def read_file(path):
    with open(path, "r") as file:
        return file.read().splitlines()


def discovery_dns_ip():
    dns, type = input_values_dns()
    subdomains = read_file(input("PATH: "))
    for sub in subdomains:
        try:
            target = f"{sub}.{dns}"
            res = resolver.resolve(target, type)
            for value in res:
                print(f"\n SUBDOMAIN: {sub} \n DNS: {dns} \n IP: {value} \n \n PROCESSING....")

                
        except Exception as e:
            print(f"processing error: {e}")
    print("\n \n PROCESSING FINISHED!")



