from collections import defaultdict
from math import log
from .File_to_Graph import normalize_text
import numpy as np
def calculate_pagerank(graph, damping=0.85, max_iter=100, tol=1e-6, initial_weights=None):
    """
    带权重初始化的PageRank算法
    :param damping: 阻尼系数(通常0.85)
    :param initial_weights: 初始权重字典 {'word': weight}
    """
    nodes = sorted(graph.nodes)
    n = len(nodes)
    node_index = {node: i for i, node in enumerate(nodes)}

    # 构建转移矩阵
    M = np.zeros((n, n))
    for (src, dest), weight in graph.edges.items():
        M[node_index[dest], node_index[src]] = weight

    # 列归一化
    M = M / np.maximum(M.sum(axis=0), 1)

    # 处理悬挂节点(全为0的列)
    dangling = np.where(M.sum(axis=0) == 0)[0]
    for col in dangling:
        M[:, col] = 1.0 / n

    # 初始化PR值
    if initial_weights:
        pr = np.array([initial_weights.get(node, 1.0 / n) for node in nodes])
    else:
        pr = np.ones(n) / n
    pr = pr / pr.sum()  # 归一化

    # 迭代计算
    for _ in range(max_iter):
        new_pr = damping * M @ pr + (1 - damping) / n
        delta = np.abs(new_pr - pr).sum()
        pr = new_pr
        if delta < tol:
            break

    return {node: pr[i] for i, node in enumerate(nodes)}



def compute_tfidf(documents):
    """计算单词的TF-IDF权重"""
    word_docs = defaultdict(int)
    tf = defaultdict(dict)
    total_docs = len(documents)

    # 计算TF和DF
    for i, doc in enumerate(documents):
        words = set(normalize_text(doc).split())
        for word in words:
            tf[i][word] = tf[i].get(word, 0) + 1
            word_docs[word] += 1

    # 归一化TF并计算TF-IDF
    tfidf = defaultdict(dict)
    for doc_id, word_counts in tf.items():
        max_tf = max(word_counts.values())
        for word, count in word_counts.items():
            tf = 0.5 + 0.5 * (count / max_tf)
            idf = log(total_docs / (1 + word_docs[word]))
            tfidf[doc_id][word] = tf * idf

    # 合并文档权重
    global_weights = defaultdict(float)
    for doc_weights in tfidf.values():
        for word, weight in doc_weights.items():
            global_weights[word] += weight

    return global_weights


def analyze_pagerank(graph, text_corpus=None):
    """PageRank分析入口"""
    # 计算初始权重（如果提供语料）
    initial_weights = None
    if text_corpus:
        print("Computing TF-IDF weights...")
        initial_weights = compute_tfidf(text_corpus)

    print("\nCalculating PageRank...")
    pr = calculate_pagerank(graph, initial_weights=initial_weights)

    # 可视化结果
    print("\n" + "=" * 60)
    print("PageRank Results (Top 20)".center(60))
    print("=" * 60)
    sorted_pr = sorted(pr.items(), key=lambda x: -x[1])
    for word, score in sorted_pr[:20]:
        print(f"{word.ljust(15)}: {score:.6f}")

    # 可选：导出完整结果
    if input("\nExport full results? (y/N): ").lower() == 'y':
        with open("../picture/pagerank_results.csv", "w") as f:
            f.write("word,pagerank\n")
            for word, score in sorted_pr:
                f.write(f"{word},{score}\n")
        print("Results saved to pagerank_results.csv")