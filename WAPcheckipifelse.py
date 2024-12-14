ip_address = int(input("Enter Your IP Address Without point > "))

if ip_address == 127001:
    print(f"{ip_address} is Loopback Address ")
elif ip_address == 0000:
    print(f"{ip_address} is not Valid IP Address ")
elif ip_address < 255255255255255:    
    print(f"{ip_address} is not Valid IP Address ")
else:
    print(f"{ip_address} is a Valid IP Address ")    
