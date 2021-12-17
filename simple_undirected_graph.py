import random
import itertools

def Graph():
    #importing randoom and itertools function
    graph = {}
    edges = []
    vertices = ["a", "b", "c", "d", "e", "f", "g", "h","i","j"]
    print("Vertices :", "\n", vertices)

    #creating random edges for the vertices
    #for every vertice
    for n in vertices:
        #select a random  number from 0 to 8
        num = random.randint(0, 8)
        #create random edges with the sample function using the random number generated above as the amount of degrees for the vertice and index to select
        edge = random.sample(range(len(vertices)), num)
        #using the index to select the edges chosen above
        edge2 = [vertices[n] for n in edge]
        #creating the graph as a dictionary
        graph[n] = edge2
        #checking and removing loops since an undirected simple graph can't have a loop
        for e in graph[n]:
            if e == n:
                graph[n].remove(e)

    print("Graph :","\n", graph)

    #This section joins the vertex and prints them out
    #collating a list of the edges
    edge = [r for r in graph.values()]
    #collating a list of the vertex
    node = [r for r in graph.keys()]
    #for every node and for every othe vertex in the list of edges belonging to the initial vertex, join them together in a list
    for n in node:
        #checking if there are no loops with if statement
        e = [[n,e] for e in edge[node.index(n)] if n != e]
        edges += e
    print("Edges :","\n",edges)

    #this section checks if the graph is connected
    #creating a variable and setting it to 0
    count = 0
    #creating all possible combinations of the vertices
    all_edges = [i[1] for i in edges]
    #for each combination in the list above
    for i in all_edges:
        #remove all duplicates first
        all_edges.remove(i[::-1])
        #if a combination exists in the edges list
        if i or i[::-1] in edges:
            #add 0 to the count
            count += 0
        #else if there's a combination not in the edges list
        else:
            #add 1 to the count
            count += 1
    #if the count is greater than 2, then the graph is not connected
    if count > 2:
        print("This is an unconnected graph")
    #else the count is connected
    else:
        print("This is a connected graph")

    #This function prints an euler path
    def euler_path():
        #checking the degrees of each vertice
        length = [len(graph[i]) for i in graph]
        #selecting the node with the highest degree that would be the starting point
        maxi = max(length)
        start = node[length.index(maxi)]
        #creating a condition for a while loop
        done = "no"
        #creating  a list to contain the circuit
        pathway = []
        while done == "no":
            #create  a list called path
            path = []
            #for every edge connedcted to the starting point
            for i in edges:
                #add it to the path list
                if i[0] == start:
                    path.append(i)
            #for evert edge connected to the starting point
            for k in path:
                #checking if the edge is conected to other edges, and if it isn't remove it form the path list
                if len(graph[k[1]]) == 0:
                    path.remove(k)
            #picking the next vertex to go through
            next = path[0]
            #removing the edge that has been passed
            edges.remove(next)
            try:
                #if the edge exists twice, remove the second one
                edges.remove(next[::-1])
            except ValueError:
                #ignore if it doesn't
                pass
            #appending the vertex passed to the pathway list
            pathway.append(start)
            #changing the starting vertex to the next one selected
            start = next[1]
            #if the edges list is finally empty, then end the loop
            if edges == []:
                done = "yes"

        print(pathway)

#This section checks if there's an euler circuit
    #create a variable count and equate to 0
    count = 0
    #for every vertice in the graph
    for i in graph:
        #check if it has an even degree
        if len(graph[i]) % 2 == 0:
            #add 1 to the count if it does
            count += 1
    #if the count variable is equal to ten, then it contains an euler circuit
    if count == 10:
        print("This graph contains an euler circuit")
        #call the function to print the euler path
        euler_path()
    else:
        print("This graph contains no euler circuit")





Graph()
