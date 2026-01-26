IoT Device Container  ──►  IoT Server Container
        │
        │ (tcpdump capture)
        ▼
   capture.pcap  ──►  CICFlowMeter  ──►  flows.csv  ──►  ML Model


iot_device
   ↓
tcpdump (running continuously)
   ↓ writes PCAP chunks
/shared/capture.pcap
   ↓
flow_meter container reads PCAP repeatedly
   ↓
generates flow CSV


To confirm real application data is being transmitted:

docker exec -it iot_device tcpdump -nn -r /shared/capture.pcap | grep "Flags \[P"
