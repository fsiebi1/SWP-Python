import random


class ListItem:
    obj: int
    next_item: "ListItem"

    def __init__(self, obj: int):
        self.obj = obj
        self.next_item = None

    def set_next_item(self, item: "ListItem"):
        self.next_item = item

    def get_next_item(self) -> "ListItem":
        return self.next_item

    def get_obj(self) -> int:
        return self.obj

    def __str__(self) -> str:
        return self.obj.__str__()


class ChainedList:
    def __init__(self):
        self.head = ListItem("head")

    def append(self, obj: int):
        new_item = ListItem(obj)
        if self.head.get_next_item() is None:
            self.head.set_next_item(new_item)
        else:
            self[self.size() - 1].set_next_item(new_item)

    def append_all(self, objs: list):
        for obj in objs:
            self.append(obj)

    def insert_after(self, prev_obj: int, new_obj: int) -> bool:
        index = self.find(prev_obj)
        if index == -1:
            return False

        self.insert_at(index + 1, new_obj)
        return True

    def insert_at(self, index: int, obj: int):
        if index > self.size():
            raise IndexError("list index out of range")

        if index == 0:
            prev_obj = self.head
        else:
            prev_obj = self[index - 1]
        new_item = ListItem(obj)
        new_item.set_next_item(prev_obj.get_next_item())
        prev_obj.set_next_item(new_item)

    def pop(self) -> bool:
        if self.size() == 0:
            return False
        if self.size() == 1:
            self.head.set_next_item(None)
        else:
            self[self.size() - 2].set_next_item(None)
        return True

    def delete_obj(self, obj: int) -> bool:
        index = self.find(obj)
        if index == -1:
            return False

        self.delete_at(index)
        return True

    def delete_at(self, index: int):
        if index == 0:
            self.head.set_next_item(self[1])
        else:
            self[index - 1].set_next_item(self[index].get_next_item())

    def get(self, index: int) -> ListItem:
        if index >= self.size():
            raise IndexError("list index out of range")

        ort = 0
        for item in self:
            if ort == index:
                return item
            ort += 1

        return None

    def find(self, obj: int) -> int:
        for i in range(self.size()):
            if self[i].get_obj() == obj:
                return i
        return -1

    def get_first(self) -> ListItem:
        if self.size() == 0:
            return None
        return self[0]

    def get_last(self) -> ListItem:
        if self.size() == 0:
            return None
        if self.size() == 1:
            return self.head.get_next_item()
        return self[self.size() - 1]

    def to_list(self) -> list:
        liste = []
        for o in self:
            liste.append(o.get_obj())

        return liste

    def size(self) -> int:
        anz = 0
        for _ in self:
            anz += 1

        return anz

    def __iter__(self) -> "ChainedListIter":
        return ChainedListIter(self)

    def __getitem__(self, index) -> ListItem:
        return self.get(index)

    def __str__(self) -> str:
        string = "["
        for i in self:
            string += i.get_obj().__str__() + ", "

        if len(string) > 1:
            string = string[:-2]
        return string + "]"

    def copy(self) -> "ChainedList":
        cop = ChainedList()
        items = self.to_list()
        cop.append_all(items)

        return cop

    def reverse(self):
        objs = self.to_list()
        objs.reverse()
        neu = ChainedList()
        neu.append_all(objs)

        self.head = neu.head

    def sort(self):
        objs = self.to_list()
        objs.sort()
        sorted = ChainedList()
        sorted.append_all(objs)

        self.head = sorted.head

    def shuffle(self):
        objs = self.to_list()
        random.shuffle(objs)
        shuffled = ChainedList()
        shuffled.append_all(objs)

        self.head = shuffled.head

    def sublist(self, start: int, end: int = -1) -> "ChainedList":
        if start < 0 or start >= self.size():
            raise IndexError("list index out of range")
        if end == -1:
            end = self.size()
        if end > self.size():
            raise IndexError("list index out of range")
        if end <= start:
            raise ValueError("end must not be less or equal to start")

        cop = ChainedList()
        items = self.to_list()[start:end]
        cop.append_all(items)

        return cop

    def unique(self):
        uni = ChainedList()
        temp = {x for x in self.to_list()}
        uni.append_all(temp)
        self.head = uni.head


class ChainedListIter:
    def __init__(self, chained_list: ChainedList):
        self.cur_element = chained_list.head

    def __iter__(self) -> "ChainedListIter":
        return self

    def __next__(self) -> ListItem:
        self.cur_element = self.cur_element.get_next_item()
        if self.cur_element != None:
            return self.cur_element
        raise StopIteration


def test_chained_list():
    clist = ChainedList()
    print("Leere Liste:")
    print(clist)

    clist.append(4)
    print("\nAppend 4:")
    print(clist)

    a = [7, 2, 5, 0, 1, 2, 9]
    clist.append_all(a)
    print("\nAppend list [7, 2, 5, 0, 1, 9]:")
    print(clist)

    clist.insert_after(7, 3)
    print("\nInsert 3 after 7:")
    print(clist)

    clist.insert_at(2, 8)
    print("\nInsert 8 at index 2:")
    print(clist)

    clist.pop()
    print("\nPop:")
    print(clist)

    clist.delete_obj(8)
    print("\nDelete 8:")
    print(clist)

    clist.delete_at(2)
    print("\nDelete at index 2:")
    print(clist)

    print(f"\nGet item at index 3: \t{clist.get(3)}")

    print(f"\nFind object 7: \t{clist.find(7)} ")

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

    subl = cop.sublist(1, 5)
    print("\nSublist from 1 to 5:")
    print(subl)

    subl.unique()
    print("\nUnique items: ")
    print(subl)


if __name__ == "__main__":
    test_chained_list()
