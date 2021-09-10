# 2. Закодируйте любую строку по алгоритму Хаффмана.
from queue import PriorityQueue


class MyPriorityQueue(PriorityQueue):
    def __str__(self):
        r = ""
        for i in self.queue:
            r += f"Priority {i[0]} - \n" + str(i[1])
            r += "\n"
        return r


class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        r = "\n"
        r += f"Node {self.data}"
        r += "\n"
        r += f"Left {self.left}"
        r += "\n"
        r += f"Right {self.right}"
        r += "\n"
        return r

    # defining comparators less_than and equals
    def __lt__(self, other):
        #  print(f"Comparing {self.data[1]} and {other.data[1]}")
        return self.data[1] < other.data[1]

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return self.data == other.data


def get_frequency(s):
    frequency = {}
    for i in s:
        frequency[i] = s.count(i)
    return frequency


def prepare_queue(frequency: dict):
    haffman_queue = MyPriorityQueue()

    for key in frequency:
        item = frequency[key]
        haffman_queue.put((item, Node((key, item))))

    return haffman_queue


def search(tree: Node, path, table):
    print(f"Walk Left {tree.left} path {path} table {table}")
    if tree.data[0] != '':
        table[tree.data[0]] = path
    if tree.left is not None:
        search(tree.left, path + "0", table)
    print(f"\nWalk Right {tree.right}")
    if tree.right is not None:
        search(tree.right, path + "1", table)
    return table


def create_table(haffman_queue: MyPriorityQueue):
    item: Node = haffman_queue.get_nowait()[1]
    binary_table = search(item, "", {})
    print(binary_table)
    return binary_table


def string_to_bin(binary_table, s):
    pass


def haffman_encoding(s):
    frequency = get_frequency(s)
    haffman_queue = prepare_queue(frequency)
    while True:
        item1 = None
        item2 = None
        try:
            item1 = haffman_queue.get_nowait()
            item2 = haffman_queue.get_nowait()
            # print(f"Item1 {item1[1]}")
            # print(f"Item2 {item2[1]}")
            new_item = Node(data=('', item1[0] + item2[0]), left=item1[1], right=item2[1])
            # print(f"New item {new_item}")
            haffman_queue.put((new_item.data[1], new_item))
        except Exception as e:
            print(e)
            if item1 is not None:
                haffman_queue.put((item1[0], item1[1]))
            break
    binary_table = create_table(haffman_queue)
    return string_to_bin(binary_table, s)


s = input("Input string: ")
print(f"Encoded String:\n {haffman_encoding(s)}")
