# solution 1 - (Trie,dfs) - (159ms) - (2025.07.20) RE
from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name
        self.children = dict()
        self.to_delete = False

def build_trie(paths):
    root = Node("")
    for path in paths:
        curr = root
        for folder in path:
            if folder not in curr.children:
                curr.children[folder] = Node(folder)
            curr = curr.children[folder]
    return root

def serialize(node, counter):
    if not node.children:
        return "" # 자식이 없으면 빈 문자열

    # 자식 이름을 정렬해서 고정된 순서로 서명 만들기
    parts = []
    for child_name in sorted(node.children):
        child_node = node.children[child_name]
        part = f"{child_name}({serialize(child_node, counter)})"
        parts.append(part)
    sig = "".join(parts)
    counter[sig].append(node)
    return sig

def collect_paths(node, path, result):
    for child in node.children.values():
        if not child.to_delete:
            path.append(child.name)
            result.append(path[:])
            collect_paths(child, path, result)
            path.pop()

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = build_trie(paths)
        counter = defaultdict(list)
        serialize(root, counter)
        for nodes in counter.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.to_delete = True
        result = []
        collect_paths(root, [], result)
        return result


'''
폴더 구조를 트리로 만든 뒤, 자식 구조를 문자열로 직렬화해서 중복된 가지를 찾아 제거하고, 남은 경로만 반환하는 문제!
'''