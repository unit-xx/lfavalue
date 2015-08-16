# pricing the option value for 150018

import sys
import random
import ConfigParser

def apath(d0, m0, a0, baratio):
    # a's cash flow path
    at = a0
    mt = m0
    day = d0
    tdelta = 1.0 / DOY

    # cash flow tick and amount
    cfamt = []

    stoploop = False
    dolwreset = False

    while stoploop:
        # loop until long enough (T>Tmax) and a lower bound reset is done
        day = d0 + 1
        at += rdef * tdelta
        rday = rfree * tdeta + sig * (tdelta**0.5) * random.gauss(0, 1)
        mt = mt * (1 + rday)
        bt = (mt * (1+baratio) - at) / baratio

        if (bt < lwbound):
            # lower reset
            dolwreset = True
            cflow = bt * adiscount + (at - bt) * 0.97
            cfamt.append( ((day-d0)/DOY, cflow) )
            mt = 1.0
            at = 1.0
        elif (bt > ubound):
            # upper reset
            bt = 1.0

        if abs(day % DOY) < 1e-6:
            # a new year
            cfamt.append( ((day-d0)/DOY, at-1.0) )
            at = 1.0

        if (day > Dmax) and dolwreset:
            stoploop = True
        else:
            dolwreset = False

    return cfamt

def NPV(cfamt):
    npv = 0.0
    for tick, amt in cfamt:
        npv = amt * math.exp(-rfree * tick)

    return npv

def avalue(m, d0, rfree, sig, ubound, lwbound, baratio, rdef, adiscount, DOY):
    # a's value by averaging many a's cash flow path

    while True:
        pa = apath()
        av = NPV(pa)

        avavg += av

        pcount += 1
        if (pcount == Npath):
            avavg = avavg / Npath
            break

    return avavg


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
