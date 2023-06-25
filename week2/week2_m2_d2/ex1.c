#include <stdio.h>
#include <math.h>

#define PIGRECO 3.14

int area_quadrato(int base, int altezza){
	int result = (base * altezza); 
	return result;
};

float area_cerchio(float raggio){
	float result = (PIGRECO * pow(raggio,2)); 
	return result;
};

int area_triangolo(float lato, float altezza){
	float result = ((lato * altezza) / 2.0); 
	return result;
};

int main() {
	int a = area_quadrato(5,2);
	float b = area_cerchio(11.0);
	float c = area_triangolo(10.0,5.0);
	printf("L'area del quadrato è %d\n", a);
	printf("L'area del cerchio è %.2f\n", b);
	printf("L'area del triangolo è %.2f\n", c);

	return 0 ;

};	
