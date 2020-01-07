#!/bin/bash
# 0010101011111010101
curl -sX POST -d @"$2" -H "Content-Type: application/json" "$1"
