#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ==============================================================================
# PAQUETE: canaima-instalador
# ARCHIVO: canaimainstalador/main.py
# COPYRIGHT:
#       (C) 2012 William Abrahan Cabrera Reyes <william@linux.es>
#       (C) 2012 Erick Manuel Birbe Salazar <erickcion@gmail.com>
#       (C) 2012 Luis Alejandro Martínez Faneyth <luis@huntingbears.com.ve>
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

# Módulos globales
import gtk, re, Image

# Módulos locales
from canaimainstalador.pasos.bienvenida import PasoBienvenida
from canaimainstalador.clases.common import UserMessage, AboutWindow, aconnect, \
    debug_list
from canaimainstalador.config import BAR_ICON

class Wizard(gtk.Window):
    def __init__(self, ancho, alto, titulo, banner):
        self.pasos = {}
        self.actual = ''

        # Creo la ventana
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        gtk.Window.set_position(self, gtk.WIN_POS_CENTER_ALWAYS)
        self.set_icon_from_file(BAR_ICON)
        self.titulo = titulo
        self.set_title(titulo)
        self.set_size_request(ancho, alto)
        self.set_resizable(0)
        self.set_border_width(0)

        # Creo el contenedor principal
        self.c_principal = gtk.Fixed()
        self.add(self.c_principal)

        # Calculo tamaño del banner
        self.banner_img = Image.open(banner)
        self.banner_w = self.banner_img.size[0]
        self.banner_h = self.banner_img.size[1]

        # Creo el banner
        self.banner = gtk.Image()
        self.banner.set_from_file(banner)
        self.banner.set_size_request(ancho, self.banner_h)
        self.c_principal.put(self.banner, 0, 0)

        # Creo el contenedor de los pasos
        self.c_pasos = gtk.VBox()
        self.c_pasos.set_size_request((ancho - 10), (alto - 50 - self.banner_h))
        self.c_principal.put(self.c_pasos, 5, (self.banner_h + 5))

        # Creo la botonera
        self.botonera = gtk.Fixed()
        self.botonera.set_size_request(ancho, 40)
        self.c_principal.put(self.botonera, 0, (alto - 40))

        # Creo la linea divisoria
        self.linea = gtk.HSeparator()
        self.linea.set_size_request(ancho, 5)
        self.botonera.put(self.linea, 0, 0)


        # Cancelar
        self.cancelar = gtk.Button(stock=gtk.STOCK_QUIT)
        self.cancelar.set_size_request(100, 30)
        self.cancelar.connect('clicked', self.close)
        self.botonera.put(self.cancelar, 10, 10)

        # Acerca
        self.acerca = gtk.Button(stock=gtk.STOCK_ABOUT)
        self.acerca.set_size_request(100, 30)
        self.acerca.connect('clicked', AboutWindow)
        self.botonera.put(self.acerca, 110, 10)

        self.connect("destroy", self.close)
        self.connect("delete-event", self.close)

        self.show_all()

    def close(self, widget=None, event=None):
        '''
            Cierra la ventana
        '''
        return UserMessage(
            'Hasta Luego...', 'Salir',
            gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO, c_1=gtk.RESPONSE_YES,
            f_1=gtk.main_quit, p_1=()
            )

    def next(self, nombre, init, params, paso):
        '''
            muestra el paso especificado en nombre
        '''
        if not nombre in self.pasos:
            if self.actual != nombre:
                if self.actual != '':
                    self.pasos[self.actual].hide_all()
                self.actual = nombre

            init(params)
            self.pasos[nombre] = paso
            self.c_pasos.add(self.pasos[nombre])
            self.pasos[nombre].show_all()


    def formulario(self, nombre):
        '''
            devulve el objeto asociado al paso
        '''
        if nombre in self.pasos:
            return self.pasos[nombre]
        else:
            return False

class Bienvenida():
    '''
        Inicia el paso que muestra el mensaje de bienvenida
    '''
    def __init__(self, CFG):
        #CFG['s'] = aconnect(CFG['w'].siguiente, CFG['s'], self.siguiente, (CFG))
        #CFG['w'].anterior.set_sensitive(False)
        pass

    def init(self, CFG):
        CFG['w'].next('Bienvenida', Bienvenida, (CFG), PasoBienvenida(CFG))

    def siguiente(self, CFG):
		pass 
        #CFG['w'].next('Teclado', Teclado, (CFG), PasoTeclado(CFG))


