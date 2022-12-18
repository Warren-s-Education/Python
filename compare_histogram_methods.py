from timeit import timeit
from os import strerror

try:
    stream = open('histogram_v2.py')
    case_1_statement = stream.read()
    stream.close()

    stream = open('histogram_v3.py')
    case_2_statement = stream.read()
    stream.close()

    # print(case_1_statement)
    # print("\n\n")
    # print(case_2_statement)
except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)

case_1_time = timeit(stmt=case_1_statement, globals=globals())
case_2_time = timeit(stmt=case_2_statement, globals=globals())

print(
    f"""\
{case_1_time = :.2f}
{case_2_time = :.2f}
"""
)
