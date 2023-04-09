# Peak
from math import sqrt
def transform(A):
    peak_pos = len(A)
    last_height = A[-1]
    for p in range(len(A) - 1, 0, -1):
        if (A[p - 1] < A[p] > last_height):
            peak_pos = p
        last_height = A[p]
        A[p] = peak_pos
    A[0] = peak_pos
def can_fit_flags(A, k):
    flag = 1 - k
    for i in range(k):
        # we plant the next flag at A[flag + k]
        if flag + k > len(A) - 1:
            return False
        flag = A[flag + k]
    return flag < len(A)  # last flag planted successfully
def solution(A):
    transform(A)
    lower = 0
    upper = int(sqrt(len(A))) + 2
    assert not can_fit_flags(A, k=upper)
    while lower < upper - 1:
        next = (lower + upper) // 2
        if can_fit_flags(A, k=next):
            lower = next
        else:
            upper = next
    return lower

A = [1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(A))

'''
`O(N)` preprocessing (done inplace):
    A[i] := next peak or end position after or at position i
            (i for a peak itself, len(A) after last peak)
If we can plant `k` flags then we can certainly plant `k' < k` flags as well.
If we can not plant `k` flags then we certainly can not plant `k' > k` flags either.
We can always set 0 flags.
Let us assume we can not set `X` flags.
Now we can use binary search to find out exactly how many flags can be planted.
    Steps:
      1. X/2
      2. X/2 +- X/4
      3. X/2 +- X/4 +- X/8
      ...
      log2(X) steps in total
With the preprocessing done before, each step testing whether `k` flags can be planted can be performed in `O(k)` operations:
* flag(0) = next(0)
* flag(1) = next(flag(1) + k)
...
* flag(k-1) = next(flag(k-2) + k)
total cost - worst case - when `X - 1` flags can be planted:
>  == X * (1/2 + 3/4 + ... + (2^k - 1)/(2^k))
>  == X * (log2(X) - 1 + (<1))
>  <= X * log(X)
Using `X == N` would work, and would most likely also be sublinear, but is not good enough to use in a proof that the total upper bound for this algorithm is under `O(N)`.
Now everything depends on finding a good `X`, and it since `k` flags take about `k^2` positions to fit, it seems like a good upper limit on the number of flags should be found somewhere around `sqrt(N)`.
If `X == sqrt(N)` or something close to it works, then we get an upper bound of `O(sqrt(N) * log(sqrt(N)))` which is definitely sublinear.
Let's look for a more exact upper bound on the number of required flags around `sqrt(N)`:
* we know `k` flags requires `Nk := k^2 - k + 3` flags
* by solving the equation `k^2 - k + 3 - N = 0` over `k` we find that if `k >= 3`, then any number of flags <= the resulting `k` can fit in some sequence of length N and a larger one can not; solution to that equation is `1/2 * (1 + sqrt(4N - 11))`
* for `N >= 9` we know we can fit 3 flags
  ==> for `N >= 9`, `k = floor(1/2 * (1 + sqrt(4N - 11))) + 1` is a strict upper bound on the number of flags we can fit in `N`
* for `N < 9` we know 3 is a strict upper bound but those cases do not concern us for finding the big-O algorithm complexity
> floor(1/2 * (1 + sqrt(4N - 11))) + 1
>   == floor(1/2 + sqrt(N - 11/4)) + 1
>   <= floor(sqrt(N - 11/4)) + 2
>   <= floor(sqrt(N)) + 2
==> `floor(sqrt(N)) + 2` is also a good strict upper bound for a number of flags that can fit in `N` elements + this one holds even for `N < 9` so it can be used as a generic strict upper bound in our implementation as well
If we choose `X = floor(sqrt(N)) + 2` we get the following total algorithm upper bound:
    O((floor(sqrt(N)) + 2) * log(floor(sqrt(N)) + 2))
       {floor(...) <= ...}
    O((sqrt(N) + 2) * log(sqrt(N) + 2))
       {for large enough N >= 4: sqrt(N) + 2 <= 2 * sqrt(N)}
    O(2 * sqrt(N) * log(2 * sqrt(N)))
       {lose the leading constant}
    O(sqrt(N) * (log(2) + loq(sqrt(N)))
    O(sqrt(N) * log(2) + sqrt(N) * log(sqrt(N)))
       {lose the lower order bound}
    O(sqrt(N) * log(sqrt(N)))
    O(sqrt(N) * log(N))
'''