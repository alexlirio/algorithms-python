from unittest import TestCase


def depth_first_search_recursion(tree, root, target, path=[]):
    """ DFS using recursion """
    path.append(root)
    if target in path:
        return path
    for child in tree[root]:
        depth_first_search_recursion(tree, child, target, path)
    return path if target in path else None


def depth_first_search_recursion__print_all_in_order(tree, root):
    """ DFS using recursion """
    print(root)
    for child in tree[root]:
        depth_first_search_recursion__print_all_in_order(tree, child)


class Test(TestCase):
    def test_depth_first_search_recursion(self):
        expected = ['a', 'b', 'd', 'f', 'c']
        root = 'a'
        tree = {
            'a': ['b', 'c'],
            'b': ['d'],
            'c': ['e'],
            'd': ['f'],
            'e': [],
            'f': []
        }
        result = depth_first_search_recursion(tree, root, 'c')  # return ['a', 'b', 'd', 'f', 'c']
        self.assertEqual(expected, result)

        result = depth_first_search_recursion(tree, root, 'z')  # return None
        self.assertIsNone(result)

        depth_first_search_recursion__print_all_in_order(tree, root)  # print ['a', 'c', 'e', 'b', 'd', 'f']
