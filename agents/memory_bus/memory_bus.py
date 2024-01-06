class MemoryBus:
    def __init__(self, memory=[]):
        self._memory = memory

    def read(self):
        return self._memory
    
    def write(self, memory):
        self._memory = memory

    def get_size(self):
        return self._memory