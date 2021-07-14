import random
cat=input("input?\n:")
ST=""
List=[]
L=''
R=random.randrange(0,9)
for i in range(len(cat)):
    L=cat[i]
    if L==" ":
        print("공백")
        List.append("/")
    else:
        List.append(L)
        print("입력")
List.append(R)
for i in range(len(List)):
    if List[i-1:i]==["a"]:
        ST+="1"
        print("a감지")
    elif List[i-1:i]==["/"]:
        ST+="0"
        print("공백 감지")
    elif List[i-1:i]==["b"]:
        ST+="2"
        print("b감지")
    elif List[i-1:i]==["c"]:
        ST+="3"

print(ST)
print(List)
#뜨어쓰기도 구분하는 걸로 만들긴함
#다만....노가다 하기 싫은데 어쩌지
#복호화는 또 어케하지? 역순으로 가야하나 으으으으아아아아아아아아ㅏㅏㅏㅏ