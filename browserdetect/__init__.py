from zope.cachedescriptors.property import Lazy


UNKNOWN = u"Unknown"


class Browser(object):

    def __init__(self, request):
        self.request = request
        self.agent = self.request.META.get('HTTP_USER_AGENT', u'')
        self._ua = self.agent.lower()

    @Lazy
    def platform(self):
        if self.is_mac:
            return u'Mac (OS X)'
        elif self.is_linux:
            return u'Linux'
        elif self.is_windows:
            return u'Microsoft Windows'
        elif self.is_freebsd:
            return u'FreeBSD'
        else:
            return UNKNOWN

    @Lazy
    def name(self):
        if self.is_safari:
            if self.is_safari3:
                return u'Safari 3.x'
            elif self.is_safari4:
                return u'Safari 4.x'
            elif self.is_safari5:
                return u'Safari 5.x'
            else:
                return u'Safari'
        elif self.is_gecko:
            out = u''
            if self.is_gecko2:
                out = u'Gecko 2.x'
            elif self.is_gecko3:
                out = u'Gecko 3.x'
            elif self.is_gecko4:
                out = u'Gecko 4.x'
            else:
                out = u'Gecko'

            if self.is_firefox:
                if self.is_firefox1:
                    return '%s / Firefox 1.x' % out
                elif self.is_firefox2:
                    return '%s / Firefox 2.x' % out
                elif self.is_firefox3:
                    return '%s / Firefox 3.x' % out
                elif self.is_firefox4:
                    return '%s / Firefox 4.x' % out
                else:
                    return '%s / Firefox' % out
            return out

        elif self.is_ie:
            if self.is_ie6:
                return u'Internet Explorer 6.x'
            elif self.is_ie7:
                return u'Internet Explorer 7.x'
            elif self.is_ie8:
                return u'Internet Explorer 8.x'
            elif self.is_ie9:
                return u'Internet Explorer 9.x'
            else:
                return u'Internet Explorer'
        elif self.is_chrome:
            return u'Chrome'
        elif self.is_opera:
            return u'Opera'
        else:
            return UNKNOWN

    @Lazy
    def is_webkit(self):
        return (self._ua.find('webkit') >= 0)

    @Lazy
    def is_opera(self):
        return (self._ua.find('opera') >= 0)

    @Lazy
    def is_chrome(self):
        return (self._ua.find('chrome/') >= 0)

    @Lazy
    def is_safari(self):
        return (not self.is_chrome) and (self._ua.find('safari') >= 0)

    @Lazy
    def is_safari3(self):
        return self.is_safari and (self._ua.find('version/3') > 0)

    @Lazy
    def is_safari4(self):
        return self.is_safari and (self._ua.find('version/4') > 0)

    @Lazy
    def is_safari5(self):
        return self.is_safari and (self._ua.find('version/5') > 0)

    @Lazy
    def is_ie(self):
        return (not self.is_opera) and (self._ua.find('msie') >= 0)

    @Lazy
    def is_ie7(self):
        return self.is_ie and (self._ua.find('msie 7') >= 0)

    @Lazy
    def is_ie8(self):
        return self.is_ie and (self._ua.find('msie 8') >= 0)

    @Lazy
    def is_ie6(self):
        return self.is_ie and not (self.is_ie7 or self.is_ie8 or self.is_ie9)

    @Lazy
    def is_ie9(self):
        return self.is_ie and (self._ua.find('msie 9') >= 0)

    @Lazy
    def is_gecko(self):
        return not (self.is_webkit or self.is_opera) and (self._ua.find('gecko') >= 0)

    @Lazy
    def is_gecko4(self):
        return self.is_gecko and (self._ua.find('rv:2.') > 0)

    @Lazy
    def is_gecko3(self):
        return self.is_gecko and (self._ua.find('rv:1.9') > 0)

    @Lazy
    def is_gecko2(self):
        return self.is_gecko and not (self.is_gecko3 or self.is_gecko4)

    @Lazy
    def is_firefox(self):
        return self.is_gecko and (self._ua.find('firefox/') > 0)

    @Lazy
    def is_firefox1(self):
        return self.is_gecko and (self._ua.find('firefox/1') > 0)

    @Lazy
    def is_firefox2(self):
        return self.is_gecko and (self._ua.find('firefox/2') > 0)

    @Lazy
    def is_firefox3(self):
        return self.is_gecko and (self._ua.find('firefox/3') > 0)

    @Lazy
    def is_firefox4(self):
        return self.is_gecko and (self._ua.find('firefox/4') > 0)

    @Lazy
    def is_windows(self):
        return (self._ua.find('windows') > 0) or (self._ua.find('win32') > 0)

    @Lazy
    def is_mac(self):
        return (self._ua.find('macintosh') > 0) or (self._ua.find('mac os x') > 0)

    @Lazy
    def is_linux(self):
        return (self._ua.find('linux') > 0)

    @Lazy
    def is_freebsd(self):
        return (self._ua.find('freebsd') > 0)
