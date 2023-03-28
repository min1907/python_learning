class Sort:
    def bubblesort(self, a: list[int]) -> list:

        for i in range(len(a)):
            isSorted = True
            for j in range(len(a) - i - 1):
                if a[j] > a[j + 1]:
                    isSorted = False
                    t = a[j]
                    a[j] = a[j + 1]
                    a[j + 1] = t
            print(f"{i}:{a}")
            if isSorted:
                break

        return a

    def selectionsort(self, array: list[int]) -> list:
        for step in range(len(array)):

            minIndex = step

            # select minimum element in each loop
            for j in range(step + 1, len(array)):
                if array[j] < array[minIndex]:
                    minIndex = j

            # put min in correct position
            (array[step], array[minIndex]) = (array[minIndex], array[step])

            print(f"{step}:{array}")

        return array

    def insertionsort(self, array: list[int]) -> list:

        for step in range(1, len(array)):
            key = array[step]
            j = step - 1

            # Compare key with each element on the left of it until an element is smaller than it is found
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1

            # Place key at after the element just smaller than it
            array[j + 1] = key
            print(f"{step}:{array}")
        return array


# Ref: https://www.programiz.com/dsa/insertion-sort

tmp = Sort()
b = [5, 3, 2, 7, 8, 1, 3]
# print(tmp.bubblesort(b))
print(tmp.selectionsort(b))
# print(tmp.insertionsort(b))
