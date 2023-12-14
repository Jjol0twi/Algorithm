#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    }

    int prev = 0;
    int current = 1;

    for (int i = 2; i <= n; ++i) {
        int temp = (prev + current) % 1234567;
        prev = current;
        current = temp;
    }

        answer = current % 1234567;
        return answer;
}