#importing a library for random
import random
#the input is for putting characters or word using the keyboard
#assigning variable question to the input command
#answer generates the random values between 1 and 9

"""this is a multiline comment """
question=input("ask lenz a question")
answer=random.randint(1,9)
if answer==1:
    print("It is certain")#what is displayed when user enters key 1
elif answer==2:
    print("quite good")#what is displayed when user enters key or character 2
elif answer==3:
    print ("its ok")#what is displayed when user enters key or character 3
elif answer==4:
    print ("I dont know")#what is displayed when user enters key or character 4
elif answer==5:
    print ("try try again")#what is displayed when user enters key or character 5
elif answer==6:
    print("hi")#what is displayed when user enters key or character 6
elif answer==7:
    print ("your number is correct")#what is displayed when user enters key or character 7
elif answer==8:
    print("ok not yet")#what is displayed when user enters key or character 8
elif answer==9:
    print("bye for now")#what is displayed when user enters key or character 9

