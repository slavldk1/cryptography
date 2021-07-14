cat=input("input?\n:")
RT=""
List=[]
L=""
for i in range(len(cat)):
    L=cat[i]
    List.append(L)
List.append("0")
for i in range(len(List)):
    if List[i-1:i]==["1"]:
        RT+="a"
        print("1감지")
    elif List[i-1:i]==["0"]:
        RT+=" "
        print("0감지")
    elif List[i-1:i]==["2"]:
        RT+="b"
        print("2감지")
    elif List[i-1:i]==["3"]:
        RT+="c"
        print("3감지")
print(RT)
print(List)

#작동됨, 이제 해야할것은 조금더 간단하게 하는 법을 배우면 됨
#작동 겁나 잘됨