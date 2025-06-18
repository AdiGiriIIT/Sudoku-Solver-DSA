import pandas as pd
import random
import os

DATASET_PATH = "/home/aditya/sudoku_solver/data/sudoku.csv"

def load_dataset():
    df = pd.read_csv(DATASET_PATH)
    return df

def get_random_puzzle_from_dataset():
    df = load_dataset()
    row = df.sample(1).iloc[0]
    puzzle_str = row['quizzes']
    solution_str = row['solutions']

    puzzle = [[int(puzzle_str[i * 9 + j]) for j in range(9)] for i in range(9)]
    solution = [[int(solution_str[i * 9 + j]) for j in range(9)] for i in range(9)]

    return puzzle, solution
