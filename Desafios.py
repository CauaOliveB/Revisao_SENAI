merge = [3,1,12,4,5,10]

left = merge[0:3]
right = merge[3:6]

print(f"Left = {left}")
print(f"Right = {right}")

# for i in range(0,right,1):
#     print(i)
    
    

for i in merge:
    aux = str(i)
    if len(aux) == 2:
        aux1 = aux[0]
        aux2 =aux[1]
        
        aux1 = int(aux1)
        print(aux1+aux2)
        aux2 = int(aux2)
        print(aux1+aux2)
        print(aux1, aux2)