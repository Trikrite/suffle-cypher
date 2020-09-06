#A PROGRAM NEM SZERETI A SPACE!!!

def split(word):
    return [char for char in word]
fasz = ""
anyad = []
ass = split(input())
i = 0
def minusencrypt(text, s):
    result = ""



# transverse the plain text
    for i in range(len(ass)):
        char = ass[i2]
        # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
     # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result
# check the above function
text = ass[i]
s = -6

def plusencrypt(text, s):
    result = ""


# transverse the plain text
    for i in range(len(ass)):
        char = ass[i2]
        # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
     # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result
# check the above function
text = ass[i]
s = 6

code = input("kód(+-)")
listcode = split(code)
for i in range(len(ass)):
    i2 = i
    text = ass[i]
    if listcode[i]=="-":
        anyad.append(minusencrypt(ass[i],-6))
    elif listcode[i]=="+":
        anyad.append(plusencrypt(ass[i],6))
    else:
        exit()
for i in range(len(anyad)):
    lofasz = anyad[i]
    nyomorek = lofasz[0]
    fasz = fasz+nyomorek

print(fasz)