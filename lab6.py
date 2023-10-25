def encoded(password):   # encoded by pavel kioutchoukov)
    encode_password = ''
    for character in password:
        number = int(character)
        encoded_number = ''
        if number >= 7:
            encoded_number = str((number+3) % 10)
        else:
            encoded_number = str((number+3))

        encode_password += encoded_number
    return encode_password

def main():

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option:"))

        if option == 1:
            password = input("Please enter your password to encode:")
            encoded_password = encoded(password)
            print("Your password has been encoded and stored!")
        #elif option == 2:
            #print("The encoded password is", encoded_password, "and the original password is", password)
        elif option == 3:
            return False

if __name__ == "__main__":
    main()