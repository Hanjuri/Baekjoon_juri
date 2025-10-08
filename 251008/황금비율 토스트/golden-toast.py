#문제 풀이
#Node 클래스를 만들어준다
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# 이중 연결 리스트 클래스를 만들어준다
class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)    # dummy node : 실제 데이터는 없지만 리스트의 시작이나 끝을 표시하기 위함
        self.head = self.END
        self.tail = self.END     #self.tail은 맨 끝 더미 노드로 END다. self.tail.prev가 실제 마지막 노드!
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        
        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None
    
    def push_back(self, new_data):     #원소를 맨 끝 위치에 넣기
        if self.begin() == self.end(): #만약 리스트가 비어있다면
            self.push_front(new_data)  # 맨 앞에 원소를 넣어주는 것과 로직 동일
        
        else:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node
        
    
    def erase(self, node):
        next_node = node.next
        
        if node == self.begin(): #만약 head가 삭제되어야 한다면
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
        
        return next_node
    
    def insert(self, node, new_data):
        if node == self.end():
            self.push_back(new_data)
        
        elif node == self.begin():
            self.push_front(new_data)
        
        else :
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
    
    def begin(self):
        return self.head
    
    def end(self):
	    return self.tail
	          

bread_no, recipe_no = map(int, input().split())
bread_state = input()


l = DoublyLinkedList()

for letter in bread_state:
    l.push_back(letter)

#iterator 정의
it = l.end()

for _ in range(recipe_no):
    command = input()
    
    if command.startswith("L"):
        if it != l.begin():
            it = it.prev
    
    elif command.startswith("R"):
        if it != l.end():
            it = it.next
    
    elif command.startswith("D"):
        if it != l.end():
            it = l.erase(it)
    
    else:
        _, c = command.split()
        l.insert(it, c)

#출력
it = l.begin()
while it != l.end():
    print(it.data, end="")
    it= it.next