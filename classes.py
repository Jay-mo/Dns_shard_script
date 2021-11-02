# Define classes for DNS script.
import dns.resolver
import libraries
import itertools
from tabulate import tabulate

class Server:
    def __init__(self, server_name) -> None:
        self.server_name = server_name
        self.server_ip = None


class MerakiShard(Server):

    domain = 'meraki.com'


    def __init__(self, server_name) -> None:
        super().__init__(server_name)
    
    @property
    def meraki_shard_name(self):
        return self.server_name + '.' + MerakiShard.domain

    @property
    def meraki_shard_ipv4(self):
        dns_response = dns.resolver.query(self.meraki_shard_name, 'A')
        return [ ip.address for ip in dns_response ]


    # @staticmethod
    # def get_all_meraki_shards():


class MerakiMethods:

    domain = MerakiShard.domain

    server_prefix = 'n'

    
    @classmethod
    def get_all_shards(cls):

        error_count = 0

        for i in itertools.count(start=1):
            server_name = cls.server_prefix + str(i)
            # print (cls.domain)
            # server_url = server_name + cls.domain

            shard = MerakiShard(server_name)

            try:
                server_public_ipv4 = shard.meraki_shard_ipv4[0]

                server_url = shard.meraki_shard_name


                #print (f'Meraki shard {server_url} has a public ipv4 address of {*server_public_ipv4,}')

                table = [[server_url, server_public_ipv4]]
                headers=["Meraki Shard", "IPv4 Address"]

                #print(table)

                if i == 1:

                    print (tabulate(table, headers, tablefmt="grid"))
                
                else: 
                    print (tabulate(table, tablefmt="grid"))

                error_count = 0

            except:
                print (f'{shard.meraki_shard_name} has no valid IPs')
                error_count += 1


            if error_count > 5:
                print( "There are no more shards")
                break




    @classmethod
    def get_shard(cls, name):
        
        server_name = cls.server_prefix + str(name)
        shard = MerakiShard(server_name)

        try:
            server_public_ipv4 = shard.meraki_shard_ipv4[0]

            server_url = shard.meraki_shard_name


            #print (f'Meraki shard {server_url} has a public ipv4 address of {*server_public_ipv4,}')

            table = [[server_url, server_public_ipv4]]
            headers=["Meraki Shard", "IPv4 Address"]

            #print(table)

            print (tabulate(table, headers, tablefmt="grid"))

            

        except:
            print (f'{shard.meraki_shard_name} has no valid IPs')



        

