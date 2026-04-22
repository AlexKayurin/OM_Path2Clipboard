import os
import sys
import time
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QThread
from PySide6.QtGui import QGuiApplication
import _UI_Control


class FileCheckThread(QThread):
    def __init__(self):
        super().__init__()

    def checkcolors(self):
        while True:
            time.sleep(3)
            for savedfile, button  in zip(mc.savedfiles, mc.buttons):
                if os.path.isfile(savedfile):
                    button.setStyleSheet('background-color: rgb(0, 255, 0);')
                else:
                    button.setStyleSheet('background-color: rgb(255, 0, 0);')

    def run(self):
        self.checkcolors()


class MainWindow(QtWidgets.QMainWindow, _UI_Control.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clipboard = QGuiApplication.clipboard()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        # signals
        self.le_targtename.textEdited.connect(self.settargtename)
        self.buttons = [self.b_s_af_em, self.b_s_af_alt, self.b_s_af_mbes,
                        self.b_s_al_em, self.b_s_al_alt, self.b_s_al_mbes, self.b_s_al_prof,
                        self.b_m_af_tif, self.b_m_af_xy, self.b_m_af_ungr,
                        self.b_m_al_tif, self.b_m_al_xy, self.b_m_al_ungr,
                        self.b_t_af_emxyz, self.b_t_af_altxyz, self.b_t_af_emtif, self.b_t_af_alttif,
                        self.b_t_al_emxyz, self.b_t_al_altxyz, self.b_t_al_emtif, self.b_t_al_alttif]

        for button in self.buttons:
            button.clicked.connect(self.getpath)

        self.settargtename()

        self.wrk_thread = FileCheckThread()
        self.wrk_thread.start()


    def closeEvent(self, event):
        self.wrk_thread.terminate()


    def settargtename(self):
        self.parentpath = os.path.join(r'Z:\03-Processing', '02-Export', '08-ID&C',
                                       'P2381_'+ self.le_targtename.text())

        self.l_path.setText(self.parentpath)
        # set files paths
        self.s_af_em = os.path.join(self.parentpath, '04-Snapshots',
                                    self.le_targtename.text() + '_EM_AF.png')
        self.s_af_alt = os.path.join(self.parentpath, '04-Snapshots',
                                     self.le_targtename.text() + '_ALT_AF.png')
        self.s_af_mbes = os.path.join(self.parentpath, '04-Snapshots',
                                      self.le_targtename.text() + '_MBES_AF.png')
        self.s_al_em = os.path.join(self.parentpath, '04-Snapshots',
                                    self.le_targtename.text() + '_EM_AL.png')
        self.s_al_alt = os.path.join(self.parentpath, '04-Snapshots',
                                     self.le_targtename.text() + '_ALT_AL.png')
        self.s_al_mbes = os.path.join(self.parentpath, '04-Snapshots',
                                      self.le_targtename.text() + '_MBES_AL.png')
        self.s_al_prof = os.path.join(self.parentpath, '04-Snapshots',
                                      self.le_targtename.text() + '_MBES_AL_Profile.png')
        self.m_af_tif = os.path.join(self.parentpath, '01-MBES', '01-TIFF', 'AF',
                                     self.le_targtename.text() + '_AF_DTM_LAT_0.10m.tif')
        self.m_af_xy = os.path.join(self.parentpath, '01-MBES', '02-XYZ', 'AF',
                                    self.le_targtename.text() + '_AF_XYZ_LAT_0.10m.xyz')
        self.m_af_ungr = os.path.join(self.parentpath, '01-MBES', '03-UNGRIDDED', 'AF',
                                      self.le_targtename.text() + '_AF_Ungridded_LAT.xyz')
        self.m_al_tif = os.path.join(self.parentpath, '01-MBES', '01-TIFF', 'AL',
                                     self.le_targtename.text() + '_AL_DTM_LAT_0.10m.tif')
        self.m_al_xy = os.path.join(self.parentpath, '01-MBES', '02-XYZ', 'AL',
                                    self.le_targtename.text() + '_AL_XYZ_LAT_0.10m.xyz')
        self.m_al_ungr = os.path.join(self.parentpath, '01-MBES', '03-UNGRIDDED', 'AL',
                                      self.le_targtename.text() + '_AL_Ungridded_LAT.xyz')
        self.t_af_emxyz = os.path.join(self.parentpath, '03-Hydropact440', '02-EM GRIDS', '01-EM_XYZ', 'AF',
                                       self.le_targtename.text() + '_EM_AF.xyz')
        self.t_af_altxyz = os.path.join(self.parentpath, '03-Hydropact440', '03-ALT GRIDS', '01-Alti_XYZ', 'AF',
                                        self.le_targtename.text() + '_ALT_AF.xyz')
        self.t_af_emtif = os.path.join(self.parentpath, '03-Hydropact440', '02-EM GRIDS', '02-EM_Tiff', 'AF',
                                       self.le_targtename.text() + '_EM_AF.tif')
        self.t_af_alttif = os.path.join(self.parentpath, '03-Hydropact440', '03-ALT GRIDS', '02-Alti_Tiff', 'AF',
                                        self.le_targtename.text() + '_ALT_AF.tif')
        self.t_al_emxyz = os.path.join(self.parentpath, '03-Hydropact440', '02-EM GRIDS', '01-EM_XYZ', 'AL',
                                       self.le_targtename.text() + '_EM_AL.xyz')
        self.t_al_altxyz = os.path.join(self.parentpath, '03-Hydropact440', '03-ALT GRIDS', '01-Alti_XYZ', 'AL',
                                        self.le_targtename.text() + '_ALT_AL.xyz')
        self.t_al_emtif = os.path.join(self.parentpath, '03-Hydropact440', '02-EM GRIDS', '02-EM_Tiff', 'AL',
                                       self.le_targtename.text() + '_EM_AL.tif')
        self.t_al_alttif = os.path.join(self.parentpath, '03-Hydropact440', '03-ALT GRIDS', '02-Alti_Tiff', 'AL',
                                        self.le_targtename.text() + '_ALT_AL.tif')

        self.savedfiles = [self.s_af_em, self.s_af_alt, self.s_af_mbes,
                           self.s_al_em, self.s_al_alt, self.s_al_mbes, self.s_al_prof,
                           self.m_af_tif, self.m_af_xy, self.m_af_ungr,
                           self.m_al_tif, self.m_al_xy, self.m_al_ungr,
                           self.t_af_emxyz, self.t_af_altxyz, self.t_af_emtif, self.t_af_alttif,
                           self.t_al_emxyz, self.t_al_altxyz, self.t_al_emtif, self.t_al_alttif]


    def getpath(self):
        sender = self.sender()

        match sender.objectName():
            case 'b_s_af_em':
                self.savepath = self.s_af_em
            case 'b_s_af_alt':
                self.savepath = self.s_af_alt
            case 'b_s_af_mbes':
                self.savepath = self.s_af_mbes
            case 'b_s_al_em':
                self.savepath = self.s_al_em
            case 'b_s_al_alt':
                self.savepath = self.s_al_alt
            case 'b_s_al_mbes':
                self.savepath = self.s_al_mbes
            case 'b_s_al_prof':
                self.savepath = self.s_al_prof

            case 'b_m_af_tif':
                self.savepath = self.m_af_tif
            case 'b_m_af_xy':
                self.savepath = self.m_af_xy
            case 'b_m_af_ungr':
                self.savepath = self.m_af_ungr
            case 'b_m_al_tif':
                self.savepath = self.m_al_tif
            case 'b_m_al_xy':
                self.savepath = self.m_al_xy
            case 'b_m_al_ungr':
                self.savepath = self.m_al_ungr

            case 'b_t_af_emxyz':
                self.savepath = self.t_af_emxyz
            case 'b_t_af_altxyz':
                self.savepath = self.t_af_altxyz
            case 'b_t_af_emtif':
                self.savepath = self.t_af_emtif
            case 'b_t_af_alttif':
                self.savepath = self.t_af_alttif
            case 'b_t_al_emxyz':
                self.savepath = self.t_al_emxyz
            case 'b_t_al_altxyz':
                self.savepath = self.t_al_altxyz
            case 'b_t_al_emtif':
                self.savepath = self.t_al_emtif
            case 'b_t_al_alttif':
                self.savepath = self.t_al_alttif

        self.clipboard.setText(self.savepath)
        self.l_path.setText(self.savepath)
        sender.setStyleSheet("background-color: rgb(0, 0, 150);")


def main():
    global mc
    global icon
    global iconhere
    global configfold
    global iconfile

    # executable parent folder and path to config.bin
    iconhere = False
    parentfold = os.path.dirname(sys.argv[0])
    configfold = os.path.join(parentfold, '_internal')
    iconfile = os.path.join(configfold, 'blob.ico')


    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')

    mc = MainWindow()

    # icon
    if os.path.isfile(iconfile):
        iconhere = True
        icon = QtGui.QIcon(iconfile)
        mc.setWindowIcon(icon)
    mc.setWindowTitle('OM Path2Clipboard (akayurin@gmail.com)')

    mc.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()