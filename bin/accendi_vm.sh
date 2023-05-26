#!/usr/bin/env bash 


function accendi_vm() {
	for i in epicode_kali_linux_init \
		 epicode_win7_init \
		 epicode_metasploitable_init
	 do
		 sudo virsh start $i
	 done
}

function visualizza_vm() {
	exec virt-viewer spice://localhost:5900 > /dev/null  &
	exec virt-viewer spice://localhost:5901 > /dev/null  &
	exec virt-viewer spice://localhost:5902 > /dev/null  &
}


accendi_vm
visualizza_vm
