# find_bridge_words 函数需求规约

## 功能描述
查找有向图中两个单词之间的所有桥接词。桥接词定义为：
- 对于单词A和单词C，如果存在边A→B和B→C，则B是A到C的桥接词

## 输入描述
- graph: 有向图对象，需包含以下属性：
  - nodes: 图中所有节点的集合(set)
  - edges: 图中所有边的字典(dict)，键为(source, target)元组，值为边权重
- word1: 源单词(str)
- word2: 目标单词(str) 

## 输出描述
返回字符串，分为以下几种情况：
1. 正常情况(存在桥接词):
   - 单个桥接词: "The bridge word from {word1} to {word2} is: {bridge_word}."
   - 多个桥接词: "The bridge words from {word1} to {word2} are: {word1}, {word2}, ..., and {last_word}."

2. 异常情况:
   - 单词不在图中: 
     - 单个单词缺失: "No {missing_word} in the graph!"
     - 多个单词缺失: "No {word1} or {word2} in the graph!"
   - 无桥接词: "No bridge words from {word1} to {word2}!"

## 约束条件
1. 单词比较不区分大小写
2. 输入单词会自动转换为小写
3. 桥接词结果按字母顺序排序
4. 输出信息格式必须严格符合上述规范

## 等价类划分表

| 约束条件说明 | 有效等价类及其编号 | 无效等价类及其编号 |
|-------------|-------------------|-------------------|
| graph结构有效性 | EC1: 包含nodes和edges属性的有效graph对象 | EC6: 缺少nodes属性<br>EC7: 缺少edges属性<br>EC8: nodes不是集合类型<br>EC9: edges不是字典类型 |
| word1在图中 | EC2: word1存在于graph.nodes中 | EC10: word1不存在于graph.nodes中 |
| word2在图中 | EC3: word2存在于graph.nodes中 | EC11: word2不存在于graph.nodes中 |
| 桥接词存在性 | EC4: 存在至少一个桥接词<br>EC5: 存在多个桥接词 | EC12: 不存在桥接词 |
| 单词大小写 | EC13: 输入单词大小写混合 | 无(函数自动转换为小写) |

## 测试用例设计

| 测试函数 | 测试场景 | 输入 | 期望输出 | 覆盖等价类 |
|---------|---------|------|---------|-----------|
| test_existing_bridge_words | 单个桥接词 | graph: nodes={'apple','banana','cherry'}, edges={('apple','banana'):1, ('banana','cherry'):1}<br>word1='apple', word2='cherry' | "The bridge word from apple to cherry is: banana." | EC1,EC2,EC3,EC4 |
| test_existing_bridge_words | 多个桥接词 | graph: nodes={'apple','banana','cherry','date','elderberry'}, edges={('apple','banana'):1,('apple','date'):1,('banana','elderberry'):1,('date','elderberry'):1}<br>word1='apple', word2='elderberry' | "The bridge words from apple to elderberry are: banana and date." | EC1,EC2,EC3,EC5 |
| test_no_bridge_words | 无桥接词 | graph: nodes={'apple','banana','cherry'}, edges={('apple','banana'):1,('banana','cherry'):1}<br>word1='cherry', word2='apple' | "No bridge words from cherry to apple!" | EC1,EC2,EC3,EC12 |
| test_missing_words | 单个单词缺失 | graph: nodes={'apple','banana','cherry'}, edges={('apple','banana'):1,('banana','cherry'):1}<br>word1='apple', word2='fig' | "No fig in the graph!" | EC1,EC2,EC11 |
| test_missing_words | 多个单词缺失 | graph: nodes={'apple','banana','cherry'}, edges={('apple','banana'):1,('banana','cherry'):1}<br>word1='fig', word2='grape' | "No fig or grape in the graph!" | EC1,EC10,EC11 |
| test_case_insensitivity | 大小写不敏感 | graph: nodes={'APPLE','BANANA','CHERRY'}, edges={('APPLE','BANANA'):1,('BANANA','CHERRY'):1}<br>word1='APPLE', word2='CHERRY' | "The bridge word from apple to cherry is: banana." | EC1,EC2,EC3,EC4,EC13 |

## 示例
输入:
- graph: nodes={'a','b','c'}, edges={('a','b'):1, ('b','c'):1}
- word1='a', word2='c'

输出:
"The bridge word from a to c is: b."
