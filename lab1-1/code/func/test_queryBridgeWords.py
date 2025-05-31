from .queryBridgeWords import find_bridge_words

class MockGraph:
    def __init__(self):
        self.nodes = {'apple', 'banana', 'cherry', 'date', 'elderberry'}
        self.edges = {
            ('apple', 'banana'): 1,
            ('banana', 'cherry'): 1,
            ('apple', 'date'): 1,
            ('date', 'elderberry'): 1,
            ('banana', 'elderberry'): 1
        }

def test_existing_bridge_words():
    graph = MockGraph()
    # 测试存在单个桥接词的情况
    result = find_bridge_words(graph, 'apple', 'cherry')
    assert result == "The bridge word from apple to cherry is: banana."

    # 测试存在多个桥接词的情况
    graph.edges[('apple', 'cherry')] = 1  # 添加直接路径
    result = find_bridge_words(graph, 'apple', 'elderberry')
    assert "The bridge words from apple to elderberry are:" in result

def test_no_bridge_words():
    graph = MockGraph()
    # 测试没有桥接词的情况
    result = find_bridge_words(graph, 'cherry', 'apple')
    assert result == "No bridge words from cherry to apple!"

def test_missing_words():
    graph = MockGraph()
    # 测试单词不在图中的情况
    result = find_bridge_words(graph, 'apple', 'fig')
    assert result == "No fig in the graph!"

    result = find_bridge_words(graph, 'fig', 'grape')
    assert result == "No fig or grape in the graph!"

def test_case_insensitivity():
    graph = MockGraph()
    # 测试大小写不敏感
    result = find_bridge_words(graph, 'APPLE', 'CHERRY')
    assert result == "The bridge word from apple to cherry is: banana."
