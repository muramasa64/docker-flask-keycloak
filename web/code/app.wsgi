# -*- coding: UTF-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
reload(sys)
sys.setdefaultencoding('UTF-8')

from main import application
