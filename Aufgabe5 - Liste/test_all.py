from liste import ChainedList, ListItem


def test_to_str():
    clist = ChainedList()
    assert clist.__str__() == "[]"

    new_item = ListItem(1)
    clist.head.set_next_item(new_item)
    assert clist.__str__() == "[1]"

    new_item2 = ListItem(2)
    clist.head.get_next_item().set_next_item(new_item2)
    assert clist.__str__() == "[1, 2]"


def test_append():
    clist = ChainedList()
    clist.append(1)
    clist.append(2)

    assert clist.__str__() == "[1, 2]"


def test_insert_after():
    pass
