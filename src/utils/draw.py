import networkx as nx

#
# Funkcja: draw
# ------------
# maluje graf arytmetyczny wykorzystywując funkcje z biblioteki networkx
# (draw_networkx i draw_networkx_edge_labels)
#
# argumenty:
#   1) ag: <class 'ArithmGraph'> - objekt reprezentujacy graf arytmetyczny
#
# zwraca:
#   None
#
def draw(ag):
    pos = nx.planar_layout(ag.G)
    nx.draw_networkx(ag.G, pos, labels=ag.labels, width=1.4, node_size=400, node_color=ag.colors, arrowsize=18)
    nx.draw_networkx_edge_labels(ag.G, pos, edge_labels=ag.edge_labels)
