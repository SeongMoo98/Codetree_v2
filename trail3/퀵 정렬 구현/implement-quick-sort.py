# N <100,000
# 원소값 <= 100,000
# Quick Sort 구현

N = int(input())
arr = list(map(int, input().split()))

def partition(arr, left, right):
    """
    right를 pivot으로 잡고, pivot보다 작은 원소는 왼쪽으로 모은다.
    파티션이 끝나면 pivot의 최종 위치(인덱스)를 반환.
    """
    pivot = arr[right]
    i = left - 1  # pivot보다 작은 원소들의 "경계" 역할

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swap

    # pivot을 자기 자리(i+1)로 옮기기
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)  # 파티션 후 pivot의 정확한 위치를 얻음

        quick_sort(arr, left, pivot_index - 1)   # pivot 왼쪽 구간
        quick_sort(arr, pivot_index + 1, right)  # pivot 오른쪽 구간

quick_sort(arr, 0, N - 1)
print(' '.join(map(str, arr)))