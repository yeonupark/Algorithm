import Foundation

func solution(_ argv:[String]) -> Int {

    let root = makeTree(argv)
    return getDepth(root)
}

func makeTree(_ argv:[String]) -> Directory {

    let root = Directory(name: "/", parent: nil)
    var curr = root
    var Directorys = [root]

    for line in argv {
        let components = line.split(separator: " ").map(String.init)
        let command = Command(rawValue: components.first!)!

        let dirName = components[1]
        switch command {

            case .mkdir:
                let newDirectory = Directory(name: dirName, parent: curr)
                Directorys.append(newDirectory)
                curr.children.append(newDirectory)

            case .del:
                curr.children = curr.children.filter { $0.name != dirName}

            case .move:

                let dir = curr.children.filter { $0.name == dirName }.first!
                dir.parent!.children = dir.parent!.children.filter { $0.name != dirName}
                let fullPath = components[2]
                let paths = fullPath.split(separator: "/").map(String.init)

                var i = 0
                var update = root
                while i < paths.count {
                    update = update.children.filter { $0.name == paths[i] }.first!
                    i += 1
                }
                update.children.append(dir)
                dir.parent = update

            case .cd:
                if dirName == ".." {
                    if let parent = curr.parent {
                        curr = parent
                    }
                } else {
                    curr = curr.children.filter { $0.name == dirName }.first!
                }
        }
    }

    return root
}

func getDepth(_ root: Directory) -> Int {
    if root.children.isEmpty {
        return 0
    }

    var ans = 0
    for child in root.children {
        ans = max(ans, getDepth(child)+1)
    }

    return ans
}

class Directory {
    weak var parent: Directory?
    var children: [Directory] = []
    let name: String

    init(name: String, parent: Directory? = nil) {
        self.name = name
        self.parent = parent
    }
}

enum Command: String {
    case mkdir
    case del
    case move
    case cd
}

print(solution(["mkdir a1", "mkdir a2", "cd a1", "mkdir b1", "cd b1", "mkdir c1", "cd c1", "mkdir d1", "cd d1", "mkdir e1", "cd ..", "cd ..", "move c1 /a2"]))