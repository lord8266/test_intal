#include <stdio.h>
#include <stdlib.h>
#include "intal.h"
#define c_len 3000
int main(){
    char s1[1000];
    char s2[1000];
    char **f = malloc(sizeof(char*)*c_len);
    for (int i=0;i<c_len;i++){
        f[i] = malloc(1000);
    }
    int d;
    unsigned int u1,u2;
    // fprintf(stderr,"hello\n");
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
            printf("%s\n",res);
            free(res);
        }
        else if (c==3){
            scanf("%s",s1);
            scanf("%s",s2);
            printf("%d\n",intal_compare(s1,s2));
        }
        else if (c==4){
            scanf("%s",s1);
            scanf("%s",s2);
            char *res = intal_multiply(s1,s2);
            printf("%s\n",res);
            free(res);
        }
        else if (c==5){
            scanf("%s",s1);
            scanf("%s",s2);
            char *res = intal_mod(s1,s2);
            printf("%s\n",res);
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
        else if(c==10) {
            scanf("%u",&u1);
            scanf("%u",&u2);
            char *res = intal_bincoeff(u1,u2);
            printf("%s\n",res);
            free(res);
        }
        else if(c==11){
            scanf("%d",&d);
            for (int i=0;i<d;i++){
                scanf("%s",f[i]);
            }
            char *res = coin_row_problem(f,d);
            printf("%s\n",res);
            free(res);
        }
        else if(c==12){
            scanf("%d",&d);
            scanf("%s",s1);
            for (int i=0;i<d;i++){
                scanf("%s",f[i]);
            }
            
            d =intal_search(f,d,s1);
            printf("%d\n",d);
        }
        else if(c==13){
            scanf("%d",&d);
            scanf("%s",s1);
            for (int i=0;i<d;i++){
                scanf("%s",f[i]);
            }
            
            d =intal_binsearch(f,d,s1);
            printf("%d\n",d);
        }
        else if(c==14){
            scanf("%d",&d);
            for (int i=0;i<d;i++){
                scanf("%s",f[i]);
            }
            d =intal_max(f,d);
            printf("%d\n",d);
        }
        else if(c==15){
            scanf("%d",&d);
            for (int i=0;i<d;i++){
                scanf("%s",f[i]);
            }
            d =intal_min(f,d);
            printf("%d\n",d);
        }
        else if(c==16){
            scanf("%d",&d);
            for (int i=0;i<d;i++){
                scanf("%s",f[i]);
            }
            intal_sort(f,d);
            for (int i=0;i<d;i++){
                printf("%s ",f[i]);
            }
            printf("\n");
        }
        else {
            break;
        }
        fflush(stdout);
    } 
    for (int i=0;i<c_len;i++){
        free(f[i]);
    }
    free(f);
    // printf("%s\n",intal_multiply("0","123"));
}