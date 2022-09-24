#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -sd "email=hr@test@gmail.com&subject=I will always be here for PLD" "$1"
