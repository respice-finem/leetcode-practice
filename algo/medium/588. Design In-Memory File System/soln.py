class FileNode:
    def __init__(self):
        self.content = ""

class FolderNode:
    def __init__(self):
        self.folders = {}
        self.files = {}

class FileSystem:

    def __init__(self):
        self.root = FolderNode()

    def ls(self, path: str) -> List[str]:
        curr = self.root
        filePath_arr = path.split('/')

        for e in filePath_arr[1:-1]:
            curr = curr.folders[e]
        if filePath_arr[-1] in curr.files:
            return [filePath_arr[-1]]
        elif not filePath_arr[-1] or filePath_arr[-1] in curr.folders:
            directory = curr.folders[filePath_arr[-1]] if filePath_arr[-1] else curr
            folders = list(directory.folders.keys())
            files = list(directory.files.keys())
            return sorted(folders + files)

    def mkdir(self, path: str) -> None:
        curr = self.root
        for e in path.split('/')[1:]:
            if e not in curr.folders:
                curr.folders[e] = FolderNode()
            curr = curr.folders[e]

    def addContentToFile(self, filePath: str, content: str) -> None:
        filePath_arr = filePath.split('/')
        self.mkdir('/'.join(filePath_arr[:-1]))
        curr = self.root
        for e in filePath_arr[1:-1]:
            curr = curr.folders[e]
        if filePath_arr[-1] not in curr.files:
            curr.files[filePath_arr[-1]] = FileNode()
            curr.files[filePath_arr[-1]].content = content
        else:
            curr.files[filePath_arr[-1]].content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        filePath_arr = filePath.split('/')
        for e in filePath_arr[1:-1]:
            curr = curr.folders[e]
        return curr.files[filePath_arr[-1]].content