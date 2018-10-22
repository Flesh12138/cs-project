#made by DavidQi 5115 to test the memory of people
#this program is a trial version that can be used if David can't finish the fancy version
#For some reason QTimer don't work on David's computer , if you know a way, please add a timer
import random
def mem():
    difficulitie = input("input difficulitie")
    if difficulitie == "6": #these shou have buttons
        char2 = chr(random.randint(33,126)) #in acsii, only 33 to 126 are useable chararacters
        char1 = chr(random.randint(33,126))
        array = [char1,char1,char1,char2,char2,char2]
        random.shuffle(array)
        print("".join(array))
    elif difficulitie == "7.635":
        char2 = chr(random.randint(33,126))
        char1 = chr(random.randint(33,126))
        array = [char1,char1,char1,char2,char2,char2,char2,char2]
        random.shuffle(array)
        print("".join(array))
    elif difficulitie == "8":
        char2 = chr(random.randint(33,126))
        char1 = chr(random.randint(33,126))
        array = [char1,char1,char1,char1,char2,char2,char2,char2]
        random.shuffle(array)
        print("".join(array))
    elif difficulitie == "9.7":
        char2 = chr(random.randint(33,126))
        char1 = chr(random.randint(33,126))
        array = [char1,char1,char1,char1,char2,char2,char2,char2,char2,char2]
        random.shuffle(array)
        print("".join(array))
    elif difficulitie == "19":
        char2 = chr(random.randint(33,126))
        char3 = chr(random.randint(33,126))
        char1 = chr(random.randint(33,126))
        array = [char1,char1,char1,char1,char2,char2,char2,char2,char3,char3,char3,char3]
        random.shuffle(array)
        print("".join(array))
    elif difficulitie == "29.8":
        char2 = chr(random.randint(1,100))
        char3 = chr(random.randint(1,100))
        char4 = chr(random.randint(1,100))
        char1 = chr(random.randint(1,100))
        array = [char1,char1,char1,char1,char2,char2,char2,char2,char3,char3,char3,char3,char4,char4,char4,char4]
        random.shuffle(array)
        print("".join(array))
    elif difficulitie == "29.8":
        char2 = chr(random.randint(33,126))
        char3 = chr(random.randint(33,126))
        char4 = chr(random.randint(33,126))
        char1 = chr(random.randint(33,126))
        array = [char1,char1,char1,char1,char2,char2,char2,char2,char3,char3,char3,char3,char4,char4,char4,char4]
        random.shuffle(array)
        print("".join(array))
    elif difficulitie == "48":
        char2 = chr(random.randint(33,126))
        char3 = chr(random.randint(33,126))
        char4 = chr(random.randint(33,126))
        char1 = chr(random.randint(33,126))
        char5 = chr(random.randint(33,126))
        char6 = chr(random.randint(33,126))
        char8 = chr(random.randint(33,126))
        char7 = chr(random.randint(33,126))
        array = [char1,char1,char2,char2,char3,char3,char3,char4,char4,char5,char5,char6,char6,char7,char7,char8,char8]
        random.shuffle(array)
        print("".join(array))
    elif difficulitie == "UltimateChallenge":
        array = []
        for i in range(100):
            array.append(chr(random.randint(33,126)))
        random.shuffle(array)
        print("".join(array))
    question = "".join(array)
    answer = input("input the array you see") #make the string dissappear first
    if question == answer :
        print("corrrect")
    else:
        print("wrong")
    


mem()
