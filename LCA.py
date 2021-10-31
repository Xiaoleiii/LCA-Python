class Node:
    def __init__(self,val):
        self.val = val
        self.children = []
        self.parents = []

def addChild(node,child):
    node.children.append(child)

def addParent(node,parent):
    node.parents.append(parent)

def findLCA(root,node1,node2):
    if root is None:
        return False
    path1 = []
    path2 = []
    findPath(root,node1,path1)
    findPath(root,node2,path2)
    lca =0

    for i in path1:
        for j in path2:
            if i.val==j.val:
                lca = i.val
    return lca

def findPath(root,a,path):
    path.append(root)
    if a.val==root.val:
        return True

    for i in root.children:
        if findPath(i,a,path):
            return True

    path.pop()
    return False

def findAnc(root,node,anc):
    anc.append(node.val)
    if(node.val==root.val):
        return

    for i in node.parents:
        findAnc(root,i,anc)

def DAG(root,node1,node2):
    if root is None:
        return False

    anc = []
    ancestors2 = []
    findAnc(root,node1,anc)
    findAnc(root,node2,ancestors2)
    for i in anc:
        for j in ancestors2:
            if i== j:
                return i
