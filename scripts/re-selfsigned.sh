#!/bin/bash

CERTFOLDER=certs
CERTFILE=${CERTFOLDER}/cert.pem
KEYFILE=${CERTFOLDER}/key.pem

mkdir -p ${CERTFOLDER}
openssl req -x509 -newkey rsa:4096 -nodes -out ${CERTFILE} -keyout ${KEYFILE} -days 365 -subj "/C=US/ST=MA/L=Westford/O=Juniper/CN=www.example.com"
openssl x509 -noout -in ${CERTFILE} -subject 
