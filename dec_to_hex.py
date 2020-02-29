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
        
        
#input logic        
"""cont =True
while cont:
    dec_num = input("What decimal do you need converted? ")
    dec_to_hex(int(dec_num))
    question = input("Do you need another number converted? ")
    if question == "n":
        cont = False
    else:
        cont = True"""

dec_to_bin(192)
dec_to_bin(168)
dec_to_bin(4)
dec_to_bin(1)