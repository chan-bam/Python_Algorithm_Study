

# 간단한 소인수분해
# 소인수분해: 주어진 합성수를 소인수들의 곱으로 나타내는 과정
# 소인수 : 자연수의 인수 중 소수
# 소수 : 1보다 큰 자연수 중에서 1과 그 수 자신만을 약수로 가지는 수
# 소인수분해 하는 법 : 소인수로 몫이 소수가 될 때까지 나눗셈을 한다 # 모든 소인수와 마지막 몫을 곱한다
# 약수 구하기

T = int(input())
lst = [2, 3, 5, 7, 11] # 숫자 N을 구성하는 정해진 소수값 저장할 리스트

for tc in range(1, T + 1):
    res = [] # 횟수 저장할 빈 리스트 초기화
    N = int(input())
    for i in lst:  # 숫자 N을 구성하는 정해진 소수값을 기준으로 반복
        cnt = 0  # 횟수 저장할 변수 초기화
        while N % i == 0: # 숫자 N을 i로 나눈 나머지가 0이 될 때까지
            N = N // i # N을 i로 나눔
            cnt += 1 # N이 i로 나눠질 때마다 cnt변수를 1씩 증가(횟수 세기)
        res.append(cnt) # i 반복 끝날때마다 cnt 변수를 res 리스트에 추가
    print('#{} {}'.format(tc, ' '.join(map(str, res)))) # res 리스트의 요소를 map함수를 사용해서 문자열로 변환하여 join 메서드로 공백으로 나누어 출력
