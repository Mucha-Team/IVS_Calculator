
import mathlib
import unittest

class TestCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(mathlib.add(3,8),11)
		self.assertEqual(mathlib.add(3,-8),-5)
		self.assertEqual(mathlib.add(0,2),2)
		self.assertEqual(mathlib.add(0.2,1.6),1.8)

	def test_sub(self):
		self.assertEqual(mathlib.sub(3,8),-5)
		self.assertEqual(mathlib.sub(10,4),6)
		self.assertEqual(mathlib.sub(0,0),0)
		self.assertEqual(mathlib.sub(0,1),-1)
		self.assertEqual(mathlib.sub(2,-1),3)

	def test_mul(self):
		self.assertEqual(mathlib.mul(3,0),0)
		self.assertEqual(mathlib.mul(-5,-2),10)
		self.assertEqual(mathlib.mul(8645,0),0)
		self.assertEqual(mathlib.mul(0.5,0),0)
		self.assertEqual(mathlib.mul(2,1.5),3)
		self.assertEqual(mathlib.mul(32,-1),-32)

	def test_div(self):
		self.assertEqual(mathlib.div(10,2),5)
		self.assertEqual(mathlib.div(5,-1),-5)
		self.assertEqual(mathlib.div(0,5),0)
		self.assertEqual(mathlib.div(-8,-2),4)
		self.assertEqual(mathlib.div(5,2),2.5)
		self.assertEqual(mathlib.div(7,3.5),2)

		# division by zero
		with self.assertRaises(ZeroDivisionError):
			mathlib.div(5,0)

if __name__ == '__main__':
	unittest.main()
	