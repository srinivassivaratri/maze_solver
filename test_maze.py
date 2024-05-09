def test_reset_cells_visited():
    maze = Maze(0, 0, 3, 3, 10, 10)  # Create a maze object
    maze._reset_cells_visited()  # Reset cells visited
    for i in range(maze._num_cols):
        for j in range(maze._num_rows):
            assert maze._cells[i][j].visited == False  # Assert that all cells are not visited