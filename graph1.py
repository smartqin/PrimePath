#-*- coding:utf8 -*-
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
def cal_out(graph,u):#计算节点出度
        out_degree = len(graph[u])
        return out_degree
def find_all_paths(graph, start, path=[]):#找到
        path = path + [start]
        paths = []
        if len(graph[start])==0:
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
        length=len(paths)
        for i in range(length-1):
            flag=0
            #print"a=",all_paths[i]
            for j in range(i+1,length):
            #print all_paths1[i]
                A=paths[i]
                B=paths[j]
                #print"B=",B
                if(A_inc_B(A,B)):
                    flag=1
                    break
            if(flag==0):
                primepath.append(A)
        primepath.append(paths[length-1])
        return primepath
def A_inc_B(A,B):
        if(any([A==B[i:i+len(A)] for i in range(0,len(B)-len(A)+1)])):
                return 1
        return 0
def get_prime(graph,ii):
    all_paths=[]
    for u in range(0,len(graph)):
            paths=find_all_paths(graph,u)
            all_paths+=paths
    length=len(all_paths)
    all_paths = sorted(all_paths, reverse=False, key=lambda a: (len(a),a))
    #print all_paths
    primepath=findprime(all_paths)
    #print"prime:",primepath
    p_len=len(primepath)
    ans='answer'+'%d'%ii+'.txt'
    #ans="testt.txt"
    fp=open(ans,'w')
    fp.write(str(p_len))
    for i in range(0,p_len):
        fp.write('\n'+str(primepath[i]))
    fp.write('\n')   
    #print"PrimePaths:",primepath
    #print"PrimePaths Length:",p_len
if __name__ == '__main__':
    for ii in range(0,16):
        name= 'case'+'%d'%ii+'.txt'
        graph=readGraph(name)
        get_prime(graph,ii)
       
