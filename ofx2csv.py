#!/usr/bin/env python3

# Copyright 2017 Daniel Hilst Selli <danielhilst@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
from os import path
import sys
import codecs
from ofxparse import OfxParser

def ofx2csv(file_):
    with codecs.open(file_) as fileobj:
        ofx = OfxParser.parse(fileobj)
    # a = ofx.accounts                        # An account with information
    n = ofx.account.number                  # The account number
    rn = ofx.account.routing_number          # The transit id (sometimes called branch number)
    sd = ofx.account.statement.start_date    # The start date of the transactions
    ed = ofx.account.statement.end_date      # The end date of the transactions
    bal = ofx.account.statement.balance       # The money in the account as of the statement date
    for t in ofx.account.statement.transactions:  # A list of account activities
        yield '{};{};{};{};{}'.format(
            n, rn, t.date, t.memo, t.amount)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <ofxfile>'.format(path.basename(sys.argv[0])))
        sys.exit(1)
    for line in ofx2csv(sys.argv[1]):
        print(line)
                    
    
