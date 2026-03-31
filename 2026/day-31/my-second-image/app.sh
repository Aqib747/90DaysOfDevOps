#!/bin/bash

echo "====================================="
echo "    Hello from my docker image"
echo "======================================"

echo ""
echo "Container info"
echo "hostname : $(hostname)"
echo "Date: $(date)"
echo "Working dir $(pwd)"

echo "curl is installe:"

curl --version
