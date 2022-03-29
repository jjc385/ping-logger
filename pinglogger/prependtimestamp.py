import datetime

def prepend_timestamp(string, format="[%Y-%m-%d %H:%M:%S.%f] "):
    tObj = datetime.datetime.now()
    tStr = tObj.strftime(format)
    return tStr + string
