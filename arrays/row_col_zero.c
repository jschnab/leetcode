#include <stdio.h>


#define N 4


void print_matrix(int mat[][N]);


/* from cracking the code interview
 * given an NxN matrix, return a matrix where
 * the whole row and/or column is set to zero
 * if a cell contains zero */
int main(int argc, char *argv[]) {
    int mat[N][N] = {
        1, 2, 3, 0,
        5, 6, 7, 8,
        9, 0, 11, 12,
        13, 14, 15, 16
    };

    int rows[N] = {0};
    int cols[N] = {0};
    int result[N][N];

    /* determine which rows and columns should be set to zero */
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (mat[i][j] == 0) {
                rows[i] = 1;
                cols[j] = 1;
            }

    /* populate the resulting matrix */
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            if (rows[i] || cols[j])
                result[i][j] = 0;
            else
                result[i][j] = mat[i][j];
        }

    print_matrix(result);

    return 0;
}


void print_matrix(int mat[][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("|%2d", mat[i][j]);
        printf("|\n");
    } 
}
