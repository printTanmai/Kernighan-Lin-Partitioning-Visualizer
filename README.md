

# **Kernighan Lin Partitionin Visualizer**

This project demonstrates the **Kernighan-Lin algorithm** for graph partitioning. The goal is to divide the nodes of a graph into two groups while minimizing the **cut size** (number or weight of edges between the two groups). The project includes a GUI built with **Tkinter** to visualize the partitioned graph interactively. 

## **Features**
- **Graph Partitioning**: Divides nodes into two groups to minimize the edge cut size.
- **Interactive Visualization**: Displays the graph with distinct node colors for each group.
- **Custom Graph Support**: Easy to modify the input graph (nodes and edges) for different scenarios.

---

## **Getting Started**

### **Prerequisites**
Install the required Python libraries:
```bash
pip install numpy matplotlib networkx
```

---

### **Steps to Run**

1. **Clone the Repository**
   ```bash
   git clone <repository-link>
   cd <repository-name>
   ```

2. **Edit the Graph** *(Optional)*
   - Update the `nodes` list for the graph's nodes.
   - Define edges as `(node1, node2, weight)` in the `edges` list.

3. **Run the Script**
   ```bash
   python graph_partition_gui.py
   ```

4. **Visualize the Results**
   - A Tkinter window opens with a button to display the partitioned graph.
   - Nodes in **Group 1** are colored **blue**, and those in **Group 2** are colored **green**.
   - Edge weights are annotated on the graph.

---

## **Code Overview**

1. **Graph Definition**
   - Nodes and edges are defined in lists.
   - An adjacency matrix is created to represent graph connectivity.

2. **Algorithm**
   - Implements the **Kernighan-Lin algorithm**:
     - Iteratively refines two partitions to minimize the cut size.
     - Swaps nodes between groups to reduce inter-group edge weights.

3. **Visualization**
   - Uses **NetworkX** to create the graph.
   - Displays the partitioned graph with **Matplotlib**.

4. **GUI Integration**
   - A Tkinter-based interface embeds the Matplotlib graph for visualization.

---

## **Example Output**
For the given graph:
- **Nodes**: `[1, 2, 3, 4, 5, 6, 7, 8]`
- **Edges**: Connections with weights.

Resulting partition:
- **Group 1**: `[1, 2, 5, 6]` (blue)
- **Group 2**: `[3, 4, 7, 8]` (green)

![image](https://github.com/user-attachments/assets/80e156c8-6ff3-4526-8f5e-b4d0956ba99f)


---

## **Future Enhancements**
- Support for directed and weighted graphs.
- Additional layout options for graph visualization.
- Extend the algorithm to support multi-way partitioning.
- GUI input for defining custom graphs.

---

Feel free to fork and contribute to this project!
