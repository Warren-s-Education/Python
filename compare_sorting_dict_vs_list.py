#comparing_sorting_dict_vs_list.py

from timeit import timeit
from samples import dictionary_of_dictionaries, list_of_dictionaries

sorting_list = """
sorted(
    list_of_dictionaries,
    key=lambda item: item['age']
)"""

sorting_dict = """
dict(
    sorted(
        dictionary_of_dictionaries.items(),
        key=lambda item: item[1]['age']
    )
)
"""

sorting_list_time = timeit(
    stmt=sorting_list,
    globals=globals()
)

sorting_dict_time = timeit(
    stmt=sorting_dict,
    globals=globals()
)

print(
    f"""\
{sorting_list_time = :.2f}
{sorting_dict_time = :.2f}
list is {sorting_dict_time/sorting_list_time :.2f} faster
"""
)
