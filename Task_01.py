class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.is_sorted = False

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.is_sorted = False

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self.is_sorted = False

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.is_sorted = False

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def show_list(self):
        current = self.head
        while current is not None:
            print(
                "(" + str(current.data) + ")",
                end=" --> " if current.next is not None else "",
            )
            current = current.next

    # Reverse linked list
    def reverse_linked_list(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next  # Зберігаємо посилання на наступний вузол
            current.next = prev  # Змінюємо посилання на попередній вузол

            # Пересуваємо вказівники на наступну ітерацію
            prev = current
            current = next_node

        # Новий початок списку - останній вузол
        self.head = prev

    # Insertion sort
    def insertion_sort_linked_list(self):
        head = self.head
        if self is None or head.next is None:
            return self

        sorted_head = None

        while head is not None:
            next_node = head.next

            # Вставка поточного вузла у відсортований список
            sorted_head = self.insert_into_sorted(sorted_head, head)

            head = next_node

        self.head = sorted_head
        self.is_sorted = True

    @staticmethod
    def insert_into_sorted(sorted_head, node):
        if sorted_head is None or node.data <= sorted_head.data:
            node.next = sorted_head
            return node

        current = sorted_head

        while current.next is not None and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node

        return sorted_head

    # Merge two sorted lists
    def merge_sorted_lists(self, external_list):
        current = LinkedList()

        if not self.is_sorted:
            self.insertion_sort_linked_list()
        if not external_list.is_sorted:
            external_list.insertion_sort_linked_list()

        list1 = self
        list2 = external_list

        while list1.head is not None and list2.head is not None:
            if list1.head.data < list2.head.data:
                current.insert_at_end(list1.head.data)
                list1.head = list1.head.next
            else:
                current.insert_at_end(list2.head.data)
                list2.head = list2.head.next

        if list1.head is not None:
            current.insert_at_end(list1.head.data)
        elif list2.head is not None:
            current.insert_at_end(list2.head.data)

        return current


def main():
    llist = LinkedList()
    llist.insert_at_end(14)
    llist.insert_at_end(87)
    llist.insert_at_end(5)
    llist.insert_at_end(32)
    llist.insert_at_end(42)
    llist.insert_at_end(8)
    llist.insert_at_end(19)
    llist.insert_at_end(120)
    llist.show_list()

    llist.reverse_linked_list()
    print()
    llist.show_list()
    llist.insertion_sort_linked_list()
    print()
    llist.show_list()
    print()

    llist2 = LinkedList()
    llist2.insert_at_end(17)
    llist2.insert_at_end(222)
    llist2.insert_at_end(2)
    llist2.insert_at_end(68)
    llist2.insert_at_end(99)
    llist2.insert_at_end(79)
    llist2.insert_at_end(33)
    llist2.insertion_sort_linked_list()

    merged_list = llist.merge_sorted_lists(llist2)

    current = merged_list.head
    while current is not None:
        print(
            "(" + str(current.data) + ")",
            end=" --> " if current.next is not None else "",
        )
        current = current.next


if __name__ == "__main__":
    main()