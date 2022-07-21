from . import hpyfunc


def test_hpyfunc():
    test_list = [1, 2, 3, [4, 5, [6, 7]]]
    assert [1, 2, 3, 4, 5, 6, 7] == hpyfunc.flatten(test_list)
    assert [1, 2, 3, 4, 5, [6, 7]] == hpyfunc.flatten_layer(test_list)
    assert [1, 2, 3, 4, 5, 6, 7] == hpyfunc.flatten_no_recursion(test_list)
    assert [[1, 2], [3, 4]] == hpyfunc.expand_dims([1, 2, 3, 4], 2, 2)
