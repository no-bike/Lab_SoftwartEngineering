import pytest
from .calcShortestPath import (
    find_shortest_path,
    dijkstra,
    reconstruct_path,
    interactive_shortest_path
)

class MockGraph:
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes if nodes else set()
        self.edges = edges if edges else {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, src, dest, weight):
        self.edges[(src, dest)] = weight

@pytest.fixture
def basic_graph():
    """基础测试图"""
    nodes = {'a', 'b', 'c', 'd', 'e'}
    edges = {
        ('a', 'b'): 1,
        ('b', 'c'): 2,
        ('a', 'd'): 4,
        ('d', 'e'): 2,
        ('b', 'e'): 3
    }
    return MockGraph(nodes, edges)

@pytest.fixture
def empty_graph():
    """空图"""
    return MockGraph()

@pytest.fixture
def single_node_graph():
    """单节点图"""
    return MockGraph(nodes={'a'})

@pytest.fixture
def disconnected_graph():
    """不连通图"""
    nodes = {'a', 'b', 'c', 'x', 'y'}
    edges = {
        ('a', 'b'): 1,
        ('b', 'c'): 2
    }
    return MockGraph(nodes, edges)

def test_dijkstra_algorithm(basic_graph):
    """测试Dijkstra算法实现"""
    distances, prev_nodes = dijkstra(basic_graph, 'a')
    assert distances == {'a': 0, 'b': 1, 'c': 3, 'd': 4, 'e': 4}
    assert prev_nodes in [
        {'a': None, 'b': 'a', 'c': 'b', 'd': 'a', 'e': 'd'},
        {'a': None, 'b': 'a', 'c': 'b', 'd': 'a', 'e': 'b'}
    ]

def test_dijkstra_empty_graph(empty_graph):
    """测试空图的Dijkstra算法"""
    distances, prev_nodes = dijkstra(empty_graph, 'a')
    assert distances == {'a': 0}
    assert prev_nodes == {}

def test_dijkstra_single_node(single_node_graph):
    """测试单节点图的Dijkstra算法"""
    distances, prev_nodes = dijkstra(single_node_graph, 'a')
    assert distances == {'a': 0}
    assert prev_nodes == {'a': None}

def test_reconstruct_path_not_found(basic_graph):
    """测试路径重建-目标节点不存在"""
    _, prev_nodes = dijkstra(basic_graph, 'a')
    with pytest.raises(KeyError):
        reconstruct_path(prev_nodes, 'x')

def test_find_shortest_path_normal(basic_graph):
    """测试正常最短路径"""
    result = find_shortest_path(basic_graph, 'a', 'e')
    assert result in [
        "Shortest path (4): a → d → e",
        "Shortest path (4): a → b → e"
    ]

def test_find_shortest_path_no_path(disconnected_graph):
    """测试无路径情况"""
    result = find_shortest_path(disconnected_graph, 'a', 'x')
    assert result == "No path from 'a' to 'x'!"

def test_find_shortest_path_node_missing(basic_graph):
    """测试节点不存在情况"""
    result = find_shortest_path(basic_graph, 'a', 'z')
    assert result == "'z' not in graph!"
    result = find_shortest_path(basic_graph, 'z', 'a')
    assert result == "'z' not in graph!"

def test_find_shortest_path_case_insensitive(basic_graph):
    """测试大小写不敏感"""
    result = find_shortest_path(basic_graph, 'A', 'E')
    assert result in [
        "Shortest path (4): a → d → e",
        "Shortest path (4): a → b → e"
    ]

@pytest.mark.parametrize("input_str,expected_parts", [
    ("a b", ["Shortest path (1): a → b", "━━━[1]━━━▶"]),
    ("a z", ["'z' not in graph!"]),
    ("q", ["Shortest Path Finder"])
])
def test_interactive_shortest_path(monkeypatch, capsys, basic_graph, input_str, expected_parts):
    """测试交互式最短路径查询"""
    inputs = iter([input_str, 'q'])  # 添加退出命令避免无限循环
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    interactive_shortest_path(basic_graph)
    captured = capsys.readouterr()
    
    for part in expected_parts:
        assert part in captured.out
