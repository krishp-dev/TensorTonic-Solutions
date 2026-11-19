import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    arr=np.array(A)
    rows, cols = arr.shape
    result = np.zeros((cols, rows), dtype=arr.dtype)
    for i in range(rows):
        for j in range(cols):
            result[j][i]=arr[i][j]
    return result        
   
    
