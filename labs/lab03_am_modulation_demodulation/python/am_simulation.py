#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: AMPLITUDE MODULATION
# Author: SASWATI MATHAN
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
import sip
import threading



class am_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "AMPLITUDE MODULATION", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("AMPLITUDE MODULATION")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "am_simulation")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.mod_depth = mod_depth = 50
        self.carrier_frequency = carrier_frequency = 1000
        self.baseband_frequency = baseband_frequency = 40
        self.baseband_amplitude = baseband_amplitude = 0.5

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self._mod_depth_tool_bar = Qt.QToolBar(self)

        if None:
            self._mod_depth_formatter = None
        else:
            self._mod_depth_formatter = lambda x: str(x)

        self._mod_depth_tool_bar.addWidget(Qt.QLabel("MODULATION DEPTH"))
        self._mod_depth_label = Qt.QLabel(str(self._mod_depth_formatter(self.mod_depth)))
        self._mod_depth_tool_bar.addWidget(self._mod_depth_label)
        self.top_layout.addWidget(self._mod_depth_tool_bar)
        self._carrier_frequency_range = qtgui.Range(0, 16000, 1, 1000, 200)
        self._carrier_frequency_win = qtgui.RangeWidget(self._carrier_frequency_range, self.set_carrier_frequency, "CARRIER FREQUENCY", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._carrier_frequency_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('C:\\Users\\hp\\Downloads\\GNU RADIO\\SAM AUDIO.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self._baseband_frequency_range = qtgui.Range(0, 200, 1, 40, 200)
        self._baseband_frequency_win = qtgui.RangeWidget(self._baseband_frequency_range, self.set_baseband_frequency, "BASEBAND FREQUENCY", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._baseband_frequency_win)
        self._baseband_amplitude_range = qtgui.Range(0, 2, 0.01, 0.5, 200)
        self._baseband_amplitude_win = qtgui.RangeWidget(self._baseband_amplitude_range, self.set_baseband_amplitude, "BASEBAND AMPLITUDE", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._baseband_amplitude_win)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 10000, 0.5, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_wavfile_source_0, 0), (self.qtgui_time_sink_x_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "am_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_mod_depth(self):
        return self.mod_depth

    def set_mod_depth(self, mod_depth):
        self.mod_depth = mod_depth
        Qt.QMetaObject.invokeMethod(self._mod_depth_label, "setText", Qt.Q_ARG("QString", str(self._mod_depth_formatter(self.mod_depth))))

    def get_carrier_frequency(self):
        return self.carrier_frequency

    def set_carrier_frequency(self, carrier_frequency):
        self.carrier_frequency = carrier_frequency

    def get_baseband_frequency(self):
        return self.baseband_frequency

    def set_baseband_frequency(self, baseband_frequency):
        self.baseband_frequency = baseband_frequency

    def get_baseband_amplitude(self):
        return self.baseband_amplitude

    def set_baseband_amplitude(self, baseband_amplitude):
        self.baseband_amplitude = baseband_amplitude




def main(top_block_cls=am_simulation, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
