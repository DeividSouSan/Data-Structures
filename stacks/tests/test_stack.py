
import unittest
from stacks.data_structure_v1.stack import EmptyStack, Stack


class TestStackMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def tearDown(self) -> None:
        self.stack = Stack()

    def test_add_one_element(self):
        added_element = self.stack.push(1)

        self.assertEqual(added_element, 1, "Return of function not working")
        self.assertListEqual(self.stack.items, [
                             1], "Stack didn't add the element")
        self.assertEqual(self.stack.size, 1, "Stack size differ from 1")

    def test_add_various_elements(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        self.assertEqual(self.stack.items, [
                         1, 2, 3, 4], "Stack didn't add the element")
        self.assertEqual(self.stack.size, 4, "Stack size differ from 1")

    def test_pop_empty_stack(self):
        with self.assertRaises(EmptyStack) as context:
            self.stack.pop()

        self.assertIn("Can't pop empty list", str(context.exception))

    def test_pop_one_element(self):
        self.stack.push(1)

        poped_element = self.stack.pop()

        self.assertEqual(poped_element, 1, "Return of function not working")
        self.assertListEqual(self.stack.items, [],
                             "Return of function not working")
        self.assertEqual(self.stack.size, 0, "Return of function not working")

    def test_empty_stack_is_empty(self):
        # The stack is initialized empty
        self.assertListEqual(self.stack.items, [], "The stack should be empty")
        self.assertEqual(self.stack.size, 0,
                         "The stack should have no elements")

    def test_stack_is_empty_after_pop(self):
        self.stack.push(1)

        self.stack.pop()

        self.assertListEqual(self.stack.items, [], "The stack should be empty")
        self.assertEqual(self.stack.size, 0,
                         "The stack should have no elements")
