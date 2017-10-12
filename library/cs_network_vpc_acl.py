#!/usr/bin/env python

from ansible.module_utils.basic import *
from ansible.modules.cloud.cloudstack.cs_ip_address import *
from cs import CloudStack, CloudStackException, read_config
import json

def cs_required_together():
  return [['api_key', 'api_secret', 'api_url']]

class AnsibleCloudstackNetworkACL(AnsibleCloudStack):
  def __init__(self, module):
    super(AnsibleCloudstackNetworkACL, self).__init__(module)
    self.returns = {}
    self.updateACL()

  def updateACL(self):
    args = {
      'aclid': self.module.params.get('aclid'),
      'networkid': self.module.params.get('networkid')
    }

    if not self.module.check_mode:
      res = self.query_api('replaceNetworkACLList', **args)
     
def main():
  argument_spec = cs_argument_spec()
  argument_spec.update(dict(
    aclid = dict(required=True),
    state = dict(choices=['present', 'absent'], default='present'),
    networkid = dict(default=None),
    poll_async = dict(type='bool', default=True),
  ))

  # replaceNetworkACLList

  module = AnsibleModule(argument_spec=argument_spec, required_together=cs_required_together())
  acs_acl = AnsibleCloudstackNetworkACL(module)

  #ip = acs_ip_address.get_ip_address()
  result = {}
  #acs_ip_address.get_result(ip)

  module.exit_json(**result)

if __name__ == '__main__':  
  main()
