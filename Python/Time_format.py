"""WAP to convert time for 12-hour to 24-hour format!!"""
def convert_time(str1):
    if str1[-2:] == "AM" and str1[:2]=="12":
        return "00" + str1[2:-2]
    elif str1[-2:] =="AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2]=="12":
        return str1[:-2]
    else:
        return (str((int(str1[:2])+12))+str1[2:8])
    
print(convert_time("01:05:45AM"))
