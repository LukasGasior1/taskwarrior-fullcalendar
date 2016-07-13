import sys
import json
import pystache

def create_events(task):
        events = []
        if 'due' in task:
                events.append({'title': task['description'],
                               'start': task['due'],
                               'color': '#ffcc00'})
        if 'scheduled' in task:
                events.append({'title': task['description'],
                               'start': task['scheduled'],
                               'color': '#257e4a'})
        return map(json.dumps, events)

tasks = json.loads(sys.argv[1])
events = sum(map(create_events, tasks), [])
with open('index.html', 'r') as index:
        index_content = index.read()
        events_str = ','.join(events)
        print pystache.render(index_content, {'events': events_str})
