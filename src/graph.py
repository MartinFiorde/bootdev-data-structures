class Graph:
    def bfs_path(self, start, end):
        visited = []
        to_visit = [start]
        path = {start: None} # not in personal solution
        while to_visit:
            current_vertex = to_visit.pop(0)
            visited.append(current_vertex)
            if current_vertex == end:
                print("MAF3")
                print(f"visited + to_visit:  {visited}{to_visit}")
                print(f"path keys: {path.keys()}")
                # return self.course_path_builder(start, end, path) # not in personal solution
                return self.my_path_builder(start, end, visited) # personal solution

            sorted_neighbors = sorted(self.graph[current_vertex])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
                    path[neighbor] = current_vertex # not in personal solution
                    # print("MAF")
                    # print(f"visited: {visited}")
                    # print(f"to_visit: {to_visit}")
                    # print(f"path: {path}")
            # print("MAF2")
            # print(f"visited + to_visit:  {visited}{to_visit}")
            # print(f"path keys: {path.keys()}")
        return None

    def course_path_builder(self, start, end, path):
        current_vertex = end
        path_list = []
        while current_vertex is not None:
            path_list.append(current_vertex)
            current_vertex = path[current_vertex]
        path_list.reverse()
        return path_list
    
    def my_path_builder(self, start, end, visited):
        current_vertex = end
        path_list = []
        while start not in path_list:
            path_list.append(current_vertex)
            next_reverts = sorted(self.graph[current_vertex])
            shortest_index = len(visited)
            for i in next_reverts:
                if i not in visited:
                    continue
                index = visited.index(i)
                if index < shortest_index:
                    shortest_index = index
            current_vertex = visited[shortest_index]
        path_list.reverse()
        return path_list


    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
