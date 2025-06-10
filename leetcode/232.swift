class MyQueue {

    var queue: [Int]

    init() {
        queue = []
    }
    
    func push(_ x: Int) {
        queue.append(x)
    }
    
    func pop() -> Int {

        guard let first = queue.first else {
          return -1
        } 

        queue.removeFirst()
        return first
    }
    
    func peek() -> Int {
        return queue.first ?? -1
    }
    
    func empty() -> Bool {
        return queue.count == 0
    }
}