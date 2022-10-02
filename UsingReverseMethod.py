def isPalindrome(s):
    x=list(s)
    y=[]
    y.extend(x)
    x.reverse()
    if(x==y):
        return True
    return False
 
# Driver Code
s = "helloolleh"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
 
else:
    print("No")
