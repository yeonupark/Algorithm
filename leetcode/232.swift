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

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue()
 * obj.push(x)
 * let ret_2: Int = obj.pop()
 * let ret_3: Int = obj.peek()
 * let ret_4: Bool = obj.empty()
 */

let obj = MyQueue()
obj.push(7)
let ret_3: Int = obj.peek()
let ret_4: Bool = obj.empty()
let ret_2: Int = obj.pop()
print(ret_3)
print(ret_4)
print(ret_2)