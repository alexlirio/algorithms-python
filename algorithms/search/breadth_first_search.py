from unittest import TestCase


def breadth_first_search(tree, root, target):
    """ BFS uses 'queue'(FIFO) """
    result = []
    queue = [root]  # 'queue'(FIFO)
    while queue:
        current = queue.pop(0)  # 'queue' remove the first
        result.append(current)
        if target in result:
            return result
        for child in tree[current]:
            queue.append(child)  # 'queue' add at the end
    return None


def breadth_first_search__print_all_in_order(tree, root):
    """ BFS uses 'queue'(FIFO) """
    queue = [root]  # 'queue'(FIFO)
    while queue:
        current = queue.pop(0)  # 'queue' remove the first
        print(current)
        for child in tree[current]:
            queue.append(child)  # 'queue' add at the end


class Test(TestCase):
    def test_breadth_first_search(self):
        expected = ['a', 'b', 'c', 'd', 'e']
        root = 'a'
        tree = {
            'a': ['b', 'c'],
            'b': ['d'],
            'c': ['e'],
            'd': ['f'],
            'e': [],
            'f': []
        }
        result = breadth_first_search(tree, root, 'e')  # return ['a', 'b', 'c', 'd', 'e']
        self.assertEqual(expected, result)

        result = breadth_first_search(tree, root, 'z')  # return None
        self.assertIsNone(result)

        breadth_first_search__print_all_in_order(tree, root)  # print ['a', 'b', 'c', 'd', 'e', 'f']
