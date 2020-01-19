import glob
import os
grab = ""

for file in glob.glob("*.txt"):
    with open(file, "r") as data:
        arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        arr2 = ['^',';','<','>','*','?','_','-','(',')','%','.',':','!','@','#','$','+','&','/','=',',','0','9','8','7']

        lines = sum(1 for line in open(file))      
        for pos in range(0,lines):
            hold = data.readline()
            for x in range(len(hold)):  
                print("Encrypting .TXT File: " + os.path.splitext(file)[0] + os.path.splitext(file)[1])   
                
                if x == " ": 
                    grab += "\\"
                else:
                    for g in range(25):               
                        if hold[x] == arr[g]:
                            grab += arr2[g]

            print("grabbed: " + grab)
            grab += "\n"
    
    meme = open(file, "w")
    meme.write(grab)
    meme.close()
    