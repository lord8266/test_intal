#include <stdio.h>
#include <stdlib.h>
#include "intal.h"
int main(){
    char s1[10000];
    char s2[10000];
    int d;
    fprintf(stderr,"hello\n");
    while (1){
        int c;
        scanf("%d",&c);
        if (c==1){
            scanf("%s",s1);
            scanf("%s",s2);
            char *res =intal_add(s1,s2);
            printf("%s\n",res);
            free(res);
        }
        else if (c==2){
            scanf("%s",s1);
            scanf("%s",s2);
            char *res = intal_diff(s1,s2);
            printf("%s\n",intal_diff(s1,s2));
            free(res);
        }
        else if (c==3){
            scanf("%s",s1);
            scanf("%s",s2);
            int res = intal_compare(s1,s2);
            printf("%d\n",intal_compare(s1,s2));
        }
        else if (c==4){
            scanf("%s",s1);
            scanf("%s",s2);
            char *res = intal_multiply(s1,s2);
            printf("%s\n",intal_multiply(s1,s2));
            free(res);
        }
        else if (c==5){
            scanf("%s",s1);
            scanf("%s",s2);
            char *res = intal_mod(s1,s2);
            printf("%s\n",intal_mod(s1,s2));
            free(res);
        }
        else if (c==6){
            scanf("%s",s1);
            scanf("%d",&d);
            char *res = intal_pow(s1,d);
            printf("%s\n",res);
            free(res);
        }
        else if (c==7){
            scanf("%s",s1);
            scanf("%s",s2);
            char *res = intal_gcd(s1,s2);
            printf("%s\n",res);
            free(res);
        }
        else if (c==8){
            scanf("%d",&d);
            char *res = intal_factorial(d);
            printf("%s\n",res);
            free(res);
        }
        else if(c==9) {
            scanf("%d",&d);
            char *res = intal_fibonacci(d);
            printf("%s\n",res);
            free(res);
        }
        fflush(stdout);
    } 
    // printf("%s\n",intal_multiply("0","123"));
}