#!/bin/bash
# script that that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -Lsf "$1"
