def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        node.successor = prevnode
        node = nextnode
    return prevnode

# Define a simple Node class for testing
class Node:
    def __init__(self, value, successor=None):
        self.value = value
        self.successor = successor
    
    def to_list(self):
        """Helper method to convert linked list to Python list for easy comparison"""
        result = []
        current = self
        while current:
            result.append(current.value)
            current = current.successor
        return result

def test_reverse_linked_list():
    # Test case 1: Single node list
    node1 = Node(1)
    reversed_head = reverse_linked_list(node1)
    assert reversed_head.to_list() == [1], f"Expected [1], got {reversed_head.to_list()}"
    
    # Test case 2: Two node list
    node1 = Node(1)
    node2 = Node(2)
    node1.successor = node2
    reversed_head = reverse_linked_list(node1)
    assert reversed_head.to_list() == [2, 1], f"Expected [2, 1], got {reversed_head.to_list()}"
    
    # Test case 3: Three node list
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.successor = node2
    node2.successor = node3
    reversed_head = reverse_linked_list(node1)
    assert reversed_head.to_list() == [3, 2, 1], f"Expected [3, 2, 1], got {reversed_head.to_list()}"
    
    # Test case 4: Longer list
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.successor = node2
    node2.successor = node3
    node3.successor = node4
    node4.successor = node5
    reversed_head = reverse_linked_list(node1)
    assert reversed_head.to_list() == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {reversed_head.to_list()}"
    
    # Test case 5: Empty list (None)
    reversed_head = reverse_linked_list(None)
    assert reversed_head is None, f"Expected None, got {reversed_head}"
    
    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_reverse_linked_list()
