#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ==============================================================================
# PAQUETE: prometeo-abc
# ARCHIVO: prometeo-abc.py
# COPYRIGHT:
#       (C) 2012 Francisco Javier Vàsquez Guerrero <franjvasquezg@gmail.com>
# LICENCIA: GPL-3
# ==============================================================================
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# COPYING file for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# CODE IS POETRY

import os, gtk, sys

from canaimainstalador.main import Bienvenida, Wizard
from canaimainstalador.clases.common import UserMessage
from canaimainstalador.translator import MAIN_ROOT_ERROR_MSG, MAIN_ROOT_ERROR_TITLE
from canaimainstalador.config import CFG, BANNER_IMAGE

if __name__ == "__main__":
 
        CFG['w'] = Wizard(700, 470, 'Prometeo ABC', BANNER_IMAGE)
        b = Bienvenida(CFG)
        a = b.init(CFG)

        gtk.main()
        sys.exit()

