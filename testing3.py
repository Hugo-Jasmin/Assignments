# while (True):
#     userinpput = int(input("""
#         selamat datang:
#         1. Tambah
#         2. Hapus
#         3. Keranjang
#         4. Checkout
#         5. Exit \n"""))
#     if userinpput == 1:
#         print("barang sudah ditambahkan")
#         continue
#     elif userinpput == 2:
#         print("barang telah dihapus")
#         continue
#     elif userinpput == 3:
#         print("ini keranjang anda")
#         continue
#     elif userinpput == 4:
#         print("ini chekout")
#         continue
#     elif userinpput == 5:
#         print("terima kasih sudah belanja")
#         break


# for i in range(1, 10):
#     print(str(i)*i)

while True:
    password = input("what is your password? ")
    letters = []
    for char in password:
        letters.append(char)
    lowercase = False
    for letter in letters:
        if letter.isalpha():
            lowercase = True
    if lowercase == True:
        uppercase = False
        for letter in letters:
            if letter.isupper():
                uppercase = True
        if uppercase == True:
            hasNumberic = False
            for letter in letters:
                if letter.isnumeric():
                    hasNumberic = True
            if hasNumberic == True:
                hasspecial = False
                specialcases = '[@_!#$%^&*()<>?/}{~:]'
                for letter in letters:
                    for specials in specialcases:
                        if letter == specials:
                            hasspecial = True
                if hasspecial == True:
                    lowerLenCheck = False
                    if len(password) >= 6:
                        lowerLenCheck = True
                    if lowerLenCheck == True:
                        upperLenCheck = False
                        if len(password) < 17:
                            upperLenCheck = True
                        if upperLenCheck == True:   
                            print("congrats!")
                            break
                        else:
                            print("need to be shorted than 17 characters, too long")
                            continue
                    else:
                        print("need to be at least 6 characters long")
                        continue
                else:
                    print("need a special")
                    continue
            else:
                print("need a digit")
                continue
        else:
            print("need an uppercase")
            continue
    else:
        print("need a lowercase character")
        continue 