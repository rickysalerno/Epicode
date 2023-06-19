#!/usr/bin/env bash

dir_root=$(pwd)

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
	echo "Mi trovo nella dir $(pwd)"

	punto_a
	punto_b
	punto_c
	punto_d
	punto_e
	#punto_f
	punto_g
	punto_h
	punto_i

}

function punto_a() {
	printf "Copio il file compito.doc su $dir_root\n"
	cp $dir_root/studenti/nicola/scuola/compito.doc $dir_root 
}

function punto_b() {
	printf "Muovo il file relazione.doc su $dir_root\n"
	mv $dir_root/studenti/nicola/scuola/relazione.doc $dir_root
}

function punto_c() {
	printf "Rimuovo la cartella tmp\n"
	rm -rf $dir_root/tmp  
}

function punto_d() {
	printf "creo il file pippo\n"
	printf "ciao sono il file pippo\n" >  $dir_root/studenti/nicola/lavoro/pippo.txt 
}

function punto_e() {
	printf "Cambio i permessi del file pippo\n"
	chmod 664 $dir_root/studenti/nicola/lavoro/pippo.txt
}

#function punto_f() {}

function punto_g() {
	printf "Visualizzo il contenuto del file pippo\n"
	cd $dir_root/studenti/nicola/lavoro
	cat pippo.txt
	echo 
	echo
}

function punto_h(){
	printf "Rimuovo la cartella Amici sotto matteo\n"
	rm -rf $dir_root/studenti/matteo/amici
}

function punto_i(){
	read -p "Con la funzione punto_i , rimuovo tutte le cartelle, procedere? (y/n)" risposta
	echo "stampo il valore di risposta $risposta"
	if (($risposta == "y")); then
		printf "Rimuovo tutte le cartelle\n"
		#rm -rf $dir_root/*
	else
		echo "non rimuovo nessuna cartella"
	fi
}


creazione_dir
