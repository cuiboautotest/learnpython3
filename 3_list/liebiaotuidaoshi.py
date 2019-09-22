"""
各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边第一条语句是最后一层。
"""

list = [x*y for x in range(1,5) if x > 2 for y in range(1,4) if y < 3]
print(list)

