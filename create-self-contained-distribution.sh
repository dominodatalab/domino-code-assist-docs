#!/bin/bash

DCA_VERSION=$1
PYTHON_VERSION=$2
PYTHON_CONTAINER_NAME=$(echo $RANDOM | md5sum | head -c 32)

ARCHIVE_NAME="dca-${DCA_VERSION}-python-${PYTHON_VERSION}.zip"

docker run --rm -i -d --name ${PYTHON_CONTAINER_NAME} python:${PYTHON_VERSION}

# Wait for container to be ready (this is very conservative: should be almost immediate).
#
sleep 5

docker exec -i ${PYTHON_CONTAINER_NAME} /bin/bash <<EOF
apt-get update
apt-get install zip
pip wheel --wheel-dir dca-archive domino-code-assist==${DCA_VERSION}
zip -r ${ARCHIVE_NAME} dca-archive/*
EOF

docker cp ${PYTHON_CONTAINER_NAME}:${ARCHIVE_NAME} .

docker stop ${PYTHON_CONTAINER_NAME}