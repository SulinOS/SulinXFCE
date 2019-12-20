#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
#    shelltools.export("LDFLAGS", "%s -lX11" % get.LDFLAGS())
    shelltools.makedirs("m4")
    shelltools.system("/usr/bin/xdt-autogen")
    autotools.configure("--disable-dependency-tracking \
                         --enable-libnotify \
                         --enable-taglib")

    inarytools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README")
