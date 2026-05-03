def first_task() -> None:
    from lup_solver import LUPSolver

    print("-" * 25 + f"{first_task.__name__}" + "-" * 25 + "\n")

    equations = [
        "2x + 2y - 2z - 8w = -20",
        "-8x + 4y + 4z + 7w = 6",
        "9x + 2y + 7z + 8w = 135",
        "5x - 5y + 2z + 4w = 51",
    ]

    solver = LUPSolver(equations)
    print("Original matrix:")
    for row in solver.get_matrix():
        print(row)
    solver.decompose()
    print("\nDecomposed matrix:")
    for row in solver.get_matrix():
        print(row)
    print("\nLower triangular matrix:")
    for row in solver.get_Lower_triangle():
        print(row)

    solution = solver.calculate_solution()
    print("\nSolution:", solution)


def second_task() -> None:
    from net_graph import NetworkGraph

    print("\n" + "-" * 25 + f"{second_task.__name__}" + "-" * 25 + "\n")
    initial_network = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    print("Initial network:")
    for row in initial_network:
        print(row)
    print("Starting Prim's algorithm from first node...")
    graph = NetworkGraph(initial_network)
    mst = graph.prime_algorithm()
    print("\nMinimum Spanning Tree using Prim's Algorithm:")
    for row in mst:
        print(row)


if __name__ == "__main__":
    first_task()
    second_task()
