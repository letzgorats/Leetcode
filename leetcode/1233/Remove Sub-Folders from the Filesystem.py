# my solution 1
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder.sort()
        candi = set()
        answer = set()

        for fold in folder:
            # print(fold)
            s = fold.split('/')[1:]
            si = ''.join(s)
            # print(s)
            if si not in candi:
                tmp = s[0]
                for i, char in enumerate(s):
                    if tmp in candi:
                        break
                    else:
                        tmp += char
                # print(tmp)
                if tmp not in candi:
                    candi.add(tmp)
                    answer.add(fold)
                # print(candi,"candi")
        # print(answer)

        return list(answer)

# solution 2 - more simple
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        prev = ''
        for path in folder:
            # print(prev)
            if not prev or not path.startswith(prev + '/'):
                result.append(path)
                prev = path  # Update 'prev' to the current folder
        return result

# solution 3- trie
class Trie:

    def __init__(self):
        self.children = {}  # string -> Trie
        self.end_of_folder = False

    def add(self, path):
        cur = self
        for f in path.split('/'):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.end_of_folder = True

    def prefix_search(self, path):
        cur = self
        folders = path.split('/')
        for i in range(len(folders) - 1):
            cur = cur.children[folders[i]]
            if cur.end_of_folder:
                return True
        return False


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:

        trie = Trie()

        for f in folder:
            trie.add(f)

        res = []
        for f in folder:
            if not trie.prefix_search(f):
                res.append(f)

        return res