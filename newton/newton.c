#include <stdio.h>
#include <math.h>

double create_function(double x, double a, double b, double c) {
    return a * x * x + b * x + c;
}

double derivative_function(double x, double a, double b) {
    return 2 * a * x + b;
}

double newton_method(double k, double a, double b, double c) {
    double epsilon = 1e-9;
    double func_value = create_function(k, a, b, c);
    double derivative_value = derivative_function(k, a, b);

    if (fabs(func_value) < epsilon) {
        return k; 
    }

    double new_k = k - func_value / derivative_value;
    printf("x=%lf,func(x)=%lf\n",new_k,func_value);
    return newton_method(new_k, a, b, c);
}

int main() {
    double x, y, root;

    // for (x = -100; x <= 100; x += 0.01) {
    //     y = create_function(x, 1, 0, -3);
    //     printf("x = %.2f, f(x) = %.2f\n", x, y);
    // }

    root = newton_method(99, 8, 20, -61);
    printf("\nRoot found at x = %.9f\n", root);

    return 0;
}
