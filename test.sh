rm -rf /tmp/storageservice/
mkdir /tmp/storageservice/

curl --verbose --request POST --header "Content-Type:multipart/form-data"\
    --form "file=@mountains.jpg"  http://localhost:8002/upload
