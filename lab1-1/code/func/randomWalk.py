import random
import time
from datetime import datetime


def random_walk(graph, start_node=None, max_steps=1000):
    """
    随机游走直到重复边或终止节点
    :return: (路径节点列表, 经过的边集合)
    """
    if start_node is None:
        start_node = random.choice(list(graph.nodes))

    current = start_node.lower()
    if current not in graph.nodes:
        return [], set()

    path = [current]
    visited_edges = set()
    stop_reason = None

    for _ in range(max_steps):
        # 获取当前节点的出边
        out_edges = [(dest, w) for (src, dest), w in graph.edges.items() if src == current]

        # 终止条件1：无出边
        if not out_edges:
            stop_reason = "dead-end"
            break

        # 随机选择下一条边（按权重概率选择）
        destinations, weights = zip(*out_edges)
        total_weight = sum(weights)
        rand_val = random.uniform(0, total_weight)
        cumulative = 0
        for dest, w in out_edges:
            cumulative += w
            if rand_val <= cumulative:
                edge = (current, dest)
                # 终止条件2：重复边
                if edge in visited_edges:
                    stop_reason = "repeated-edge"
                    break
                visited_edges.add(edge)
                current = dest
                path.append(current)
                break
        else:
            continue
        if stop_reason:
            break

    return path, visited_edges, stop_reason


def interactive_random_walk(graph):
    """交互式随机游走控制器"""
    print("\n" + "=" * 60)
    print("Interactive Random Walk".center(60))
    print("=" * 60)

    # 用户选择起点
    start = input(f"Enter start node (or press Enter to random select from {len(graph.nodes)} nodes): ").strip().lower()
    if not start:
        start = None
    elif start not in graph.nodes:
        print(f"Node '{start}' not found in graph!")
        return

    # 开始游走
    walk_log = []
    path, edges, reason = [], set(), None
    try:
        for i in range(1, 101):  # 最大100步安全限制
            path, edges, reason = random_walk(graph, start, max_steps=i)
            walk_log.append(path[-1])

            # 实时显示
            print(f"\nStep {i}: {path[-1]}", end="")
            if i % 10 == 0:
                print(f"\nCurrent path: {' → '.join(path[-10:])}")

            # 检查终止条件
            if reason:
                print(f"\n\nTermination: {reason}")
                break

            # 用户控制
            if input("\nContinue? (Enter=yes, s=stop): ").lower() == 's':
                print("\nUser stopped the walk")
                break

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nWalk interrupted by user")

    # 保存结果
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"../picture/random_walk_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(" ".join(path))
    print(f"\nWalk saved to {filename}")

    # 显示统计信息
    print("\nWalk Statistics:")
    print(f"- Total steps: {len(path)}")
    print(f"- Unique nodes visited: {len(set(path))}")
    print(f"- Unique edges traversed: {len(edges)}")
    print(f"- Final path: {' → '.join(path[-10:])}")