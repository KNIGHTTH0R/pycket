# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgingDialog.ui'
#
# Created: Wed Nov 18 05:32:13 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(553, 447)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_eth = QtGui.QWidget()
        self.tab_eth.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab_eth.setObjectName(_fromUtf8("tab_eth"))
        self.gridLayout = QtGui.QGridLayout(self.tab_eth)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_source_mac = QtGui.QLabel(self.tab_eth)
        self.label_source_mac.setObjectName(_fromUtf8("label_source_mac"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_source_mac)
        self.line_edit_source_mac = QtGui.QLineEdit(self.tab_eth)
        self.line_edit_source_mac.setMaxLength(17)
        self.line_edit_source_mac.setObjectName(_fromUtf8("line_edit_source_mac"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_edit_source_mac)
        self.label_destination_mac = QtGui.QLabel(self.tab_eth)
        self.label_destination_mac.setObjectName(_fromUtf8("label_destination_mac"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_destination_mac)
        self.line_edit_destination_mac = QtGui.QLineEdit(self.tab_eth)
        self.line_edit_destination_mac.setMaxLength(17)
        self.line_edit_destination_mac.setObjectName(_fromUtf8("line_edit_destination_mac"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.line_edit_destination_mac)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_eth, _fromUtf8(""))
        self.tab_ip = QtGui.QWidget()
        self.tab_ip.setObjectName(_fromUtf8("tab_ip"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_ip)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_source_ip = QtGui.QLabel(self.tab_ip)
        self.label_source_ip.setObjectName(_fromUtf8("label_source_ip"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_source_ip)
        self.line_edit_source_ip = QtGui.QLineEdit(self.tab_ip)
        self.line_edit_source_ip.setMaxLength(15)
        self.line_edit_source_ip.setObjectName(_fromUtf8("line_edit_source_ip"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_edit_source_ip)
        self.label_destination_ip = QtGui.QLabel(self.tab_ip)
        self.label_destination_ip.setObjectName(_fromUtf8("label_destination_ip"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_destination_ip)
        self.line_edit_destination_ip = QtGui.QLineEdit(self.tab_ip)
        self.line_edit_destination_ip.setMaxLength(15)
        self.line_edit_destination_ip.setObjectName(_fromUtf8("line_edit_destination_ip"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.line_edit_destination_ip)
        self.label_ttl = QtGui.QLabel(self.tab_ip)
        self.label_ttl.setObjectName(_fromUtf8("label_ttl"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_ttl)
        self.spin_box_ttl = QtGui.QSpinBox(self.tab_ip)
        self.spin_box_ttl.setMinimum(1)
        self.spin_box_ttl.setMaximum(255)
        self.spin_box_ttl.setProperty("value", 64)
        self.spin_box_ttl.setObjectName(_fromUtf8("spin_box_ttl"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.spin_box_ttl)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_ip, _fromUtf8(""))
        self.tab_transport_layer = QtGui.QWidget()
        self.tab_transport_layer.setObjectName(_fromUtf8("tab_transport_layer"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_transport_layer)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.combo_box_transport = QtGui.QComboBox(self.tab_transport_layer)
        self.combo_box_transport.setObjectName(_fromUtf8("combo_box_transport"))
        self.combo_box_transport.addItem(_fromUtf8(""))
        self.combo_box_transport.addItem(_fromUtf8(""))
        self.combo_box_transport.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.combo_box_transport)
        self.stacked_widget_transport = QtGui.QStackedWidget(self.tab_transport_layer)
        self.stacked_widget_transport.setObjectName(_fromUtf8("stacked_widget_transport"))
        self.page_tcp = QtGui.QWidget()
        self.page_tcp.setObjectName(_fromUtf8("page_tcp"))
        self.gridLayout_5 = QtGui.QGridLayout(self.page_tcp)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_tcp_source_port = QtGui.QLabel(self.page_tcp)
        self.label_tcp_source_port.setObjectName(_fromUtf8("label_tcp_source_port"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_tcp_source_port)
        self.spin_box_tcp_source_port = QtGui.QSpinBox(self.page_tcp)
        self.spin_box_tcp_source_port.setMinimum(1)
        self.spin_box_tcp_source_port.setMaximum(65535)
        self.spin_box_tcp_source_port.setProperty("value", 8000)
        self.spin_box_tcp_source_port.setObjectName(_fromUtf8("spin_box_tcp_source_port"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.spin_box_tcp_source_port)
        self.label_tcp_destination_port = QtGui.QLabel(self.page_tcp)
        self.label_tcp_destination_port.setObjectName(_fromUtf8("label_tcp_destination_port"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_tcp_destination_port)
        self.spin_box_tcp_destination_port = QtGui.QSpinBox(self.page_tcp)
        self.spin_box_tcp_destination_port.setMinimum(1)
        self.spin_box_tcp_destination_port.setMaximum(65535)
        self.spin_box_tcp_destination_port.setProperty("value", 8000)
        self.spin_box_tcp_destination_port.setObjectName(_fromUtf8("spin_box_tcp_destination_port"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.spin_box_tcp_destination_port)
        self.label_tcp_sequence = QtGui.QLabel(self.page_tcp)
        self.label_tcp_sequence.setObjectName(_fromUtf8("label_tcp_sequence"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_tcp_sequence)
        self.spin_box_tcp_sequence = QtGui.QSpinBox(self.page_tcp)
        self.spin_box_tcp_sequence.setMaximum(2147483647)
        self.spin_box_tcp_sequence.setProperty("value", 420)
        self.spin_box_tcp_sequence.setObjectName(_fromUtf8("spin_box_tcp_sequence"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.spin_box_tcp_sequence)
        self.label_tcp_acknowledgement = QtGui.QLabel(self.page_tcp)
        self.label_tcp_acknowledgement.setObjectName(_fromUtf8("label_tcp_acknowledgement"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_tcp_acknowledgement)
        self.spin_box_tcp_acknowledgement = QtGui.QSpinBox(self.page_tcp)
        self.spin_box_tcp_acknowledgement.setMaximum(2147483647)
        self.spin_box_tcp_acknowledgement.setObjectName(_fromUtf8("spin_box_tcp_acknowledgement"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.spin_box_tcp_acknowledgement)
        self.label_tcp_data = QtGui.QLabel(self.page_tcp)
        self.label_tcp_data.setObjectName(_fromUtf8("label_tcp_data"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_tcp_data)
        self.line_edit_tcp_data = QtGui.QLineEdit(self.page_tcp)
        self.line_edit_tcp_data.setMaxLength(512)
        self.line_edit_tcp_data.setFrame(True)
        self.line_edit_tcp_data.setObjectName(_fromUtf8("line_edit_tcp_data"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.FieldRole, self.line_edit_tcp_data)
        self.gridLayout_5.addLayout(self.formLayout_4, 0, 0, 1, 1)
        self.stacked_widget_transport.addWidget(self.page_tcp)
        self.page_icmp = QtGui.QWidget()
        self.page_icmp.setObjectName(_fromUtf8("page_icmp"))
        self.gridLayout_6 = QtGui.QGridLayout(self.page_icmp)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_icmp_type = QtGui.QLabel(self.page_icmp)
        self.label_icmp_type.setObjectName(_fromUtf8("label_icmp_type"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_icmp_type)
        self.label_icmp_code = QtGui.QLabel(self.page_icmp)
        self.label_icmp_code.setObjectName(_fromUtf8("label_icmp_code"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_icmp_code)
        self.label_icmp_data = QtGui.QLabel(self.page_icmp)
        self.label_icmp_data.setObjectName(_fromUtf8("label_icmp_data"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_icmp_data)
        self.spin_box_icmp_type = QtGui.QSpinBox(self.page_icmp)
        self.spin_box_icmp_type.setMaximum(18)
        self.spin_box_icmp_type.setProperty("value", 8)
        self.spin_box_icmp_type.setObjectName(_fromUtf8("spin_box_icmp_type"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.spin_box_icmp_type)
        self.spin_box_icmp_code = QtGui.QSpinBox(self.page_icmp)
        self.spin_box_icmp_code.setMaximum(15)
        self.spin_box_icmp_code.setProperty("value", 0)
        self.spin_box_icmp_code.setObjectName(_fromUtf8("spin_box_icmp_code"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.spin_box_icmp_code)
        self.line_edit_icmp_data = QtGui.QLineEdit(self.page_icmp)
        self.line_edit_icmp_data.setMaxLength(512)
        self.line_edit_icmp_data.setObjectName(_fromUtf8("line_edit_icmp_data"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.line_edit_icmp_data)
        self.gridLayout_6.addLayout(self.formLayout_5, 0, 0, 1, 1)
        self.stacked_widget_transport.addWidget(self.page_icmp)
        self.page_udp = QtGui.QWidget()
        self.page_udp.setObjectName(_fromUtf8("page_udp"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page_udp)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_udp_source_port = QtGui.QLabel(self.page_udp)
        self.label_udp_source_port.setObjectName(_fromUtf8("label_udp_source_port"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_udp_source_port)
        self.spin_box_udp_source_port = QtGui.QSpinBox(self.page_udp)
        self.spin_box_udp_source_port.setMinimum(1)
        self.spin_box_udp_source_port.setMaximum(65535)
        self.spin_box_udp_source_port.setProperty("value", 8000)
        self.spin_box_udp_source_port.setObjectName(_fromUtf8("spin_box_udp_source_port"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.spin_box_udp_source_port)
        self.label_udp_destination_port = QtGui.QLabel(self.page_udp)
        self.label_udp_destination_port.setObjectName(_fromUtf8("label_udp_destination_port"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_udp_destination_port)
        self.spin_box_udp_destination_port = QtGui.QSpinBox(self.page_udp)
        self.spin_box_udp_destination_port.setMinimum(1)
        self.spin_box_udp_destination_port.setMaximum(65535)
        self.spin_box_udp_destination_port.setProperty("value", 8000)
        self.spin_box_udp_destination_port.setObjectName(_fromUtf8("spin_box_udp_destination_port"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.spin_box_udp_destination_port)
        self.label_udp_data = QtGui.QLabel(self.page_udp)
        self.label_udp_data.setObjectName(_fromUtf8("label_udp_data"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_udp_data)
        self.line_edit_udp_data = QtGui.QLineEdit(self.page_udp)
        self.line_edit_udp_data.setMaxLength(512)
        self.line_edit_udp_data.setObjectName(_fromUtf8("line_edit_udp_data"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.line_edit_udp_data)
        self.gridLayout_4.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.stacked_widget_transport.addWidget(self.page_udp)
        self.verticalLayout.addWidget(self.stacked_widget_transport)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_transport_layer, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.stacked_widget_transport.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Packet forging", None))
        self.label_source_mac.setText(_translate("Dialog", "Source MAC", None))
        self.line_edit_source_mac.setText(_translate("Dialog", "42:42:42:42:42:42", None))
        self.label_destination_mac.setText(_translate("Dialog", "Destination MAC", None))
        self.line_edit_destination_mac.setText(_translate("Dialog", "ff:ff:ff:ff:ff:ff", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_eth), _translate("Dialog", "Ethernet", None))
        self.label_source_ip.setText(_translate("Dialog", "Source IP", None))
        self.line_edit_source_ip.setText(_translate("Dialog", "216.58.211.227", None))
        self.label_destination_ip.setText(_translate("Dialog", "Destination IP", None))
        self.line_edit_destination_ip.setText(_translate("Dialog", "216.58.211.238", None))
        self.label_ttl.setText(_translate("Dialog", "TTL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ip), _translate("Dialog", "IP", None))
        self.combo_box_transport.setItemText(0, _translate("Dialog", "TCP", None))
        self.combo_box_transport.setItemText(1, _translate("Dialog", "ICMP", None))
        self.combo_box_transport.setItemText(2, _translate("Dialog", "UDP", None))
        self.label_tcp_source_port.setText(_translate("Dialog", "Source port", None))
        self.label_tcp_destination_port.setText(_translate("Dialog", "Destination port", None))
        self.label_tcp_sequence.setText(_translate("Dialog", "Sequence number", None))
        self.label_tcp_acknowledgement.setText(_translate("Dialog", "Acknowlegement", None))
        self.label_tcp_data.setText(_translate("Dialog", "Data", None))
        self.label_icmp_type.setText(_translate("Dialog", "Type", None))
        self.label_icmp_code.setText(_translate("Dialog", "Code", None))
        self.label_icmp_data.setText(_translate("Dialog", "Data", None))
        self.label_udp_source_port.setText(_translate("Dialog", "Source port", None))
        self.label_udp_destination_port.setText(_translate("Dialog", "Destination port", None))
        self.label_udp_data.setText(_translate("Dialog", "Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_transport_layer), _translate("Dialog", "TransportLayer", None))

