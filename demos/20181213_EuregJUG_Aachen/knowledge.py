### Identifikation von Wissensinseln

from ausi import d3

# Gruppieren mit minimalen Zeitdauer und Zeilenanzahl
knowledge = log.groupby(
    ['path', 'author']).agg(
        {'timestamp':'min', 'line':'count'}
    )
# Wissensanteile berechnen
knowledge['all'] = knowledge.groupby('path')['line'].transform('sum')
knowledge['knowing'] = knowledge['line'] / knowledge['all']

# Maximales Wissen pro Datei identifizieren
max_knowledge_per_file = knowledge.groupby(['path'])['knowing'].transform(max)
knowledge_carriers = knowledge[knowledge['knowing'] == max_knowledge_per_file]
knowledge_carriers = knowledge_carriers.reset_index(level=1)

# Export in D3 Visualisierung "Zoomable Circle Packing"
d3.create_json_for_zoomable_circle_packing(
    knowledge_carriers.reset_index(),
    'author',
    'author',
    'path',
    '/',
    'all',
    'knowing',
    'linux_circle_packing'
)

