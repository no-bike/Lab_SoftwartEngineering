import random
from .File_to_Graph import normalize_text


def expand_text_with_bridges(graph, text):
    """使用桥接词扩展新文本"""
    words = normalize_text(text).split()
    new_text = []

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        new_text.append(word1)  # 添加当前词

        # 查找桥接词
        bridges = find_bridge_words_list(graph, word1, word2)
        if bridges:
            chosen_bridge = random.choice(bridges)
            new_text.append(chosen_bridge)

    new_text.append(words[-1])  # 添加最后一个词
    return ' '.join(new_text).capitalize()


def find_bridge_words_list(graph, word1, word2):
    """返回桥接词列表（不包含输出逻辑）"""
    word1, word2 = word1.lower(), word2.lower()
    if word1 not in graph.nodes or word2 not in graph.nodes:
        return []

    bridges = []
    for (src, mid), _ in graph.edges.items():
        if src == word1 and (mid, word2) in graph.edges:
            bridges.append(mid)
    return bridges


def interactive_text_expansion(graph):
    """交互式文本扩展"""
    print("\n" + "=" * 40)
    print("Text Expansion with Bridge Words".center(40))
    print("=" * 40)

    while True:
        input_text = input("\nEnter new text (or 'q' to quit): ").strip()
        if input_text.lower() == 'q':
            break

        expanded_text = expand_text_with_bridges(graph, input_text)
        print("\nOriginal:", input_text)
        print("Expanded:", expanded_text)