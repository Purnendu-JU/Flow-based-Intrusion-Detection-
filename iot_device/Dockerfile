FROM python:3.9-slim

WORKDIR /app

# Install dependencies + tcpdump
RUN apt-get update && \
    apt-get install -y tcpdump && \
    pip install requests && \
    apt-get clean

COPY sensor.py .

CMD sh -c "tcpdump -i eth0 -w /shared/capture.pcap & python sensor.py"

## This command starts tcpdump in the background to capture all network traffic on the eth0 interface

## the traffic is going to be captured by tcpdump running on the iot device