#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:09:17 2020

@author: orchard
"""

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
app = QtGui.QApplication([])

p = pg.plot()
p.setWindowTitle('pyqtgraph example: PlotSpeedTest')
p.setLabel('bottom', 'Index', units='B')
curve = p.plot()

#curve.setFillBrush((0, 0, 100, 100))
#curve.setFillLevel(0)

#lr = pg.LinearRegionItem([100, 4900])
#p.addItem(lr)

n = 1000
data = np.random.normal(size=(n))
ptr = 4
lastTime = time()
fps = None
x2 = 8
p.setRange(QtCore.QRectF(0, -10, x2, 20))

def update():
    global curve, data, ptr, p, lastTime, fps, x2
    print(ptr)
    if ptr > x2 :
        x2 = np.exp(np.log(2)*np.ceil(np.log(ptr)/np.log(2)))
        p.setRange(QtCore.QRectF(0, -10, x2, 20))
    curve.setData(data[0:ptr])
    ptr += 1
    ptr &= 1023
    p.setTitle('%0.2f fps' % fps)
    app.processEvents()  ## force complete redraw for every plot
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)
    
## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
