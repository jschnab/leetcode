#include <stdio.h>


/* counter length = number of printable characters on ASCII table */
#define COUNTERLENGTH 127 - 32


int has_unique(char *s);


/* determine if input string has only unique characters
 * time complexity: O(n) we iterate once through the string
 * space complexity: O(1) we use an array to store counts, the size
 * of the array is the same regarless of the input length
 */
int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("usage: ./unique_chars <string>\n");
        return 1;
    }
    if (has_unique(*++argv))
        printf("all characters are unique\n");
    else
        printf("not all characters are unique\n");
    return 0;
}


int has_unique(char *s) {
    int counter[COUNTERLENGTH] = {0};
    char c;
    while ((c = *s++) != '\0') {
        if (counter[c-' '] > 0)
            return 0;
        counter[c-' ']++;
    }
    return 1;
}
