#!/usr/bin/env bash 


function spegni_vm() {
	for i in epicode_kali_linux_init \
		 epicode_win7_init \
		 epicode_metasploitable_init
	 do
		 sudo virsh shutdown $i && pkill -9 virt-viewer
	 done

	sleep 10
	echo "Necessario eseguire un destroy della vm......."
	sleep 3 
	sudo virsh destroy epicode_metasploitable_init
}

spegni_vm
