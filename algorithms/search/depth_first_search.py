from unittest import TestCase


def depth_first_search(tree, root, target):
    """ DFS uses 'stack'(FILO) """
    result = []
    stack = [root]  # 'stack'(FILO)
    while stack:
        current = stack.pop()  # 'stack' remove from top
        result.append(current)
        if target in result:
            return result
        for child in tree[current]:
            stack.append(child)  # 'stack' add on top
    return None


def depth_first_search__print_all_in_order(tree, root):
    """ DFS uses 'stack'(FILO) """
    stack = [root]  # 'stack'(FILO)
    while stack:
        current = stack.pop()  # 'stack' remove from top
        print(current)
        for child in tree[current]:
            stack.append(child)  # 'stack' add on top


class Test(TestCase):
    def test_depth_first_search(self):
        expected = ['a', 'c', 'e', 'b', 'd']
        root = 'a'
        tree = {
            'a': ['b', 'c'],
            'b': ['d'],
            'c': ['e'],
            'd': ['f'],
            'e': [],
            'f': []
        }
        result = depth_first_search(tree, root, 'd')  # return ['a', 'c', 'e', 'b', 'd']
        self.assertEqual(expected, result)

        result = depth_first_search(tree, root, 'z')  # return None
        self.assertIsNone(result)

        depth_first_search__print_all_in_order(tree, root)  # print ['a', 'c', 'e', 'b', 'd', 'f']
