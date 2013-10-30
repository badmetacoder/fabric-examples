from fabric.api import sudo
from fabric.api import run
from fabric.api import local 
from fabric.api import env
from fabric.api import get

def _record(cmd, dump_file):

    """The real hard worker. Executes the given command and transfers the output
file to the local directory.
    """

    cmd_str = cmd % dump_file
    out_file = ''

    if env.host:
        out_file = '%s-%s' % (str(env.host), dump_file)
        sudo(cmd_str)
        get('/tmp/%s' % dump_file, out_file)
        sudo('rm -f /tmp/%s' % dump_file)
    else:
        out_file = 'localhost-%s' % dump_file
        local('sudo %s' % cmd_str)
        local('mv /tmp/%s %s' % (dump_file, out_file))
        local('sudo rm -f /tmp/%s' % dump_file)

    return out_file


def host_type_inventory(dump_file='host_type-dump.txt'):
    """dumps host type
    """
    cmd_str = 'uname -a > /tmp/%s'
    return _record(cmd_str, dump_file)


def diskspace_inventory(dump_file='diskspace-dump.txt'):
    """dumps output of df -h
    """
    cmd_str = 'df -h > /tmp/%s'
    return _record(cmd_str, dump_file)

def filesystem_inventory(dump_file = 'filesystem-dump.txt'):
    """dumps / filesystem except /tmp, /dev, /proc
    """
    cmd_str = 'find / -name "*" | sed -e \'/^\/tmp/d\' | sed -e \'/^\/dev/d\' | sed -e \'/^\/proc/d\' > /tmp/%s'
    return _record(cmd_str, dump_file)


def users_inventory(dump_file='user-list-dump.txt'):
    """dumps user list
    """
    cmd_str = 'cat /etc/shadow | cut -f 1 -d \':\' | sort | uniq > /tmp/%s'
    return _record(cmd_str, dump_file)


def crontab_inventory(dump_file='user-list-dump.txt'):
    """dumps user crontabs
    """

    warn_only_state = env['warn_only']
    env['warn_only'] = True

    user_list = users_inventory(dump_file)

    with open(user_list, 'r') as fh:
        f = fh.read()
        f = f.split()
        for line in f:
            dump_file = 'user-%s-crontab-dump.txt' % line
            cmd_str = 'crontab -u %s -l > /tmp/%%s' % line
            try:
                _record(cmd_str, dump_file)
            except Exception as e:
                print e.message

    env['warn_only'] = warn_only_state


def process_inventory(dump_file='process-dump.txt'):
    """dumps output of ps auxw
    """
    cmd_str = 'ps auxw > /tmp/%s'
    return _record(cmd_str, dump_file)


def net_servers_inventory(dump_file='net-servers-dump.txt'):
    """dumps output of netstat -tulpn
    """
    cmd_str = 'sudo netstat -tulpn > /tmp/%s'
    return _record(cmd_str, dump_file)

def server_inventory():

    host_type_inventory()
    diskspace_inventory()
    filesystem_inventory()
    crontab_inventory()
    process_inventory()
    net_servers_inventory()
