from collections import defaultdict
#here x and y arre jug1 and jug2
x, y, aim = 4, 3, 2
visited = defaultdict(lambda: False)
def waterJugSolver(amt1, amt2):
        if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
                 print(amt1, amt2)
                 return True
        if visited[(amt1, amt2)] == False:
                 print(amt1, amt2)
                 visited[(amt1, amt2)] = True
                 return (
                         waterJugSolver(0, amt2) or
                         waterJugSolver(amt1, 0) or
                         waterJugSolver(x, amt2) or
                         waterJugSolver(amt1, y) or
                         waterJugSolver(amt1 + min(amt2,(x-amt1)),amt2 - min(amt2,(x-amt1)))or
                         waterJugSolver(amt1 - min(amt1,(y-amt2)),amt2 + min(amt1,(y-amt2)))
                         )


        else:
              return False
print("Steps: ")
waterJugSolver(0, 0)
print("MARIA LOKHANDWALA-109")
