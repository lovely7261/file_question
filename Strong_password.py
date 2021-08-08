 

alphabet=input("enter the alphabet")
specail_char=(input("enter the specail_char"))
numbers=(input("enter the numbers"))
if alphabet =="A" or "Z":
     print(alphabet+specail_char+numbers)
elif specail_char =="@" or "*" or "#" or "$" or "&":
    print(alphabet+specail_char+numbers)
elif numbers >"1" or numbers<"99":
     print(alphabet+specail_char+numbers)
else:
     print("incorect password")
    