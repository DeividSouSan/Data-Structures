import unittest
from Queues.data_structure.queue import Queue

class TestQueue(unittest.TestCase):
    def test_enqueue_on_empty_queue(self):
        queue = Queue()
        success = queue.enqueue(1)
        
        self.assertEqual(success, None)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.size, 1)
        self.assertEqual(queue.start, 1)
        self.assertEqual(queue.end, 1)
        
    def test_enqueue_various_values(self):
        queue = Queue()
        
        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(2)
        queue.enqueue(9)
        
        self.assertEqual(queue.peek(), 3)
        self.assertEqual(queue.size, 4)
        self.assertEqual(queue.start, 3)
        self.assertEqual(queue.end, 9)
        
        
    def test_dequeue_almost_all_values(self):
        queue = Queue()
        
        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(2)
        queue.enqueue(9)
        
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        
        self.assertEqual(queue.peek(), 9)
        self.assertEqual(queue.size, 1)
        self.assertEqual(queue.start, 9)
        self.assertEqual(queue.end, 9)
        
    def test_dequeue_all_values(self):
        queue = Queue()
        
        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(2)
        queue.enqueue(9)
        
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        
        self.assertEqual(queue.peek(), None)
        self.assertEqual(queue.size, 0)
        self.assertEqual(queue.start, None)
        self.assertEqual(queue.end, None)
        
        
    def test_dequeue_empty_queue(self):
        queue = Queue()
        
        queue.dequeue()
        
        self.assertEqual(queue.peek(), None)
        self.assertEqual(queue.size, 0)
        self.assertEqual(queue.start, None)
        self.assertEqual(queue.end, None)