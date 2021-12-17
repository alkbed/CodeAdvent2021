def firstProblem():  
   f = open("./Inputs/day1p1.txt")
   firstLine = True
   prevLine = -1
   countLines = 0
   countIncreased = 0
   for line in f:
      if firstLine:
         firstLine = False

      else:
         if int(line) > prevLine:
            countIncreased+=1
      countLines+=1
      prevLine = int(line)
      

   print("Number of increased lines: " + str(countIncreased))
   print("Number of lines: " + str(countLines))


def secondProblem():
   f = open("./Inputs/day1p2.txt")
   lineNum = 0
   lineArr = []
   sumArr = []
   sumIndex = 0
   numTriplesIncreased = 0

   for line in f:
      lineArr.append(int(line))
      if lineNum >= 2:
         sumArr.append(lineArr[lineNum - 2] + lineArr[lineNum - 1] + lineArr[lineNum])
         if sumIndex != 0:
            if (sumArr[sumIndex] > sumArr[sumIndex - 1]):
               numTriplesIncreased += 1
         sumIndex += 1
         
      lineNum +=1

   print("Number of triples increased: " + str(numTriplesIncreased))

if __name__ == "__main__":
   firstProblem()
   secondProblem()