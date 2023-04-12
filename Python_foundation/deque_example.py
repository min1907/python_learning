from collections import deque

queue = deque([1, 2, 3])
# print(queue) #deque([1, 2, 3])

queue.append(4)
# print(queue) #deque([1, 2, 3, 4])

queue.appendleft(0)
# print(queue) #deque([0, 1, 2, 3, 4])
# print(list(queue)) #[0, 1, 2, 3, 4]

queue.pop()
# print(queue) #deque([0, 1, 2, 3])

queue.popleft()
# print(queue) #deque([1, 2, 3])

#### ACCESSING ITEMS FROM DEQUE
"""
- index(ele, beg, end):- This function returns the first index of the value mentioned in arguments,
                        starting searching from beg till end index.

- insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.

- remove():- This function removes the first occurrence of the value mentioned in arguments.

- count():- This function counts the number of occurrences of value mentioned in arguments.
"""
queue = deque([1, 2, 3, 3, 4, 2, 4])
# using index() to print the first occurrence of 4
print(queue.index(4, 2, 5))  # index = 4

# using insert() to insert the value 3 at 5th position
queue.insert(4, 3)
print(queue)  # deque([1, 2, 3, 3, 3, 4, 2, 4])

# using count() to count the occurrences of 3
print(queue.count(3))  # 3

# # using remove() to remove the first occurrence of 3
queue.remove(3)
print(queue)  # deque([1, 2, 3, 3, 4, 2, 4])

#### SIZE OF DEQUE
print(len(queue))  # 7
print(queue[0])  # 1
print(queue[-1])  # 4

#### DIFFERENT OPERATION ON DEQUE
"""
- extend(iterable):- This function is used to add multiple values at the right end of the deque.
                    The argument passed is iterable.

- extendleft(iterable):- This function is used to add multiple values at the left end of the deque.
                    The argument passed is iterable. Order is reversed as a result of left appends.

- reverse():- This function is used to reverse the order of deque elements.

- rotate():- This function rotates the deque by the number specified in arguments.
            If the number specified is negative, rotation occurs to the left. Else rotation is to right.
"""
queue = deque([1, 2, 3])
queue.extend([4, 5, 6])
print(queue)  # deque([1, 2, 3, 4, 5, 6])


queue.extendleft([7, 8, 9])
print(queue)  # deque([9, 8, 7, 1, 2, 3, 4, 5, 6])

queue.reverse()
print(queue)  # deque([6, 5, 4, 3, 2, 1, 7, 8, 9])

queue.rotate(-3)
print(queue)  # deque([3, 2, 1, 7, 8, 9, 6, 5, 4])
