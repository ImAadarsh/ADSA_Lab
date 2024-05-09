class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_linked_lists(head1, head2, len1, len2):
    # Joining the heads of the two lists
    current = head1
    while current.next:
        current = current.next
    current.next = head2

    # Traverse len1 steps to the right
    ptr1 = head1
    for _ in range(len1):
        print(ptr1.value, end=" -> ")
        ptr1 = ptr1.next

    # Traverse len2 steps to the left
    ptr2 = head2
    for _ in range(len2):
        print(ptr2.value, end=" <- ")
        ptr2 = ptr2.next

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Creating linked list 1: 1 -> 2 -> 3
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)

# Creating linked list 2: 7 -> 6 -> 5
list2 = ListNode(7)
list2.next = ListNode(6)
list2.next.next = ListNode(5)

# Set the lengths of the lists
len1 = 3
len2 = 3

# Joining the lists and traversing
merge_linked_lists(list1, list2, len1, len2)
