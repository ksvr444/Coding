// class Graph
// {
//   int ver;
//   LinkedList<LinkedList<Integer>> li = new LinkedList<LinkedList<Integer>>();
//   Graph(int ver)
//   {
//       for(int i = 0; i < ver; i++)
//       {
//           li.add(new LinkedList<Integer>());
//       }
//   }
//
//   void addEdge(int a, int b)
//   {
//       li.get(a).add(b);
//       li.get(b).add(a);
//   }
//
//   void calculate(int ver, boolean visited[], int parent)
//   {
//       visited[ver] = true;
//       LinkedList <Integer> temp = new LinkedList<Integer>();
//       temp.add(ver);
//       while(temp.size() != 0)
//       {
//         int x = temp.poll();
//         Iterator it = li.get(x).iterator();
//         while(it.hasNext())
//         {
//           int val = it.next();
//           if(!visited[val])
//           {
//             visited[val] = true;
//             temp.add(val);
//           }
//
//         }
//       }
//   }
//
// }
//
//
// class CheckGraphIsTree
// {
//   public static void main(String[]qw)
//   {
//     Scanner sc = new Scanner(System.in);
//     int n = sc.nextInt();
//     int m = sc.nextInt();
//     Graph g = new Graph(n);
//     for(int i = 0; i < m; i++)
//     {
//         int a = sc.nextInt();
//         int b = sc.nextInt();
//         g.addEdge(a, b);
//
//     }
//   }
// }
//


import java.io.*;
import java.util.*;

// This class represents a directed graph using adjacency
// list representation
class CheckGraphIsTree
{
    private int V;   // No. of vertices
    private LinkedList<Integer> adj[]; //Adjacency List

    // Constructor
    CheckGraphIsTree(int v)
    {
        V = v;
        adj = new LinkedList[v];
        for (int i=0; i<v; ++i)
            adj[i] = new LinkedList();
    }

    // Function to add an edge into the graph
    void addEdge(int v,int w)
    {
        adj[v].add(w);
        adj[w].add(v);
    }

    // A recursive function that uses visited[] and parent
    // to detect cycle in subgraph reachable from vertex v.
    Boolean isCyclicUtil(int v, Boolean visited[], int parent, ArrayList temp, ArrayList<ArrayList> main_list)
    {
        // Mark the current node as visited
        visited[v] = true;
        Integer i;

        // Recur for all the vertices adjacent to this vertex
        Iterator<Integer> it = adj[v].iterator();
        while (it.hasNext())
        {
            i = it.next();
            temp.add(i);
            // If an adjacent is not visited, then recur for
            // that adjacent
            if (!visited[i])
            {
                if (isCyclicUtil(i, visited, v, temp, main_list))
                {
                  main_list.add(temp);
                  temp.clear();
                    return true;
                  }
            }

            // If an adjacent is visited and not parent of
            // current vertex, then there is a cycle.
            else if (i != parent)
              {
                main_list.add(temp);
                temp.clear();
               return true;
             }
        }
        return false;
    }

    // Returns true if the graph is a tree, else false.
    Boolean isTree()
    {
        // Mark all the vertices as not visited and not part
        // of recursion stack
        Boolean visited[] = new Boolean[V];
        for (int i = 0; i < V; i++)
            visited[i] = false;

        // The call to isCyclicUtil serves multiple purposes
        // It returns true if graph reachable from vertex 0
        // is cyclcic. It also marks all vertices reachable
        // from 0.
        ArrayList temp = new ArrayList();
        ArrayList<ArrayList> main_list = new ArrayList<ArrayList>();
        boolean x = isCyclicUtil(0, visited, -1, temp, main_list);

            // for(int i = 0; i < V; i++)
            // {
            //   System.out.println(visited[i]);
            // }
            // return false;
              System.out.println(main_list);
          System.out.println(temp);


        // If we find a vertex which is not reachable from 0
        // (not marked by isCyclicUtil(), then we return false

        for (int u = 0; u < V; u++)
            if (!visited[u])
                return false;

        return true;
    }

    // Driver method
    public static void main(String args[])
    {
        // Create a graph given in the above diagram
        CheckGraphIsTree g1 = new CheckGraphIsTree(5);
        g1.addEdge(1, 0);
        g1.addEdge(0, 2);
        g1.addEdge(0, 3);
        g1.addEdge(3, 4);
        if (g1.isTree())
            System.out.println("Graph is Tree");
        else
            System.out.println("Graph is not Tree");

        CheckGraphIsTree g2 = new CheckGraphIsTree(5);
        g2.addEdge(1, 0);
        g2.addEdge(0, 2);
        g2.addEdge(2, 1);
        g2.addEdge(0, 3);
        g2.addEdge(3, 4);

        if (g2.isTree())
            System.out.println("Graph is Tree");
        else
            System.out.println("Graph is not Tree");

    }
}
