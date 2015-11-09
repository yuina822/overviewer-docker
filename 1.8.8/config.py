#!/usr/bin/env python
import os

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://minotar.net/helm/%s/32" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']

world_path = os.environ.get('OVERVIEWER_WORLD_PATH')
texturepath = '/texture'

world_name = os.environ.get('OVERVIEWER_WORLD_NAME')

worlds[world_name] = world_path

renders['day-left'] = {
    'world': world_name,
    'title': 'Day(left)',
    'rendermode': smooth_lighting,
    'dimension': 'overworld',
    'northdirection': 'upper-left',
    'markers': [dict(name='Players', filterFunction=playerIcons, checked=True)],
}

renders['day-right'] = {
    'world': world_name,
    'title': 'Day(right)',
    'rendermode': smooth_lighting,
    'dimension': 'overworld',
    'northdirection': 'upper-right',
    'markers': [dict(name='Players', filterFunction=playerIcons, checked=True)],
}

renders['night-left'] = {
    'world': world_name,
    'title': 'Night(left)',
    'rendermode': smooth_night,
    'dimension': 'overworld',
    'northdirection': 'upper-left',
    'markers': [dict(name='Players', filterFunction=playerIcons, checked=True)],
}

renders['night-right'] = {
    'world': world_name,
    'title': 'Night(right)',
    'rendermode': smooth_night,
    'dimension': 'overworld',
    'northdirection': 'upper-right',
    'markers': [dict(name='Players', filterFunction=playerIcons, checked=True)],
}

renders['nether-left'] = {
    'world': world_name,
    'title': 'Nether(left)',
    'rendermode': nether_smooth_lighting,
    'dimension': 'nether',
    'northdirection': 'upper-left',
    'markers': [dict(name='Players', filterFunction=playerIcons, checked=True)],
}

renders['nether-right'] = {
    'world': world_name,
    'title': 'Nether(right)',
    'rendermode': nether_smooth_lighting,
    'dimension': 'nether',
    'northdirection': 'upper-right',
    'markers': [dict(name='Players', filterFunction=playerIcons, checked=True)],
}

renders['end-left'] = {
    'world': world_name,
    'title': 'The End(left)',
    'rendermode': smooth_lighting,
    'dimension': 'end',
    'northdirection': 'upper-left',
    'markers': [dict(name='Players', filterFunction=playerIcons, checked=True)],
}

renders['end-right'] = {
    'world': world_name,
    'title': 'The End(right)',
    'rendermode': smooth_lighting,
    'dimension': 'end',
    'northdirection': 'upper-right',
    'markers': [dict(name='Players', filterFunction=playerIcons, checked=True)],
}
