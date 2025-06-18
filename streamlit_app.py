import streamlit as st
from solver import solve_sudoku, validate_input
from puzzles import get_random_puzzle_from_dataset

st.title("🧠 Sudoku Solver")

if "grid" not in st.session_state:
    puzzle, solution = get_random_puzzle_from_dataset()
    st.session_state.grid = puzzle
    st.session_state.solution = solution

if st.button("🔀 Generate New Puzzle"):
    puzzle, solution = get_random_puzzle_from_dataset()
    st.session_state.grid = puzzle
    st.session_state.solution = solution

input_grid = []
st.write("### 🎯 Input Sudoku")
for i in range(9):
    cols = st.columns(9)
    row = []
    for j in range(9):
        value = st.session_state.grid[i][j]
        num = cols[j].number_input("", min_value=0, max_value=9, value=value, key=f"{i}-{j}")
        row.append(num)
    input_grid.append(row)

if st.button("✅ Solve Puzzle"):
    board = [row[:] for row in input_grid]  # Deep copy
    if solve_sudoku(board):
        st.success("Solution found:")
        for i in range(9):
            cols = st.columns(9)
            for j in range(9):
                cols[j].text_input("", value=str(board[i][j]), key=f"sol-{i}-{j}")
    else:
        st.error("No solution found!")

board = st.session_state.solution
status_grid = validate_input(input_grid, board)

st.write("### ✅ Feedback Grid")

for i in range(9):
    cols = st.columns(9)
    for j in range(9):
        cell_val = input_grid[i][j]
        status = status_grid[i][j]
        display = "" if cell_val == 0 else str(cell_val)
        bg_color = {
            "correct": "lightgreen",
            "wrong": "tomato",
            "empty": "#f0f0f0"
        }[status]
        
        border_style = "2px solid black" if i % 3 == 0 or j % 3 == 0 else "1px solid gray"

        cols[j].markdown(
            f"<div style='background-color:{bg_color}; padding:10px; text-align:center; border:{border_style}; border-radius:5px'>{display}</div>",
            unsafe_allow_html=True
        )

