#%%

from random import shuffle
from typing import List


class Array:
    last: int
    array: List[int]

    def __init__(self, objs: List[int] = []):
        size_max = max(10, len(objs))
        self.size_max = size_max
        self.last = 0
        self.array = [0] * size_max
        self.append_all(objs)

    def append(self, obj: int):
        if self.last < self.size_max:
            self.array[self.last] = obj
            self.last += 1
        else:
            self._resize()
            self.append(obj)

    def append_all(self, objs: List[int]):
        self._resize(self.size_max + len(objs))
        for obj in objs:
            self.append(obj)

    def append_front(self, obj: int):
        if self.last < self.size_max:
            temp = obj
            for i in range(self.last):
                temp, self.array[i] = self.array[i], temp
            self.array[self.last] = temp
            self.last += 1
        else:
            self._resize()
            self.append_front(obj)

    def append_front_all(self, objs: List[int]):
        self._resize(self.size_max + len(objs))
        for i in range(self.last - 1, -1, -1):
            self.array[i + len(objs)] = self.array[i]
        for i in range(len(objs)):
            self.array[i] = objs[i]
        self.last += len(objs)

    def insert_after(self, prev_obj: int, new_obj: int) -> bool:
        index = self.find(prev_obj)
        if index == -1:
            return False

        self.insert_at(new_obj, index + 1)
        return True

    def insert_at(self, obj: int, index: int):
        if index > self.last or index < 0:
            raise IndexError("List index out of range")

        if self.last < self.size_max:
            for i in range(self.last, index, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = obj
            self.last += 1
        else:
            self._resize()
            self.insert_at(obj, index)

    def _resize(self, size_max: int = None):
        if size_max is None:
            size_max = self.size_max * 2
        if size_max < self.size_max:
            raise ValueError(
                "for resizing the new size_max must be greater than current size_max"
            )
        if size_max < 2 * self.size_max:
            size_max = 2 * self.size_max

        self.array = self.array + [0] * (size_max - self.size_max)
        self.size_max = size_max

    def remove(self, obj: int) -> bool:
        index = self.find(obj)
        if index == -1:
            return False

        self.remove_at(index)
        return True

    def remove_at(self, index: int):
        if index >= self.last or index < 0:
            raise IndexError("List index out of range")

        for i in range(index, self.last - 1):
            self.array[i] = self.array[i + 1]
        self.last -= 1

    def find(self, obj: int) -> int:
        for i in range(self.last):
            if self.array[i] == obj:
                return i
        return -1

    def get(self, index: int) -> int:
        if index >= self.last or index < 0:
            raise IndexError("List index out of range")

        return self.array[index]

    def get_first(self) -> int:
        return self.get(0)

    def get_last(self) -> int:
        return self.get(self.last - 1)

    def set(self, index: int, obj: int):
        if index >= self.last or index < 0:
            raise IndexError("List index out of range")

        self.array[index] = obj

    def size(self) -> int:
        return self.last

    def copy(self) -> List[int]:
        return self.array[: self.last]

    def reverse(self):
        for i in range(self.last // 2):
            self.array[i], self.array[self.last - i - 1] = (
                self.array[self.last - i - 1],
                self.array[i],
            )

    def sort(self):
        for i in range(self.last):
            for j in range(i, self.last):
                if self.array[i] > self.array[j]:
                    self.array[i], self.array[j] = self.array[j], self.array[i]

    def sublist(self, start: int, end: int = -1) -> List[int]:
        if end == -1:
            end = self.last
        if start < 0 or end > self.last or start > end:
            raise IndexError("List index out of range")

        return self.array[start:end]

    def shuffle(self):
        shuffle(self.array[: self.last])

    def __str__(self) -> str:
        return str(self.array[: self.last])

    def __repr__(self) -> str:
        return f"Array({self.array[: self.last]})"

    def __len__(self) -> int:
        return self.last

    def __getitem__(self, index: int) -> int:
        return self.get(index)

    def __setitem__(self, index: int, obj: int):
        self.set(index, obj)

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index >= self.last:
            raise StopIteration
        self.iter_index += 1
        return self.array[self.iter_index - 1]

    def __contains__(self, obj: int) -> bool:
        return self.find(obj) != -1


def test_arry():
    arr = Array()
    print("Leeres Array:")
    print(arr)

    a = 1
    arr.append(a)
    print(f"\nAppend {a}")
    print(arr)

    a = [2, 3, 4, 5]
    arr.append_all(a)
    print(f"\nAppend All {a}")
    print(arr)

    a = 6
    arr.append_front(a)
    print(f"\nAppend Front {a}")
    print(arr)

    a = [7, 8, 9, 10]
    arr.append_front_all(a)
    print(f"\nAppend Front All {a}")
    print(arr)

    a = 11
    b = 10
    arr.insert_after(b, a)
    print(f"\nInsert {a} after {b}")
    print(arr)

    a = 12
    b = 5
    arr.insert_at(a, b)
    print(f"\nInsert {a} at {b}")
    print(arr)

    a = 10
    arr.remove(a)
    print(f"\nRemove {a}")
    print(arr)

    a = 5
    arr.remove_at(a)
    print(f"\nRemove at {a}")
    print(arr)

    a = 11
    print(f"\nFind {a}: {arr.find(a)}")

    a = 5
    print(f"Get {a}: {arr.get(a)}")

    print(f"Get First: {arr.get_first()}")
    print(f"Get Last: {arr.get_last()}")
    print(f"Size: {arr.size()}")
    print(f"\nCopy: \n{arr.copy()}")

    arr.reverse()
    print(f"\nReverse: \n{arr}")
    arr.sort()
    print(f"\nSort: \n{arr}")

    a = 2
    b = 5
    print(f"\nSublist from {a} till {b}: \n{arr.sublist(a, b)}")

    arr.shuffle()
    print(f"\nShuffle: \n{arr}")


if __name__ == "__main__":
    test_arry()
