#include <stdio.h>
#include <string.h>

int main(){
    int n;
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        int a, b, c;
        int flag;

        scanf("%d%d%d", &a,&b,&c);
        if(a+b+c < 2){
            flag++;
        }
        printf("%d", flag);
    }
    return 0;
}