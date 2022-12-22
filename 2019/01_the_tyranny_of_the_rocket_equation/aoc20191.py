import os
import pathlib

from aocd.models import Puzzle


os.environ["AOC_SESSION"] = "53616c7465645f5f8d306bee4b76ded123bae5a8186a8223cb8598a4e40c45bf45dfd536f0da518393030fc887c264d4d987971c0cb6246184eced0fb5d3b503"

PUZZLE_DIRECTORY = pathlib.Path(__file__).parent

with open(PUZZLE_DIRECTORY, mode='w'):
    

day1 = Puzzle(year=2019, day=1)
print(pathlib.Path(__file__).parent)
