def doProblem2():
   f = open(".\Inputs\Day3\day3p1.txt")
   oxygenRatingNum = []
   co2ScrubberRating = []
   lineLength = len(f.readline()) - 1
   f.seek(0)

   stopOx = False
   stopCO2 = False
   for i in range(lineLength):
      numOnesOx = 0
      numZerosOx = 0
      numOnesCO2 = 0
      numZerosCO2 = 0
      numLineMatchingOx = 0
      numLineMatchingCO2 = 0
      LineMatchingOx = {}
      LineMatchingCO2 = {}
      for line in f:
         if (lineStartsWith(line, oxygenRatingNum) and not stopOx):
            numLineMatchingOx += 1
            LineMatchingOx[numLineMatchingOx] = line
            if int(line[i]) == 1:
               numOnesOx += 1
            elif int(line[i]) == 0:
               numZerosOx += 1

         if (lineStartsWith(line, co2ScrubberRating) and not stopCO2):
            numLineMatchingCO2 += 1
            LineMatchingCO2[numLineMatchingCO2] = line
            if int(line[i]) == 1:
               numOnesCO2 += 1
            elif int(line[i]) == 0:
               numZerosCO2 += 1
      f.seek(0)      
      
      if numLineMatchingOx == 1:
         stopOx = True
         oxygenRatingNum.clear()
         for num in LineMatchingOx[numLineMatchingOx]:
            if num.isdigit():
               oxygenRatingNum.append(int(num))

      if numLineMatchingCO2 == 1:
         stopCO2 = True
         co2ScrubberRating.clear()
         for num in LineMatchingCO2[numLineMatchingCO2]:
            if num.isdigit():
               co2ScrubberRating.append(int(num))

      if not stopOx:
         if numOnesOx > numZerosOx:
            oxygenRatingNum.append(1)

         elif numOnesOx < numZerosOx:
            oxygenRatingNum.append(0)

         elif numOnesOx == numZerosOx:
            oxygenRatingNum.append(1)

      if not stopCO2:
         if numOnesCO2 > numZerosCO2:
            co2ScrubberRating.append(0)

         elif numOnesCO2 < numZerosCO2:
            co2ScrubberRating.append(1)

         elif numOnesCO2 == numZerosCO2:
            co2ScrubberRating.append(0)
   
   print("The oxygen rating is: " + str(ConvertBinaryArrayToInt(oxygenRatingNum)))
   print(oxygenRatingNum)
   print("The CO2 Scrubber rating is: " + str(ConvertBinaryArrayToInt(co2ScrubberRating)))
   print(co2ScrubberRating)

   print("Multiplied together:" + str(ConvertBinaryArrayToInt(co2ScrubberRating) * ConvertBinaryArrayToInt(oxygenRatingNum)))
   
def lineStartsWith(line, rating):
   for i in range(len(rating)):
      if int(line[i]) != rating[i]:
         return False

   return True

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
   doProblem2()