#include <stdio.h>
#include <string.h>


/* reverse a string provided as a command line argument
 * time complexity: O(n) two pointers start from string ends and meet
 * space complexity: O(1) the string is reversed in place
 */
int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("usage: ./reverse <word>\n");
        return 1;
    }
    int i = 0, j = strlen(argv[1]) - 1;
    while (i < j) {
        char tmp = argv[1][i];
        argv[1][i] = argv[1][j];
        argv[1][j] = tmp;
        i++;
        j--;
    }
    printf("%s\n", argv[1]);
    return 0;
}
