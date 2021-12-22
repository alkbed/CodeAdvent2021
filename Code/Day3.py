def doProblem1():
   f = open(".\Inputs\Day3\day3p1.txt")
   countOnesDict = {}
   countZerosDict = {}
   for line in f:
      key = 0
      for input in line:
         if input.isdigit():
            if int(input) == 1:
               if key in countOnesDict.keys():
                  countOnesDict[key] += 1
               else:
                  countOnesDict[key] = 1
               
               if key not in countZerosDict.keys():
                  countZerosDict[key] = 0
         
            if int(input) == 0:
               if key in countZerosDict.keys():
                  countZerosDict[key] += 1
               else:
                  countZerosDict[key] = 1  

               if key not in countOnesDict.keys():
                  countOnesDict[key] = 0 

            key += 1

   gammaRate = []
   epsilonRate = []
   for key in countOnesDict.keys():
      if (countOnesDict[key] > countZerosDict[key]):
         gammaRate.append(1)
         epsilonRate.append(0)

      else:
         gammaRate.append(0)
         epsilonRate.append(1)

   print("The multiplication is: " + str(ConvertBinaryArrayToInt(gammaRate) * ConvertBinaryArrayToInt(epsilonRate)))
   
def ConvertBinaryArrayToInt(binaryArr):
   largestPower = len(binaryArr) - 1
   constructionInt = 0
   for bit in binaryArr:
      constructionInt += bit * (2**largestPower)
      largestPower -= 1

   return constructionInt

if __name__ == "__main__":
   doProblem1()