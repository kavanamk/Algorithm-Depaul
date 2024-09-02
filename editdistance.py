import sys

def editDistance(A, B):
    m = len(A) + 1
    n = len(B) + 1
    Edit = [[0 for _ in range(n)] for _ in range(m)]

    for j in range(n):
        Edit[0][j] = j

    for i in range(1, m):
        Edit[i][0] = i
        for j in range(1, n):
            ins = Edit[i][j - 1] + 1
            dele = Edit[i - 1][j] + 1
            if A[i - 1] == B[j - 1]:
                rep = Edit[i - 1][j - 1]
            else:
                rep = Edit[i - 1][j - 1] + 1
            Edit[i][j] = min(ins, dele, rep)
    

    return Edit

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    print("Kavana Manvi Krishnamurthy")
    if len(sys.argv) != 3:
        print("Usage: python editDistance.py x y")
    else:
        x = sys.argv[1]
        y = sys.argv[2]
        print(x)
        print(y)
        result = editDistance(x, y)
        print_matrix(result)
