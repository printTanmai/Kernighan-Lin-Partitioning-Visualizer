# **Kernighan Lin Partitioning Visualizer**

This project demonstrates the **Kernighan-Lin algorithm** for graph partitioning, a heuristic algorithm designed to optimize the division of graph nodes into two groups while minimizing the **cut size** (number or weight of edges between the two groups). This project features a user-friendly GUI built with **Tkinter**, which allows for interactive visualization of the partitioning process.

## **Features**
- **Graph Partitioning**: Divides graph nodes into two groups to achieve minimal cut size.
- **Interactive Visualization**: Displays the graph with distinct node colors representing partitions.
- **Custom Graph Support**: Users can easily modify input graphs by editing the nodes and edges.
- **Edge Weights Display**: Annotates the graph with weights of the edges.

---

## **Getting Started**

### **Prerequisites**
Before running the project, install the required Python libraries:
```bash
pip install numpy matplotlib networkx
```

---

### **Steps to Run**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/printTanmai/Kernighan-Lin-Partitioning-Visualizer.git
   cd Kernighan-Lin-Partitioning-Visualizer
   ```

2. **Edit the Graph** *(Optional)*
   - Open the `KL_algorithm.py` file.
   - Update the `nodes` list to specify the nodes in your graph.
   - Define edges as tuples `(node1, node2, weight)` in the `edges` list. These tuples represent connections and their weights.

3. **Run the Script**
   ```bash
   python KL_algorithm.py
   ```

4. **Visualize the Results**
   - A Tkinter window opens, displaying a button labeled **"Show Partitioned Graph"**.
   - Clicking the button renders the graph with:
     - **Blue nodes** for **Group 1**.
     - **Green nodes** for **Group 2**.
   - Edge weights are displayed directly on the graph.

---

## **Code Overview**

### 1. **Graph Definition**
- The graph is defined using a `nodes` list and an `edges` list.
- An adjacency matrix is created to represent connections and edge weights.

### 2. **Algorithm**
- **Kernighan-Lin Algorithm**:
  - The algorithm begins by randomly dividing nodes into two groups.
  - Iteratively refines the partitions by swapping nodes between groups to minimize the cut size.
  - Stops when no further improvement in cut size is possible.

### 3. **Visualization**
- **NetworkX** is used to create the graph structure.
- The graph is visualized using **Matplotlib**, with:
  - Nodes colored based on their assigned group.
  - Weights displayed for all edges.
- The Tkinter GUI embeds the Matplotlib graph to provide an interactive experience.

### 4. **GUI Integration**
- The project leverages **Tkinter** to:
  - Create a window for visualization.
  - Include a button for triggering graph updates.
  - Embed Matplotlib plots directly into the Tkinter window using `FigureCanvasTkAgg`.

---

## **Example Output**

For the given graph:
- **Nodes**: `[1, 2, 3, 4, 5, 6, 7, 8]`
- **Edges**: Defined with weights between nodes.

Resulting partition:
- **Group 1**: `[1, 2, 5, 6]` (blue)
- **Group 2**: `[3, 4, 7, 8]` (green)

A visualization window will show the graph with nodes grouped by color and edge weights annotated.

![image](https://github.com/user-attachments/assets/80e156c8-6ff3-4526-8f5e-b4d0956ba99f)


---

## **Repository Structure**
- **`KL_algorithm.py`**: Main script containing the graph definition, Kernighan-Lin implementation, and GUI code.
- **`README.md`**: Instructions and documentation for running and understanding the project.

---

## **Future Enhancements**
- Add support for:
  - **Directed Graphs**: Extend functionality to handle directionality of edges.
  - **Multi-Way Partitioning**: Partition the graph into more than two groups.
- Provide additional layout options for graph visualization (e.g., circular, spectral).
- Enhance GUI to:
  - Allow user input for custom graphs via forms or file uploads.
  - Display intermediate steps of the Kernighan-Lin algorithm.

---

Feel free to fork the repository, experiment with the code, and contribute improvements. Happy coding!
