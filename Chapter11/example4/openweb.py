# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *

class WebView(QWebEngineView):
     def __init__(self ):
        super(WebView, self).__init__()
        url = 'http://www.cnblogs.com/wangshuo1/p/6707631.html'  
        self.load( QUrl( url ) )             
        self.show()
        QTimer.singleShot(1000*5 , self.close)  