#!/bin/bash

set -e

mkdir -p certs private

openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout private/key.pem \
  -out certs/cert.pem \
  -subj "/CN=localhost"

echo "SSL certificate generated successfully."
