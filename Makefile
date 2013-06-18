# Makefile
#
# ==================================================================================
# PAQUETE: prometeo abc
# DESCRIPCIÓN:Aplicaci�n para aprender el abecedario en legua de se�as venezolana.
# COPYRIGHT:
#  (C) 2011 Francisco Vasquez Guerrero <franjvasquezg@gmail.com>
# LICENCIA: GPL3
# ==================================================================================
#
# Este programa es software libre. Puede redistribuirlo y/o modificarlo bajo los
# términos de la Licencia Pública General de GNU (versión 3).

SHELL := sh -e

SCRIPTS = "debian/postinst configure" "debian/postrm remove"

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
	mkdir -p $(DESTDIR)/usr/share/prometeo-abc/
	mkdir -p $(DESTDIR)/usr/share/applications/
	mkdir -p $(DESTDIR)/usr/share/icons/Gnamon/apps/scalable/

	cp -r desktop/prometeo-abc.desktop $(DESTDIR)/usr/share/applications/
	cp -r icono/prometeo-abc.svg $(DESTDIR)/usr/share/icons/Gnamon/apps/scalable/
	cp -r prometeo/* $(DESTDIR)/usr/share/prometeo-abc/
	cp -r /usr/share/prometeo-abc/prometeo-abc.sh $(DESTDIR)/usr/bin/prometeo-abc
	
	
	
	
uninstall:

	rm -rf /usr/share/prometeo-abc/
	rm -f /usr/share/applications/prometeo-abc.desktop
	rm -f /usr/bin/prometeo-abc
	

	
# se creó en el install

clean:

# Borrar todo lo hecho en build para que quede todo como estaba antes de la
# compilación

reinstall: uninstall install
