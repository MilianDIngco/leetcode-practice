public class topSort {
    
}
/**
 * topSort(graph) adjacency list
 * n = num of nodes
 * visitedNodes[n] = false
 * order[n] = 0
 * i = n - 1; //keep track of last one added, goes backwards
 * 
 * for(nodes : graph) {
 * 
 * if(node is not visited)
 *  i = dfs(i, node, visitedNodes, order, graph)
 * 
 * }
 * 
 * return order
 * 
 * dfs(i, node, visitedNodes, order, graph) {
 *  visitedNodes[node] = true;
 *  
 *  for(node : graph[node].nodes) { //for all the nodes that it's connected to
 *      if(node is not visited) { 
 *          i = dfs(i, node, visitedNodes, order, graph)
 *      }
 *  }
 *  order[i] = node
 *  return i - 1;
 * 
 * }
 * 
 */