#!/usr/bin/env python

from hashlib import sha1
import hmac
import binascii
import datetime

def getUrl(request):
    devId = '1000820'
    key = 'bdb70532-55fa-11e6-a0ce-06f54b901f07'
    request = request + ('&' if ('?' in request) else '?')
    raw = request+'devid={0}'.format(devId)
    hashed = hmac.new(key, raw, sha1)
    signature = hashed.hexdigest()
    return 'http://timetableapi.ptv.vic.gov.au'+raw+'&signature={1}'.format(devId, signature)
print getUrl('/v2/disruptions/modes')
