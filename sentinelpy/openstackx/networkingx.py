__author__ = "Kiran Vemuri"
__email__ = "kiran_vemuri@adaranetworks.com"
__status__ = "Development"
__maintainer__ = "Kiran Vemuri"

import requests
import json


class Networking:
    """
    Interface to interact with neutron service using REST
    """

    def __init__(self, url, auth_token):
        """

        :param url: <str> URL to reach networking service
        :param auth_token: <str> auth_token to authorize the request
        """
        self.url = url
        self.auth_token = auth_token
        self.request_headers = {"Content-type": "application/json",
                                "X-Auth-Token": self.auth_token}

    # Internal Network

    def list_networks(self):
        """
        List existing networks
        :return: response object received from list_networks request
        """
        response = requests.get(self.url + "/v2.0/networks",
                                headers=self.request_headers)
        return response

    def show_network(self, network_uuid):
        """
        Show network details
        :param network_uuid: <uuid> UUID of the network to fetch network details
        :return: response object from show_network request
        """
        response = requests.get(self.url + "/v2.0/networks/{}".format(network_uuid),
                                headers=self.request_headers)
        return response

    def create_network(self, network_name, admin_state=True, shared=False, external=False):
        """
        Create a network
        :param network_name: <str> Name for the new network being created
        :param admin_state: <bool> boolean flag for admin_state up/down. Default = True
        :param shared: <bool> boolean flag to indicate network shared true/false. Default = False
        :param external: <bool> boolean flag to indicate whether the network is external true/false. Default = False
        :return: response object from create_network request
        """
        request_data = json.dumps({
            "network": {
                "name": network_name,
                "admin_state_up": admin_state,
                "shared": shared,
                "router:external": external
            }
        })
        response = requests.post(self.url + "/v2.0/networks",
                                 headers=self.request_headers,
                                 data=request_data)
        return response

    def update_network(self, network_uuid, network_name):
        """
        Update a network
        :param network_uuid: <uuid> UUID of the network to be updated
        :param network_name: <str> New name to be updated for the network
        :return: response object returned by the update_network request
        """
        request_data = json.dumps({
            "network": {
                "name": network_name
            }
        })
        response = requests.put(self.url + "/v2.0/networks/{}".format(network_uuid),
                                headers=self.request_headers,
                                data=request_data)
        return response

    def delete_network(self, network_uuid):
        """
        Delete a network
        :param network_uuid: <UUID> UUID of the network to be deleted
        :return: Response object generated by the network_delete request. Error Codes: 409, 404, 204, 401
        """
        response = requests.delete(self.url + "/v2.0/networks/{}".format(network_uuid),
                                   headers=self.request_headers)
        return response

    # External Network

    # Subnets

    def list_subnets(self):
        """
        List existing subnets
        :return: response object generated by the list_subnets request.
        """
        response = requests.get(self.url + "/v2.0/subnets",
                                headers=self.request_headers)
        return response

    def create_subnet(self, network_uuid, cidr, ip_version=4):
        """
        Create a subnet attached to a network
        :param network_uuid: <UUID> UUID of the network to which the subnet is to be associated
        :param cidr: <cidr> valid subnet CIDR
        :param ip_version: <int> ip protocol version 4/6. default = 4
        :return: response object returned by create_subnet request
        """
        request_data = json.dumps({
            "subnet": {
                "network_id": network_uuid,
                "ip_version": ip_version,
                "cidr": cidr
            }
        })
        response = requests.post(self.url + "/v2.0/subnets",
                                 headers=self.request_headers,
                                 data=request_data)
        return response

    def show_subnet(self, subnet_uuid):
        """
        Show subnet details
        :param subnet_uuid: <UUID> UUID of the subnet whose details are being requested
        :return: response object returned by the show_subnet request
        """
        response = requests.get(self.url + "/v2.0/subnets/{}".format(subnet_uuid),
                                headers=self.request_headers)
        return response

    def delete_subnet(self, subnet_uuid):
        """
        Delete a subnet
        :param subnet_uuid: <UUID> UUID of the subnet that is to be deleted
        :return: response object returned by the delete_subnet request
        """
        response = requests.delete(self.url + "/v2.0/subnets/{}".format(subnet_uuid),
                                   headers=self.request_headers)
        return response

    # Ports

    def list_ports(self):
        """
        List existing ports
        :return: response object returned by list_ports request
        """
        response = requests.get(self.url + "/v2.0/ports",
                                headers=self.request_headers)
        return response

    def show_port(self, port_uuid):
        """
        Show port details
        :param port_uuid: <uuid> UUID of the port
        :return: response object returned by the show_port request
        """
        response = requests.get(self.url + "/v2.0/ports/{}".format(port_uuid),
                                headers=self.request_headers)
        return response

    def create_port(self):
        pass
        # TODO

    def delete_port(self, port_uuid):
        """
        Delete a port
        :param port_uuid: <uuid> UUID of the port that is to be deleted
        :return: response object returned by the delete_port request
        """
        response = requests.delete(self.url + "/v2.0/ports/{}".format(port_uuid),
                                   headers=self.request_headers)
        return response

    # Routers

    def list_routers(self):
        """
        List existing routers
        :return: response object returned by the list_routers request
        """
        request_headers = {"Content-type": "application/json",
                           "X-Auth-Token": self.auth_token}
        response = requests.get(self.url + "/v2.0/routers",
                                headers=request_headers)
        return response

    def show_router(self, router_uuid):
        """
        Show router details
        :param router_uuid: <UUID> UUID of the router whose details are to be requested
        :return: response object returned by the show_router request
        """
        response = requests.get(self.url + "/v2.0/routers/{}".format(router_uuid),
                                headers=self.request_headers)
        return response

    def create_router(self, router_name, admin_state=True):
        """
        Create a router
        :param router_name: <str> Name for the router that is being created
        :param admin_state: <bool> boolean flag to represent if the admin_state of the router is up/down. Default = True
        :return: response object returned by the create_router request
        """
        request_data = json.dumps({
            "router": {
                "name": router_name,
                "admin_state_up": admin_state
            }
        })
        response = requests.post(self.url + "/v2.0/routers",
                                 headers=self.request_headers,
                                 data=request_data)
        return response

    def delete_router(self, router_uuid):
        """
        Delete router
        :param router_uuid: <uuid> UUID of the router that is to be deleted
        :return: response object returned by the delete_router request
        """
        response = requests.delete(self.url + "/v2.0/routers/{}".format(router_uuid),
                                   headers=self.request_headers)
        return response

    def add_router_interface(self, router_uuid, subnet_uuid):
        """
        Add a router interface from a subnet to the router
        :param router_uuid: <uuid> UUID of the router
        :param subnet_uuid: <uuid> UUID of the subnet to which a router_interface will be added
        :return: response object returned by the add_router_interface request
        """
        request_data = json.dumps({
            "subnet_id": subnet_uuid
        })
        response = requests.put(self.url + "/v2.0/routers/{}/add_router_interface".format(router_uuid),
                                headers=self.request_headers,
                                data=request_data)
        return response

    def remove_router_interface(self, router_uuid, subnet_uuid):
        """
        Remove a router interface from a subnet
        :param router_uuid: <uuid> UUID of the router
        :param subnet_uuid: <uuid> UUID of the subnet to which a router_interface will be added
        :return: response object returned by the add_router_interface request
        """
        request_data = json.dumps({
            "subnet_id": subnet_uuid
        })
        response = requests.put(self.url + "/v2.0/routers/{}/remove_router_interface".format(router_uuid),
                                headers=self.request_headers,
                                data=request_data)
        return response
