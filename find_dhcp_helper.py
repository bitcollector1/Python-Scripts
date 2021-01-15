#!/usr/bin/env python

import click
import paramiko
import getpass
import time
import os


@click.command()
@click.argument('host')
def main(host):
    """See all DHCP helpers defined on a switch\n
    Example:
    find_dhcp_helper lca1-s2-csw01.nw.linkedin.com
    """

    command = r'sh run | i "interface|desc|dhcp"'
    filename = "running_config"

    print "Please enter your Tacacs password:"
    tacacs = getpass.getpass()

    f = os.popen("host {0} | awk '/has address/ {{print $4}}' " .format(host))
    host_ip = f.read().strip()

    def disable_paging(remote_conn):
        '''Disable paging on a Cisco router'''

        remote_conn.send("terminal length 0\n")
        time.sleep(1)

        # Clear the buffer on the screen
        output = remote_conn.recv(1000)

        return output

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(host, username=getpass.getuser(), password=tacacs, look_for_keys=False, allow_agent=False)
    time.sleep(5)
    print ("SSH connection established to {0}" .format(host_ip))

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()

    print "Interactive SSH session established"

    # Turn off paging
    disable_paging(remote_conn)

    remote_conn.send(command + "\n")

    # wait until the buffer gets some data
    while not remote_conn.recv_ready():
        time.sleep(1)

    # give channel time to complete sending data
    time.sleep(5)

    command_return = remote_conn.recv(200000)

    f = open(filename, "w")
    f.write(command_return)
    f.close()

    from ciscoconfparse import CiscoConfParse
    cisco_cfg = CiscoConfParse(filename)

    dhcp_interfaces = cisco_cfg.find_objects_w_child(parentspec=r"^interface", childspec=r"ip dhcp relay address")

    for interface in dhcp_interfaces:
        print "\n" + interface.text

        for child in interface.children:
            if 'description' in str(child):
                print child.text

            if 'ip dhcp relay address' in str(child):
                print child.text

    os.remove(filename)


if __name__ == '__main__':
    main()


