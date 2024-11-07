import pandas as pd
from matplotlib.colors import rgb2hex
from matplotlib import cm
import json
import os
from IPython.core.display import HTML



# preprocess data for plotting
def create_plot_data(df, color_column_name, size_column_name, seperator):
    plot_data = pd.DataFrame(index=df.index)
    plot_data['value_for_color'] = df[color_column_name]
    plot_data['ratio_for_color'] = plot_data['value_for_color'] / plot_data['value_for_color'].max()
    plot_data['color'] = plot_data['ratio_for_color'].apply(lambda x : rgb2hex(cm.coolwarm(x)))
    plot_data['size'] = df[size_column_name]
    plot_data[['path', 'name']] = df.index.str.rsplit(seperator, n=1).to_list()
    plot_data['path_list'] = plot_data['path'].str.split(seperator)
    return plot_data


# convert to d3 data format
def create_flare_json(df):

    json_data = {'name': 'flare', 'children': []}

    for _, series in df.iterrows():
        hierarchical_data = series['path_list']

        children = json_data['children']
        for part in hierarchical_data:
            entry = next((child for child in children if child.get('name', '') == part), None)
            if not entry:
                entry = {'name': part, 'children': []}
                children.append(entry)
            children = entry['children']

        children.append({
            'name': f"{series['name']} ({series['size']} [{series['value_for_color']}])",
            'size': series['size'],
            'color': series['color']
        })

    return json_data


# Put data into template
def create(hotspots, color_column_name, size_column_name, separator):
    json_data = create_flare_json(create_plot_data(hotspots, color_column_name, size_column_name,separator))
            
    with open("vis/template_circle_pack_hierarchy_chart_d3_inline.html") as html_template:
        html = html_template.read().replace("###JSON###", str(json_data))
        
        os.makedirs("output", exist_ok=True)
        with open(f'output/hotspots.html', mode='w') as html_out:
            html_out.write(html)
            
        return HTML('<a href="output/hotspots.html" target="_blank">Hotspots</a>')