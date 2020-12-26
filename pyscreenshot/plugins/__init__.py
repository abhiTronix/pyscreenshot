from pyscreenshot.plugins.gdk3pixbuf import Gdk3PixbufWrapper
from pyscreenshot.plugins.gnome_dbus import GnomeDBusWrapper
from pyscreenshot.plugins.gnome_screenshot import GnomeScreenshotWrapper
from pyscreenshot.plugins.imagemagick import ImagemagickWrapper
from pyscreenshot.plugins.kwin_dbus import KwinDBusWrapper
from pyscreenshot.plugins.mac_quartz import MacQuartzWrapper
from pyscreenshot.plugins.mac_screencapture import ScreencaptureWrapper
from pyscreenshot.plugins.maim import MaimWrapper
from pyscreenshot.plugins.msswrap import MssWrapper
from pyscreenshot.plugins.pilwrap import PilWrapper
from pyscreenshot.plugins.pyside2_grabwindow import PySide2GrabWindow
from pyscreenshot.plugins.pyside_grabwindow import PySideGrabWindow
from pyscreenshot.plugins.qt4grabwindow import Qt4GrabWindow
from pyscreenshot.plugins.qt5grabwindow import Qt5GrabWindow
from pyscreenshot.plugins.scrot import ScrotWrapper
from pyscreenshot.plugins.grim import GrimWrapper
from pyscreenshot.plugins.wxscreen import WxScreen

# from pyscreenshot.plugins.xwd import XwdWrapper

backend_dict = {
    PilWrapper.name: PilWrapper,
    MssWrapper.name: MssWrapper,
    ScrotWrapper.name: ScrotWrapper,
    GrimWrapper.name: GrimWrapper,
    MaimWrapper.name: MaimWrapper,
    ImagemagickWrapper.name: ImagemagickWrapper,
    Qt5GrabWindow.name: Qt5GrabWindow,
    Qt4GrabWindow.name: Qt4GrabWindow,
    PySide2GrabWindow.name: PySide2GrabWindow,
    PySideGrabWindow.name: PySideGrabWindow,
    WxScreen.name: WxScreen,
    Gdk3PixbufWrapper.name: Gdk3PixbufWrapper,
    ScreencaptureWrapper.name: ScreencaptureWrapper,
    MacQuartzWrapper.name: MacQuartzWrapper,
    GnomeDBusWrapper.name: GnomeDBusWrapper,
    GnomeScreenshotWrapper.name: GnomeScreenshotWrapper,
    KwinDBusWrapper.name: KwinDBusWrapper,
    # XwdWrapper.name: XwdWrapper,
}
