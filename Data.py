class DataController:
  
  def __init__(self):  
    self.Threshold = 0
    self.MoistureLevelRaw = 0
    self.MoistureLevelPercent = 0
    self.RainLevelRaw = 0
    self.raining = 0

#sets Threshold if value is valid and assigns it
  def setThreshold(self,i):
        if i <= 100:
          if i >= 0:
            Threshold = i
            print('Threshold Test:')
            return True
             
        else: 
          return False
            
    
            
            
#  checks if moisture percent is valid and assigns it 
  def moistureinPercent(self,j):
        if j <=100:
          if j >=0:
            MoistureLevelPercent = j
            print('Moisture Level Test:')
            print('valid moistureLevel : ',MoistureLevelPercent)
           
        else:
          print('invalid moistureLevel', j)
          
  #checks if raining or not            
  def isRaining(self,i):
    if i <= 100:
      if i >= 0:
        Raining = i
        print('If raining:')
        return True
         
    else: 
      return False  

                    


    
    