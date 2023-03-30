class Demo_recursive:
    def giaithua(self, num):
        if num == 0:
            return 1
        return num * self.giaithua(num - 1)

    def fibonacci(self, num):
        if num == 0:
            return 0
        if num == 1:
            return 1
        return self.fibonacci(num - 1) + self.fibonacci(num - 2)


tmp = Demo_recursive()

array = [*range(20)]

# array_map_giaithua = map(tmp.giaithua, array)
# print(list(array_map_giaithua))

array_map_fibonacci = map(tmp.fibonacci, array)
print(list(array_map_fibonacci))
