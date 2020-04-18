def mergeSort(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    leftHalf = array[:middle]
    rightHalf = array[middle:]

    return merge(mergeSort(leftHalf), mergeSort(rightHalf))


def merge(leftArray, rightArray):
    # initialize lengths
    leftLength = len(leftArray)
    rightLength = len(rightArray)

    # initialize helperArray
    helperArray = [None for _ in range(leftLength + rightLength)]

    leftPointer = 0
    rightPointer = 0

    for i in range(leftLength + rightLength):
        if leftArray[leftPointer] < rightArray[rightPointer]:
            helperArray[i] = leftArray[leftPointer]
            leftPointer += 1
        else:
            helperArray[i] = rightArray[rightPointer]
            rightPointer += 1

        if leftPointer == leftLength:
            helperArray[leftPointer + rightPointer:] = rightArray[rightPointer:]
            break
        if rightPointer == rightLength:
            helperArray[rightPointer + leftPointer:] = leftArray[leftPointer:]
            break

    return helperArray

print(mergeSort([8, -6, 7, 10, 8, -1, 6, 2, 4, -5, 1, 10, 8, -10, -9, -10, 8, 9, -2, 7, -2, 4]))