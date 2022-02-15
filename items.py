from pyfiglet import Figlet

f = Figlet(width=80)
hostname = '.'.join(node.hostname.split('.')[:-3])
domainname = '.'.join(node.hostname.split('.')[-2:])

# generate Message Of the Day
motd = node.metadata.get('motd', [])

if not isinstance(motd, list):
    motd = motd.split('\n')

motd += f.renderText(hostname).split('\n')
motd += [f'Hostname: {node.hostname}', ]

issue = f.renderText(domainname).replace('\\', '\\\\').split('\n')
issue += f.renderText(str(node.os).capitalize() + str(node.os_version[0])).replace('\\', '\\\\').split('\n')

issue += [
    "Hostname: \\n",
    "TTY: \\l",
    "IP: \\4",
    "",
]

files = {
    "/etc/motd": {
        'content': '\n'.join(motd) + '\n',
        'owner': "root",
        'group': "root",
        'mode': "0644",
    },
    '/etc/issue': {
        'content': '\n'.join(issue) + '\n',
        'owner': "root",
        'group': "root",
        'mode': "0644",
    }
}
