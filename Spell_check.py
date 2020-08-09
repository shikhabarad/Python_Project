import os.path
from os import path

pattern_file_name = ""
input_file_name = ""
output_file_name = ""

flg = 0
while True :
    if flg == 0 : 
        print("please input pattern file name")
    else :
        print("There is no such file as ", pattern_file_name, "!", "please input pattern file name again")
    pattern_file_name = input()
    if path.exists(pattern_file_name) == True :
        break
    flg += 1

flg = 0
while True :
    if flg == 0 : 
        print("please input file name that include wrong words.")
    else :
        print("There is no such file as ", input_file_name, "!", "please input file name that include wrong words again.")
    input_file_name = input()
    if path.exists(input_file_name) == True :
        break
    flg += 1

print("please input file name that you want to output the correct word.")
output_file_name = input()

pattern_text = open(pattern_file_name, "r")

pt_str = pattern_text.read()

pattern = {}

temp = ""
for i in pt_str :
    if i.isupper() == True :
        temp += i.lower()
        continue
    if i.islower() == False :
        if temp == "" :
            continue
        if temp in pattern :
            pattern[temp] = pattern[temp] + 1
        else :
            pattern[temp] = 1
        temp = ""
    else :
        temp += i

if temp != "" :
    if temp in pattern :
        pattern[temp] = pattern[temp] + 1
    else :
        pattern[temp] = 1
    temp = ""

def chk_spell(txt) :
    txt = txt.replace("\n", "")
    if txt in pattern :
        return txt
    ans = txt
    mat = 0
    mem = txt
    for x in pattern :
        ky = x
        txt = mem
        if abs(len(x) - len(txt)) > 1 :
            continue
        if len(x) > len(txt) :
            tmp = x
            x = txt
            txt = tmp
        i = 0
        j = 0
        f = 0
        while i < len(x) and j < len(txt) :
            if x[i] == txt[j] :
                i += 1
                j += 1
                continue
            if i+1 < len(x) and j+1 < len(txt) and x[i] == txt[j+1] and x[i+1] == txt[j] and f == 0 :
                f = 1
                i += 2
                j += 2
                continue
            if len(x) < len(txt) and j+1 < len(txt) and x[i] == txt[j+1] and f == 0 :
                i += 1
                j += 2
                f = 1
                continue
            if f == 1 :
                f += 2
                break
            f += 1
            i += 1
            j += 1
        if f < 2 and i == len(x) and j == len(txt) :
            if pattern[ky] > mat :
                mat = pattern[ky]
                ans = ky
            elif pattern[ky] == mat and x < ans :
                mat = pattern[ky]
                ans = ky
    if mat == 0 :
        ans = ans + " : this word is not in the list!"

    return ans

freq = open("frequency.txt", "w")

for x in pattern :
    fstr = "frequency of " + x + " is " + str(pattern[x]) + "\n"
    freq.write(fstr)

freq.close()

# while True:
#     temp = input()
#     temp = chk_spell(temp)
#     print(temp)

rfile = open(input_file_name, "r")
wfile = open(output_file_name, "w")

n = rfile.readline()
if(n[0].isdigit() == False) :
    print("Please input N which sepcify the number of words into the input file at the first.")
    exit()

n = int(n)
for i in range(n) :
    temp = rfile.readline()
    temp = temp.replace(" ", "")
    temp = chk_spell(temp)	
    temp = temp + "\n"
    wfile.write(temp)

rfile.close()
wfile.close()
