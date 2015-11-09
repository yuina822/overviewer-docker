#!/bin/bash

if [ -z $OVERVIEWER_CYCLE ]; then
	export OVERVIEWER_CYCLE=3600
fi

if [ -z $OVERVIEWER_WORLD_PATH ]; then
	export OVERVIEWER_WORLD_PATH="/data/world"
fi

if [ -z $OVERVIEWER_MAP_PATH ]; then
	export OVERVIEWER_MAP_PATH="/usr/share/nginx/html"
fi

if [ -z $OVERVIEWER_TEXTURE_URL ]; then
	export OVERVIEWER_TEXTURE_URL="https://s3.amazonaws.com/Minecraft.Download/versions/1.8.8/1.8.8.jar"
fi

if [ -z $OVERVIEWER_WORLD_NAME ]; then
	export OVERVIEWER_WORLD_NAME="myworld"
fi

wget $OVERVIEWER_TEXTURE_URL -O /texture
mkdir -p $OVERVIEWER_MAP_PATH

while true; do
	/usr/src/app/overviewer/overviewer.py --config="/config.py" --genpoi
	/usr/src/app/overviewer/overviewer.py --config="/config.py"
	sleep $OVERVIEWER_CYCLE
done
