#!/bin/bash
# 0001010100001010101000010101
curl -sI "$1"|grep Allow|cut -d " " -f2-
