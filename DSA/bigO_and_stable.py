# O(log(n))
def func2(n):
    if n<= 1:
        return
    else:
        print(n)
        func2(n/2)

# O(n)
def func3(numbers):
    for num in numbers:
        print(num)

# O(n * log(n))
def func4(n):
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <= 1:
        return
    
    func4(n/2)

# O(n**2)
def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()


#func5([1, 2, 3, 4, 5])

l = [(1, 'Mike'), (5, 'Rina'), (2, 'Bill'), (4, 'Emily'), (2, 'June')]
def stable(l):
    l[1], l[2] = l[2], l[1]
    l[2], l[4] = l[4], l[2]
    return l

print(stable(l))