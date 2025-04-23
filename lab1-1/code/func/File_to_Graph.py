import re
import sys
from collections import defaultdict

class DirectedGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(int)  # (src, dest): weight

    def add_edge(self, src, dest):
        self.nodes.update([src, dest])
        self.edges[(src, dest)] += 1

    def __str__(self):
        edge_list = [f"{src}→{dest}({weight})" for (src, dest), weight in self.edges.items()]
        return f"Nodes: {self.nodes}\nEdges: {' '.join(edge_list)}"


def normalize_text(text):
    """文本标准化处理"""
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # 非字母字符替换为空格
    text = re.sub(r'\s+', ' ', text).strip()  # 合并连续空格
    return text.lower()


def build_graph(text):
    """构建有向图核心逻辑"""
    graph1 = DirectedGraph()
    words = normalize_text(text).split()

    for i in range(len(words) - 1):
        src, dest = words[i], words[i + 1]
        graph1.add_edge(src, dest)

    return graph1


def load_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        sys.exit(1)