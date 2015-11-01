#!/usr/bin/env python
import os

world_path = os.environ.get('OVERVIEWER_WORLD_PATH')
if not world_path :
    world_path = "/data/world"

outputdir = os.environ.get('OVERVIEWER_MAP_PATH')
if not outputdir :
    outputdir = "/mcmap"

renders["day"] = {
    "world": "myworld",
    "title": "Daytime",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}

renders["night"] = {
    "world": "myworld",
    "title": "Nighttime",
    "rendermode": smooth_night,
    "dimension": "overworld",
}

renders["nether"] = {
    "world": "myworld",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}
