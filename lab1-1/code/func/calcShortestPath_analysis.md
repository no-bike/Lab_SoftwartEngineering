## 6.5 测试用例设计

| 测试用例编号 | 输入数据 | 期望的输出 | 所覆盖的基本路径编号 |
|-------------|---------|-----------|-------------------|
| TC1 | 空图, start='a' | distances={'a':0}, prev_nodes={} | 基本路径1 |
| TC2 | 单节点图, start='a' | distances={'a':0}, prev_nodes={'a':None} | 基本路径2 |
| TC3 | 正常图, start='a' | distances={'a':0,'b':1,'c':3,'d':4,'e':4}, prev_nodes包含正确的前驱节点关系 | 基本路径3 |
| TC4 | 不连通图, start='a', target='x' | 返回字符串"No path from 'a' to 'x'!" | 基本路径3 |
| TC5 | 节点不存在, start='z' | 返回字符串"'z' not in graph!" | 基本路径4 |
| TC6 | 大小写混合输入(如'A','E') | 返回正确的最短路径(如"Shortest path (4): a → d → e"或"Shortest path (4): a → b → e") | 基本路径3 |
| TC7 | 重建不存在的节点路径(prev_nodes, 'x') | 抛出KeyError异常，提示节点不存在 | 基本路径3 |
| TC8 | 交互模式输入'q' | 程序正常退出，无错误 | 基本路径1 |
| TC9 | 交互模式单节点输入(如"a") | 显示格式化的最短路径输出(如"→ b: 1\n→ c: 3\n→ d: 4\n→ e: 4") | 基本路径2 |
| TC10 | 交互模式双节点输入(如"a e") | 显示格式化的最短路径输出(如"Shortest path (4): a → d → e")和可视化路径 | 基本路径3 |

说明：
1. TC1对应test_dijkstra_empty_graph测试空图情况
2. TC2对应test_dijkstra_single_node测试单节点图
3. TC3对应test_dijkstra_algorithm测试正常图
4. TC4对应test_find_shortest_path_no_path测试不连通图
5. TC5对应test_find_shortest_path_node_missing测试节点不存在
6. TC6对应test_find_shortest_path_case_insensitive测试大小写不敏感
7. TC7对应test_reconstruct_path_not_found测试重建不存在节点路径
8. TC8对应test_interactive_shortest_path测试交互退出
9. TC9对应交互模式单节点输入测试
10. TC10对应交互模式双节点输入测试
