import unittest
from func import avg

#You must start the test case functionname with test

class FunctionText(unittest.TestCase):
    def test_avg(self):
        self.assertEqual(avg(1, 2, 3, 4), 2.5)
    
    def test_avg_2(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, "4"), 2)
     
     
    def test_avg_4(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, float), 2)  
            
    def test_avg_3(self):
            self.assertTrue(isinstance(avg(1, 2, 3), float))  


if __name__ == "__main__":
    unittest.main()