def first_task() -> None:
    from lup_solver import LUPSolver

    equations = [
        "2x + 3y - z + 4w = 5",
        "-x + 4y + 2z - w = 3",
        "9x - 2y + 5z + 2w = 7",
        "x + y - 3z + 6w = 2",
    ]

    solver = LUPSolver(equations)
    print("Original matrix:")
    for row in solver.get_matrix():
        print(row)
    solver.decompose()
    print("Decomposed matrix:")
    for row in solver.get_matrix():
        print(row)
    print("Lower triangular matrix:")
    for row in solver.get_Lower_triangle():
        print(row)

    solution = solver.calculate_solution()
    print("Solution:", solution)


def second_task() -> None:
    from net_graph import NetworkGraph

    initial_network = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]

    graph = NetworkGraph(initial_network)
    mst = graph.prime_algorithm()
    for row in mst:
        print(row)


if __name__ == "__main__":
    first_task()
    second_task()
