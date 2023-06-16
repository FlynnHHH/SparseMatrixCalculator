class Matrix:
    




row1, col1 = map(int, input().split())
row2, col2 = map(int, input().split())
if row1 <= 0 or row1 > 20 or col1 <= 0 or col1 > 20 or row2 <= 0 or row2 > 20 or col1 <= 0 or col1 > 20:
    print("ERROR")
else:
    