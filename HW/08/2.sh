#!bin/bash
songpath=$(find . -type f -name '*.mp3' | shuf -n 1)
mplayer $songpath



if [ -f "$songpath" ]; then
  read -p "Rate the song between 1 to 10 " songrate
  exho $songrate >>songpath.txt



  avg=$ awk '{ total += $1; count++ } END { print total/count }' songpath.txt
  awk '{$2=$2 "$avg"}1' $songpath.txt

else
  touch $songpath.txt
  read -p "Rate the song between 1 to 10 " songrate
  exho $songrate >>songpath.txt
  avg=$ awk '{ total += $1; count++ } END { print total/count }' songpath.txt
  awk '{$2=$2 "$avg"}1' $songpath.txt
fi
