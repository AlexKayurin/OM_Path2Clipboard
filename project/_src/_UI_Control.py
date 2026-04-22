# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_UI_Control.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 470)
        MainWindow.setMinimumSize(QSize(400, 470))
        MainWindow.setMaximumSize(QSize(400, 470))
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 20))
        self.label.setMaximumSize(QSize(100, 20))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.le_targtename = QLineEdit(self.centralwidget)
        self.le_targtename.setObjectName(u"le_targtename")
        self.le_targtename.setMinimumSize(QSize(150, 20))
        self.le_targtename.setMaximumSize(QSize(150, 20))

        self.horizontalLayout.addWidget(self.le_targtename)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(80, 360))
        self.groupBox_3.setMaximumSize(QSize(80, 360))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"")
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(8, 0, 8, 0)
        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(60, 160))
        self.groupBox.setMaximumSize(QSize(60, 160))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 0, 3, 0)
        self.b_s_af_em = QPushButton(self.groupBox)
        self.b_s_af_em.setObjectName(u"b_s_af_em")
        self.b_s_af_em.setMinimumSize(QSize(50, 30))
        self.b_s_af_em.setMaximumSize(QSize(50, 30))

        self.verticalLayout.addWidget(self.b_s_af_em)

        self.b_s_af_alt = QPushButton(self.groupBox)
        self.b_s_af_alt.setObjectName(u"b_s_af_alt")
        self.b_s_af_alt.setMinimumSize(QSize(50, 30))
        self.b_s_af_alt.setMaximumSize(QSize(50, 30))

        self.verticalLayout.addWidget(self.b_s_af_alt)

        self.b_s_af_mbes = QPushButton(self.groupBox)
        self.b_s_af_mbes.setObjectName(u"b_s_af_mbes")
        self.b_s_af_mbes.setMinimumSize(QSize(50, 30))
        self.b_s_af_mbes.setMaximumSize(QSize(50, 30))

        self.verticalLayout.addWidget(self.b_s_af_mbes)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(60, 160))
        self.groupBox_2.setMaximumSize(QSize(60, 160))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.b_s_al_em = QPushButton(self.groupBox_2)
        self.b_s_al_em.setObjectName(u"b_s_al_em")
        self.b_s_al_em.setMinimumSize(QSize(50, 30))
        self.b_s_al_em.setMaximumSize(QSize(50, 30))

        self.verticalLayout_2.addWidget(self.b_s_al_em)

        self.b_s_al_alt = QPushButton(self.groupBox_2)
        self.b_s_al_alt.setObjectName(u"b_s_al_alt")
        self.b_s_al_alt.setMinimumSize(QSize(50, 30))
        self.b_s_al_alt.setMaximumSize(QSize(50, 30))

        self.verticalLayout_2.addWidget(self.b_s_al_alt)

        self.b_s_al_mbes = QPushButton(self.groupBox_2)
        self.b_s_al_mbes.setObjectName(u"b_s_al_mbes")
        self.b_s_al_mbes.setMinimumSize(QSize(50, 30))
        self.b_s_al_mbes.setMaximumSize(QSize(50, 30))

        self.verticalLayout_2.addWidget(self.b_s_al_mbes)

        self.b_s_al_prof = QPushButton(self.groupBox_2)
        self.b_s_al_prof.setObjectName(u"b_s_al_prof")
        self.b_s_al_prof.setMinimumSize(QSize(50, 30))
        self.b_s_al_prof.setMaximumSize(QSize(50, 30))

        self.verticalLayout_2.addWidget(self.b_s_al_prof)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(80, 360))
        self.groupBox_4.setMaximumSize(QSize(80, 360))
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet(u"")
        self.groupBox_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(8, 0, 8, 0)
        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(60, 160))
        self.groupBox_5.setMaximumSize(QSize(60, 160))
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.groupBox_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 0, 3, 0)
        self.b_m_af_tif = QPushButton(self.groupBox_5)
        self.b_m_af_tif.setObjectName(u"b_m_af_tif")
        self.b_m_af_tif.setMinimumSize(QSize(50, 30))
        self.b_m_af_tif.setMaximumSize(QSize(50, 30))

        self.verticalLayout_5.addWidget(self.b_m_af_tif)

        self.b_m_af_xy = QPushButton(self.groupBox_5)
        self.b_m_af_xy.setObjectName(u"b_m_af_xy")
        self.b_m_af_xy.setMinimumSize(QSize(50, 30))
        self.b_m_af_xy.setMaximumSize(QSize(50, 30))

        self.verticalLayout_5.addWidget(self.b_m_af_xy)

        self.b_m_af_ungr = QPushButton(self.groupBox_5)
        self.b_m_af_ungr.setObjectName(u"b_m_af_ungr")
        self.b_m_af_ungr.setMinimumSize(QSize(50, 30))
        self.b_m_af_ungr.setMaximumSize(QSize(50, 30))

        self.verticalLayout_5.addWidget(self.b_m_af_ungr)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(60, 160))
        self.groupBox_6.setMaximumSize(QSize(60, 160))
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.groupBox_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 0, 3, 0)
        self.b_m_al_tif = QPushButton(self.groupBox_6)
        self.b_m_al_tif.setObjectName(u"b_m_al_tif")
        self.b_m_al_tif.setMinimumSize(QSize(50, 30))
        self.b_m_al_tif.setMaximumSize(QSize(50, 30))

        self.verticalLayout_6.addWidget(self.b_m_al_tif)

        self.b_m_al_xy = QPushButton(self.groupBox_6)
        self.b_m_al_xy.setObjectName(u"b_m_al_xy")
        self.b_m_al_xy.setMinimumSize(QSize(50, 30))
        self.b_m_al_xy.setMaximumSize(QSize(50, 30))

        self.verticalLayout_6.addWidget(self.b_m_al_xy)

        self.b_m_al_ungr = QPushButton(self.groupBox_6)
        self.b_m_al_ungr.setObjectName(u"b_m_al_ungr")
        self.b_m_al_ungr.setMinimumSize(QSize(50, 30))
        self.b_m_al_ungr.setMaximumSize(QSize(50, 30))

        self.verticalLayout_6.addWidget(self.b_m_al_ungr)


        self.verticalLayout_4.addWidget(self.groupBox_6)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(80, 360))
        self.groupBox_7.setMaximumSize(QSize(80, 360))
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet(u"")
        self.groupBox_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(8, 0, 8, 0)
        self.groupBox_8 = QGroupBox(self.groupBox_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(60, 160))
        self.groupBox_8.setMaximumSize(QSize(60, 160))
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.groupBox_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 0, 3, 0)
        self.b_t_af_emxyz = QPushButton(self.groupBox_8)
        self.b_t_af_emxyz.setObjectName(u"b_t_af_emxyz")
        self.b_t_af_emxyz.setMinimumSize(QSize(50, 30))
        self.b_t_af_emxyz.setMaximumSize(QSize(50, 30))

        self.verticalLayout_8.addWidget(self.b_t_af_emxyz)

        self.b_t_af_altxyz = QPushButton(self.groupBox_8)
        self.b_t_af_altxyz.setObjectName(u"b_t_af_altxyz")
        self.b_t_af_altxyz.setMinimumSize(QSize(50, 30))
        self.b_t_af_altxyz.setMaximumSize(QSize(50, 30))

        self.verticalLayout_8.addWidget(self.b_t_af_altxyz)

        self.b_t_af_emtif = QPushButton(self.groupBox_8)
        self.b_t_af_emtif.setObjectName(u"b_t_af_emtif")
        self.b_t_af_emtif.setMinimumSize(QSize(50, 30))
        self.b_t_af_emtif.setMaximumSize(QSize(50, 30))

        self.verticalLayout_8.addWidget(self.b_t_af_emtif)

        self.b_t_af_alttif = QPushButton(self.groupBox_8)
        self.b_t_af_alttif.setObjectName(u"b_t_af_alttif")

        self.verticalLayout_8.addWidget(self.b_t_af_alttif)


        self.verticalLayout_7.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.groupBox_7)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(60, 160))
        self.groupBox_9.setMaximumSize(QSize(60, 160))
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.groupBox_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 0, 3, 0)
        self.b_t_al_emxyz = QPushButton(self.groupBox_9)
        self.b_t_al_emxyz.setObjectName(u"b_t_al_emxyz")
        self.b_t_al_emxyz.setMinimumSize(QSize(50, 30))
        self.b_t_al_emxyz.setMaximumSize(QSize(50, 30))

        self.verticalLayout_9.addWidget(self.b_t_al_emxyz)

        self.b_t_al_altxyz = QPushButton(self.groupBox_9)
        self.b_t_al_altxyz.setObjectName(u"b_t_al_altxyz")
        self.b_t_al_altxyz.setMinimumSize(QSize(50, 30))
        self.b_t_al_altxyz.setMaximumSize(QSize(50, 30))

        self.verticalLayout_9.addWidget(self.b_t_al_altxyz)

        self.b_t_al_emtif = QPushButton(self.groupBox_9)
        self.b_t_al_emtif.setObjectName(u"b_t_al_emtif")
        self.b_t_al_emtif.setMinimumSize(QSize(50, 30))
        self.b_t_al_emtif.setMaximumSize(QSize(50, 30))

        self.verticalLayout_9.addWidget(self.b_t_al_emtif)

        self.b_t_al_alttif = QPushButton(self.groupBox_9)
        self.b_t_al_alttif.setObjectName(u"b_t_al_alttif")
        self.b_t_al_alttif.setMinimumSize(QSize(50, 30))
        self.b_t_al_alttif.setMaximumSize(QSize(50, 30))

        self.verticalLayout_9.addWidget(self.b_t_al_alttif)


        self.verticalLayout_7.addWidget(self.groupBox_9)


        self.horizontalLayout_2.addWidget(self.groupBox_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.l_path = QLabel(self.centralwidget)
        self.l_path.setObjectName(u"l_path")
        self.l_path.setMinimumSize(QSize(385, 50))
        self.l_path.setMaximumSize(QSize(385, 50))
        font1 = QFont()
        font1.setPointSize(7)
        font1.setBold(False)
        self.l_path.setFont(font1)
        self.l_path.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.l_path)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Path2Clipboard", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Target name:", None))
        self.le_targtename.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"SCR-SHOTS", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"AF", None))
        self.b_s_af_em.setText(QCoreApplication.translate("MainWindow", u"EM", None))
        self.b_s_af_alt.setText(QCoreApplication.translate("MainWindow", u"ALT", None))
        self.b_s_af_mbes.setText(QCoreApplication.translate("MainWindow", u"MBES", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"AL", None))
        self.b_s_al_em.setText(QCoreApplication.translate("MainWindow", u"EM", None))
        self.b_s_al_alt.setText(QCoreApplication.translate("MainWindow", u"ALT", None))
        self.b_s_al_mbes.setText(QCoreApplication.translate("MainWindow", u"MBES", None))
        self.b_s_al_prof.setText(QCoreApplication.translate("MainWindow", u"PROF", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"MBES", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"AF", None))
        self.b_m_af_tif.setText(QCoreApplication.translate("MainWindow", u"TIFF", None))
        self.b_m_af_xy.setText(QCoreApplication.translate("MainWindow", u"XYZ", None))
        self.b_m_af_ungr.setText(QCoreApplication.translate("MainWindow", u"UNGR", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"AL", None))
        self.b_m_al_tif.setText(QCoreApplication.translate("MainWindow", u"TIFF", None))
        self.b_m_al_xy.setText(QCoreApplication.translate("MainWindow", u"XYZ", None))
        self.b_m_al_ungr.setText(QCoreApplication.translate("MainWindow", u"UNGR", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"TSS", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"AF", None))
        self.b_t_af_emxyz.setText(QCoreApplication.translate("MainWindow", u"EM XYZ", None))
        self.b_t_af_altxyz.setText(QCoreApplication.translate("MainWindow", u"ALT XYZ", None))
        self.b_t_af_emtif.setText(QCoreApplication.translate("MainWindow", u"EM TIF", None))
        self.b_t_af_alttif.setText(QCoreApplication.translate("MainWindow", u"ALT TIF", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"AL", None))
        self.b_t_al_emxyz.setText(QCoreApplication.translate("MainWindow", u"EM XYZ", None))
        self.b_t_al_altxyz.setText(QCoreApplication.translate("MainWindow", u"ALT XYZ", None))
        self.b_t_al_emtif.setText(QCoreApplication.translate("MainWindow", u"EM TIF", None))
        self.b_t_al_alttif.setText(QCoreApplication.translate("MainWindow", u"ALT TIF", None))
        self.l_path.setText(QCoreApplication.translate("MainWindow", u"PATH", None))
    # retranslateUi

