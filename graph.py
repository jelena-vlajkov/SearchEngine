from vertex import Vertex
import globals

class Graph:

    def __init__(self):
        self.graph = {}

    def addTo(self, name, links, words):
        globals.allFiles[name] = Vertex(name, words)
        # TODO: implement rest