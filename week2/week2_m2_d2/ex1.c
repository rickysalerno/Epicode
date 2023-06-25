#include <stdio.h>
#include <math.h>

#define PIGRECO 3.14

int area_quadrato(int base, int altezza){
	int result = (base * altezza); 
	return result;
};

int area_quadrato2(){
	printf("Area quadrato. \n");
	int base; 
	int altezza ;
	printf("Inserisci il valore della base: ");
	scanf("%d" , &base);
	printf("Inserisci il valore dell'altezza: ");
	scanf("%d" , &altezza);
	int result = (base * altezza); 
	printf("L'area del quadrato è %d\n", result);
	return result;
};

float area_cerchio(float raggio){
	float result = (PIGRECO * pow(raggio,2)); 
	return result;
};

float area_cerchio2(){
	printf("Area cerchio. \n");
	float raggio;
	printf("Inserisci il valore del raggio: ");
	scanf("%2f" , &raggio);
	float result = (PIGRECO * pow(raggio,2)); 
	printf("L'area del cerchio è %.2f\n", result);
	return result;
};

int area_triangolo(float lato, float altezza){
	float result = ((lato * altezza) / 2.0); 
	return result;
};

int area_triangolo2(){
	printf("Area triangolo. \n");
	float lato; float altezza;
	printf("Inserisci il valore del lato: ");
	scanf("%2f" , &lato);
	printf("Inserisci il valore dell'altezza: ");
	scanf("%2f" , &altezza);
	float result = ((lato * altezza) / 2.0); 
	printf("L'area del triangolo è %.2f\n", result);
	return result;
};

int main() {
	// funzioni senza scanf
	int a = area_quadrato(5,2);
	float b = area_cerchio(11.0);
	float c = area_triangolo(10.0,5.0);
	// fine funz 
	
	printf("Adesso eseguo le funzioni senza scanf....\n");
	printf("L'area del quadrato è %d\n", a);
	printf("L'area del cerchio è %.2f\n", b);
	printf("L'area del triangolo è %.2f\n", c);

	printf("Eseguo le funzioni con scanf.....\n");
	
	// funzioni scanf
	area_quadrato2();
	area_cerchio2();
	area_triangolo2();
	// fine funz 
	

	return 0 ;

};	
