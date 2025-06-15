class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_cycle_listnode(arr, pos):
    if not arr:
        return None

    nodes = [ListNode(x) for x in arr]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos == -1:
        return nodes[0]

    nodes[-1].next = nodes[pos]

    return nodes[0]


def main():
    test_list = [
        [[3, 2, 0, -4], 1],  # true
        [[1, 2], 0],  # true
        [[1], -1],  # false
    ]
    for head, pos in test_list:
        res = build_cycle_listnode(head, pos)
        print(f"res: {res}")  # This will print the ListNode structure or None
        # You can implement a function to print the ListNode for better visualization if needed


if __name__ == "__main__":
    main()
