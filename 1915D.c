#include <stdio.h>
int main() {
    int n;
    scanf("%d", &n);
    char s[n];
    scanf("%s", s);
    for(int i=1; i<n; i++){
        if(s[i] == "a" || s[i] == "e"){
            s[i-1] = "." + s[i-1];
        }
    }
    printf("%s", s);
} 