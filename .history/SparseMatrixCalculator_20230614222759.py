class Matrix:
    
row1, col = map(int, input().split())
if row <= 0 or row > 20 or col <= 0 or col > 20:
    print("ERROR")
else:
    