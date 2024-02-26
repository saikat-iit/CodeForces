#include "stdio.h"

int _length(char arr[]) {
    int count = 0;
    while(arr[count]) count++;
    return count;
}

int main() {
    char word[110];
    int count = 1;
    scanf("%s",word);
    int i = 0;
    while(word[i]) {
        if((int)word[i] >= 97) count++;
    }

    if(count > _length(word)-count) {printf();}
}