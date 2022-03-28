def cutString(arr):
    for i in range(len(arr)):
        if len(arr[i]) > 10:
            arr[i] = arr[i][:7] + '...'
    print(arr)

