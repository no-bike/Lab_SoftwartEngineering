import argparse
from operator import index

from func import File_to_Graph as ftg
from func import showDirectedGraph as showDG


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


if __name__ == "__main__":
    main()