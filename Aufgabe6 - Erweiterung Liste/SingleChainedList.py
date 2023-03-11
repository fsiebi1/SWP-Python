#%%

import random
from typing import List


class SingleChainedListItem:
    obj: int
    _next_item: "SingleChainedListItem"

    def __init__(self, obj: int):
        self.obj = obj
        self._next_item = None

    def set_next_item(self, item: "SingleChainedListItem"):
        self._next_item = item

    def get_next_item(self) -> "SingleChainedListItem":
        return self._next_item

    def get_obj(self) -> int:
        return self.obj

    def __str__(self) -> str:
        return self.obj.__str__()


class SingleChainedList:
    head: SingleChainedListItem

    def __init__(self, objs: List[int] = []):
        self.head = None
        self.append_all(objs)

    def append(self, obj: int):
        new_item = SingleChainedListItem(obj)
        if self.head is None:
            self.head = new_item
        else:
            last = self.get_last()
            if last is None:
                self.head = new_item
            else:
                last.set_next_item(new_item)

    def append_all(self, objs: List[int]):
        if len(objs) == 0:
            return
        if len(objs) == 1:
            self.append(objs[0])
            return

        first_item = SingleChainedListItem(objs[0])
        cur_item = first_item
        for obj in objs[1:]:
            cur_item.set_next_item(SingleChainedListItem(obj))
            cur_item = cur_item.get_next_item()

        self._append_item(first_item)

    def _append_item(self, item: SingleChainedListItem):
        last = self.get_last()
        if last is None:
            self.head = item
        else:
            last.set_next_item(item)

    def append_front(self, obj: int):
        new_item = SingleChainedListItem(obj)
        new_item.set_next_item(self.head)
        self.head = new_item

    def append_front_all(self, objs: List[int]):
        if len(objs) == 0:
            return
        if len(objs) == 1:
            self.append_front(objs[0])
            return

        first_item = SingleChainedListItem(objs[0])
        cur_item = first_item
        for obj in objs[1:]:
            cur_item.set_next_item(SingleChainedListItem(obj))
            cur_item = cur_item.get_next_item()

        self._append_front_item(first_item)

    def _append_front_item(self, item: SingleChainedListItem):
        item.set_next_item(self.head)
        self.head = item

    def insert_after(self, prev_obj: int, new_obj: int) -> bool:
        index = self.find(prev_obj)
        if index == -1:
            return False

        self.insert_at(index + 1, new_obj)
        return True

    def insert_at(self, index: int, obj: int):
        if index > self.size():
            raise IndexError("List index out of range")

        new_item = SingleChainedListItem(obj)

        if index == 0:
            new_item.set_next_item(self.head)
            self.head = new_item
        else:
            prev_obj = self._get_list_item(index - 1)
            new_item.set_next_item(prev_obj.get_next_item())
            prev_obj.set_next_item(new_item)

    def remove(self, obj: int) -> bool:
        index = self.find(obj)
        if index == -1:
            return False

        self.remove_at(index)
        return True

    def remove_at(self, index: int):
        if index >= self.size():
            raise IndexError("List index out of range")

        if index == 0:
            self.head = self._get_list_item(1)
        else:
            davor_item = self._get_list_item(index - 1)
            del_item = self._get_list_item(index)
            davor_item.set_next_item(del_item.get_next_item())

    def get(self, index: int) -> int:
        item = self._get_list_item(index)
        if item is None:
            return None
        return item.get_obj()

    def _get_list_item(self, index: int) -> SingleChainedListItem:
        if index >= self.size() or index < 0:
            raise IndexError("List index out of range")

        item = self.head
        for x in range(self.size()):
            if x == index:
                return item
            item = item.get_next_item()

        return None

    def find(self, obj: int) -> int:
        item = self.head
        for i in range(self.size()):
            if item.get_obj() == obj:
                return i
            item = item.get_next_item()

        return -1

    def get_first(self) -> SingleChainedListItem:
        if self.size() == 0:
            return None
        return self.head

    def get_first_value(self) -> int:
        first = self.get_first()
        if first is None:
            return None
        return first.get_obj()

    def _set_first(self, item: SingleChainedListItem):
        self.head = item

    def get_last(self) -> SingleChainedListItem:
        if self.size() == 0:
            return None
        item = self.head
        while item.get_next_item() is not None:
            item = item.get_next_item()
        return item

    def get_last_value(self) -> int:
        last = self.get_last()
        if last is None:
            return None
        return last.get_obj()

    def to_list(self) -> List[int]:
        liste = []
        item = self.head
        while item is not None:
            liste.append(item.get_obj())
            item = item.get_next_item()

        return liste

    def to_list_reversed(self) -> List[int]:
        liste = []
        item = self.head
        while item is not None:
            liste.insert(0, item.get_obj())
            item = item.get_next_item()

        return liste

    def size(self) -> int:
        anz = 0
        item = self.head
        while item is not None:
            anz += 1
            item = item.get_next_item()

        return anz

    def __iter__(self) -> "SingleChainedListIter":
        return SingleChainedListIter(self)

    def __getitem__(self, index) -> int:
        return self.get(index)

    def __str__(self) -> str:
        string = "["
        item = self.head
        while item is not None:
            string += item.get_obj().__str__() + ", "
            item = item.get_next_item()

        if len(string) > 1:
            string = string[:-2]
        return string + "]"

    def __len__(self) -> int:
        return self.size()

    def __repr__(self) -> str:
        return f"SingleChainedList({str(self)})"

    def copy(self) -> "SingleChainedList":
        cop = SingleChainedList()
        items = self.to_list()
        cop.append_all(items)

        return cop

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.get_next_item()
            current.set_next_item(prev)
            prev = current
            current = next
        self.head = prev

    def sort(self):
        objs = self.to_list()
        objs.sort()
        sorted = SingleChainedList()
        sorted.append_all(objs)

        self.head = sorted.head

    def shuffle(self):
        objs = self.to_list()
        random.shuffle(objs)
        shuffled = SingleChainedList()
        shuffled.append_all(objs)

        self.head = shuffled.head

    def sublist(self, start: int, end: int = -1) -> "SingleChainedList":
        if start < 0 or start >= self.size():
            raise IndexError("List index out of range")
        if end == -1:
            end = self.size()
        if end > self.size():
            raise IndexError("List index out of range")
        if end <= start:
            raise ValueError("end must not be less or equal to start")

        cop = SingleChainedList()
        items = self.to_list()[start:end]
        cop.append_all(items)

        return cop

    def unique(self):
        uni = SingleChainedList()
        temp = {x for x in self.to_list()}
        list_temp = [x for x in temp]
        uni.append_all(list_temp)
        self.head = uni.head


class SingleChainedListIter:
    def __init__(self, chained_list: SingleChainedList):
        self.cur_element = chained_list.head

    def __iter__(self) -> "SingleChainedListIter":
        return self

    def __next__(self) -> SingleChainedListItem:
        if self.cur_element != None:
            temp = self.cur_element
            self.cur_element = self.cur_element.get_next_item()
            return temp.get_obj()
        raise StopIteration


def test_chained_list():
    clist = SingleChainedList()
    print("Leere Liste:")
    print(clist)

    a = 4
    clist.append(a)
    print(f"\nAppend {a}:")
    print(clist)

    a = [7, 2, 5, 0, 1, 2, 9]
    clist.append_all(a)
    print(f"\nAppend list {a}:")
    print(clist)

    a = 7
    b = 3
    clist.insert_after(a, b)
    print(f"\nInsert {b} after {a}:")
    print(clist)

    a = 2
    b = 8
    clist.insert_at(a, b)
    print(f"\nInsert {b} at index {a}:")
    print(clist)

    clist.pop()
    print("\nPop:")
    print(clist)

    a = 8
    clist.delete_obj(a)
    print(f"\nDelete {a}:")
    print(clist)

    a = 2
    clist.delete_at(a)
    print(f"\nDelete at index {a}:")
    print(clist)

    a = 3
    print(f"\nGet item at index {a}: \t{clist.get(a)}")

    a = 7
    print(f"\nFind object {a}: \t{clist.find(a)} ")

    print(f"\nFirst elemenet: {clist.get_first()}")
    print(f"Last element: \t{clist.get_last()}")

    print(f"\nTo list: \t{clist.to_list()}")
    print(f"Size: \t\t{clist.size()}")

    cop = clist.copy()
    print(f"\nCopy list: \t{cop}")

    cop.reverse()
    print(f"Reverse: \t{cop}")

    cop.shuffle()
    print(f"Shuffle: \t{cop}")

    cop.sort()
    print(f"Sort: \t\t{cop}")

    a = 1
    b = 5
    subl = cop.sublist(a, b)
    print(f"\nSublist from {a} to {b}:")
    print(subl)

    subl.unique()
    print("\nUnique items: ")
    print(subl)

    print("\nRepr:")
    print(subl.__repr__())


if __name__ == "__main__":
    test_chained_list()
