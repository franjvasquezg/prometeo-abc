# Makefile
#
# ==============================================================================
# PAQUETE: canaima-fondos-dinamicos
# ARCHIVO: postinst
# DESCRIPCIÓN: Configura el sistema despues la instalación del paquete.
# COPYRIGHT:
#  (C) 2011 Francisco Vasquez Guerrero <franjvasquezg@gmail.com>
# LICENCIA: GPL3
# ==============================================================================
#
# Este programa es software libre. Puede redistribuirlo y/o modificarlo bajo los
# términos de la Licencia Pública General de GNU (versión 3).

SHELL := sh -e

SCRIPTS = "debian/preinst install" "debian/postinst configure" "debian/prerm remove" "debian/postrm remove"

all: build

test:



	@echo -n "\n===== Comprobando posibles errores de sintaxis en los scripts de mantenedor =====\n\n"

	@for SCRIPT in $(SCRIPTS); \
	do \
		echo -n "$${SCRIPT}\n"; \
		bash -n $${SCRIPT}; \
	done

	@echo -n "\n=================================================================================\nHECHO!\n\n"

build:


	@echo "Nada para compilar!"

install:

	mkdir -p $(DESTDIR)/usr/bin/
	mkdir -p $(DESTDIR)/usr/share/canaima-fondos-dinamicos/
	mkdir -p $(DESTDIR)/usr/share/applications/
	mkdir -p $(DESTDIR)/usr/share/icons/canaima-iconos/apps/scalable/
	mkdir -p $(DESTDIR)/usr/share/icons/canaima-iconos/apps/48/
	mkdir -p $(DESTDIR)/usr/share/gnome/help

	cp -r desktop/canaima-fondo-dinamico.desktop $(DESTDIR)/usr/share/applications/
	cp -r icono/canaima-fondos-dinamicos.svg $(DESTDIR)/usr/share/icons/canaima-iconos/apps/scalable/
	cp -r icono/canaima-fondos-dinamicos.png $(DESTDIR)/usr/share/icons/canaima-iconos/apps/48/
	cp -r scripts/* $(DESTDIR)/usr/share/canaima-fondos-dinamicos/
	ln -s /usr/share/canaima-fondos-dinamicos/canaima-fondos-dinamicos $(DESTDIR)/usr/bin/canaima-fondos-dinamicos
	cp -r ayuda/canaima-fondos-dinamicos $(DESTDIR)/usr/share/gnome/help
	
	
	
uninstall:

	rm -rf /usr/share/canaima-fondo-dinamico/
	rm -f /usr/share/applications/canaima-fondo-dinamico.desktop
	rm -f /usr/bin/canaima-fondos-dinamicos
	#rm -f /etc/skel/.gnome2/

	
# se creó en el install

clean:

# Borrar todo lo hecho en build para que quede todo como estaba antes de la
# compilación

reinstall: uninstall install
