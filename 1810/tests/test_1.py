import pytest
# 111111111111
# def python_string_slicer(str):
#    if len(str) < 50 or "python" in str:
#        return str
#    else:
#        return str[0:50]
#
#
# @pytest.fixture(scope="function", params=[
#    ("Короткая строка", "Короткая строка"),
#    ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
#     , "Длинная строка, не то чтобы прям очень длинная, но"),
#    ("Короткая строка со словом python", "Короткая строка со словом python"),
#    ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
#     , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python")],
#     ids = ["len < 50", "len > 50", "len < 50, contains pyton", "len > 50, containt pyton"])
# def param_fun(request):
#    return request.param
#
# def test_pyton_string_slicer(param_fun):
#     input_f, expected_out = param_fun
#     result = python_string_slicer(input_f)
#     print(f"Входная строка: {input_f} \nВыходная строка: {result} \nОжидаемое значение: {expected_out}")
#     assert result == expected_out

# 22222222222
# @pytest.mark.parametrize("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
# @pytest.mark.parametrize("y", [100, 1000], ids=["3 digit", "4 digit"])
# def test_multiply_params(x, y):
#    print(f"x: {x}, y: {y}")
#    assert True

# def  is_triangle(a, b, c):
#     if a <= c + b and b <= a + c and c <= a + b and a > 0 and b > 0 and c > 0:
#         return True
#     else:
#         return False
#
# @pytest.mark.parametrize("a", [-1, 0, 1, 4, 10], ids=["negative", "zero", "positive", "notbignotsmall", "big"])
# @pytest.mark.parametrize("b", [-1, 0, 1, 4, 10], ids=["negative", "zero", "positive", "notbignotsmall", "big"])
# @pytest.mark.parametrize("c", [-1, 0, 1, 4, 10], ids=["negative", "zero", "positive", "notbignotsmall", "big"])
# def test_is_triangle(a, b, c):
#     # print(f"a: {a}, b: {b}, c: {c}")
#     result = is_triangle(a, b, c)
#     assert result == True