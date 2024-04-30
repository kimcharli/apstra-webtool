#!/bin/bash
set +e
set +x

CERTFOLDER=certs
CERTFILE=${CERTFOLDER}/cert.pem
KEYFILE=${CERTFOLDER}/key.pem
SUBJECT="/C=US/ST=MA/L=Westford/O=Juniper/CN=www.example.com"
V3FILE=${CERTFOLDER}/v3.ext
CSRFILE=${CERTFOLDER}/csr.pem
CONFIGFILE=${CERTFOLDER}/openssl.cnf

cat > ${V3FILE} <<EOF
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid:always,issuer:always
basicConstraints       = CA:TRUE
keyUsage               = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment, keyAgreement, keyCertSign
subjectAltName         = DNS:example.com, DNS:*.example.com, localhost, 127.0.0.1, 10.85.192.2
issuerAltName          = issuer:copy
EOF

cat > ${CONFIGFILE} <<EOF
[ req ]
distinguished_name = dn
x509_extensions = default_extensions
prompt = no
?req_extensions = v3_req

[ default_extensions ]
# 1.2.3.4 = ASN1:UTF8String:Something
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = server1.pslab.link
DNS.2 = server2.pslab.link
IP.1 = 10.85.192.2
IP.2 = 127.0.0.1

[ dn ]
C = US
ST = MA
L = Westford
O = Juniper
OU = PS
CN = myserver.pslab

# [v3_req]
# subjectKeyIdentifier   = hash
# authorityKeyIdentifier = keyid:always,issuer:always
# basicConstraints       = CA:TRUE
# keyUsage               = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment, keyAgreement, keyCertSign
# subjectAltName         = DNS:example.com, DNS:*.example.com, localhost, 127.0.0.1, 10.85.192.2
# issuerAltName          = issuer:copy
EOF


mkdir -p ${CERTFOLDER}
# openssl req -x509 -newkey rsa:4096 -nodes -out ${CERTFILE} -keyout ${KEYFILE} -days 365 -subj "${SUBJECT}"
# openssl x509 -noout -in ${CERTFILE} -subject 


# # openssl genrsa -des3 -out ${KEYFILE} 2048
# openssl genrsa -out ${KEYFILE} 2048
# echo 1
# openssl req -new -key ${KEYFILE} -out ${CSRFILE} -subj "${SUBJECT}"
# echo 2
# # openssl rsa -in ${KEYFILE}.org -out ${KEYFILE}
# openssl x509 -req -in ${CSRFILE} -signkey ${KEYFILE} -out ${CERTFILE} -days 3650 -sha256 -extfile ${V3FILE}
# echo 3
# openssl x509 -noout -in ${CERTFILE} -subject 
# echo 4


# openssl req -x509 -newkey rsa:4096 -keyout ${KEYFILE} -out ${CERTFILE} -days 365 -subj "${SUBJECT}" -config ${CONFIGFILE}
openssl req -x509 -newkey rsa:4096 -keyout ${KEYFILE} -out ${CERTFILE} -nodes -days 365 -config ${CONFIGFILE}
openssl x509 -noout -in ${CERTFILE} -subject 
openssl x509 -in ${CERTFILE} -noout -text -certopt ca_default,no_sigdump,no_validity,no_serial