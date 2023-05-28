str = input("please enter a string\t")

def alternative_upper(str):
    cnt =0
    x=""
    for i in range(len(str)+1):
        if str[i]==" " and i<=len(str):
            x=(str[i+1])
            cnt +=1
            if cnt%2!=0:
                print('\t',x.upper())
            else:
                print('\t',x.lower())
            continue

def upper_first(str):
    j=0
    for i in range(len(str)+1):
        if str[i]==" ":
            x=(str[i+1]).upper()
            print('\t',x)
            break
    i=j
    for j in range(len(str)+1):
        if str[j] == " ":
            x = (str[i + 1]).lower()
            print('\t', x)