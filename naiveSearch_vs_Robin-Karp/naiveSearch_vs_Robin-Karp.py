#!/usr/bin/env python3
import time

######
def searchN(pat, txt):  #naive search algorithm
    M = len(pat)
    N = len(txt)

    # A loop to slide pat[] one by one
    for i in range(N-M + 1):
        # For current index i, check for pattern match
        for j in range(M):
            if txt[i + j] != pat[j]:
                break
            if j == M-1: # if pat[0...M-1] = txt[i, i + 1, ...i + M-1]
                print(" col: " + str(i))

######
# d is the number of characters in input alphabet
d = 256
q=101

# pat  -> pattern
# txt  -> text
# q    -> A prime number

def searchR(pat, txt, q):   #Robin-Karp search algorithm
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*d)%q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q

    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p==t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break

            j+=1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                print("col: " + str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t+q
######
files_names=['1000_pattern.txt','2000_pattern.txt','3000_pattern.txt','4000_pattern.txt','5000_pattern.txt']

###### NAIVE_SEARCH#####:
start = time.time()
for i in range(5):
    with open(files_names[i]) as file:
        txt = file.readlines()
        txt = [x.strip() for x in txt]

    with open('wzorzec.txt') as file:
        pat = file.readlines()
        pat = [x.strip() for x in pat]
        pat = ''.join(pat)
    # Driver program to test the above function
    for j in range (0,(i+1)*1000):
        print('line: ',(j+1))
        searchN(pat,txt[j])
end = time.time()

time_N=end-start

##### ROBIN_KARP ALGO#####:
print('ROBIN_KARP')
start = time.time()
for i in range(5):
    with open(files_names[i]) as file:
        txt = file.readlines()
        txt = [x.strip() for x in txt]

    with open('wzorzec.txt') as file:
        pat = file.readlines()
        pat = [x.strip() for x in pat]
        pat = ''.join(pat)
    # Driver program to test the above function
    for j in range (0,(i+1)*1000):
        print('line: ',(j+1))
        searchR(pat,txt[j],q)
end = time.time()

time_R=end-start
print('time_N: ',time_N)
print('time_R: ',time_R)
