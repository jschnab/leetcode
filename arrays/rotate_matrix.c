#include <stdio.h>


#define N 4

/* this problem is from the book "cracking the code interview"
 * even if one has not matrix operations knowledge, it's easy
 * to derive a rule by drawing small matrices and generalize
 * time complexity: O(n) we iterate once through the matrix
 * space complexity: O(n) we create a new rotated matrix
 */

/* rotate a 2D NxN matrix by 90 degrees clockwise */
int main(int argc, char *argv[]) {
    int i, j;
    int mat[N][N] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    int result[N][N];

    /* this is a 90 degrees anti-clockwise rotation
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            result[i][j] = mat[j][N-i-1];
        }
    }
    */

    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            result[i][j] = mat[N-j-1][i];

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            printf("|%2d", result[i][j]);
        }
        printf("|\n");
    }

    return 0;
}
