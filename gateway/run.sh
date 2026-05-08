#!/bin/bash
set -euo pipefail

mkdir -p ${PCAP_DIR} ${FLOW_DIR} ${FLOW_ARCHIVE_DIR} ${RESULT_DIR}

echo '{"normal":0,"dos":0,"recon":0,"blocked_ips":[]}' > /app/data/status.json

echo "[*] Starting packet capture"
tcpdump -i eth0 -s 0 -G 60 -U -w ${PCAP_DIR}/traffic_%Y%m%d%H%M%S.pcap -Z root &
TCPDUMP_PID=$!

sleep 2

echo "[*] Starting Gateway & IDS"
python3 gateway.py &
GATEWAY_PID=$!

echo "[*] Starting Dashboard HTTP server"
python3 /app/cors_server.py &
HTTP_PID=$!

trap "echo '[*] Stopping...'; kill $TCPDUMP_PID $GATEWAY_PID $HTTP_PID" SIGTERM SIGINT

wait