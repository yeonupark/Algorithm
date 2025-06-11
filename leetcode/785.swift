class Solution {

    func isBipartite(_ graph: [[Int]]) -> Bool {

        var groups = Array(repeating: 0, count: graph.count)

        for v in 0...graph.count-1 {
            if groups[v] == 0 {
                if !splitIntoTwo(v, 1, graph, &groups) {
                    return false
                }
            }
        }

        return true
    }

    func splitIntoTwo(_ v: Int, _ idx: Int, _ graph: [[Int]], _ groups: inout [Int]) -> Bool {

        groups[v] = idx

        for c in graph[v] {
            if groups[c] == idx {
                return false
            } 
            if groups[c] == 0 {
                if !splitIntoTwo(c, idx*(-1), graph, &groups) {
                    return false
                }
            }
        }
        return true
    }
}