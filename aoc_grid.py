import numpy as np
from colorama import Cursor
import os

os.system('cls')

grid = np.array(
    [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 2, 1],
        [1, 1, 1, 1, 1],
    ]
)

num_rows, num_cols = grid.shape
for row in range(num_rows):
    for col in range(num_cols):
        symbol = " *o"[grid[row, col]]
        print(f"{Cursor.POS(col + 1, row + 1)}{symbol}")


print(f"{Cursor.POS(50, 0)}text")
print("\n\n\n\n\n\n")
