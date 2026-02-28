def sieve(n):
    # 입력: n (정수)
    # 상태: 0~n까지 소수 여부 배열
    is_prime = [True] * (n + 1)

    # 조건: 0,1은 소수가 아님 (불변량 정리)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False

    # 연산: i ≤ sqrt(n) 까지만 배수 제거
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:  # 아직 제거되지 않았다면
            # 상태 변화: i의 배수 제거
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    # 결과 확인: True인 인덱스만 반환
    return [i for i in range(2, n + 1) if is_prime[i]]
