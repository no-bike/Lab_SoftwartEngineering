import re

def find_bridge_words(graph, word1, word2):
    """查找桥接词核心逻辑"""
    word1, word2 = word1.lower(), word2.lower()

    # 检查节点存在性
    if word1 not in graph.nodes or word2 not in graph.nodes:
        missing = []
        if word1 not in graph.nodes: missing.append(word1)
        if word2 not in graph.nodes: missing.append(word2)
        return f"No {' or '.join(missing)} in the graph!"

    # 查找桥接词
    bridges = set()
    for (src, mid), _ in graph.edges.items():
        if src == word1 and (mid, word2) in graph.edges:
            bridges.add(mid)

    # 格式化输出
    if not bridges:
        return f"No bridge words from {word1} to {word2}!"
    else:
        bridge_list = sorted(bridges)
        if len(bridge_list) == 1:
            return f"The bridge word from {word1} to {word2} is: {bridge_list[0]}."
        else:
            return f"The bridge words from {word1} to {word2} are: {', '.join(bridge_list[:-1])} and {bridge_list[-1]}."


def interactive_query(graph):
    """交互式桥接词查询"""
    print("\n" + "=" * 40)
    print("Bridge Word Query".center(40))
    print("=" * 40)

    while True:
        input_str = input("\nEnter two words (format: word1 word2) or 'q' to quit: ").strip()
        if input_str.lower() == 'q':
            break

        words = [w for w in re.split(r'\s+', input_str) if w]
        if len(words) != 2:
            print("Error: Please enter exactly two words.")
            continue

        result = find_bridge_words(graph, words[0], words[1])
        print("\n" + result)
