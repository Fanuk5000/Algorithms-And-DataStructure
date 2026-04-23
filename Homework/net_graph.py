class NetworkGraph:
    def __init__(self, matrix: list[list[int]]):
        self.__num_nodes = len(matrix)
        self.__validate_symmetry(matrix)

        self.__matrix = matrix
        self.__square_matrix(self.__matrix)

    def __validate_symmetry(self, matrix: list[list[int]]):
        for i in range(self.__num_nodes):
            for j in range(self.__num_nodes):
                if matrix[i][j] != matrix[j][i]:
                    raise ValueError(
                        f"PC`s connection matrix must be symmetric, but found asymmetry between ({i}, {j}) "
                        f"(written {matrix[i][j]} and {matrix[j][i]})."
                    )

    def __square_matrix(self, matrix: list[list[int]]) -> None:
        for i in range(self.__num_nodes):
            for j in range(self.__num_nodes):
                matrix[i][j] = matrix[i][j] ** 2

    def prime_algorithm(self) -> list[list[float]]:
        mst_matrix: list[list[float]] = [
            [0] * self.__num_nodes for _ in range(self.__num_nodes)
        ]

        visited_nodes = set()
        visited_nodes.add(0)

        edges_count = 0

        while edges_count < self.__num_nodes - 1:
            min_weight = float("inf")
            best_visited = -1
            best_new = -1

            for node in visited_nodes:
                for new_node in range(self.__num_nodes):
                    if (
                        new_node not in visited_nodes
                        and self.__matrix[node][new_node] > 0
                    ):
                        if self.__matrix[node][new_node] < min_weight:
                            min_weight = self.__matrix[node][new_node]
                            best_visited = node
                            best_new = new_node

            if best_new != -1 and best_visited != -1:
                visited_nodes.add(best_new)
                mst_matrix[best_visited][best_new] = min_weight
                mst_matrix[best_new][best_visited] = min_weight
                edges_count += 1

        return mst_matrix
