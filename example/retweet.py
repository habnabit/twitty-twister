#!/usr/bin/env python
"""

Copyright (c) 2008  Dustin Sallings <dustin@spy.net>
Copyright (c) 2010 Dustin Sallings <dustin@spy.net>
"""

import os
import sys

sys.path.append(os.path.join(sys.path[0], '..', 'twittytwister'))
sys.path.append('twittytwister')

from twisted.internet import reactor, protocol, defer, task

import twitter

def got_it(x):
    print "Retweet ID:", x.id

def cb(x):
    print "DONE"

def eb(e):
    print e

twitter.Twitter(sys.argv[1], sys.argv[2]).retweet(sys.argv[3], got_it
    ).addCallback(cb).addErrback(eb).addBoth(lambda x: reactor.stop())

reactor.run()
