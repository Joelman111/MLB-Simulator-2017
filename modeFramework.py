# Framework for game modes in pygame
def boxScoreMousePressed(self, x, y):
    pass

def boxScoreMouseReleased(self, x, y):
    pass

def boxScoreMouseMotion(self, x, y):
    pass

def boxScoreMouseDrag(self, x, y):
    pass

def boxScoreKeyPressed(self, keyCode, modifier):
    pass

def boxScoreKeyReleased(self, keyCode, modifier):
    pass

def boxScoreTimerFired(self, dt):
    pass

def boxScoreRedrawAll(self, screen):
    pass

def boxScoreIsKeyPressed(self, key):
    return self._keys.get(key, False)