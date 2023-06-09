proposicoes = ['^', 'v', '>']
ramo = []
ramo2 =[]
class Node:
    def __init__(self, expression):
        self.expression = expression
        self.inner = True
        self.left = None
        self.right = None
        self.middle = None
        self.parent = None
    def __repr__(self):
        return f"Node(expression={self.expression} {self.inner}, left={self.left}, right={self.right}, middle={self.middle}))"
        
def sentenceSplitter(char_array):
    if len(char_array) == 1:
        return None, None, '', True, True
    global proposicoes
    found = False 
    colchetesExteriores = 0 
    proposicao = ''
    left = []
    right = []
    leftIsFalse = False
    rightIsFalse = False 
        
    for id,char in enumerate(char_array):
        if char == '(':
            colchetesExteriores += 1
            if id == 0:
                continue
        elif char == ')':
            colchetesExteriores -= 1
            if id == len(char_array) - 1:
                return ''.join(left), ''.join(right), proposicao, leftIsFalse, rightIsFalse
        if  char in proposicoes and colchetesExteriores == 1: 
            found = True
            proposicao = char
            continue
        if not(found) and char != '':
            left.append(char)
        elif found and char != '':
            right.append(char)

def descerArvore(node, expression, expressionInner):
    if node is None:
        return
    if expression is None:
        return 
    if node.middle != None:
        descerArvore(node.middle, expression, expressionInner)
        return 
    if node.left != None or node.right != None:
        descerArvore(node.left, expression, expressionInner)
        descerArvore(node.right, expression, expressionInner)
        return
    construirNode(node, expression, expressionInner)
    
def construirNode(node, expression, expressionInner):
    if node is None:
        return 
    if expression is None:
        return
    left, right, prop, leftIsFalse, rightIsFalse = sentenceSplitter(expression)
    if left != None:
        if len(left) > 1 and left[0] == "~":
            left = left[1:]
            leftIsFalse = True
    if right != None:
        if len(right) > 1 and right[0] == "~":
            right = right[1:]
            rightIsFalse = True
    if prop == '>' and expressionInner == False:
        node.middle = Node(left)
        node.middle.inner = True 
        if leftIsFalse == True:
            node.middle.inner = False
        node.middle.middle = Node(right)
        node.middle.middle.inner = False
        if rightIsFalse == True:
            node.middle.middle.inner = True
    elif prop == '>' and expressionInner == True:
        node.left = Node(left)
        node.left.inner = False
        if leftIsFalse == True:
            node.left.inner = True    
        node.right = Node(right)
        node.right.inner = True
        if rightIsFalse == True:
            node.right.inner = False
    elif prop == '^' and expressionInner == True:
        node.middle = Node(left)
        node.middle.inner = True 
        if leftIsFalse == True:
            node.middle.inner = False
        node.middle.middle = Node(right)
        node.middle.middle.inner = True
        if rightIsFalse == True:
            node.middle.middle.inner = False
    elif prop == '^' and expressionInner == False:
        node.left = Node(left)
        node.left.inner = False
        if leftIsFalse == True:
            node.left.inner = True
        node.right = Node(right)
        node.right.inner = False
        if rightIsFalse == True:
            node.right.inner = True
    elif prop == 'v' and expressionInner == False:
        node.middle = Node(left)
        node.middle.inner = False
        if leftIsFalse == True:
            node.middle.inner = True
        node.middle.middle = Node(right)
        node.middle.middle.inner = False
        if rightIsFalse == True:
            node.middle.middle.inner = True
    elif prop == 'v' and expressionInner == True:
        node.left = Node(left)
        node.left.inner = True
        if leftIsFalse == True:
            node.left.inner == False
        node.right = Node(right)
        node.right.inner = True
        if rightIsFalse == True:
            node.right.inner = False
    if node.left != None and expressionInner != None:
        descerArvore(node.left, node.left.expression, node.left.inner)
        descerArvore(node.right, node.right.expression, node.right.inner)
    elif node.middle != None:
        descerArvore(node.middle, node.middle.expression, node.middle.inner)
        if node.middle.middle != None:
            descerArvore(node.middle.middle, node.middle.middle.expression, node.middle.middle.inner)

def consertarNodos(node):
    if len(node.expression) == 1:
        if node.expression.isupper() and node.inner == False:
            node.expression = node.expression.lower()
        elif node.expression.islower() and node.inner == False:
            node.expression = node.expression.upper()
    if node.middle != None:
        consertarNodos(node.middle)
    if node.left != None or node.right != None:
        consertarNodos(node.left)
        consertarNodos(node.right)

def funcaoDescida(node):
    if node.middle != None:
        node.middle.parent = node
        funcaoDescida(node.middle)
        return
    elif node.left != None or node.right != None:
        node.left.parent = node
        node.right.parent = node 
        funcaoDescida(node.left)
        funcaoDescida(node.right)
        return
    if node.middle is None and node.left is None and node.right is None:
        funcaoSubida(node)

def funcaoSubida(node):
    global ramo
    global ramo2
    if node.parent != None:
        if len(node.expression) == 1:
            if node.expression.isupper() and node.expression.lower() in ramo:
                ramo =[]
                return
            elif node.expression.islower() and node.expression.upper() in ramo:
                ramo = []
                return
            ramo.append(node.expression)
        funcaoSubida(node.parent)
    elif node.parent == None:
        ramo2.append(ramo)
        ramo = []

def main():
    global ramo
    sentenca = list(input("Digite a proposição: "))
    raiz = Node(sentenca)
    raiz.inner = False
    construirNode(raiz, raiz.expression, raiz.inner)
    consertarNodos(raiz)
    funcaoDescida(raiz)
    print(repr(raiz))
    if len(ramo2) != 0:
        print("Esta proposição é inválida, valores possíveis:")
        print(ramo2)
    else:
        print(ramo2)
        print("Válida!")
main()
        