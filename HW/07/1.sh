read -r FILENAME
if [ -f "$FILENAME" ]; then
    tail -n 10 "$FILENAME"
else
    echo "$FILENAME does not exist."
    exit 2
fi
