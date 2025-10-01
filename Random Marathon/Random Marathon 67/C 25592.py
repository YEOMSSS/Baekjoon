
# 뭘 복잡하게 수식 쓰고 앉았냐.. 어차피 100000까지밖에 안된다

N = int(input())

total = 1
# 내차례면 0, 쟤차례면 1
turn = 1
cnt = 1
while total <= N:
    cnt += 1
    total += cnt
    # 다음 차례가 누군지를 나타내게 된다.
    turn ^= 1 # 자기 턴이 끝나고 상대에게 턴을 넘겨준다.
    
if not turn:
    print(0)
else:
    print(total - N)
