import argparse
from operator import index

from func import File_to_Graph as ftg
from func import showDirectedGraph as showDG
from func import queryBridgeWords as queryBW
from func import generateNewText as genText
from func import calcShortestPath
from func import calPageRank as calPR
from func import randomWalk as rw

#1234
def main():
    # 命令行参数解析
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='?', help="Path to text file")
    args = parser.parse_args()
    f1 = "../data/Easy Test.txt"
    f2 = "../data/Cursed Be The Treasure.txt"
    index1 = 0
    # 交互式文件输入（当无命令行参数时）
    if args.file:
        file_path = args.file
    else:
        index1 = input("choose file:\n1.Easy Test.txt 2.Cursed Be The Treasure.txt:\n")
        if index1 == "1":
            file_path = f1
        elif index1 == "2":
            file_path = f2
        else:
            print("Invalid choice. Exiting.")
            return


    # 构建并输出图
    text = ftg.load_file(file_path)
    graph = ftg.build_graph(text)
    print("Generated Graph:")
    showDG.display_graph_cli(graph)
    if index == "1":
        showDG.export_graph_image(graph,str(index1))


    #查询
    index1 = input("Do you want to query Bridge Words? (y/n):\n")
    if index1.lower() == 'y':
        print("Interactive Bridge Word Query:")
        queryBW.interactive_query(graph)
    else:
        print("Exiting without queries.")

    #生成
    index1 = input("Do you want to generate New Text with Bridge? (y/n):\n")
    if index1.lower() == 'y':
        print("Interactive Text Expansion:")
        genText.interactive_text_expansion(graph)
    else:
        print("Exiting without expansion.")

    #计算最短路径
    index1 = input("Do you want to find Shortest Path? (y/n):\n")
    if index1.lower() == 'y':
        print("Interactive Shortest Path Finder:")
        calcShortestPath.interactive_shortest_path(graph)
    else:
        print("Exiting without shortest path.")

    #计算PageRank
    index1 = input("Do you want to calculate PageRank? (y/n):\n")
    if index1.lower() == 'y':
        print("Interactive PageRank Calculation:")
        calPR.analyze_pagerank(graph)
    else:
        print("Exiting without PageRank calculation.")

     #随机游走
    index1 = input("Do you want to generate Random Text? (y/n):\n")
    if index1.lower() == 'y':
        print("Interactive Random Walk:")
        rw.interactive_random_walk(graph)
    else:
        print("Exiting without Random Walk.")



if __name__ == "__main__":
    main()