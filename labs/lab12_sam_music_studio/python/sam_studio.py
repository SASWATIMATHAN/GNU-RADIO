#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: SAM MUSIC STUDIO
# Author: SASWATI MATHAN
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import audio
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import threading



class sam_studio(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SAM MUSIC STUDIO", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("SAM MUSIC STUDIO")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "sam_studio")

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
        self.reverb3_delay = reverb3_delay = 0.12
        self.reverb2_delay = reverb2_delay = 0.07
        self.reverb1_delay = reverb1_delay = 0.03
        self.echo_delay = echo_delay = 0.25
        self.rev3_samples = rev3_samples = int(reverb3_delay * samp_rate)
        self.rev2_samples = rev2_samples = int(reverb2_delay * samp_rate)
        self.rev1_samples = rev1_samples = int(reverb1_delay * samp_rate)
        self.mix = mix = 0.6
        self.feedback_gain = feedback_gain = 0.4
        self.echo_samples = echo_samples = int(echo_delay * samp_rate)
        self.echo_gain = echo_gain = 0.5

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
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
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            3,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('C:\\Users\\hp\\Downloads\\GNU RADIO\\SAM AUDIO.wav', True)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_multiply_const_vxx_5 = blocks.multiply_const_ff(mix)
        self.blocks_multiply_const_vxx_4 = blocks.multiply_const_ff(feedback_gain)
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_ff(feedback_gain)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_ff(feedback_gain)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff((1 - mix))
        self.blocks_delay_1_1 = blocks.delay(gr.sizeof_float*1,  rev3_samples)
        self.blocks_delay_1_0 = blocks.delay(gr.sizeof_float*1,  rev2_samples)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1,  rev1_samples)
        self.blocks_add_xx_2 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_const_vxx_5, 0))
        self.connect((self.blocks_add_xx_2, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_add_xx_2, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.blocks_add_xx_2, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_add_xx_2, 0), (self.qtgui_waterfall_sink_x_0, 2))
        self.connect((self.blocks_delay_1, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_delay_1_0, 0), (self.blocks_multiply_const_vxx_3, 0))
        self.connect((self.blocks_delay_1_1, 0), (self.blocks_multiply_const_vxx_4, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_2, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_const_vxx_4, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_multiply_const_vxx_5, 0), (self.blocks_add_xx_2, 1))
        self.connect((self.blocks_multiply_const_vxx_5, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_multiply_const_vxx_5, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_multiply_const_vxx_5, 0), (self.qtgui_waterfall_sink_x_0, 1))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_delay_1_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_delay_1_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle2_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "sam_studio")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_echo_samples(int(self.echo_delay * self.samp_rate))
        self.set_rev1_samples(int(self.reverb1_delay * self.samp_rate))
        self.set_rev2_samples(int(self.reverb2_delay * self.samp_rate))
        self.set_rev3_samples(int(self.reverb3_delay * self.samp_rate))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_reverb3_delay(self):
        return self.reverb3_delay

    def set_reverb3_delay(self, reverb3_delay):
        self.reverb3_delay = reverb3_delay
        self.set_rev3_samples(int(self.reverb3_delay * self.samp_rate))

    def get_reverb2_delay(self):
        return self.reverb2_delay

    def set_reverb2_delay(self, reverb2_delay):
        self.reverb2_delay = reverb2_delay
        self.set_rev2_samples(int(self.reverb2_delay * self.samp_rate))

    def get_reverb1_delay(self):
        return self.reverb1_delay

    def set_reverb1_delay(self, reverb1_delay):
        self.reverb1_delay = reverb1_delay
        self.set_rev1_samples(int(self.reverb1_delay * self.samp_rate))

    def get_echo_delay(self):
        return self.echo_delay

    def set_echo_delay(self, echo_delay):
        self.echo_delay = echo_delay
        self.set_echo_samples(int(self.echo_delay * self.samp_rate))

    def get_rev3_samples(self):
        return self.rev3_samples

    def set_rev3_samples(self, rev3_samples):
        self.rev3_samples = rev3_samples
        self.blocks_delay_1_1.set_dly(int( self.rev3_samples))

    def get_rev2_samples(self):
        return self.rev2_samples

    def set_rev2_samples(self, rev2_samples):
        self.rev2_samples = rev2_samples
        self.blocks_delay_1_0.set_dly(int( self.rev2_samples))

    def get_rev1_samples(self):
        return self.rev1_samples

    def set_rev1_samples(self, rev1_samples):
        self.rev1_samples = rev1_samples
        self.blocks_delay_1.set_dly(int( self.rev1_samples))

    def get_mix(self):
        return self.mix

    def set_mix(self, mix):
        self.mix = mix
        self.blocks_multiply_const_vxx_1.set_k((1 - self.mix))
        self.blocks_multiply_const_vxx_5.set_k(self.mix)

    def get_feedback_gain(self):
        return self.feedback_gain

    def set_feedback_gain(self, feedback_gain):
        self.feedback_gain = feedback_gain
        self.blocks_multiply_const_vxx_2.set_k(self.feedback_gain)
        self.blocks_multiply_const_vxx_3.set_k(self.feedback_gain)
        self.blocks_multiply_const_vxx_4.set_k(self.feedback_gain)

    def get_echo_samples(self):
        return self.echo_samples

    def set_echo_samples(self, echo_samples):
        self.echo_samples = echo_samples

    def get_echo_gain(self):
        return self.echo_gain

    def set_echo_gain(self, echo_gain):
        self.echo_gain = echo_gain




def main(top_block_cls=sam_studio, options=None):

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
