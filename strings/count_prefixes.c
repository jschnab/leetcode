#include <stdio.h>
#include <string.h>


/* we use the function strstr(const char *s1, const char *s2)
 * which returns a pointer to the first occurrence of s2 in s1
 * or a null pointer if s2 is not part of s1
 * the matching process does not include \0 but stops there */
int count_prefixes(char **words, int words_size, char *string) {
    int result = 0;
    char *c;
    for (int i = 0; i < words_size; ++i) {
        c = strstr(string, words[i]);
        if (c != NULL && c == string) {
            ++result;
        }
    }
    return result;
}


void test1() {
    char *words[6] = {"a", "b", "c", "ab", "bc", "abc"};
    char *string = "abc";
    if (count_prefixes(words, 6, string) == 3) {
        printf("test 1 successful\n");
    }
    else { printf("test 1 failed\n"); }
}


void test2() {
    char *words[2] = {"a", "a"};
    char *string = "aa";
    if (count_prefixes(words, 2, string) == 2) {
        printf("test 2 successful\n");
    }
    else { printf("test 2 failed\n"); }
}


int main() {
    test1();
    test2();
    return 0;
}
