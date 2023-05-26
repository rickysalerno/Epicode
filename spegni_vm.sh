#!/usr/bin/env bash 


function spegni_vm() {
	for i in epicode_kali_linux_init \
		 epicode_win7_init 
	 do
		 sudo virsh shutdown $i && pkill -9 virt-viewer
	 done
}

spegni_vm
