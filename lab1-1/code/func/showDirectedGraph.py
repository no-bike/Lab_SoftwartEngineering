from collections import defaultdict


def display_graph_cli(graph):
    """优化后的命令行可视化输出"""
    print("\n" + "=" * 40)
    print("Directed Word Co-occurrence Graph".center(40))
    print("=" * 40)

    # 节点统计
    print(f"\nNodes ({len(graph.nodes)}):")
    print(", ".join(sorted(graph.nodes)))

    # 边统计（按权重排序）
    print(f"\nEdges ({len(graph.edges)}):")
    max_src_len = max(len(src) for src, _ in graph.edges.keys()) if graph.edges else 0
    sorted_edges = sorted(graph.edges.items(), key=lambda x: -x[1])

    for (src, dest), weight in sorted_edges:
        arrow = "→"
        print(f"{src.ljust(max_src_len)} {arrow} {dest.ljust(max_src_len)} [weight: {weight}]")

    # 权重分布统计
    weight_counts = defaultdict(int)
    for w in graph.edges.values():
        weight_counts[w] += 1
    print("\nWeight Distribution:")
    for w, count in sorted(weight_counts.items()):
        print(f"  {w}: {count} edges")


def export_graph_image(graph, graph_name = 'graph',filename="D:\\repos\Lab_SoftwartEngineering\lab1-1\picture\graph"):
    """通过Graphviz自动生成可视化图形"""
    try:
        from graphviz import Digraph
    except ImportError:
        print("Warning: graphviz not installed. Run 'pip install graphviz'")
        return False

    dot = Digraph(comment=graph_name)

    # 添加节点
    for node in graph.nodes:
        dot.node(node)

    # 添加边（线宽反映权重）
    for (src, dest), weight in graph.edges.items():
        dot.edge(src, dest, label=str(weight), penwidth=str(0.5 + weight / 2))
    filename = f"{filename}_{graph_name}"
    # 保存文件
    dot.render(filename, format='svg', cleanup=True)
    print(f"Graph exported to {filename}")
    return True