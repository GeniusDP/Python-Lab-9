
def Input(): #inputing string
    return input("Type in your string:\n")

def solve(s):#the "main" function

    #array for counting "how many times
    #was character i(ASCII) used"
    cnt=[]
    for i in range(257):
        cnt.append(0)
	
    #result array
    positions=[]
	
    #feeling cnt[]
    for i in s:
        cnt[ord(i)]+=1

    #getting characters, which
    #have been used only at ones 
    for i in range(0, len(cnt)):
        if cnt[i]==1:
            positions.append( s.find(chr(i))+1 )
    
    printCharsOfString(s)
    Bubblesort(positions)
    printpositions(positions)
    pass

def printpositions(arr):#printing answer
    if len(arr)>0:
        print("\nThis is array of positions: ")
        for i in range(0, len(arr)):
            print("{:>5}".format(str(arr[i])), end="")
    else:
        print( "There are any such characters!" )    
    pass

def Bubblesort(arr):#bubble sort algorithm
    for i in range(0, len(arr)-1):
        for j in range(i, len(arr)):
            if arr[i]>arr[j]:
                arr[i], arr[j]=arr[j], arr[i]
    pass
    


def printCharsOfString(s):#partial solution output
    print("Infromation about the string: ")
    for i in s:
        print("{:>5}".format(i), end="")#symbols of s
    print()
    for i in range(0, len(s)):
        print("{:>5}".format(str(i+1)), end="")#indexex
    pass

