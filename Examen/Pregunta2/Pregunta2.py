import time
import threading

import threading
import time
from collections import defaultdict
class Proces:
 def __init__(self, process_id):
    self.process_id = process_id
    self.state = None
    self.channels = defaultdict(list)
    self.neighbors = []
    self.marker_received = {}
    self.local_snapshot = None
    self.lock = threading.Lock()
 def set_neighbors(self, neighbors):
    self.neighbors = neighbors
    for neighbor in neighbors:
     self.marker_received[neighbor.process_id] = False
 def initiate_snapshot(self):
  with self.lock:
   self.local_snapshot = self.state
   print(f"Process {self.process_id} taking local snapshot:{self.local_snapshot}")
   self.send_marker_messages()
 def send_marker_messages(self):
   for neighbor in self.neighbors:
     self.send_message(neighbor, 'MARKER')
 def send_message(self, neighbor, message_type, content=None):
   message = (message_type, self.process_id, content)
   neighbor.receive_message(message)
 def receive_message(self, message):
  message_type, sender_id, content = message
  with self.lock:
   if message_type == 'MARKER':
      if not self.marker_received[sender_id]:
        self.marker_received[sender_id] = True
        if self.local_snapshot is None:
            self.local_snapshot = self.state
            print(f"Process {self.process_id} taking local snapshot: {self.local_snapshot}")
            self.send_marker_messages()
        else:
            self.channels[sender_id].append(content)
      else:
        self.channels[sender_id].append(content)
   else:
      if self.local_snapshot is not None:
        self.channels[sender_id].append(content)
      else:
        self.process_message(message)
 def process_message(self, message):
# Simulate processing of a normal message
        print(f"Process {self.process_id} received message from Process {message[1]}: {message[2]}")
 def update_state(self, new_state):
        self.state = new_state
class RaymondMutex:
    def __init__(self, node_id, parent=None):
        self.node_id = node_id
        self.parent = parent
        self.token_holder = (parent is None)
        self.request_queue = []

    def request_access(self):
        if self.token_holder:
            self.enter_critical_section()
        else:
            self.request_queue.append(self.node_id)
            self.send_request_to_parent()

    def send_request_to_parent(self):
        if self.parent:
            self.parent.receive_request(self)

    def receive_request(self, requester):
        if not self.token_holder:
            self.request_queue.append(requester.node_id)
            self.send_request_to_parent()
        elif requester.node_id == self.node_id:
            self.enter_critical_section()
        else:
            self.send_token(requester)

    def send_token(self, requester):
        self.token_holder = False
        requester.receive_token(self)

    def receive_token(self, sender):
        self.token_holder = True
        if self.request_queue and self.request_queue[0] == self.node_id:
            self.enter_critical_section()
        else:
            self.send_token_to_next_in_queue()

    def send_token_to_next_in_queue(self):
        if self.request_queue:
            next_node_id = self.request_queue.pop(0)
            next_node = [node for node in nodes if node.node_id == next_node_id][0]
            self.send_token(next_node)

    def enter_critical_section(self):
        print(f"Nodo {self.node_id} ingresando a la sección crítica")
        # Código de sección crítica aquí
        self.leave_critical_section()

    def leave_critical_section(self):
        print(f"Nodo {self.node_id} dejando la sección crítica")
        if self.request_queue:
            self.send_token_to_next_in_queue()
class VectorClock:
    def __init__(self, num_nodes, node_id):
        self.clock = [0] * num_nodes
        self.node_id = node_id
    def tick(self):
        self.clock[self.node_id] += 1
    def send_event(self):
        self.tick()
        return self.clock[:]
    def receive_event(self, received_vector):
        for i in range(len(self.clock)):
            self.clock[i] = max(self.clock[i], received_vector[i])
            self.clock[self.node_id] += 1
class GenerationalCollector:
 def __init__(self, size):
        self.size = size
        self.young_gen = [None] * size
        self.old_gen = [None] * size
        self.young_ptr = 0
        self.old_ptr = 0
 def allocate(self, obj, old=False):
        if old:
            if self.old_ptr >= self.size:
                self.collect_old()
            addr = self.old_ptr
            self.old_gen[addr] = obj
            self.old_ptr += 1
        else:
            if self.young_ptr >= self.size:
                self.collect_young()
            addr = self.young_ptr
            self.young_gen[addr] = obj
            self.young_ptr += 1
        return addr
 def collect_young(self):
    self.old_gen = self.old_gen + [obj for obj in self.young_gen if obj is not None]
    self.young_gen = [None] * self.size
    self.young_ptr = 0
 def collect_old(self):
    self.old_gen = [obj for obj in self.old_gen if obj is not None]
    self.old_ptr = len(self.old_gen)
    self.old_gen += len(self.old_ptr)


class coordinacion:
    def __init__(self,num_nodes,num_tareas):
        self.nodes=[Proces(i) for i in range(num_nodes)]
        self.mutexes=[RaymondMutex(i) for i in range(num_nodes)]
        self.tareas=[False] * num_tareas
        self.collector = GenerationalCollector(10)
    def synchronize_clocks(self):
        return initiate_snapshot(self.nodes)
    def reserve_tareas(self, node_id, tarea_id):
        mutex = self.mutexes[node_id]
        mutex.request_cs()
        if not self.tareas[tarea_id]:
            self.tareas[tarea_id] = True
            reservation = object()
            self.collector.allocate(reservation)
            print(f"Nodo {node_id} reservó la tarea {tarea_id}")
            result = True
        else:
            print(f"Tarea {tarea_id} no disponible")
            result = False
        mutex.release_cs()
        return result

    def get_precise_time(self):
        times = [(node.time, 1) for node in self.nodes]  # 1 es una incertidumbre arbitraria
        return VectorClock(times)
if __name__ == "__main__":
    system = coordinacion(3, 2)
    
    print("Sincronizando relojes:")
    print(system.synchronize_clocks())

    print("\nReservando TAreas:")
    system.reserve_tarea(0, 0)
    system.reserve_tarea(1, 1)
    system.reserve_tarea(2, 0)  # Debería fallar

    print("\nTiempo preciso del sistema:")
    print(system.get_precise_time())

    print("\nRecolección de basura:")
    system.collect_old()

