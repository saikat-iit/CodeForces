#include <stdio.h>
#include <string.h>

int main(){
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        char s[101];
        scanf("%100s", &s);

        if(strlen(s) > 10) {
            printf("%c%d%c\n", s[0], strlen(s)-2, s[strlen(s)-1]);
        }
        else{
            printf("%s\n", s);
        }
    }
    return 0;
}