#Start up
print("""
$$$$$$__ $$____$$_ __$$$$$___ __$$$___ _$$$$$__ $$$$_ __$$$$_
$$___$$_ _$$__$$__ __$$__$$__ _$$_$$__ $$___$$_ _$$__ _$$____
$$___$$_ __$$$$___ __$$$$$___ $$___$$_ _$$$____ _$$__ $$_____
$$$$$$__ ___$$____ __$$___$$_ $$$$$$$_ ___$$$__ _$$__ $$_____
$$______ ___$$____ __$$___$$_ $$___$$_ $$___$$_ _$$__ _$$____
$$______ ___$$____ __$$$$$$__ $$___$$_ _$$$$$__ $$$$_ __$$$$_                                                                          
v0.1                                                                             
""")
file_name = input("File Name/>: ")

#var set
cache = {}
count = 0
cache_ins = ""
cache_str = ""
a = 0
cache_bol = True
#file read


# file to chache
with open(file_name+".txt", "r") as fp:
    Lines = fp.readlines()
    for line in Lines:
        count += 1
        cache[count] = line.strip()

#reset count
count = 0
# excute
while count <= int(len(cache)-1):
        
        count += 1
        
        item = cache[count]
        # print str
        if item == "print":
            cache_ins = "print"
        # print var
        elif item == "printvar.a":
            cache_ins = "printvar.a"
        # goto line
        elif item == "goto":
            cache_ins = "goto"
        # + var a
        elif item == "var+.a":
            cache_ins = "var+.a"



        # print s str
        elif cache_ins == "print":
            print(item)
            cache_ins = ""
         # print s str
        elif cache_ins == "printvar.a":
            if item == "Null/Data" :
                print(str(a))
                cache_ins = ""
            else:
                print(str(a), item)
                cache_ins = ""
        # add # to a
        elif cache_ins == "var+.a":
            a += int(item)
            cache_ins = ""
        # go to line
        elif cache_ins == "goto":
            count = int(item)-1
            cache_ins = ""
        else:
            print("Unable to use code")
        
