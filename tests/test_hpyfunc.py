import inspect

from . import hpyfunc


def test_hpyfunc():
    test_list = [1, 2, 3, [4, 5, [6, 7]]]
    assert [1, 2, 3, 4, 5, 6, 7] == hpyfunc.flatten(test_list)
    assert [1, 2, 3, 4, 5, [6, 7]] == hpyfunc.flatten_layer(test_list)
    assert [1, 2, 3, 4, 5, 6, 7] == hpyfunc.flatten_no_recursion(test_list)
    assert [[1, 2], [3, 4]] == hpyfunc.expand_dims([1, 2, 3, 4], 2, 2)

    easy_text_hash = hpyfunc.easy_text_hash

    def fun_name_aaa():
        """给组员：你要是改了，有你好果子吃,,,"""
        if not easy_text_hash(inspect.getsource(fun_name_aaa)) == "!!!":  # ""里面的是标识符
            print("改了是吧，有你好果子吃")

    assert "283" == hpyfunc.dont_change_my_code(fun=fun_name_aaa, sign="!!!")
    assert "283" == hpyfunc.dont_change_my_code(
        fun=fun_name_aaa, sign="!!!", hash_fun=easy_text_hash, multisign=True
    )
