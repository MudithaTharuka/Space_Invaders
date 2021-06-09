s = input()
s_split = s.split()
print("\n")
li = []
sul = []
val = 0

print(int(s_split[0])*2)

n = input()
n_split = n.split()
n_split_int = []
# for i in n_split:
#     n_split_int.append(int(n_split[i]))
q_splited = []

for i in range(int(s_split[1])):
    q = input()
    q_split = q.split()
    q_splited+=q_split
#     x = int(q_split[0])
#     y = int(q_split[1])
    #print(int(n_split[x])
    #sul.append(int(n_split[x]) + int(q_split[y]))

for j in range(0,len(q_splited),2):
    x = int(q_splited[int(j)])
    y = int(q_splited[int(j)+1])

    for k in range(x,y+1):
        val+=int(n_split[int(k)])
        print(val)
    sul.append(val)

print(sul)
