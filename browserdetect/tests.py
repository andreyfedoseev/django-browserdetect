from browserdetect import Browser
from django.http import HttpRequest
import unittest


# user agent strings are taken from http://www.useragentstring.com/
TEST_DATA = {
    # Firefox 1
    "firefox1_windows": ("Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU; rv:1.7.7) Gecko/20050414 Firefox/1.0.3", ("is_firefox", "is_firefox1", "is_windows", "is_gecko", "is_gecko2")),
    "firefox1_linux": ("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.7) Gecko/20050421 Firefox/1.0.3 (Debian package 1.0.3-2)", ("is_firefox", "is_firefox1", "is_linux", "is_gecko", "is_gecko2")),
    "firefox1_freebsd": ("Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7.7) Gecko/20060303 Firefox/1.0.3", ("is_firefox", "is_firefox1", "is_freebsd", "is_gecko", "is_gecko2")),
    "firefox1_mac": ("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3", ("is_firefox", "is_firefox1", "is_mac", "is_gecko", "is_gecko2")),
    # Firefox 2
    "firefox2_windows": ("Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.8.1.2) Gecko/20070219 Firefox/2.0.0.2", ("is_firefox", "is_firefox2", "is_windows", "is_gecko", "is_gecko2")),
    "firefox2_linux": ("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20061201 Firefox/2.0.0.2", ("is_firefox", "is_firefox2", "is_linux", "is_gecko", "is_gecko2")),
    "firefox2_mac": ("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.2) Gecko/20070224 Firefox/2.0.0.2", ("is_firefox", "is_firefox2", "is_mac", "is_gecko", "is_gecko2")),
    # Firefox 3
    "firefox3_windows": ("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)", ("is_firefox", "is_firefox3", "is_windows", "is_gecko", "is_gecko3")),
    "firefox3_linux": ("Mozilla/5.0 (X11; U; Linux x86_64; es-ES; rv:1.9.0.12) Gecko/2009072711 CentOS/3.0.12-1.el5.centos Firefox/3.0.12", ("is_firefox", "is_firefox3", "is_linux", "is_gecko", "is_gecko3")),
    "firefox3_mac": ("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; fr; rv:1.9.0.13) Gecko/2009073021 Firefox/3.0.13", ("is_firefox", "is_firefox3", "is_mac", "is_gecko", "is_gecko3")),
    # Firefox 4
    "firefox4_windows": ("Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)", ("is_firefox", "is_firefox4", "is_windows", "is_gecko", "is_gecko3")),
    "firefox4_linux": ("Mozilla/5.0 (X11; Linux x86_64; rv:2.0b9pre) Gecko/20110111 Firefox/4.0b9pre", ("is_firefox", "is_firefox4", "is_linux", "is_gecko", "is_gecko4")),
    "firefox4_mac": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b8) Gecko/20100101 Firefox/4.0b8", ("is_firefox", "is_firefox4", "is_mac", "is_gecko", "is_gecko4")),
    # IE6
    "ie6_windows": ("Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)", ("is_ie", "is_ie6", "is_windows")),
    # IE7
    "ie7_windows": ("Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR)", ("is_ie", "is_ie7", "is_windows")),
    # IE8
    "ie8_windows": ("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8; InfoPath.3; .NET4.0C; .NET4.0E) chromeframe/8.0.552.224", ("is_ie", "is_ie8", "is_windows")),
    # IE9
    "ie9_windows": ("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)", ("is_ie", "is_ie9", "is_windows")),
    # Chrome
    "chrome_windows": ("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.241.0 Safari/532.4", ("is_chrome", "is_windows", "is_webkit")),
    "chrome_linux": ("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10", ("is_chrome", "is_linux", "is_webkit")),
    "chrome_mac": ("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.414.0 Safari/534.1", ("is_chrome", "is_mac", "is_webkit")),
    # Safari 3
    "safari3_windows": ("Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/525.28 (KHTML, like Gecko) Version/3.2.2 Safari/525.28.1", ("is_safari", "is_safari3", "is_windows", "is_webkit")),
    "safari3_mac": ("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; fr-fr) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1", ("is_safari", "is_safari3", "is_mac", "is_webkit")),
    # Safari 4
    "safari4_windows": ("Mozilla/5.0 (Windows; U; Windows NT 6.0; ru-RU) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16", ("is_safari", "is_safari4", "is_windows", "is_webkit")),
    "safari4_mac": ("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/4.0.1 Safari/530.18", ("is_safari", "is_safari4", "is_mac", "is_webkit")),
    # Safari 5
    "safari4_windows": ("Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5", ("is_safari", "is_safari5", "is_windows", "is_webkit")),
    "safari4_mac": ("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4", ("is_safari", "is_safari5", "is_mac", "is_webkit")),
    # Opera
    "opera_windows": ("Opera/9.80 (Windows NT 6.0; U; Gecko/20100115; pl) Presto/2.2.15 Version/10.10", ("is_opera", "is_windows")),
    "opera_linux": ("Opera/9.80 (X11; Linux x86_64; U; en) Presto/2.2.15 Version/10.00", ("is_opera", "is_linux")),
    "opera_mac": ("Opera/9.80 (Macintosh; Intel Mac OS X; U; nl) Presto/2.6.30 Version/10.61", ("is_opera", "is_mac")),
}


TESTED_ATTRIBUTES = filter(lambda x: x.startswith("is_"),
                           Browser.__dict__.keys())


class TestBrowserDetect(unittest.TestCase):
    pass


def make_request(agent):
    request = HttpRequest()
    request.META["HTTP_USER_AGENT"] = agent
    return request


def add_test_method(method_name):

    def test_method(self):
        agent, attrs = TEST_DATA[method_name]
        browser = Browser(make_request(agent))
        for attr in TESTED_ATTRIBUTES:
            if attr in attrs:
                self.assertTrue(getattr(browser, attr), attr)
            else:
                self.assertFalse(getattr(browser, attr), attr)

    func_name = "test_%s" % method_name
    test_method.func_name = func_name
    setattr(TestBrowserDetect, func_name, test_method)


for method_name in TEST_DATA:
    add_test_method(method_name)


if __name__ == '__main__':
    unittest.main()
