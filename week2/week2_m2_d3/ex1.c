#include <stdio.h>
#include <string.h>


void formatter(){	
	for (int i = 0; i < 2; ++i) {
		printf("\n");
	}
}

void presentazione_gioco() {
	puts("Salve, vi presento il nuovo gioco.\n");
	formatter();
	char a[] = "Ti farò tre domande, ad ognuna di queste vi saranno delle risposte a scelta multipla."; 
	char b[] = "Dovrai selezionare solo la lettera antecedente alle risposte.";
	char c[] = "Ad ogni risposta, verrà assegnato un punteggio.";
	printf("%s\n%s\n%s\n", a , b, c);
	formatter();
}

void domande_gioco() {
	formatter();
	char risposta[3];
	int punteggio = 0;
	printf("Quanto fa 2+2? \n");
	formatter();
	printf("\ta)4 \n");
	printf("\tb)7 \n");
	printf("\tc)9 \n");
	scanf("%s" , &risposta[0]);
	switch (risposta[0]) {
		case 'a':
			punteggio += 3;
			break;
		case 'A':
			punteggio += 3;
			break;
		default:
			punteggio += 0 ;
			break;
	}
	printf("Il punteggio è di %d\n", punteggio);

	printf("Qual'è il mio nome? \n");
	formatter();
	printf("\ta)Roberto   \n");
	printf("\tb)Riccardo  \n");
	printf("\tc)Ronald    \n");
	scanf("%s" , &risposta[1]);
	switch (risposta[1]) {
		case 'b':
			punteggio += 3;
			break;
		case 'B':
			punteggio += 3;
			break;
		default:
			punteggio += 0 ;
			break;
	}
	printf("Il punteggio è di %d\n", punteggio);
	
	printf("Qual'è il mio cognome? \n");
	formatter();
	printf("\ta)Ughi    \n");
	printf("\tb)Sozzi   \n");
	printf("\tc)Salerno \n");
	scanf("%s" , &risposta[2]);
	switch (risposta[2]) {
		case 'c':
			punteggio += 3;
			break;
		case 'C':
			punteggio += 3;
			break;
		default:
			punteggio += 0 ;
			break;
	}
	printf("Il tuo punteggio è: %d\n", punteggio);
}

void opzioni_gioco() {
	char scelta;
	printf("A) Iniziare una nuova partita;\n\nB) Uscire dal gioco\n\n");
	scanf("%c", &scelta);
	switch (scelta) {
		case 'A':
			printf("Ok, iniziamo la partita.  \n");
			formatter();
			domande_gioco();
			break;
		case 'a':
			printf("Ok, iniziamo la partita.  \n");
			formatter();
			domande_gioco();
			break;
		default:
			printf("Esco dal gioco. \n");
			break;
			
	}
}



int main() {
	
	presentazione_gioco();
	opzioni_gioco();
	return 0;	
}
