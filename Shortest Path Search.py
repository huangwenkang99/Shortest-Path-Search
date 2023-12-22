# 确保已经通过本地环境安装了 osmnx, networkx, matplotlib 库
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import sklearn

# 定义地点名称
place_name = "Ariake, Japan"

# 创建图形和获取节点和边
graph = ox.graph_from_address(place_name, network_type='bike')
fig, ax = ox.plot_graph(graph)
gdf_nodes, gdf_edges = ox.graph_to_gdfs(graph)

# 输出节点和边的信息
print("NODES")
print(gdf_nodes.head())
print("EDGES")
print(gdf_edges.head())

# 定义 Dijkstra 算法
def dijkstra(node_list, edge_list, start, end):
    distances = {node: float('inf') for node in node_list}
    distances[start] = 0
    previous_nodes = {node: None for node in node_list}
    nodes = set(node_list)

    while nodes:
        min_node = None
        for node in nodes:
            if min_node is None:
                min_node = node
            elif distances[node] < distances[min_node]:
                min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = distances[min_node]

        for edge in edge_list.get(min_node, []):
            weight = current_weight + edge_list[min_node][edge]
            if weight < distances[edge]:
                distances[edge] = weight
                previous_nodes[edge] = min_node

    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()

    return path, distances


# 添加边的速度和旅行时间
G = ox.speed.add_edge_speeds(graph)
G = ox.speed.add_edge_travel_times(graph)

# 转换为GeoDataFrame
gdf_nodes, gdf_edges = ox.graph_to_gdfs(G, nodes=True, edges=True)

# 创建边列表
edge_list = {}
for u, v, data in G.edges(data=True):
    edge_list.setdefault(u, {})[v] = data['length']

# 创建节点列表
node_list = list(G.nodes)

# 指定起点和终点
orig = ox.distance.nearest_nodes(G, X=139.7840, Y=35.6311)
dest = ox.distance.nearest_nodes(G, X=139.7886, Y=35.6294)

# 执行 Dijkstra 算法
route, distances = dijkstra(node_list, edge_list, orig, dest)

# 绘制路径
fig, ax = ox.plot_graph_route(G, route, node_size=0)
plt.show()
