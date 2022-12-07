def main():
    class FileTreeNode:
        def __init__(self, name, parent=None):
            self.name = name
            self.size = 0 # initial size
            self.parent = parent
            self.children = []

        def add_child(self, child_dir):
            self.children.append(child_dir)
        
    def get_size(dir):
        whole_size = dir.size + sum([get_size(child) for child in dir.children])
        sizes.append(whole_size)
        return whole_size

    # filename = '7.1test.txt'
    filename = '7.1input.txt'

    output = []
    with open(filename) as f:
        for line in f:
            output.append(line.rstrip().split())

    root = FileTreeNode(name='/')
    current_dir = root

    for command in output[1:]:
        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] == '..':
                    current_dir = current_dir.parent
                else:
                    for child in current_dir.children:
                        if child.name == command[2]:
                            current_dir = child
        else:
            if command[0] == 'dir':
                current_dir.add_child(FileTreeNode(name=command[1], parent=current_dir))
            else:
                current_dir.size += int(command[0])

    sizes = []
    get_size(root)
    for s in sorted(sizes):
        if s >= 30000000 - (70000000 - max(sizes)):
            print(s)
            break


if __name__ == '__main__':
    main()
