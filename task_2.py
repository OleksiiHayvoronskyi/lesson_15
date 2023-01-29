# Завдання 2. Взявши за основу код з дом. завдання лекції 14,
# розробіть набір тестів з використання бібліотеки pytest для методів
# додавання нових елементів, пошуку мін. та макс. значень і видалення елементів
# бінарного дерева.

print('\n--- Task 2 ---')

''' Рядки з кодом тестування програми: 
42–47, 56-60, 69-73, 105-110, 132, 136-137, 140 '''


# Клас Binary Search Tree
class BSTree:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    # Метод вставки нового елемента.
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTree(val)
            print('\nAdded to the left:', val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTree(val)
        print('\nAdded to the right:', val)

    # ТЕСТУВАННЯ 1. Метод INSERT.
    def test_insert(self, val):
        assert self.insert(val) == self.insert(val)
        print('========' * 5)
        print('TEST 1. INSERT method (OK): result =', val)
        print('========' * 5, '\n')

    # Метод пошуку мінімального елемента.
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    # ТЕСТУВАННЯ 2. Метод GET_MIN.
    def test_get_min(self):
        print('========' * 5)
        assert self.get_min() == self.get_min()
        print('TEST 2. GET_MIN method (OK): result =', self.get_min())

    # Метод пошуку максимального елемента.
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    # ТЕСТУВАННЯ 3. Метод GET_MAX.
    def test_get_max(self):
        assert self.get_max() == self.get_max()
        print('TEST 3. GET_MAX method (OK): result =', self.get_max())
        print('========' * 5, '\n')

    # Метод видалення елемента.
    def delete(self, val):
        if self is None:
            return self

        elif val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        print(val, 'was deleted')

        if self.right is None:
            return self.left

        if self.left is None:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)

        return self

    # ТЕСТУВАННЯ 4. Метод DELETE!
    def test_delete(self, val):
        assert self.delete(val) == self.delete(val)
        print('========' * 5)
        print('TEST 4. DELETE method (OK): result =', val)
        print('========' * 5)

    # Метод друку.
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()


tree = BSTree(12)
tree.left = BSTree(2)
tree.left = BSTree(3)
tree.left = BSTree(4)
tree.right = BSTree(5)
tree.right.left = BSTree(23)

print("Binary tree:")
tree.print_tree()

# tree.insert(25)
tree.test_insert(25)  # ТЕСТУВАННЯ для insert.

print('Min:', tree.get_min())
print('Max:', tree.get_max())
tree.test_get_min()  # ТЕСТУВАННЯ для get_min.
tree.test_get_max()  # ТЕСТУВАННЯ get_max.

# tree.delete(4)
tree.test_delete(4)  # ТЕСТУВАННЯ delete.
