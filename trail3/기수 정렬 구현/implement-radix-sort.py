# N <= 100,000
# 원소값 <= 100,000
# Radix sort 구현

def radix_sort(arr, k):
    """
    arr: 정렬할 리스트
    k: 처리할 최대 자릿수 (예: 100000이면 6자리)
    """
    for pos in range(k):  # 1의 자리(pos=0)부터 시작해서 큰 자리로
        buckets = [[] for _ in range(10)]  # 0~9 자리 숫자별 바구니

        for num in arr:
            digit = (num // (10 ** pos)) % 10  # pos번째 자릿수 추출
            buckets[digit].append(num)

        # 바구니 0번부터 9번까지 순서대로 이어붙이기
        arr = []
        for bucket in buckets:
            arr.extend(bucket)

    return arr

N = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
K = len(str(max_val))  # 최대값의 자릿수만큼만 돌리면 충분

result = radix_sort(arr, K)
print(' '.join(map(str, result)))
