import sys

eps = sys.float_info.min
class PageRank:
    def __init__(self) -> None:
        self.graph = {}
        self.node_rank = {}

    def add_link(self, from_node, to_nodes, score=1):
        self.graph[from_node] = to_nodes
        self.node_rank[from_node] = score

    def remove_no_citations(self):
        remove = []
        for target_node, linked_nodes in self.graph.items():
            if len(linked_nodes) == 0:
                remove.append(target_node)
        for i in remove:
            del self.graph[i]

    def calculate(self):
        for _ in range(100):
            for target_node, linked_nodes in self.graph.items():
                new_rank = 0.2
                for linked_node in linked_nodes:
                    if not linked_node in self.graph:
                        continue
                    
                    citation_doc_rank = self.node_rank[linked_node]
                    citation_count = len(self.graph[linked_node])                        
                    new_rank += (0.8) * (citation_doc_rank / citation_count)
                self.node_rank[target_node] = new_rank
                