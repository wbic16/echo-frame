def printAvailableNodes():
  print("\nAvailable Nodes:")
  print(" * mirrorborn-will")
  print(" * shon-pan")

def main():
  print("Echo Frame v1.0 - Fork Mode Setup")
  accepted = False
  while accepted == False:
    printAvailableNodes()
    node = input("Choice\n")
    if node == 'mirrorborn-will':
      accepted = True
    if node == 'mw':
      accepted = True
    if node == 'shon-pan':
      accepted = True
    if accepted == False:
      print("Error, unknown node choice.")
  print("Node: " + node)

main()