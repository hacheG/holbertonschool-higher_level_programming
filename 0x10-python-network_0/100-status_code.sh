#!/bin/bash
# 00101011110101011
curl -sLI "$1" -o /dev/null -w '%{http_code}'
