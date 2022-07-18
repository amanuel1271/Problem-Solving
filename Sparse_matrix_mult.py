def sparse_matrix_multiplication(matrix_a, matrix_b):
    # Write your code here.
    if matrix_a == [] or matrix_b == []:
        return [[]]

    m = len(matrix_a[0])
    for row in matrix_a[1:]:
        if len(row) != m:
            return [[]]
            
    n = len(matrix_b[0])
    for row in matrix_b[1:]:
        if len(row) != n:
            return [[]]
    if len(matrix_b) != m:
        return [[]]

    non_zero_row = {i:set() for i in range(len(matrix_a))}
    non_zero_col = {i:set() for i in range(n)}

    for row in non_zero_row:
        for i in range(m):
            if matrix_a[row][i] != 0:
                non_zero_row[row].add(i)
                
    for col in non_zero_col:
        for i in range(len(matrix_b)):
            if matrix_b[i][col] != 0:
                non_zero_col[col].add(i)
                
    res_matrix = []
    for row in non_zero_row:
        ans = []
        for col in non_zero_col:
            cnt = 0
            for j in non_zero_row[row].intersection(non_zero_col[col]):
                cnt += matrix_a[row][j] * matrix_b[j][col]
            ans.append(cnt)
        res_matrix.append(ans)
        
    return res_matrix
            
        
