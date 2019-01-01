class Node:

    def __init__(self, value):
        self.info = value
        self.link = None


class SinglyLinkedList:

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print('List is empty')
            return
        else:
            print('List is : ')
            p = self.start
            while p is not None:
                print(p.info, ' ', end='')
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print('Number of nodes in our list are ', n)

    def search(self, x):
        pos = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print('Element is present at ', pos)
                return True
            pos += 1
            p = p.link

        else:
            print(x, ' not found')
            return False

    def insert_beg(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_end(self, data):
        temp = Node(data)
        p = self.start
        if p is None:
            self.start = temp
            return

        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input('No. of nodes : '))
        if n==0:
            return
        for i in range(n):
            data = int(input('Enter data : '))
            self.insert_end(data)


    def insert_after(self, data, x):
        pass

    def insert_before(self, data, x):
        pass

    def insert_position(self, data, k):
        pass

    def delete_node(self, x):
        pass

    def del_first(self):
        pass

    def del_last(self):
        pass

    def reverse(self):
        pass

    def bubble_sort_exdata(self):
        pass

    def bubble_sort_exlinks(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge2(self, list2):
        pass

    def _merge2(self, list1, list2):
        pass

    def merge_sort(self):
        pass


list = SinglyLinkedList()

list.create_list()

while True:

    print('##################################################################################################################################')
    print('1. Display list')
    print('2. Count no. of nodes')
    print('3. Searching list')
    print('4. Insertion at Beginning')
    print('5. Insertion at End')
    print('6. Create list')
    option = int(input('Enter option :'))
    if option == 1:
        list.display_list()
    if option == 2:
        list.count_nodes()
    if option == 3:
        data = int(input('Enter the data to be searched : '))
        list.search(data)
    if option == 4:
        data = int(input('Enter the data : '))
        list.insert_beg(data)
    if option == 5:
        data = int(input('Enter the data : '))
        list.insert_end(data)
    if option == 6:
        list.create_list()


