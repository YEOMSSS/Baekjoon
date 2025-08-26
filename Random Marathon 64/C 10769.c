/*
#include <stdio.h>
#include <string.h>

int main(void) {

    char arr[256];
    fgets(arr, sizeof(arr), stdin);

    char prev = '\0';
    int happy = 0, sad = 0;

    size_t len = strlen(arr);
    for (size_t i = 0; i < len; i++) {

        if (arr[i] == ':') {
            prev = ':';
        }
        else if  (prev == ':') {
            if (arr[i] == '-') {
                prev = '-';
            }
            else {
                prev = '\0';
            }
        }
        else if (prev == '-') {
            if (arr[i] == ')'){
                happy += 1;
                prev = '\0';
            }
            else if (arr[i] == '(') {
                sad += 1;
                prev = '\0';
            }
            else {
                prev = '\0';
            }
        }
        else {
            continue;
        }
    }

    if (happy == 0 && sad == 0) printf("none");
    else if (happy == sad) printf("unsure");
    else if (happy > sad) printf("happy");
    else if (happy < sad) printf("sad");

    return 0;
}
*/

#include <stdio.h>
#include <string.h>

int main(void) {

    char arr[256];
    fgets(arr, sizeof(arr), stdin);

    int happy = 0, sad = 0;

    size_t len = strlen(arr);
    for (size_t i = 0; i + 2 < len; i++) {
        if (arr[i] == ':' && arr[i + 1] == '-') {
            if (arr[i + 2] == ')') happy++;
            else if (arr[i + 2] == '(') sad++;
        }
    }

    if (happy == 0 && sad == 0) printf("none");
    else if (happy == sad) printf("unsure");
    else if (happy > sad) printf("happy");
    else if (happy < sad) printf("sad");

    return 0;
}


