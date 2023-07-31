





def compound():
    p = float(input("What is your starting amount\n"))
    r = float(input("What is your rate (in decimal)\n"))
    n = float(input("What is the number of compounds per year\n"))
    t = float(input("What is the number of years you are investing\n"))

    output = (p*(1+r/n)**n*t)
    outputInt = int(output - .5)
    
    print("Your total after "+ str(t)+" years is about $"+ str(outputInt))


def simple():
    p = float(input("What is your starting amount\n"))
    r = float(input("What is your rate (in decimal)\n"))
    
    t = float(input("What is the number of years you are investing\n"))

    output = (p*(1+r*t))
    outputInt = int(output - .5)
    
    print("Your total after "+ str(t)+" years is about $"+ str(outputInt))


def tip():
    p = float(input("What is your starting amount\n"))
    r = float(input("What percentage would you like to tip\n"))
    output = int(p*(r/100))
    print("To tip " +str(r)+ "% you will have to tip $"+str(output))


def binary():
    global carry
    carry = False
    first = input("Input your first binary number: ")
    second = input("Input your second binary number: ")
    total = []

    def add(digit1, digit2):
        global carry
        if(digit1 == '1' and digit2 == '1' and carry == False ):
            total.append( '0')
            carry = True
            print('1')
        elif(digit1 == '1' and digit2 == '1' and carry == True):
            total.append( '1')
            carry = True
            print('2')
        elif(digit1 == '0' and digit2 == '1' and carry == False):
            total.append( '1')
            print('3')
        elif(digit1 == '0' and digit2 == '1' and carry == True):
            total.append( '0')
            carry = True
            print('4')
        elif(digit1 == '1' and digit2 == '0' and carry == False):
            total.append( '1')       
            print('5')
        elif(digit2 == '1' and digit1 == '0' and carry == False):
            total.append( '1')
            print('6')
        elif(digit1 == '1' and digit2 == '0' and carry == True):
            total.append( '0')
            carry = True
            print('7')
        elif(digit2 == '1' and digit1 == '0' and carry == True):
            total.append( '1')
            carry = True
            print('8')
        elif(digit1 == '0' and digit2 == '0' and carry == False):
            total.append( '0')     
            print('9')
        elif(digit2 == '0' and digit1 == '0' and carry == False):
            total.append( '0')
            print('10')
        elif(digit1 == '0' and digit2 == '0' and carry == True):
            total.append( '1')
            carry = False
            print('11')
        elif(digit2 == '0' and digit1 == '0' and carry == True):
            total.append('1')
            carry = False
            print('12')
        
    def split(word, word2):
        word = [char for char in word]
        word2 = [char for char in word2]

        if len(word) > len(word2):
            while len(word) > len(word2):
                word2.insert(0, "0")
        elif len(word2) > len(word):
            while len(word2) > len(word):
                word.insert(0, "0")
        for i in range(len(word) -1,-1,-1):
           
            add(word[i], word2[i])
        
    split(first, second)
    if carry == True:
        total.append('1')
        print("carried")
        carry = False
    def binaryToDecimal(binary):
        decimals = []
        place = 0
        finalInt = 0
        for i in range(len(binary)):
            
            tempInt = int(binary[0]) * (2**place)
            binary.pop(0)
            decimals.append(tempInt)
            place = place +1 
            
        for number in decimals:
            finalInt = finalInt + number
        return(finalInt)
        


        
    
    totalJoined = ''.join(total)
    totalReversed = totalJoined[::-1] #reverse the output because it appends backwards
    print("Binary Addition:",totalReversed, "Carry = "+ str(carry),"\n")
    print(totalReversed, "is equal to:",binaryToDecimal(total),"\n")

    
        
    









def main():
    #Global carry

    print("Welcome to your personal calculator!!!!!!!")

    print("Options:")
    print("Compound Interest Calculator == a")
    print("Simple Interes Calculator == b")
    print("Tip Calculator == c")
    print("Binary Calculator == d")
    print("Quit == q")
    
    user_input = input("Enter something: ")

    while(user_input != "q"):

        if (user_input == 'a'):
            compound()
            pass
        elif(user_input == 'b'):
            simple()
            pass
        elif(user_input == 'c'):
            tip()
            pass
        elif(user_input == 'd'):
            binary()
            pass
        elif (user_input == 'q'):
            break
        else:
            print("that was not an option")

        print("Options:")
        print("Compound Interest Calculator == a")
        print("Simple Interes Calculator == b")
        print("Tip Calculator == c")
        print("Binary Calculator == d")
        print("Quit == q")

        user_input = input("Enter something: ")

    print("we are done now")
    
main()













































