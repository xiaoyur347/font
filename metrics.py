#!/usr/bin/env python

from __future__ import print_function
import sys


class Metrics:
    def __init__(self):
        self.leading = 0.0
        self.top = 0.0
        self.ascent = 0.0
        self.descent = 0.0
        self.bottom = 0.0

    def elegant(self, size):
        self.leading = 0
        self.top = -size * 2500.0 / 2048
        self.ascent = -size * 1900.0 / 2048
        self.descent = size * 500.0 / 2048
        self.bottom = size * 1000.0 / 2048

    # (NotoSansHans)top = -180.7,ascent = -88.0,descent = 12.0,bottom = 104.700005,leading = 50.0
    def otf_sans_hans(self, size):
        self.leading = size * 0.5 # OS/2 TypoLineGap / 1000
        self.top = -size * 1.807
        # https://github.com/adobe-fonts/source-han-sans/blob/1.000/Medium/features.CN
        self.ascent = -size * 0.88 # OS/2 TypoAscender / 1000
        self.descent = size * 0.12 # OS/2 TypoDescender / 1000
        self.bottom = size * 1.047

    # (NotoSerifSC)top = -180.8,ascent = -115.100006,descent = 28.600002,bottom = 104.799995,leading = 0.0
    def otf_serif_sc(self, size):
        self.leading = 0
        self.top = -size * 1.808
        self.ascent = -size * 1.151
        self.descent = size * 0.286
        self.bottom = size * 1.048

    # (NotoSansSC)top = -180.7,ascent = -116.0,descent = 32.0,bottom = 104.700005,leading = 0.0
    def otf_sans_sc(self, size):
        self.leading = 0
        self.top = -size * 1.807
        self.ascent = -size * 1.16
        self.descent = size * 0.32
        self.bottom = size * 1.047

    # top = -105.615234,ascent = -92.77344,descent = 24.414063,bottom = 27.09961,leading = 0
    def ttf(self, size):
        self.leading = 0
        self.top = -size * 2163.0 / 2048
        self.ascent = -size * 1900.0 / 2048
        self.descent = size * 500.0 / 2048
        self.bottom = size * 555.0 / 2048

    def printer(self):
        print("top = " + str(self.top)
              + ",ascent = " + str(self.ascent)
              + ",descent = " + str(self.descent)
              + ",bottom = " + str(self.bottom)
              + ",leading = " + str(self.leading))

if __name__ == '__main__':
    metrics = Metrics()

    size = int(sys.argv[1])

    print('elegant:')
    metrics.elegant(size)
    metrics.printer()

    print('NotoSansHans-Medium(1.000):')
    metrics.otf_sans_hans(size)
    metrics.printer()

    print('NotoSansHans-Medium(1.002):')
    metrics.otf_sans_hans(size)
    metrics.leading = 0
    metrics.printer()

    print('NotoSansSC-Medium(1.004):')
    metrics.otf_sans_sc(size)
    metrics.printer()

    print('Native-Medium:')
    metrics.ttf(size)
    metrics.printer()

    print('NotoSerifSC-Medium:')
    metrics.otf_serif_sc(size)
    metrics.printer()
