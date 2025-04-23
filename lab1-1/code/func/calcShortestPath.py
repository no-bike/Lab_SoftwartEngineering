import heapq

def dijkstra(graph, start):
    """Dijkstra算法计算单源最短路径"""
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    prev_nodes = {node: None for node in graph.nodes}
    heap = [(0, start)]

    while heap:
        current_dist, current = heapq.heappop(heap)
        if current_dist > distances[current]:
            continue

        for (src, dest), weight in graph.edges.items():
            if src == current:
                new_dist = current_dist + weight
                if new_dist < distances[dest]:
                    distances[dest] = new_dist
                    prev_nodes[dest] = current
                    heapq.heappush(heap, (new_dist, dest))

    return distances, prev_nodes


def reconstruct_path(prev_nodes, target):
    """重建路径"""
    path = []
    while target is not None:
        path.append(target)
        target = prev_nodes[target]
    return path[::-1]


def find_shortest_path(graph, word1, word2):
    """查找并可视化最短路径"""
    word1, word2 = word1.lower(), word2.lower()

    # 检查节点存在性
    if word1 not in graph.nodes:
        return f"'{word1}' not in graph!"
    if word2 not in graph.nodes:
        return f"'{word2}' not in graph!"

    # 计算最短路径
    distances, prev_nodes = dijkstra(graph, word1)
    if distances[word2] == float('inf'):
        return f"No path from '{word1}' to '{word2}'!"

    path = reconstruct_path(prev_nodes, word2)

    # 格式化输出
    path_str = " → ".join(path)
    return f"Shortest path ({distances[word2]}): {path_str}"


def visualize_path(graph, path):
    """在CLI中突出显示路径"""
    print("\n" + "=" * 60)
    print("Shortest Path Visualization".center(60))
    print("=" * 60)

    max_len = max(len(node) for node in path) if path else 0
    for i in range(len(path) - 1):
        src, dest = path[i], path[i + 1]
        weight = graph.edges.get((src, dest), 0)
        print(f"{src.ljust(max_len)} ━━━[{weight}]━━━▶ {dest}")
    print("=" * 60)


def interactive_shortest_path(graph):
    """交互式最短路径查询"""
    print("\n" + "=" * 40)
    print("Shortest Path Finder".center(40))
    print("=" * 40)

    while True:
        input_str = input("\nEnter words (format: word1 word2) or 'q' to quit: ").strip()
        if input_str.lower() == 'q':
            break

        words = input_str.split()
        if len(words) == 1:
            # 单节点模式
            start = words[0].lower()
            if start not in graph.nodes:
                print(f"'{start}' not in graph!")
                continue

            distances, _ = dijkstra(graph, start)
            print(f"\nShortest paths from '{start}':")
            for node, dist in sorted(distances.items()):
                if node != start and dist != float('inf'):
                    print(f"  → {node}: {dist}")

        elif len(words) == 2:
            # 双节点模式
            result = find_shortest_path(graph, words[0], words[1])
            print("\n" + result)

            if "path" in result.lower():
                path = result.split(": ")[1].split(" → ")
                visualize_path(graph, path)

        else:
            print("Error: Please enter 1 or 2 words")