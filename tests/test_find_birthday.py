import pytest
from src.Congratulator.find_birthday import find_birthday

# import importlib.util
#
#
# spec = importlib.util.spec_from_file_location(
#     name="my_module",  # note that ".test" is not a valid module name
#     # location="/path/to/.test.py",
#     location=r"C:\Users\Иван\PycharmProjects\Congratulator\src\Congratulator\find_birthday.py",
# )
# my_module = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(my_module)
# find_birthday = my_module.find_birthday


class TestTasksSuite:
    # Фикстура и параметризатор для позитивного тестирования
    @pytest.fixture(
        scope='function',
        params=[('-08-15', (['dualking1991@gmail.com', 'JackSlater777@yandex.ru'], ['test1', 'test2'])),
                ('-1', (['dualking1991@gmail.com', 'JackSlater777@yandex.ru', 'fletcher-lind@mail.ru'], ['test1', 'test2', 'test3'])),
                ('2022.08.08', ([], [])),
                ('', (['dualking1991@gmail.com', 'JackSlater777@yandex.ru', 'fletcher-lind@mail.ru'],
                      ['test1', 'test2', 'test3']))],
        ids=lambda args: f"Test with args: {args}"
    )
    def parametrize_find_birthday_pos(self, request):
        return request.param

    # Позитивный тест-кейс
    def test_find_birthday_pos(self, parametrize_find_birthday_pos):
        data, result = parametrize_find_birthday_pos
        assert find_birthday(data, [], []) == result

    # Фикстура и параметризатор для негативного тестирования
    @pytest.fixture(
        scope='function',
        params=[(set(), ([], [])),
                ([], ([], [])),
                ({}, ([], [])),
                (-1, ([], [])), ],
        ids=lambda args: f"Test with args: {args}"
    )
    def parametrize_find_birthday_neg(self, request):
        return request.param

    # Негативный тест-кейс
    def test_find_birthday_neg_2(self, parametrize_find_birthday_neg):
        data, result = parametrize_find_birthday_neg
        with pytest.raises(TypeError):
            find_birthday(data, [], [])


if __name__ == '__main__':
    pytest.main()
