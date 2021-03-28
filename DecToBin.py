class DecToBin:
    def decToBinConv1(self,decimalNum):
        num = decimalNum
        conversion_res = ""
        while num > 0:
            rem = num % 2
            # bitList.append(rem)
            num = num // 2
            conversion_res = str(rem) + conversion_res
        return conversion_res




def decToBinConv(decNum):
    num = decNum
    # bitList = []
    result = ""
    while num > 0:
        rem = num % 2
        # bitList.append(rem)
        num = num // 2
        result = str(rem) + result

    print(f'Mao, {result}')  # Press Ctrl+F8 to toggle the breakpoint.
    return result

try:

    n = int (input ("Enter a decimal number: "))

    obj = DecToBin()
    binNum=obj.decToBinConv1(n)
    print(f'Bhou, {binNum}')


    #binNum = decToBinConv(n)
    #print(f'Bhou, {binNum}')

    #num = n
    #bitList = []
    #result=""
    # while n>0:
    #     rem = n%2
    #     #bitList.append(rem)
    #     n=n//2
    #     result=str(rem)+result

    #print(f'Mao, {result}')  # Press Ctrl+F8 to toggle the breakpoint.
    # i = len(bitList)-1
    # print ("The binary equialent of ",num," = ",end="")
    # while i>=0:
    #     print(bitList[i],end="")
    #     i-=1

except:
    print ("Wrong Input! Numeral expected")

#print (bitList[::-1])-- to print a list in reverse order
