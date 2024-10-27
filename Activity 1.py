string=input("Please Enter Your String: ")
cha=input("Please Enter Your Own Character: ")
index_position=0
count=0
while index_position<len(string):
    if string[index_position]==cha:
        count=count+1
    index_position=index_position+1
print("Total Number Of Times The Character Has Occurred Is",count)