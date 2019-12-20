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
    autotools.configure("--prefix=/usr \
                         --libexecdir=/usr/lib \
                         --disable-static \
                         --disable-gtk-doc \
                         --enable-gladeui \
                         --enable-debug \
                         --with-vendor-info='Sulin'")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())
    inarytools.dodoc('NEWS', 'COPYING', 'README', 'TODO', 'ChangeLog', 'AUTHORS', 'THANKS')
