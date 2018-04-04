#!/bin/bash
ls -1 images | while read filename
do  
    file=$(basename -- "$filename");
    dirr="${file%.*}";

    echo "Building image: ${dirr} ..."
    docker build -t ${dirr} -f images/$filename $dirr/ 
done

# Run postgres container
docker build --name postgres-server --restart always -d postgres-image