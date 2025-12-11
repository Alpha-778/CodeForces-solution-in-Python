import sys
import threading
def main():
    class DSU:
        def __init__(self, total):
            self.parent = list(range(total + 2))
            self.rank = [0] * (total + 2)
        def find(self, node):
            stack = []
            while self.parent[node] != node:
                stack.append(node)
                node = self.parent[node]
            for item in stack:
                self.parent[item] = node
            return node
        def union(self, node1, node2):
            root1 = self.find(node1)
            root2 = self.find(node2)
            if root1 == root2:
                return False
            if self.rank[root1] < self.rank[root2]:
                root1, root2 = root2, root1
            self.parent[root2] = root1
            if self.rank[root1] == self.rank[root2]:
                self.rank[root1] += 1
            return True
    read_input = sys.stdin.readline
    case_count = int(read_input())
    for _ in range(case_count):
        length = int(read_input())
        entity_list = []
        index = 1
        while index <= length:
            start_end = read_input()
            while start_end.strip() == '':
                start_end = read_input()
            start_point, end_point = map(int, start_end.strip().split())
            spread = end_point - start_point
            entity_list.append([spread, start_point, end_point, index])
            index += 1
        entity_list.sort(key=lambda item: -item[0])
        structure = DSU(2 * length + 10)
        picked = []
        position = 0
        while position < length:
            item = entity_list[position]
            if structure.union(item[1], item[2]):
                picked.append(item[3])
            position += 1
        sys.stdout.write(str(len(picked)) + '\n')
        if picked:
            sys.stdout.write(' '.join(map(str, picked)) + '\n')
        else:
            sys.stdout.write('\n')
threading.Thread(target=main,).start()