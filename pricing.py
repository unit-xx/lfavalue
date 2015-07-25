# pricing the option value for 150018

import sys
import ConfigParser

def apath():
    # a's cash flow path
    pass

def avalue(m, t0, rfree, sig, ubound, lwbound, baratio, rdef, adiscount, doy):
    # a's value by averaging many a's cash flow path

    a = 1.0 + rdef * t0
    b = (m * (1+baratio) - a) / baratio

    dt = 1.0 / doy

    while True:
        rday = mu * dt + sig * (dt**0.5) * random.gauss(0, 1)

def main():
    cfg = ConfigParser.ConfigParser()
    cfg.optionxform = str
    try:
        cfgfn = sys.argv[1]
    except IndexError:
        cfgfn = 'price.ini'

    cfg.read(cfgfn)

    param = dict(cfg.items('main'))

    v = value()

if __name__=='__main__':
    main()

# $Id: pricing.py 920 2014-08-06 05:34:17Z gaochongnan@gmail.com $
