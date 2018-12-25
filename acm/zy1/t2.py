import sys
def max_area_histogram(histogram):
    stack = list()
    max_area = 0
    index = 0
    while index < len(histogram):
        # print("index  :"+str(index))
        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1
            # print(stack)
        else:
            top_of_stack = stack.pop()
            area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            # print("area  :"+str(area))
            # print(stack)
            max_area = max(max_area, area)
    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)
    return max_area


def max_square(matrix):
    row = len(matrix)
    col = len(matrix[0])
    max_area = 0
    height = []
    for i in range(col):
        height.append(0)
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                height[j] = 0
            else:
                height[j] = height[j] + 1
        # print(height)
        max_area = max(max_area, max_area_histogram(height))
    return max_area


if __name__ == '__main__':
    # line1 = [1, 1, 1, 1]
    # line2 = [1, 0, 1, 1]
    # line3 = [1, 1, 1, 0]
    # matrix = [line1, line2, line3]
    # print(max_square(matrix))
    matrix = []
    while True:
        numStr = sys.stdin.readline().strip()
        if numStr == '':
            break
        arr = list(map(int, numStr.split()))
        matrix.append(arr)
    print(max_square(matrix))