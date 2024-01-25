container = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
             "n","o","p","q","r","s","t","u","v","w","x","y","z",]
doUcont = "yes"
while(doUcont=="yes"):
    msg = input("type your message: ").lower()
    shift = int(input("enter shift: "))
    def encrypt(msg):
        temp = []
        for i in  msg:
            jump = container.index(i) + shift
            if jump >= 26:
                jump = jump - 26
            temp.append(container[jump])
        result = ("").join(temp)
        return result
    enc = encrypt(msg)
    def decrypt():
        temp = []
        for i in  enc:
            jumpBack = container.index(i) - shift
            if jumpBack < 0:
                jumpBack = 26 + jumpBack
            temp.append(container[jumpBack])
        result = ("").join(temp)
        return result
    print (f"\nencryption {enc}\ndecryption {decrypt()}\n\n")
    doUcont = "yes" if input("do u want to continue(yes or other-key): ").lower() == "yes" else "no"