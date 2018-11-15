#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function
__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ["preview"],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_vpn_tunnel
description:
- VPN tunnel resource.
short_description: Creates a GCP VpnTunnel
version_added: 2.7
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
  name:
    description:
    - Name of the resource. The name must be 1-63 characters long, and comply with
      RFC1035. Specifically, the name must be 1-63 characters long and match the regular
      expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must
      be a lowercase letter, and all following characters must be a dash, lowercase
      letter, or digit, except the last character, which cannot be a dash.
    required: true
  description:
    description:
    - An optional description of this resource.
    required: false
  target_vpn_gateway:
    description:
    - URL of the Target VPN gateway with which this VPN tunnel is associated.
    - 'This field represents a link to a TargetVpnGateway resource in GCP. It can
      be specified in two ways. You can add `register: name-of-resource` to a gcp_compute_target_vpn_gateway
      task and then set this target_vpn_gateway field to "{{ name-of-resource }}"
      Alternatively, you can set this target_vpn_gateway to a dictionary with the
      selfLink key where the value is the selfLink of your TargetVpnGateway'
    required: true
  router:
    description:
    - URL of router resource to be used for dynamic routing.
    - 'This field represents a link to a Router resource in GCP. It can be specified
      in two ways. You can add `register: name-of-resource` to a gcp_compute_router
      task and then set this router field to "{{ name-of-resource }}" Alternatively,
      you can set this router to a dictionary with the selfLink key where the value
      is the selfLink of your Router'
    required: false
  peer_ip:
    description:
    - IP address of the peer VPN gateway. Only IPv4 is supported.
    required: true
  shared_secret:
    description:
    - Shared secret used to set the secure session between the Cloud VPN gateway and
      the peer VPN gateway.
    required: true
  ike_version:
    description:
    - IKE protocol version to use when establishing the VPN tunnel with peer VPN gateway.
    - Acceptable IKE versions are 1 or 2. Default version is 2.
    required: false
    default: '2'
  local_traffic_selector:
    description:
    - Local traffic selector to use when establishing the VPN tunnel with peer VPN
      gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`.
      The ranges should be disjoint.
    - Only IPv4 is supported.
    required: false
  remote_traffic_selector:
    description:
    - Remote traffic selector to use when establishing the VPN tunnel with peer VPN
      gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`.
      The ranges should be disjoint.
    - Only IPv4 is supported.
    required: false
  labels:
    description:
    - Labels to apply to this VpnTunnel.
    required: false
  region:
    description:
    - The region where the tunnel is located.
    required: true
extends_documentation_fragment: gcp
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels)'
- 'Cloud VPN Overview: U(https://cloud.google.com/vpn/docs/concepts/overview)'
- 'Networks and Tunnel Routing: U(https://cloud.google.com/vpn/docs/concepts/choosing-networks-routing)'
'''

EXAMPLES = '''
- name: create a network
  gcp_compute_network:
      name: "network-vpn_tunnel"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: network

- name: create a router
  gcp_compute_router:
      name: "router-vpn_tunnel"
      network: "{{ network }}"
      bgp:
        asn: 64514
        advertise_mode: CUSTOM
        advertised_groups:
        - ALL_SUBNETS
        advertised_ip_ranges:
        - range: 1.2.3.4
        - range: 6.7.0.0/16
      region: us-central1
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: router

- name: create a target vpn gateway
  gcp_compute_target_vpn_gateway:
      name: "gateway-vpn_tunnel"
      region: us-west1
      network: "{{ network }}"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: gateway

- name: create a vpn tunnel
  gcp_compute_vpn_tunnel:
      name: "test_object"
      region: us-west1
      target_vpn_gateway: "{{ gateway }}"
      router: "{{ router }}"
      shared_secret: super secret
      project: "test_project"
      auth_kind: "serviceaccount"
      service_account_file: "/tmp/auth.pem"
      state: present
'''

RETURN = '''
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
name:
  description:
  - Name of the resource. The name must be 1-63 characters long, and comply with RFC1035.
    Specifically, the name must be 1-63 characters long and match the regular expression
    `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase
    letter, and all following characters must be a dash, lowercase letter, or digit,
    except the last character, which cannot be a dash.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource.
  returned: success
  type: str
targetVpnGateway:
  description:
  - URL of the Target VPN gateway with which this VPN tunnel is associated.
  returned: success
  type: dict
router:
  description:
  - URL of router resource to be used for dynamic routing.
  returned: success
  type: dict
peerIp:
  description:
  - IP address of the peer VPN gateway. Only IPv4 is supported.
  returned: success
  type: str
sharedSecret:
  description:
  - Shared secret used to set the secure session between the Cloud VPN gateway and
    the peer VPN gateway.
  returned: success
  type: str
sharedSecretHash:
  description:
  - Hash of the shared secret.
  returned: success
  type: str
ikeVersion:
  description:
  - IKE protocol version to use when establishing the VPN tunnel with peer VPN gateway.
  - Acceptable IKE versions are 1 or 2. Default version is 2.
  returned: success
  type: int
localTrafficSelector:
  description:
  - Local traffic selector to use when establishing the VPN tunnel with peer VPN gateway.
    The value should be a CIDR formatted string, for example `192.168.0.0/16`. The
    ranges should be disjoint.
  - Only IPv4 is supported.
  returned: success
  type: list
remoteTrafficSelector:
  description:
  - Remote traffic selector to use when establishing the VPN tunnel with peer VPN
    gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`.
    The ranges should be disjoint.
  - Only IPv4 is supported.
  returned: success
  type: list
labels:
  description:
  - Labels to apply to this VpnTunnel.
  returned: success
  type: dict
labelFingerprint:
  description:
  - The fingerprint used for optimistic locking of this resource. Used internally
    during updates.
  returned: success
  type: str
region:
  description:
  - The region where the tunnel is located.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            description=dict(type='str'),
            target_vpn_gateway=dict(required=True, type='dict'),
            router=dict(type='dict'),
            peer_ip=dict(required=True, type='str'),
            shared_secret=dict(required=True, type='str'),
            ike_version=dict(default=2, type='int'),
            local_traffic_selector=dict(type='list', elements='str'),
            remote_traffic_selector=dict(type='list', elements='str'),
            labels=dict(type='dict'),
            region=dict(required=True, type='str')
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#vpnTunnel'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind, fetch)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            labels_update(module, module.params, fetch)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind, fetch):
    update_fields(module, resource_to_request(module),
                  response_to_hash(module, fetch))
    return fetch_resource(module, self_link(module), kind)


def update_fields(module, request, response):
    if response.get('labels') != request.get('labels'):
        labels_update(module, request, response)


def labels_update(module, request, response):
    auth = GcpSession(module, 'compute')
    auth.post(
        ''.join([
            "https://www.googleapis.com/compute/v1/",
            "projects/{project}/regions/{region}/vpnTunnels/{name}/setLabels"
        ]).format(**module.params),
        {
            u'labels': module.params.get('labels'),
            u'labelFingerprint': response.get('labelFingerprint')
        }
    )


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#vpnTunnel',
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'targetVpnGateway': replace_resource_dict(module.params.get(u'target_vpn_gateway', {}), 'selfLink'),
        u'router': replace_resource_dict(module.params.get(u'router', {}), 'selfLink'),
        u'peerIp': module.params.get('peer_ip'),
        u'sharedSecret': module.params.get('shared_secret'),
        u'ikeVersion': module.params.get('ike_version'),
        u'localTrafficSelector': module.params.get('local_traffic_selector'),
        u'remoteTrafficSelector': module.params.get('remote_traffic_selector'),
        u'labels': module.params.get('labels')
    }
    return_vals = {}
    for k, v in request.items():
        if v:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/vpnTunnels/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/vpnTunnels".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'name': response.get(u'name'),
        u'description': module.params.get('description'),
        u'targetVpnGateway': replace_resource_dict(module.params.get(u'target_vpn_gateway', {}), 'selfLink'),
        u'router': replace_resource_dict(module.params.get(u'router', {}), 'selfLink'),
        u'peerIp': response.get(u'peerIp'),
        u'sharedSecret': response.get(u'sharedSecret'),
        u'sharedSecretHash': response.get(u'sharedSecretHash'),
        u'ikeVersion': response.get(u'ikeVersion'),
        u'localTrafficSelector': response.get(u'localTrafficSelector'),
        u'remoteTrafficSelector': response.get(u'remoteTrafficSelector'),
        u'labels': response.get(u'labels'),
        u'labelFingerprint': response.get(u'labelFingerprint')
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#vpnTunnel')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], 'message')
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation')
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


if __name__ == '__main__':
    main()
