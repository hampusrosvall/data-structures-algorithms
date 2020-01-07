'''
Iterative fib solution.

Runs in O(N) time and O(1) space

Recursive memoized fib solution

Runs in O(N) time and O(N) space due to the number of calls saved in function call stack

'''

def fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        count = 2
        arr = [0, 1]

        while count < N:
            next = arr[0] + arr[1]
            arr[0] = arr[1]
            arr[1] = next
            count += 1

        return arr[0] + arr[1]

def memoize_fib(N, memoize = {0 : 0, 1 : 1}):
    if N in memoize:
        return memoize[N]
    else:
        memoize[N] = memoize_fib(N - 1, memoize) + memoize_fib(N - 2, memoize)

    return memoize[N]

if __name__ == '__main__':
    print(fib(10))

