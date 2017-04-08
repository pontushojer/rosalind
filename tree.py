#!/usr/bin/env python3

"""
Problem: Completing a Tree
url: http://rosalind.info/problems/tree/

Given: A positive integer nn (n≤1000n≤1000) and an adjacency list corresponding to a graph on nn nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.
"""

def inputAdjacencies(file_name):
    with open(file_name,"r") as file:
        firstLine = True
        adjList = []
        for line in file.readlines():
            line = line.replace('\n','')
            if firstLine:
                nodesTotal = int(line)
                firstLine = False
            else:
                adjList.append(line.split(' ')) 
    return adjList, nodesTotal
        
        

def main():
    [adjList, nodesTotal] = inputAdjacencies("./data/rosalind_tree.txt")
    
    clusters = {node:[] for node in range(1,nodesTotal+1)}
    
    for nodes in adjList:
        n0 = int(nodes[0])
        n1 = int(nodes[1])
        clusters[n0].append(n1)
        clusters[n1].append(n0)
        
    trees=[]
    for c in clusters:
        newTree=True
        for tree in trees:
            if c in tree:
                tree.update(clusters[c])
                newTree=False
        if newTree:
            currentSet=set()
            currentSet.add(c)
            currentSet.update(clusters[c])
            trees.append(currentSet)
        
    print(len(trees)-1)
     
   

if __name__ == '__main__':
    main()

