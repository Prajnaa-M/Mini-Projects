#---------------------------------------strings------------------------------------
name="ha"
age=str(19)
print(name+" is my name and my age is "+age)    #concatenation
print(''' beau

 is
                                                 
 39

 years old''')                                   #multiline string


# LEN() FUNCTION
name="PRAJNAA"
print(len(name))
print("aa" in name.lower())


#functions for strings
#these return a brand new string and does not alter the original
print("BEAU".lower())                     
print("beau".upper())
print("beAU".title())
print("beAU".islower())
print("BEAU".isupper())
print(" b e a u ".isalpha())
print("B e3tg".isalnum())
print("1234".isdecimal())
print("Prajnaa".lower().startswith("praj"))
print("prajna".endswith("naa"))
print("hello world".replace("world", "Python"))
print("ahahahahahhhah".split("a"))
print("   hel ooo   ".strip())
print("---hellooo---".strip("-"))
print("   hel ooo   ".strip(" "))  #same as strip()
words = ["I", "love", "Python"]
print(" ".join(words))
text = "programming"
print(text.find("gram"))
print(text.find("xyz"))
print("    hellooo   ".lstrip())
print("    hellooo   ".rstrip())


#what if string contains "/ ' then "be"au" is invalid
print("be\"au")  #is valid
print("be\au")   #\ will remove 'a'
print("be\\au")  #if we need a \ in our atring


#slicing
a="hdafggfkdfg"
print(a[3])
#print(a[30]) INDEX ERROR!!! 
print(a[:30])
print(a[5:7])
