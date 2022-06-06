from unittest import TestCase


def quick_sort(items):
    if len(items) <= 1:
        return items
    else:
        pivot = items.pop()

    items_greater = []
    items_lower = []
    for item in items:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


class Test(TestCase):
    def test_quick_sort(self):
        expected = [0, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9]
        result = quick_sort([5, 6, 7, 8, 9, 8, 7, 6, 5, 7, 8, 9, 0])  # return [0, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9]
        self.assertEqual(expected, result)
