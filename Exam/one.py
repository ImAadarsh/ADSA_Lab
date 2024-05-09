class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_linked_lists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    # Store the heads of both lists for later use
    merged_head = head1
    temp_head2 = head2

    while head1.next:
        head1 = head1.next

    head1.next = temp_head2

    return merged_head

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

# Creating linked list 2: 4 -> 5 -> 6
list2 = ListNode(4)
list2.next = ListNode(5)
list2.next.next = ListNode(6)

# Merging linked lists
merged_head = merge_linked_lists(list1, list2)

# Printing merged linked list
print("Merged Linked List:")
print_linked_list(merged_head)
