'''
NAME: ALBASIL ALRAWAHI         ID: 138410

ALGORITHM:

1. Read the map and instructions:
    I read the size of the map, the number of people, and their movement instructions from a file.
    I also read the map itself, where spaces represent walkable areas and other characters represent obstacles.

2. Simplify instructions:
    For each person's instructions, I process them to handle any repetitions (e.g., "RRRRR" becomes "R5").

3. Calculate final positions:
    I use the simplified instructions to determine where each person would end up on the map based on their starting positions.

4. Check if positions are reachable:
    I check each person's final position to see if I could get there from the edge of the map (the boundary).
    I imagine myself trying to walk from their final spot to the edge. If I can only hit obstacles or go off the map entirely, then I can't reach it.

5. Write results:
    I write "Yes" to a file if I can reach the final position and "No" if I can't.

'''
# Function to process a string with nested repeated directions and simplify it
def getDirections(s):
  stack = []
  current_number = 0
  current_string = ''

  for char in s:
    if char.isdigit():
      # Update current number by concatenating digits
      current_number = current_number * 10 + int(char)
    elif char == '[':
      # Push current string and count onto stack for nested repetition
      stack.append((current_string, current_number))
      current_string = ''
      current_number = 0
    elif char == ']':
      # Pop previous string and count, apply repetition, and continue processing
      prev_string, repeat_times = stack.pop()
      current_string = prev_string + current_string * repeat_times
    else:
      # Add non-digit characters to current string
      current_string += char

  return current_string

# Function to check if a position on a grid is reachable from the boundary
def boundary(x, y, done, G):
  done.append((x, y))  # Mark current position as visited
  if x == 0 or y == 0 or x == len(G)-1 or y == len(G)-1:
    return True  # Boundary reached if on edge of grid
  if (x, y) not in done:
    # Check if boundary is reachable from any of the four directions
    if boundary(x-1, y, done, G):
      return True
    if boundary(x+1, y, done, G):
      return True
    if boundary(x, y-1, done, G):
      return True
    if boundary(x, y+1, done, G):
      return True
  return False  # No reachable direction leads to boundary

# Function to calculate final coordinates after following a sequence of directions
def location(s):
  x = 0
  y = 0
  for i in range(len(s)):
    if s[i] == 'U':
      y -= 1  # Move up (decrease y)
    elif s[i] == 'D':
      y += 1  # Move down (increase y)
    elif s[i] == 'L':
      x -= 1  # Move left (decrease x)
    elif s[i] == 'R':
      x += 1  # Move right (increase x)
  return (x, y)

# Main execution block
def main():
  f = open("input_file.txt", "r")
  mapDimension = f.readline()
  print(mapDimension)
  NumOfPeople = f.readline()
  print(NumOfPeople)
  f.readline()  # Skip empty line

  theMap = []
  directions = []

  for i in range(int(NumOfPeople)):
    t = f.readline().strip()  # Read and clean direction string
    print(t)
    t = getDirections(t)  # Process directions
    directions.append(location(t))  # Calculate ending position

  f.readline()  # Skip empty line

  for i in range(int(mapDimension)):
    t = f.readline().strip()
    theMap.append([])
    for j in range(len(t)):
      if t[j] != ' ':
        theMap[i].append(t[j])  # Build map representation
    print(theMap[i])

  o = open("output_file.txt", "w")
  done = []
  for i in range(len(directions)):
    x, y = directions[i]
    if boundary(x, y, done, theMap):
      print("Yes")
      o.write("Yes\n")
    else:
      print("No")
      o.write("No\n")
  o.close()

if __name__ == "__main__":
  main()
