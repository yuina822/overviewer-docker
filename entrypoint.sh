#!/bin/bash
if [ -z $OVERVIEWER_CYCLE ]; then
		OVERVIEWER_CYCLE=86400
fi

/usr/src/app/overviewer/overviewer.py --config="/config.py"
