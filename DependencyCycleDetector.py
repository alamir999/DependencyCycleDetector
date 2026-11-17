def has_cycle(graph, node, visited, path):
    visited.add(node)
    path.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, path):
                return True
        elif neighbor in path:
            return True
    path.remove(node)
    return False

def main():
    print("Enter dependencies (e.g., 'A B' means A depends on B).")
    print("Type 'done' to finish.\n")
    graph = {}
    while True:
        line = input("Dep: ")
        if line.lower() == 'done':
            break
        parts = line.split()
        if len(parts) == 2:
            u, v = parts[0], parts[1]
            if u not in graph:
                graph[u] = []
            graph[u].append(v)

            if v not in graph:
                graph[v] = []
    visited = set()
    path = set()
    cycle_found = False
    for node in graph:
        if node not in visited:
            print(f"Checking path starting at '{node}'...")
            if has_cycle(graph, node, visited, path):
                cycle_found = True
                break
    print("-" * 40)
    if cycle_found:
        print("Result: Cycle Detected! The tasks cannot be completed.")
    else:
        print("Result: No cycles found. All tasks are valid.")
    print("-" * 40)
if __name__ == "__main__":
    main()