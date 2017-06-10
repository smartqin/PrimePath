#-*- coding:utf8 -*-
import graph1
def readGraph(fileName):
    graph = []
    with open(fileName,'r') as f:
        f.readline()
        while 1:
            line = f.readline()
            if not line:
                break
            line = line.strip('[]\n')
            a = list(line.split(","))
            a = [int(x) for x in a]
            if a[0] == -1:
                a = []
            graph.append(a)
    
    return graph
def cal_out(u):#计算节点出度
        out_degree = len(graph[u])
        return out_degree
def find_all_paths(graph, start, path=[]):#找到
        path = path + [start]
        paths = []
        if cal_out(start)==0:
            return [path]
        for node in graph[start]:
            if node not in path:
                    newpaths = find_all_paths(graph, node, path)
                    for newpath in newpaths:
                            paths.append(newpath)#在结尾添加
            elif node==path[0]:
                    newpath=path+[node]
                    paths.append(newpath)
                    continue
            else:
                    newpath=path                

                    paths.append(newpath)
                    continue
                
        return paths
def findprime(paths):
        primepath=[]
        for i in range(length-1):
            flag=0
            #print"a=",all_paths[i]
            for j in range(i+1,length):
            #print all_paths1[i]
                A=all_paths[i]
                B=all_paths[j]
                #print"B=",B
                if(A_inc_B(A,B)):
                    flag=1
                    break
            if(flag==0):
                primepath.append(A)
        primepath.append(all_paths[length-1])
        return primepath
def A_inc_B(A,B):
        if(any([A==B[i:i+len(A)] for i in range(0,len(B)-len(A)+1)])):
                return 1
        return 0


if __name__ == '__main__':
        name="testt.txt"
        #p=primepaths()
        graph=readGraph(name)
        all_paths=[]
        for u in range(0,len(graph)):
            paths=find_all_paths(graph,u)
            all_paths+=paths
        length=len(all_paths)
        all_paths = sorted(all_paths, reverse=False, key=lambda a: (len(a),a))
        #print all_paths
        
        primepath=findprime(all_paths)  
        print"PrimePaths:",primepath
        #print"PrimePaths Length:",p_len
    
