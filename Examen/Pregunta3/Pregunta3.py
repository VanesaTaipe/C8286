import time
class Process:
 def __init__(self, process_id, neighbors):
    self.process_id = process_id
    self.neighbors = neighbors
    self.parent = None
    self.children = set()
    self.active = True
 def send_message(self, recipient):
    recipient.receive_message(self, self.process_id)
 def receive_message(self, sender, sender_id):
    if self.parent is None:
        self.parent = sender
        self.children.add(sender_id)
        self.process_task()
 def process_task(self):
# Simulate task processing
    self.active = False
    self.check_termination()
 def check_termination(self):
  if not self.active and not self.children:
   if self.parent:
     self.parent.receive_termination(self.process_id)
 def receive_termination(self, child_id):
    self.children.remove(child_id)
    self.check_termination()

class RicartAgrawalaMutex:
 def __init__(self, node_id, num_nodes):
    self.node_id = node_id
    self.num_nodes = num_nodes
    self.clock = 0
    self.request_queue = []
    self.replies_received = 0
 def request_access(self):
    self.clock += 1
    self.request_queue.append((self.clock, self.node_id))
    for node in nodes:
       if node.node_id != self.node_id:
         node.receive_request(self.clock, self.node_id)
 def receive_request(self, timestamp, sender_id):
    self.clock = max(self.clock, timestamp) + 1
    self.request_queue.append((timestamp, sender_id))
    self.request_queue.sort()
    self.send_reply(sender_id)
 def send_reply(self, target_id):
  for node in nodes:
   if node.node_id == target_id:
    node.receive_reply(self.node_id)
 def receive_reply(self, sender_id):
  self.replies_received += 1
  if self.replies_received == self.num_nodes - 1:
    self.enter_critical_section()
 def enter_critical_section(self):
   print(f"Nodo {self.node_id} ingresando a la seccion critica")
# Critical section code here
   self.leave_critical_section()
 def leave_critical_section(self):
    self.replies_received = 0
    self.request_queue = [(t, n) for t, n in self.request_queue if n != self.node_id]
    for timestamp, node_id in self.request_queue:
       self.send_reply(node_id)
    print(f"Nodo {self.node_id} dejando la seccion critica")
class BerkeleyNode:
    def __init__(self, node_id, time):
        self.node_id = node_id
        self.time = time

    def adjust_time(self, offset):
        self.time += offset

def berkeley_sync(nodes):
    avg_time = sum(node.time for node in nodes) / len(nodes)
    for node in nodes:
        node.adjust_time(avg_time - node.time)
    return [(node.node_id, node.time) for node in nodes]
class CheneyCollector:
 def __init__(self, size):
    self.size = size
    self.from_space = [None] * size
    self.to_space = [None] * size
    self.free_ptr = 0
 def allocate(self, obj):
    if self.free_ptr >= self.size:
       self.collect()
    addr = self.free_ptr
    self.from_space[addr] = obj
    self.free_ptr += 1
    return addr
 def collect(self):
    self.to_space = [None] * self.size
    self.free_ptr = 0
    for obj in self.from_space:
     if obj is not None:
        self.copy(obj)
    self.from_space, self.to_space = self.to_space,self.from_space
 def copy(self, obj):
    addr = self.free_ptr
    self.to_space[addr] = obj
    self.free_ptr += 1
    return addr
class Message:
  def __init__(self, num_nodes, num_rooms):
        self.nodes = [Process(i, []) for i in range(num_nodes)]
        self.initiador=[send_message(processes)]
        self.mutexes = [RicartAgrawalaMutex(i, num_nodes) for i in range(num_nodes)]
     
        self.rooms = [False] * num_rooms  # False significa disponible
        self.collector = CheneyCollector(100)  # 100 es un tamaño arbitrario
if __name__=="__main__":
    processes = [Process(i, []) for i in range(5)]
    for process in processes:
     process.neighbors = [p for p in processes if p != process]
    # Iniciar la detección de terminación
    initiator = processes[0]
    initiator.send_message(processes[1])
    # Ejemplo de uso
    num_nodes = 3
    nodes = [RicartAgrawalaMutex(i, num_nodes) for i in range(num_nodes)]
    # Simulate node 0 requesting access
    nodes[0].request_access()
    time.sleep(2)
    nodes[0].leave_critical_section()
    collector = CheneyCollector(10)
    addr1 = collector.allocate("obj1")
    print(f"Asignado obj1 en: {addr1}")
    collector.collect()
    print("Recoleccion de basura completa")
    nodes = [BerkeleyNode(i, time) for i, time in enumerate([10, 20, 30])]
    master = berkeley_sync(nodes)
    print(master)
