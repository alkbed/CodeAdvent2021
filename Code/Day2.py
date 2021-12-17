from enum import Enum

class command_enum(Enum):
   UP = 1
   DOWN = 2
   FORWARD = 3
   NONE = 4

def parse_command(line):
   command = line.split()
   amt = int(command[1])
   action = command_enum.NONE
   if command[0] == "up":
      action = command_enum.UP

   elif command[0] == "down":
      action = command_enum.DOWN

   elif command[0] == "forward":
      action = command_enum.FORWARD

   return (action, amt)
   
def apply_command_to_location(x_loc, depth, command):
   if command[0] == command_enum.DOWN:
      depth += command[1]
   if command[0] == command_enum.UP:
      depth -= command[1]
   if command[0] == command_enum.FORWARD:
      x_loc += command[1]
   return (x_loc, depth)

def apply_command_to_location_p2(x_loc, depth, aim, command):
   if command[0] == command_enum.DOWN:
      aim += command[1]
   if command[0] == command_enum.UP:
      aim -= command[1]
   if command[0] == command_enum.FORWARD:
      x_loc += command[1]
      depth += aim * command[1]

   return (x_loc, depth, aim)


def doProblem1():
   f = open("./Inputs/Day2/day2p1.txt", 'r')
   x_loc = 0
   depth = 0

   for line in f:
      parsed_command = parse_command(line)
      new_loc = apply_command_to_location(x_loc, depth, parsed_command)
      x_loc = new_loc[0]
      depth = new_loc[1]
      
   print ("The final location is: " + str(x_loc) + ", " + str(depth))
   print("Multiplied together: " + str(x_loc * depth))

def doProblem2():
   f = open("./Inputs/Day2/day2p1.txt", 'r')
   x_loc = 0
   depth = 0
   aim = 0

   for line in f:
      parsed_command = parse_command(line)
      new_loc = apply_command_to_location_p2(x_loc, depth, aim, parsed_command)
      x_loc = new_loc[0]
      depth = new_loc[1]
      aim = new_loc[2]
      
   print ("The final location for part 2 is: " + str(x_loc) + ", " + str(depth))
   print("Multiplied together: " + str(x_loc * depth))

if __name__ == "__main__":
   doProblem1()
   doProblem2()
   