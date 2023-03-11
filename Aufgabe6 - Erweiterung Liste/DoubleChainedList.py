#%%

import random
from typing import List, Tuple


class DoubleChainedListItem:
    obj: int
    _next_item: "DoubleChainedListItem"
    _prev_item: "DoubleChainedListItem"

    def __init__(self, obj: int):
        self.obj = obj
        self._next_item = None
        self._prev_item = None

    def set_next_item(self, item: "DoubleChainedListItem"):
        self._next_item = item

    def get_next_item(self) -> "DoubleChainedListItem":
        return self._next_item

    def set_prev_item(self, item: "DoubleChainedListItem"):
        self._prev_item = item

    def get_prev_item(self) -> "DoubleChainedListItem":
        return self._prev_item

    def get_obj(self) -> int:
        return self.obj

    def set_obj(self, obj: int):
        self.obj = obj

    def __str__(self) -> str:
        return self.obj.__str__()


class DoubleChainedList:
    head: DoubleChainedListItem
    tail: DoubleChainedListItem

    def __init__(self, objs: List[int] = []):
        self.head = None
        self.tail = None
        self.append_all(objs)

    def append(self, obj: int):
        new_item = DoubleChainedListItem(obj)
        if self.tail is None:
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.set_next_item(new_item)
            new_item.set_prev_item(self.tail)
            self.tail = new_item

    def append_all(self, objs: List[int]):
        if len(objs) == 0:
            return
        if len(objs) == 1:
            self.append(objs[0])
            return

        first_item = DoubleChainedListItem(objs[0])
        cur_item = first_item
        for obj in objs[1:]:
            new_item = DoubleChainedListItem(obj)
            cur_item.set_next_item(new_item)
            new_item.set_prev_item(cur_item)

            cur_item = new_item

        self._append_item(first_item, cur_item)

    def _append_item(
        self, first_item: DoubleChainedListItem, last_item: DoubleChainedListItem
    ):
        if self.tail is None:
            self.head = first_item
            self.tail = last_item
        else:
            self.tail.set_next_item(first_item)
            first_item.set_prev_item(self.tail)
            self.tail = last_item

    def append_front(self, obj: int):
        new_item = DoubleChainedListItem(obj)
        if self.head is None:
            self.head = new_item
            self.tail = new_item
        else:
            self.head.set_prev_item(new_item)
            new_item.set_next_item(self.head)
            self.head = new_item

    def append_front_all(self, objs: List[int]):
        if len(objs) == 0:
            return
        if len(objs) == 1:
            self.append_front(objs[0])
            return

        first_item = DoubleChainedListItem(objs[0])
        cur_item = first_item
        for obj in objs[1:]:
            new_item = DoubleChainedListItem(obj)
            cur_item.set_next_item(new_item)
            new_item.set_prev_item(cur_item)

            cur_item = new_item

        self._append_front_item(first_item, cur_item)

    def _append_front_item(
        self, first_item: DoubleChainedListItem, last_item: DoubleChainedListItem
    ):
        if self.head is None:
            self.head = first_item
            self.tail = last_item
        else:
            self.head.set_prev_item(last_item)
            last_item.set_next_item(self.head)
            self.head = first_item

    def insert_after(self, obj: int, after: int) -> bool:
        new_item = DoubleChainedListItem(obj)
        cur_item = self.head
        while cur_item is not None:
            if cur_item.get_obj() == after:
                new_item.set_next_item(cur_item.get_next_item())
                new_item.set_prev_item(cur_item)
                cur_item.set_next_item(new_item)

                if new_item.get_next_item() is not None:
                    new_item.get_next_item().set_prev_item(new_item)
                else:
                    self.tail = new_item
                return True

            cur_item = cur_item.get_next_item()

        return False

    def insert_at(self, obj: int, index: int) -> bool:
        if index >= self.size() or index < 0:
            raise IndexError("List index out of range")

        new_item = DoubleChainedListItem(obj)
        if index < self.size() / 2:
            cur_item = self.head
            cur_index = 0
            while cur_item is not None:
                if cur_index == index:
                    new_item.set_next_item(cur_item)
                    new_item.set_prev_item(cur_item.get_prev_item())
                    cur_item.set_prev_item(new_item)

                    if new_item.get_prev_item() is not None:
                        new_item.get_prev_item().set_next_item(new_item)
                    else:
                        self.head = new_item
                    return True

                cur_item = cur_item.get_next_item()
                cur_index += 1
        else:
            cur_item = self.tail
            cur_index = self.size() - 1
            while cur_item is not None:
                if cur_index == index:
                    new_item.set_prev_item(cur_item)
                    new_item.set_next_item(cur_item.get_next_item())
                    cur_item.set_next_item(new_item)

                    if new_item.get_next_item() is not None:
                        new_item.get_next_item().set_prev_item(new_item)
                    else:
                        self.tail = new_item
                    return True

                cur_item = cur_item.get_prev_item()
                cur_index -= 1

        return False

    def remove(self, obj: int) -> bool:
        cur_item = self.head
        while cur_item is not None:
            if cur_item.get_obj() == obj:
                if cur_item.get_prev_item() is not None:
                    cur_item.get_prev_item().set_next_item(cur_item.get_next_item())
                else:
                    self.head = cur_item.get_next_item()

                if cur_item.get_next_item() is not None:
                    cur_item.get_next_item().set_prev_item(cur_item.get_prev_item())
                else:
                    self.tail = cur_item.get_prev_item()

                return True

            cur_item = cur_item.get_next_item()

        return False

    def remove_at(self, index: int) -> bool:
        if index >= self.size() or index < 0:
            raise IndexError("List index out of range")

        if index < self.size() / 2:
            cur_item = self.head
            cur_index = 0
            while cur_item is not None:
                if cur_index == index:
                    if cur_item.get_prev_item() is not None:
                        cur_item.get_prev_item().set_next_item(cur_item.get_next_item())
                    else:
                        self.head = cur_item.get_next_item()

                    if cur_item.get_next_item() is not None:
                        cur_item.get_next_item().set_prev_item(cur_item.get_prev_item())
                    else:
                        self.tail = cur_item.get_prev_item()

                    return True

                cur_item = cur_item.get_next_item()
                cur_index += 1
        else:
            cur_item = self.tail
            cur_index = self.size() - 1
            while cur_item is not None:
                if cur_index == index:
                    if cur_item.get_prev_item() is not None:
                        cur_item.get_prev_item().set_next_item(cur_item.get_next_item())
                    else:
                        self.head = cur_item.get_next_item()

                    if cur_item.get_next_item() is not None:
                        cur_item.get_next_item().set_prev_item(cur_item.get_prev_item())
                    else:
                        self.tail = cur_item.get_prev_item()

                    return True

                cur_item = cur_item.get_prev_item()
                cur_index -= 1

        return False

    def find(self, obj: int) -> int:
        cur_item = self.head
        cur_index = 0
        while cur_item is not None:
            if cur_item.get_obj() == obj:
                return cur_index

            cur_item = cur_item.get_next_item()
            cur_index += 1

        return -1

    def get(self, index: int) -> int:
        item = self._get_list_item(index)
        if item is not None:
            return item.get_obj()
        return None

    def _get_list_item(self, index: int) -> DoubleChainedListItem:
        if index >= self.size() or index < 0:
            raise IndexError("List index out of range")

        if index < self.size() / 2:
            cur_item = self.head
            cur_index = 0
            while cur_item is not None:
                if cur_index == index:
                    return cur_item

                cur_item = cur_item.get_next_item()
                cur_index += 1
        else:
            cur_item = self.tail
            cur_index = self.size() - 1
            while cur_item is not None:
                if cur_index == index:
                    return cur_item

                cur_item = cur_item.get_prev_item()
                cur_index -= 1

        return None

    def get_first(self) -> int:
        if self.head is not None:
            return self.head.get_obj()
        return None

    def get_last(self) -> int:
        if self.tail is not None:
            return self.tail.get_obj()
        return None

    def set(self, index: int, obj: int) -> bool:
        item = self._get_list_item(index)
        if item is not None:
            item.set_obj(obj)
            return True
        return False

    def get_head(self) -> DoubleChainedListItem:
        return self.head

    def get_tail(self) -> DoubleChainedListItem:
        return self.tail

    def set_head(self, head: DoubleChainedListItem):
        self.head = head

    def to_list(self) -> list:
        result = []
        cur_item = self.head
        while cur_item is not None:
            result.append(cur_item.get_obj())
            cur_item = cur_item.get_next_item()
        return result

    def to_list_reverse(self) -> list:
        result = []
        cur_item = self.tail
        while cur_item is not None:
            result.append(cur_item.get_obj())
            cur_item = cur_item.get_prev_item()
        return result

    def size(self) -> int:
        cur_item = self.head
        size = 0
        while cur_item is not None:
            size += 1
            cur_item = cur_item.get_next_item()
        return size

    def copy(self):
        return DoubleChainedList(self.to_list())

    def reverse(self):
        self.head, self.tail = self.tail, self.head
        cur_item = self.head
        while cur_item is not None:
            cur_item.set_next_item(cur_item.get_prev_item())
            cur_item.set_prev_item(cur_item.get_next_item())
            cur_item = cur_item.get_next_item()

    def _split(
        self, head: DoubleChainedListItem
    ) -> Tuple[DoubleChainedListItem, DoubleChainedListItem]:
        if head is None or head.get_next_item() is None:
            return head, None

        slow = head
        fast = head.get_next_item()
        while fast is not None:
            fast = fast.get_next_item()
            if fast is not None:
                slow = slow.get_next_item()
                fast = fast.get_next_item()

        right = slow.get_next_item()
        slow.set_next_item(None)
        return head, right

    def _merge(
        self, left: DoubleChainedListItem, right: DoubleChainedListItem
    ) -> DoubleChainedListItem:
        if left is None:
            return right
        if right is None:
            return left

        if left.get_obj() <= right.get_obj():
            left.set_next_item(self._merge(left.get_next_item(), right))
            left.get_next_item().set_prev_item(left)
            left.set_prev_item(None)
            return left
        else:
            right.set_next_item(self._merge(left, right.get_next_item()))
            right.get_next_item().set_prev_item(right)
            right.set_prev_item(None)
            return right

    def _merge_sort(self, head: DoubleChainedListItem) -> DoubleChainedListItem:
        if head is None or head.get_next_item() is None:
            return head

        left, right = self._split(head)
        left = self._merge_sort(left)
        right = self._merge_sort(right)
        return self._merge(left, right)

    def sort(self):
        self.head = self._merge_sort(self.head)
        cur_item = self.head
        while cur_item.get_next_item() is not None:
            cur_item = cur_item.get_next_item()
        self.tail = cur_item

    def sublist(self, start: int, end: int = -1) -> "DoubleChainedList":
        if start < 0 or start >= self.size():
            raise IndexError("List index out of range")
        if end == -1:
            end = self.size()
        if end > self.size():
            raise IndexError("List index out of range")
        if end <= start:
            raise ValueError("end must not be less or equal to start")

        return DoubleChainedList(self.to_list()[start:end])

    def __str__(self):
        return str(self.to_list())

    def __repr__(self):
        return f"DoubleChainedList({self.to_list()})"

    def __len__(self):
        return self.size()

    def __getitem__(self, index: int):
        return self.get(index)

    def __setitem__(self, index: int, obj: int):
        self.set(index, obj)

    def __eq__(self, other: "DoubleChainedList"):
        if isinstance(other, DoubleChainedList):
            return self.to_list() == other.to_list()
        return False

    def __ne__(self, other: "DoubleChainedList"):
        return not self.__eq__(other)

    def __iter__(self):
        return DoubleChainedListIterator(self)

    def __reversed__(self):
        return DoubleChainedListReverseIterator(self)

    def __contains__(self, item: int):
        return self.find(item) != -1


class DoubleChainedListIterator:
    def __init__(self, double_chained_list: DoubleChainedList):
        self.double_chained_list = double_chained_list
        self.cur_item = self.double_chained_list.get_head()

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_item is not None:
            cur_item = self.cur_item
            self.cur_item = self.cur_item.get_next_item()
            return cur_item.get_obj()
        raise StopIteration


class DoubleChainedListReverseIterator:
    def __init__(self, double_chained_list: DoubleChainedList):
        self.double_chained_list = double_chained_list
        self.cur_item = self.double_chained_list.get_tail()

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_item is not None:
            cur_item = self.cur_item
            self.cur_item = self.cur_item.get_prev_item()
            return cur_item.get_obj()
        raise StopIteration


def test_chained_list():
    clist = DoubleChainedList()
    print("Leere Liste: ")
    print(clist)

    a = 4
    clist.append(a)
    print(f"\nAppend {a}: ")
    print(clist)

    a = [1, 2, 3, 4, 5]
    clist.append_all(a)
    print(f"\nAppend {a}: ")
    print(clist)

    a = 6
    clist.append_front(a)
    print(f"\nAppend Front {a}: ")
    print(clist)

    a = [7, 8, 9, 10, 11]
    clist.append_front_all(a)
    print(f"\nAppend Front {a}: ")
    print(clist)

    a = 12
    b = 11
    clist.insert_after(a, b)
    print(f"\nInsert {a} after {b}: ")
    print(clist)

    a = 13
    b = 6
    clist.insert_at(a, b)
    print(f"\nInsert {a} at {b}: ")
    print(clist)

    a = 1
    clist.remove(a)
    print(f"\nRemove {a}: ")
    print(clist)

    a = 7
    clist.remove_at(a)
    print(f"\nRemove at {a}: ")
    print(clist)

    a = 11
    print(f"\nFind {a}: {clist.find(a)}")

    a = 9
    print(f"Get {a}: {clist.get(a)}")

    a = 14
    b = 7
    clist.set(b, a)
    print(f"\nSet {a} at {b}: ")
    print(clist)

    print(f"\nSize: {clist.size()}")
    print(f"Head: {clist.get_head()}")
    print(f"Tail: {clist.get_tail()}")
    print(f"\nList: \n{clist.to_list()}")
    print(f"\nReversed List: \n{clist.to_list_reverse()}")

    a = 2
    b = 10
    sublist = clist.sublist(a, b)
    print(f"\nSublist from {a} to {b}:")
    print(sublist)

    print("\nRepresentation: ")
    print(clist.__repr__())

    clist.sort()
    print(f"\nSort: ")
    print(clist)


if __name__ == "__main__":
    test_chained_list()
