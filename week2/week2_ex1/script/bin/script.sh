#!/usr/bin/env bash

dir_root=$(pwd)

if [[ ! -d ex1 ]]; then
	mkdir ex1
	cd $dir_root/ex1 
fi


dir_root="$dir_root/ex1"

echo "Stampo dir_root $dir_root"

function creazione_dir() {
	cd $dir_root
	for i in dos studenti windows tmp
	do
		mkdir $i
	done

	if [[ -d tmp ]]; then
		cd tmp
		if [[ ! -f risultati.doc ]]; then
			touch risultati.doc
		fi
		cd ..
	fi


	if [[ -d studenti ]]; then
		cd studenti
	fi

	for j in nicola anna matteo
	do
		mkdir $j 
	done


	if [[ -d nicola ]]; then
		cd nicola 
		for i in scuola lavoro
		do
			mkdir $i
		done

		# Creazione file sotto nicola/scuola 
		if [[ ! -f scuola/relazione.doc ]]; then
			touch scuola/relazione.doc 
		fi
		
		if [[ ! -f scuola/compito.doc ]]; then
			touch scuola/compito.doc 
		fi

		cd ..
	fi


	if [[ -d anna ]]; then
		cd anna
		mkdir casa
		cd ..
	fi


	if [[ -d matteo ]]; then
		cd matteo
		mkdir amici
		cd ..
	fi

	cd $dir_root
	printf "Mi trovo nella dir $(pwd)\n"

	punto_a
	punto_b
	punto_c
	punto_d
	punto_e
	punto_f
	punto_g
	punto_h
	punto_i

}

function punto_a() {
	formatter
	printf "Copio il file compito.doc su $dir_root\n"
	cp $dir_root/studenti/nicola/scuola/compito.doc $dir_root 
	formatter
	visualizza_e_dormi $dir_root
}

function punto_b() {
	formatter
	printf "Muovo il file relazione.doc su $dir_root\n"
	mv $dir_root/studenti/nicola/scuola/relazione.doc $dir_root
	formatter
	visualizza_e_dormi $dir_root
}

function punto_c() {
	formatter
	printf "Rimuovo la cartella tmp\n"
	rm -rf $dir_root/tmp  
	formatter
	visualizza_e_dormi $dir_root
}

function punto_d() {
	formatter
	printf "creo il file pippo\n"
	printf "ciao sono il file pippo\n" >  $dir_root/studenti/nicola/lavoro/pippo.txt 
	formatter
	visualizza_e_dormi $dir_root/studenti/nicola/lavoro/pippo.txt
}

function punto_e() {
	formatter
	printf "Cambio i permessi del file pippo\n"
	chmod 664 $dir_root/studenti/nicola/lavoro/pippo.txt
	formatter
	visualizza_e_dormi $dir_root/studenti/nicola/lavoro/pippo.txt
}

function punto_f() {
	formatter
	printf "nascondo i contenuti della dir anna\n"
	printf "per cambiare i permessi di directory, devo eseguire il comando come root\n" 
	sudo chown nobody:nogroup $dir_root/studenti/anna
	chmod 660 $dir_root/studenti/anna
	visualizza_e_dormi $dir_root/studenti/anna
	formatter
}

function punto_g() {
	formatter
	printf "Visualizzo il contenuto del file pippo\n"
	cd $dir_root/studenti/nicola/lavoro
	cat pippo.txt
	formatter
}

function punto_h(){
	formatter
	printf "Rimuovo la cartella Amici sotto matteo\n"
	rm -rf $dir_root/studenti/matteo/amici
	formatter
	visualizza_e_dormi $dir_root/studenti/matteo
}

function punto_i(){
	formatter
	read -p "Con la funzione punto_i , rimuovo tutte le cartelle, procedere? (y/n)" risposta
	echo "stampo il valore di risposta $risposta"
	if [ $risposta = "y" ]; then
		printf "Rimuovo tutte le cartelle\n"
		sudo rm -rf $dir_root
	else
		echo "non rimuovo nessuna cartella"
	fi
	formatter
}


function visualizza_e_dormi() {
	ls -l $1 $2 $3 $4 $5  
	sleep 4
}

function formatter(){
	for (( i = 0; i < 2; i++ )); do
		echo
	done
}

creazione_dir


function background() {
	lettura_man
	esecuzione_vi
	lista_processi
	kill_vi
	esecuzione_firefox
	kill_firefox
	visualizza_spazio
}

function lettura_man(){
	formatter
	printf "Visualizzo in seq. i man di job ps e kill"
	sleep 4
	for i in job ps pkill
	do
		man $i
	done
	formatter
}

function esecuzione_vi(){
	formatter
	printf "Apro Il file vi pippo\n"
	sleep 4
	exec 4> output.txt
	vi pippo > /dev/null &
	exec 4>&-

	formatter
}

function lista_processi(){
	formatter
	printf "Lista di tutti i processi\n"
	sleep 4
	ps aux  
	formatter
}

function kill_vi(){
	formatter
	printf "Uccido il processo vi\n"
	sleep 4
	pkill -9 vi
	formatter
}

function esecuzione_firefox(){
	formatter
	printf "Apro firefox\n"
	sleep 4
	firefox  &
	formatter
}

function kill_firefox(){
	formatter
	printf "Kill firefox\n"
	sleep 4
	pkill firefox
	formatter
}
function visualizza_spazio {
	formatter
	printf "Visualizzo spazio su disco\n"
	sleep 4
	df -hT 
	formatter
}

background
