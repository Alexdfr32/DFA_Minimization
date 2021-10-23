
#READING THE DFA

print("Please separate all elementes by spaces.\n\n\n")

alphabet=str(input("Please Enter the alphabet:")).split(" ")
states=str(input("Please Enter the States:")).split(" ")


starting=str(input("Please enter the starting point:"))


finals=str(input("Please enter the final states:")).split(" ")
# print("RRR",finals,"RRR")
nonfinals=[]
for state in states:
    if state not in finals:
        # print("EE",state,'ee')
        nonfinals.append(state)

print("So finals are:",end=" ")
for element in finals:
    print(element,end="")

print("\nAnd nonfinals are:", end=' ')
for element in nonfinals:
    print(element, end = " ")
print("")
print("")
print("")








#FORMING(AND READING) THE m CORESPONDING TO STATES AND THE ALPHABET
r=dict()
c=dict()

for i in range(len(alphabet)):
    c[alphabet[i]]=i

for i in range(len(states)):
    r[states[i]]=i



m=len(r)*[len(c)*[0]]
j=0
for i in range (0,len(r)):
    for j in range(0,len(c)):
        m[i][j]=0


for i in range (len(states)):
  print("Please enter the relations of ",states[i])
  for key in c:
    print(key,end=" ")
  print("")
  var=str(input()).split(" ")
  #print("var:",var)
  m[i]=var



#pRINTING THE FIRST m
print("δ", end="   ")
for i in alphabet:
  print(i,"  ",end="")
print("")
k=-1
for i in m:
  k+=1
  print(states[k],": ",end="")
  for j in i:
    print(j," ",end=" ")
  print("")



#FORMING THE MARKING TABLE
#STEP 1 
r0=dict()
c0=dict()

for i in range(len(states)):
    c0[states[i]]=i
    r0[states[i]]=i


m0 = [[0 for x in range(len(r0))] for y in range(len(c0))] #LEN(STATES?)
#0 is for unmarked, 1 is for marked 0 is unmarked






#STEP2 

for final in finals:
    for nonfinal in nonfinals:
        # print(final," ",nonfinal)
        m0[r0[nonfinal]][c0[final]]=1
        m0[r0[final]][c0[nonfinal]]=1




#STEP 3

changes=1

while changes:
  changes=0

  for state1 in r0:

    for state2 in c0:

      if state1==state2:
        continue
      if m0[r0[state1]][c0[state2]]==1:
        continue
      
      for elem in alphabet:
        if m0[ r0[ m[ r[state1] ][ c[elem] ] ]   ][  c0[ m[ r[state2] ][ c[elem]   ]    ]]:
          m0[ r0[state1] ][ c0[state2] ]=1
          changes=1


print()


for i in range(len(states)):
    for j in range(len(states)):
        print(m0[i][j],end=" ")
    print("")

print()

printed=[]
for state1 in r0:
  for state2 in c0:
    ok=1
    if m0[r0[state1]][c0[state2]]==0 and state1!=state2:
      for elem in printed:
        if state1 in elem and state2 in elem:
          ok=0
      if ok==1:
        printed.append( (state1, state2))
        print(state1, state2,"-> Are equivalent" )