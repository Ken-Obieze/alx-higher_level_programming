#!/bin/bash
# Gets byte size of URL body.
curl -s "$1" | wc -c
