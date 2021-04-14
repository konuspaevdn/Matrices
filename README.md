
Class Matrix

Module matrix.py

- class for creating and containing matrix objects of the size MxNxKxL, where M, N are posisitive integers and K, L are positive integers or null. Available methods are:
-- getting the sizes of matrix;
-- getting the element of matrix by key;
-- getting the slice of matrix;
-- getting the transposed version of matrix without changing the matrix itself (available only for two-dimensional matrices); 
-- getting the addition of two matrices;
-- getting the multiplication of two matrices (available only for two-dimensional matrices);
-- getting the addition of matrix and number;
-- getting the multiplication of matrix and number

1) Initialisation: 

Class expects a list (a list of lists) as an initialisation object.

For instance, the following list

arr = [[1, 2, 3], [4, 5, 6]] will be implemented as a matrix of sizes 2x3.

Note: a simple list, for example, like [1, 2, 3] will be implemented as a matrix of sizes 1z3 whereas the list [[1], [2], [3]] will be implemented as a matrix of sizes 3x1.

It is required that given initialising list is completely filled without any empty cells.

2) Attributes and methods: 

-- size: returns the sizes of a matrix in tuple. Format: (m, n, k, l)

-- operator[idx_i](or [idx_i][idx_j] and so on): returns the necessary element from matrix

-- slice(slice_one, slice_two=None, slice_three=None, slice_four=None): returns the matrix object, initialised with the slice from matrix. 

For example, if arr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]], then arr.slice(slice(0, 1), slice(0, 2), slice(0, 1)) will return the matrix [[[1], [3]]]

-- transposed: returns transposed version of matrix without changing original matrix

Note: available only for two-dimensional matrices

-- operand +:
	
	-- matrix_one + matrix_two: returns the matrix of the sum of matrices
	
	-- matrix_one + number(int or float): returns the matrix of the elementwise addition with number
	
Note: left operand of operator + must always be a matrix

-- operand *:
	
	-- matrix_one * matrix_two: returns the matrix of the multiplication of matrices
	
	-- matrix_one + number(int or float): returns the matrix of the elementwise multiplication with number
	
Note1: left operand of operator * must always be a matrix
Note2: available only for two-dimensional matrices

