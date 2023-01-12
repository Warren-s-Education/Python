import pytest

# def test_always_passes():
#     assert True


# def test_always_fails():
#     assert False


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)], ids=["sum of 3 and 5 is 8", "2+4=6", "6*9=54"])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval2(test_input, expected):
    assert eval(test_input) == expected


def format_data_excel(data):
    return "excel: Mike, John"


def format_data_pdf(data):
    return "pdf: Mike, John"


@pytest.fixture
def people_data():
    return ['Mike', 'John']


@pytest.mark.parametrize("format_func, expected_result", [
    (format_data_excel, 'excel: Mike, John'),
    (format_data_pdf, "pdf: Mike, John")])
def test_formats(people_data, format_func, expected_result):
    assert format_func(people_data) == expected_result
