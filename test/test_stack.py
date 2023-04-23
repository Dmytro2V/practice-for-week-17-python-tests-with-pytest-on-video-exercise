from stack import Stack


def test_constructor_is_no_arg():
    Stack()


def test_new_stack_has_zero_elements():
    assert len(Stack()) == 0


def test_push_increases_length_by_one():
    s = Stack()
    s.push(None)
    assert len(s) == 1


def test_peek_returns_last_item_but_does_leaves_it_on_stack():
    s = Stack()
    s.push(6.28)
    assert s.peek() == 6.28
    assert len(s) == 1


def test_pop_returns_last_pushed_item_and_removes_it():

    s = Stack()
    s.push(6.28)

    result = s.pop()

    assert result == 6.28
    assert len(s) == 0


def test_push_lots_of_items_makes_the_length_large():

    s = Stack()

    for index in range(1000):
        s.push(index)

    assert len(s) == 1000


def test_popping_lots_of_values_makes_count_decrease():

    s = Stack()

    for index in range(100):
        s.push(index)
    for index in range(50):
        s.pop()

    # Assert
    assert len(s) == 50


def test_peeking_still_returns_last_pushed_element_not_popped():

    s = Stack()

    for index in range(100):
        s.push(index)
    for index in range(50):
        s.pop()

    assert s.peek() == 49
