


import unittest
from Data import DataController

class test(unittest.TestCase):
 def setUp(self):
  self.d1 = DataController()
   



 def testsetThreshold_1(self):
  a = self.d1.setThreshold(50)

  print(a)

 def testsetThreshold_2(self):
  a = self.d1.setThreshold(150)

  print(a)
  print('\n')
 
      

 def testmoistureinpercent_1(self):
  a = self.d1.moistureinPercent(50)
   
  print(a)
 
 def testmoistureinpercent_2(self):
  a = self.d1.moistureinPercent(150)
   
  print(a)
  print('\n')
  
 def testisRaining_1(self):
  a = self.d1.isRaining(50)
  
  print(a) 

 def testisRaining_2(self):
  a = self.d1.isRaining(150)
  
  print(a) 
  print('\n')
if __name__=='__main__':
 unittest.main()
 
