cd /app
echo "----- Now deployed web booting your repo ------ " 
echo "سلملي"
gunicorn app:app & python3 -m jepthon
