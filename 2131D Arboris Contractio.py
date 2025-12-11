def main():
    import sys
    data = sys.stdin.read().strip().split()
    index = 0
    total_tests = int(data[index])
    index += 1
    results = []
    for _ in range(total_tests):
        node_count = int(data[index])
        index += 1
        adjacency = [[] for _ in range(node_count + 1)]
        degree = [0] * (node_count + 1)
        for _ in range(node_count - 1):
            first = int(data[index])
            index += 1
            second = int(data[index])
            index += 1
            adjacency[first].append(second)
            adjacency[second].append(first)
            degree[first] += 1
            degree[second] += 1
        if node_count == 2:
            results.append("0")
            continue
        total_leaf_nodes = 0
        for vertex_id in range(1, node_count + 1):
            if degree[vertex_id] == 1:
                total_leaf_nodes += 1
        largest_leaf_connection = 0
        for current_vertex in range(1, node_count + 1):
            leaf_links = 0
            for neighbor in adjacency[current_vertex]:
                if degree[neighbor] == 1:
                    leaf_links += 1
            if leaf_links > largest_leaf_connection:
                largest_leaf_connection = leaf_links
        final_value = total_leaf_nodes - largest_leaf_connection
        results.append(str(final_value))
    sys.stdout.write("\n".join(results))
if __name__ == "__main__":
    main()