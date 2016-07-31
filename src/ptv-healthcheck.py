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
    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
    return 'http://timetableapi.ptv.vic.gov.au'+raw+'&signature={1}&timestamp={2}'.format(devId, signature, timestamp)
print getUrl('/v2/healthcheck')
