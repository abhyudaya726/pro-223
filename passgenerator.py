c = 0
characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

file = open("pass_list.txt","w")

for i in characters:
    for j in characters:
        for k in characters:
            for l in characters:
                pass_letter = str(i)+str(j)+str(k)+str(l)
                file.write(pass_letter)
                file.write("\n")
                c += 1
                c+=1

print("wordlist of {} passwords created".format(c))