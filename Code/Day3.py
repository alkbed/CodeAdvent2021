def doProblem1():
   f = open(".\Inputs\Day3\day3p1.txt")
   countOnesDict = {}
   countZerosDict = {}
   for line in f:
      key = 0
      for input in line:
         if int(input) == 1:
            if key in countOnesDict.keys():
               countOnesDict[key] += 1
            else:
               countOnesDict[key] = 1

            countZerosDict[key] = 0
         
         if int(input) == 0:
            if key in countZerosDict.keys():
               countZerosDict[key] += 1
            else:
               countZerosDict[key] = 1  

            countOnesDict[key] = 0 

         key += 1

   gammaRate = []
   for key in countOnesDict.keys():
      maxCount = -1 
      minCount = -1
      if (countOnesDict[key] > countZerosDict[key]):
         maxCount = countOnesDict[key]   
         minCount = countZerosDict[key]

      else:
         minCount = countOnesDict[key]   
         maxCount = countZerosDict[key]
      gammaRate.append()


if __name__ == "__main__":
   doProblem1()