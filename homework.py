octet = int(input("Enter the Last octet of the IP Address:"))
last_octet = [octet]


def ip_to_operating_system(octet):
    for num in last_octet:
        if num % 2 == 0 and num != 0:
            print("Windows")
        elif num % 2 != 0:
            print("Linux")
        elif num == 0:
            print('Router')


ip_to_operating_system(octet)
