def bubble_sort(nums):
    arr = nums[:]  # 复制避免修改原列表
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # 如果本轮没有交换，提前结束
            break
    return arr

if __name__ == "__main__":
    data = [5, 1, 9, 2, 7, 3]
    print("原始：", data)
    print("排序后：", bubble_sort(data))
