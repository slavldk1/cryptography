import time 
aya=input("암호화에 쓸 키!\n:")
moae=input("암호화할 문장!\n:")
K=[]
C=""
M=''
A=0
for i in range(len(aya)):
    C=aya[i]
    B=ord(C)
    K.append(B)
print("암호키 추가 완료")
while True:
    print("While문 시작")
    if len(K)<len(moae):
        K=K*2
        print("attend")
    else:
        break
for i in range(len(moae)):
    C=moae[i]
    B=ord(C)
    A=B+K[i]
    C=chr(A)
    
    M+=C
print(M)
print(K)

#개선점
"""
암호화에 쓸키가 짧으면 짧을수록 암호화의 위력이 떨어짐
이게 가장 중요함
현재 띄어쓰기를 인식못하는 것같음;;
ord 코드는 32번인데 우짬
확인결과 그냥 /등등을 인식을 못하는것으로 보임
null을 출력함
뭐야 한글 넣으니까 출력 재대로 됨;;
ㅅㅂ?
영어만 인식을 안함
"""