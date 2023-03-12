class frame:
    def __init__(self, buffer):
        self.buffer = buffer
    
    def get_buffer_contents(self):
        return self.buffer.buffer
    
    def set_buffer(self, buffer):
        self.buffer = buffer if buffer else self.buffer