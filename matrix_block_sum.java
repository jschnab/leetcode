// leetcode biweekly contest 17 problem 1314
// given a matrix A(m * n) and an integer K (m, n and k are between 1 and 100)
// return a matrix B where B[i][j] is the sum of elements A[r][c] for
// i - K <= r <= i + K and j - K <= c <= j + K
// all elements of A are between 1 and 100

class MatrixBlockSum {
    public int[][] matblocksum(int[][] mat, int K) {
	int m = mat.length;
	int n = mat[0].length;

	int[][] answer = new int[m][n];

	for (int i = 0; i < m; i++) {
	    for (int j = 0; j < n; j++) {
		int sum = 0;
		for (int r = Math.max(i - K, 0); r < Math.max(i + K + 1, m); r++) {
		    for (int c = Math.max(j - K, 0); c < Math.max(j + K + 1, n); c++) {
			sum += mat[r][c];
		    }
		}
		answer[i][j] = sum;
	    }
	}
	return answer;
    }
}
