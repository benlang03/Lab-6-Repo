"""Benjamin Lang - Encoder/Github Lab"""

# takes in password and returns the encoded version
def encode(password):
    pList = list(password)
    pList = [int(j) for j in pList]
    pList = [(i + 3) % 10 for i in pList]
    #for i in range(len(pList)):
        #pList[i] = (pList[i] + 3) % 10
    pList = [str(k) for k in pList]
    code = "".join(pList)
    return code

def decode(password):
    decoder = ''
    password_str = str(password)
    for i in range(len(password_str)):
        decoder += str(((int(password_str[i]) + 10) - 3) % 10)
    return decoder

# displays menu
def displayMenu():
    print('Menu')
    print('-' * 13)
    print('1. Encode'
          '\n2. Decode'
          '\n3. Quit')

# main method
def main():
    userChoice = 1
    while 0 < userChoice < 3:
        displayMenu()
        print()
        userChoice = int(input("Please enter an option: "))
        if userChoice == 1:
            password = input("Please enter your password to encode: ")
            code = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif userChoice == 2:
            password = decode(code)
            print(f"The encoded password is {code}, and the original password is {password}.")

if __name__ == '__main__':
    main()
