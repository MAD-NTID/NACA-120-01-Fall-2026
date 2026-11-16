import my_math

def test_sum_a_plus_b_is_four():
    # setup
    a = 2
    b = 2
    expected = 4

    # invoke
    result = my_math.sum(a, b)

    # analyze (True/False)
    assert result == expected

def test_sum_a_plus_b_is_not_four():
    # setup
    a = 2
    b = 3
    expected = 4

    # invoke
    result = my_math.sum(a, b)

    # analyze (True/False)
    assert result != expected

def test_sum_a_plus_b_as_string_num_not_num():
        # setup
    a = 2
    b = "2"
    expected = 4

    # invoke
    result = my_math.sum(a, b)

    # analyze (True/False)
    assert result == expected

def test_sum_a_plus_b_as_string_value_not_num():
    # setup
    a = 2
    b = "hello"
    expected = None

    # invoke
    result = my_math.sum(a, b)

    # analyze (True/False)
    assert result == expected

def test_sum_a_plus_b_as_string_value_2_not_num():
    # setup
    a = "hello"
    b = "hello"
    expected = None

    # invoke
    result = my_math.sum(a, b)

    # analyze (True/False)
    assert result == expected