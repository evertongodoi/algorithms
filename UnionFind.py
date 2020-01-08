import sys

# sets are define P and Q
#P = {0,1,4,5}; 
#Q = {2,3,6,7}; 
  
# union 1
#print("Union 1 :", P | Q)

# union 2
#print("Union 2 :", P.union(Q)) 

UF = 10
for i in range(10):
    print("contador: " + str(i))
    p = input("Digite o valor p: ")
    q = input("Digite o valor q: ")
    P = {p}
    Q = {q}
    if not bool in (P|Q):
        print("union: ", P.union(Q) , " ", str(p), " ", str(q))
    else:
        print("conectados", str(p), " ", str(q))
