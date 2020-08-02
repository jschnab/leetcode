#include <stdio.h>
#include <string.h>
#include <ctype.h>


/* given a string, replace the space between words with %20 assume that there
 * is enough space on the right to accomodate characters */


void replace_space(char *s);


int main(int argc, char *argv[]) {
    char s[] = "Mr John Smith    ";
    replace_space(s);
    printf("%s\n", s);
    return 0;
}


void replace_space(char *s) {
    int i, j, len = strlen(s);
    j = len - 1;

    /* skip end white space */
    for (i = len-1; isspace(s[i]); i--)
        ;

    /* iterate over remaining string */
    for (;i >= 0; i--) {
        if (!isspace(s[i])) {
            s[j--] = s[i];
        }
        else {
            s[j--] = '0';
            s[j--] = '2';
            s[j--] = '%';
        }
    }
}
