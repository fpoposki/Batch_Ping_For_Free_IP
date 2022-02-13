import os

'''last segment of IP address'''
ip_last = 1 

'''list of free IP addresses found'''
free_ip_list = []

'''Enter IP range of interes 192.168.xxx.(0-255).'''
while True:
    try:
        ip_range = int(input("\n Please enter IP range "))
        if  ip_range <= 255 and ip_range >= 0:
            print("You entered a valid range")
        else:
            print("INVALID RANGE")
            ip_range = int(input("\n Please enter IP range "))
    except:
        print("Please enter a valid number")
    else:
        break
    
'''How many ip adresses do you want need'''   

while True:
    try:
        ip_count = int(input("\n How many free adresses do you need "))
        while  ip_count >= 255 or ip_count =< 0:
            print("INVALID ENTRY (enter number between 0-255)")
            ip_count = int(input("\n INVALID ENTRY. PLEASE TRY AGAIN "))     
    except:
         print("Please enter a valid number (0-255)")
    else:
        break


print("Pinging all IP adresses in 192.168."+ str(ip_range) + ".(0-255)")
    
while ip_last <= 255 and ip_count > 0:
    
    return1 = os.system("ping -n 1 -w 10  192.168."+ str(ip_range) + "." +str(ip_last)+"\n")

    if return1:
        free_ip_list.append(ip_last)
        ip_count-=1
    else:
        pass

    ip_last+=1


        
print("Free IP LIST:")

for x in range(len(free_ip_list)):
    print("192.168."+ str(ip_range) + "." + str(free_ip_list[x]))
    
    
os.system("pause")
