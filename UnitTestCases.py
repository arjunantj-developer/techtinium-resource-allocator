import unittest
from allocator import result

class testResourceAllocator(unittest.TestCase):

    defaultExpectedResult = {'Output': [{'region': 'NewYork', 'total_cost': 10150, 'machines': [('8xLarge', 7), ('xLarge', 1), ('Large', 1)]}, {'region': 'India', 'total_cost': 9520, 'machines': [('8xLarge', 7), ('Large', 3)]}, {'region': 'China', 'total_cost': 8570, 'machines': [('8xLarge', 7), ('xLarge', 1), ('Large', 1)]}]}
    sample1 = {'Output': [{'region': 'NewYork', 'total_cost': 11000, 'machines': [('8xLarge', 1), ('2xLarge', 1), ('xLarge', 1), ('Large', 1)]}, {'region': 'India', 'total_cost': 10665, 'machines': [('8xLarge', 1), ('2xLarge', 1), ('Large', 3)]}, {'region': 'China', 'total_cost': 9450, 'machines': [('8xLarge', 1), ('xLarge', 3), ('Large', 1)]}]}
    sample2 = {'Output': [{'region': 'NewYork', 'total_cost': 118248, 'machines': [('8xLarge', 6), ('4xLarge', 1), ('2xLarge', 1), ('xLarge', 1)]}, {'region': 'India', 'total_cost': 112596, 'machines': [('8xLarge', 6), ('4xLarge', 1), ('2xLarge', 1), ('Large', 2)]}, {'region': 'China', 'total_cost': 100200, 'machines': [('8xLarge', 6), ('4xLarge', 1), ('xLarge', 3)]}]}
    def testDefaultTestCase(self):
        self.assertEqual(self.defaultExpectedResult, result(1150,1))

    def testSampleTest1(self):
        self.assertEqual(self.sample1, result(230,5))

    def testSampleTest2(self):
        self.assertEqual(self.sample2,result(1100,12))



if __name__=="__main__":
    unittest.main()
