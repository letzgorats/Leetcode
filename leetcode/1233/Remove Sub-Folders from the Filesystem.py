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