matrix = [[3,7,8],[9,11,13],[15,16,17]]
for row in matrix:
    print(row)
for collunm in zip(*matrix):
    print(collunm)
print(list(zip(*matrix)))