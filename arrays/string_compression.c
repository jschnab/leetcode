#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void itoa(char *, int);


/* basic string compression, replace repetitions of a character with an
 * integer which defines the number of repetitions
 * time complexity: O(n) we iterate once through the input string
 * space complexity: O(n) we generate a new string to store the compressed one
 */
int main(int argc, char *argv[]) {
    char s[] = "aabcccccaaa";
    //char s[] = "abcdefghijk";

    /* we temporarily store the compressed string in a buffer, we will
     * copy it in an array with the proper size after compression */
    char buffer[strlen(s)*2];

    /* here we store the string used when calling itoa */
    char to_str[20];

    char current = s[0];
    int counter = 1;

    int i = 1;
    int j = 0;
    int k;
    while (s[i] != '\0') {
        /* increment the counter for the current character */
        if (s[i] == current)
            counter++;

        /* when changing character, add the previous character
         * and its number on the compressed string */
        else {
            buffer[j++] = current;
            itoa(to_str, counter);
            for (k = 0; to_str[k] != '\0'; k++)
                buffer[j++] = to_str[k];
            current = s[i];
            counter = 1;
        }
        i++;
    }
    /* compress the final character */
    buffer[j++] = current;
    itoa(to_str, counter);
    for (k = 0; to_str[k] != '\0'; k++)
        buffer[j++] = to_str[k];

    buffer[j] = '\0';
    char final[strlen(buffer)];
    strcpy(final, buffer);

    printf("original: %s\n", s);
    printf("compressed: %s\n", final);
    printf("memory use of original string: %zu bytes\n", sizeof(s));
    printf("memory use of compressed string: %zu bytes\n", sizeof(final));

    return 0;
}


/* convert an integer to a string */
void itoa(char *s, int x) {
    int i = 0, j = 0;
    while (x > 0) {
        s[j++] = (x % 10) + '0';
        x /= 10;
    }
    j--;
    while (i < j) {
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
        i++;
        j--;
    }
    s[++i] = '\0';
}
