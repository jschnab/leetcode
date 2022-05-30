#include <stdio.h>
#include <string.h>


int count_texts(char *s) {
    int memo[5] = {1, 1, 1, 1, 1}, n = strlen(s);
    int max_j;
    for (int i = n - 1; i >= 0; --i) {
        memo[i % 5] = 0;
        if (n < i + (s[i] == '7' || s[i] == '9' ? 4 : 3)) {
            max_j = n;
        }
        else {
            max_j = s[i] == '7' || s[i] == '9' ? 4 : 3;
        }
        for (int j = i; j < max_j && s[i] == s[j]; ++j) {
            memo[i % 5] = (memo[i % 5] + memo[(j + 1) % 5]) % 1000000007;
        }
    }
    return memo[0];
}


int main() {
    printf("%d\n", count_texts("22233"));
    return 0;
}
