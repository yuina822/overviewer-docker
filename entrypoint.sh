#!/bin/bash
if [ -z $OVERVIEWER_CYCLE ]; then
		OVERVIEWER_CYCLE=86400
fi

watch -n $OVERVIEWER_CYCLE /usr/src/app/overviewer/overviewer.py --config="/config.py"
