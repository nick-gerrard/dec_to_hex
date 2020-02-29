conversion_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "A", "B", "C", "D", "E", "F"]
reversed_list = []
def dec_to_hex(decimal):
    global reversed_list
    hex_list = []
    if decimal < 0:
        print("We don/'t do negatives...")
        return(None)
    else:
        num = decimal // 16
        rem = decimal % 16
        reversed_list.append(rem)
        if num > 0:
            dec_to_hex(num)
        else:
            for i in range(len(reversed_list)):
                index = reversed_list.pop()
                hex_list.append(conversion_list[index])
            #print(hex_list)
            string_version = ''.join(hex_list)
            print(string_version)
            return string_version

        
def dec_to_bin(decimal):
    global reversed_list
    bin_list = []
    if decimal < 0:
        print("We don/'t do negatives...")
        return None
    else:
        num = decimal // 2
        rem = decimal % 2
        reversed_list.append(rem)
    if num > 0:
        dec_to_bin(num)
    else:
        for i in range(len(reversed_list)):
            index = reversed_list.pop()
            bin_list.append(str(index))
            #print(hex_list)
        string_version = ''.join(bin_list)
        print(string_version)
        return string_version
        

def bin_to_dec(binary):
    total = 0
    exponent_value = 0
    string_bin = str(binary)
    reversed_string_bin = string_bin[::-1]        
    for num in reversed_string_bin:
        if num == "1":
            total += 2 ** exponent_value
        exponent_value += 1
    print(total)
    return total

def hex_to_dec(hexadecimal):
    converted_list = []
    for num in hexadecimal:
        for char in conversion_list:
            if num == char:
                converted_list.append(conversion_list.index(char))
    total = 0
    exponent_value = 0
    converted_list.reverse()
    #print(converted_list)
    for num in converted_list:
        total += num * 16 ** exponent_value
        exponent_value += 1
    print(total)
    return(total)
                
        

def hex_to_bin(hexadecimal):
    dec_to_bin(hex_to_dec(hexadecimal))

def bin_to_hex(binary):
    dec_to_hex(bin_to_dec(binary))

        
#input logic        
cont =True
while cont:
    selection = input("Select you Function ")
    if selection == "hex to dec":
        value = input("Value? ")
        hex_to_dec(str(value))
    elif selection == "dec to hex":
        value = input("Value? ")
        dec_to_hex(int(value))
    elif selection == "dec to bin":
        value = input("Value? ")
        dec_to_bin(int(value))
    elif selection == "bin to dec":
        value = input("Value? ")
        bin_to_dec(int(value))
    elif selection == "hex to bin":
        value = input("Value? ")
        hex_to_bin(str(value).upper())
    elif selection == "bin to hex":
        value = input("Value? ")
        bin_to_hex(int(value))
    else:
        print("Invalid Selection...")
    question = input("Do you need another number converted? y/n? ")
    if question == "n":
        cont = False
    else:
        cont = True


#hex_to_bin("FF")
#bin_to_hex(11111111)

#hex_to_dec("FF23B")
#dec_to_bin(192)
#dec_to_bin(168)
#dec_to_bin(4)
#dec_to_bin(1)


#bin_to_dec(100101111110010111111111110001010101011111)
