#!/bin/bash
CWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $CWD
./srcds_run -game csgo -usercon -strictportbind -ip {{ hostvars[inventory_hostname]['ansible_eth0']['ipv4']['address'] }} -port 27015 +clientport 27005 +tv_port 27020 -tickrate 128 +map de_dust2 +servercfgfile server.cfg -maxplayers_override 12 +mapgroup random_classic +game_mode 1 +game_type 0

