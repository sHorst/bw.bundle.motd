from pyfiglet import Figlet

f = Figlet(width=120)
figlet = f.renderText(node.hostname)

files = {}

if node.metadata.get('motd', False):
    files["/etc/motd"] = {
        'content': node.metadata['motd'],
        'owner': "root",
        'group': "root",
        'mode': "0644",
    }
else:
    files["/etc/motd"] = {
        'source': "motd_template",
        'content_type': 'jinja2',
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'context': {'figlet': figlet.split('\n')},
    }
