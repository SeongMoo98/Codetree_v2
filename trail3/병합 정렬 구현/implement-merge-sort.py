def merge_sort(arr, l, r):
    # 종료 조건: 구간에 원소가 1개 이하면 이미 정렬된 것으로 보고 멈춘다
    if l >= r:
        return

    mid = (l + r) // 2
    merge_sort(arr, l, mid)       # 왼쪽 절반 정렬
    merge_sort(arr, mid + 1, r)   # 오른쪽 절반 정렬
    merge(arr, l, mid, r)         # 정렬된 두 절반을 합치기


def merge(arr, l, mid, r):
    i, j = l, mid + 1       # 왼쪽 구간 포인터, 오른쪽 구간 포인터
    res = [0] * (r - l + 1) # 합친 결과를 임시로 담을 배열
    k = 0

    # 양쪽 구간을 앞에서부터 비교하며 작은 값을 res에 채워넣는다
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            res[k] = arr[i]
            i += 1
        else:
            res[k] = arr[j]
            j += 1
        k += 1

    # 왼쪽 구간이 남았으면 그대로 이어붙인다
    while i <= mid:
        res[k] = arr[i]
        i += 1
        k += 1

    # 오른쪽 구간이 남았으면 그대로 이어붙인다
    while j <= r:
        res[k] = arr[j]
        j += 1
        k += 1

    # 임시 배열의 내용을 원본 배열의 [l, r] 구간에 그대로 복사
    for idx in range(len(res)):
        arr[l + idx] = res[idx]


N = int(input())
arr = list(map(int, input().split()))
merge_sort(arr, 0, N - 1)
print(' '.join(map(str, arr)))