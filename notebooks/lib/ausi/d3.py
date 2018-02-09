import pandas as pd
import os
import json

def create_flare_json(data, json_file):
    
    json_data = {}
    json_data['name'] = 'flare'
    json_data['children'] = []
    
    for row in data.iterrows():
        series = row[1]
        path, filename = os.path.split(series['path'])

        last_children = None
        children = json_data['children']

        for path_part in path.split("/"):
            entry = None

            for child in children:
                if "name" in child and child["name"] == path_part:
                    entry = child
            if not entry:
                entry = {}
                children.append(entry)

            entry['name'] = path_part
            if not 'children' in entry: 
                entry['children'] = []

            children = entry['children']
            last_children = children

        last_children.append({
            'name' : filename + " [" + series['responsible'] + ", " + "{:6.2f}".format(series['ownership']) + "]",
            'weight' : series['ownership'],
            'size' :  series['length'],
            'author_color' : series['color']})

    with open (json_file, mode='w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(json_data, indent=3))