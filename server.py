# Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random() * 10 + 1
        # Add the connection to the dictionary with the calculated load
        self.connections.update({connection_id: connection_load})
        print("connection {} added with {} load".format(connection_id, self.connections[connection_id]))

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        self.connections.pop(connection_id)
        print("Connection {} closed".format(connection_id))

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        #for x in self.connections.keys():
        #    total += self.connections[x]
        for x in self.connections.values():
            total += x
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections.update({connection_id:server})
        # Add the connection to the server
        server.add_connection(connection_id)

    def close_connection(self, connection_id):
        """Closes the connection on the server corresponding to connection_id."""
        # Find out the right server
        for srvr in self.servers:
            if connection_id in srvr.connections.keys():
                srvr.close_connection(connection_id)
                self.connections.pop(connection_id)
        print("Server removed")
        # Remove the connection from the load balancer

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load=0
        servers_count = len(self.servers)
        print("Current number of servers: {}".format(servers_count))
        for srvr in self.servers:
            for conn in srvr.connections:
                total_load+=srvr.connections[conn]
        return total_load/servers_count

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        pass

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))

#server = Server()
#server.add_connection("192.168.1.1")
#server.close_connection("192.168.1.1")
#print(server.load())

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print("Average load p/s: {}".format(l.avg_load()))
l.servers.append(Server())
print(l.avg_load())
l.close_connection("fdca:83d2::f20d")
print(l.avg_load())
for connection in range(20):
    l.add_connection(connection)
print(l)
print(l.avg_load())