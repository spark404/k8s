#!/usr/bin/env python

from ansible.module_utils.basic import *
from ansible.modules.cloud.cloudstack.cs_ip_address import *
from cs import CloudStack, CloudStackException, read_config
import json

def cs_required_together():
  return [['api_key', 'api_secret', 'api_url']]

def main():
  argument_spec = cs_argument_spec()
  argument_spec.update(dict(
    ip_address = dict(required=False),
    state = dict(choices=['present', 'absent'], default='present'),
    vpc = dict(default=None),
    network = dict(default=None),
    zone = dict(default=None),
    domain = dict(default=None),
    account = dict(default=None),
    project = dict(default=None),
    poll_async = dict(type='bool', default=True),
  ))

  module = AnsibleModule(argument_spec=argument_spec, required_together=cs_required_together())
  acs_ip_address = AnsibleCloudStackIPAddress(module)

  ip = acs_ip_address.get_ip_address()
  result = acs_ip_address.get_result(ip)

  module.exit_json(**result)

if __name__ == '__main__':  
  main()
