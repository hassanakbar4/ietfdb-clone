from pyquery import PyQuery
from Cookie import SimpleCookie

from django.urls import reverse as urlreverse

import debug                            # pyflakes:ignore

from ietf.utils.test_utils import TestCase


class CookieTests(TestCase):
    def test_settings_defaults(self):
        r = self.client.get(urlreverse("ietf.cookies.views.preferences"))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual([], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(), ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/off"]').contents(),   ['Off'])

        
    def test_settings_defaults_from_cookies(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '7', 'expires_soon' : 7, 'left_menu': 'on', })
        r = self.client.get(urlreverse("ietf.cookies.views.preferences"))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual([], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/7"]').contents(),    ['7 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/7"]').contents(),  ['7 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/on"]').contents(),    ['On'])
        
    def test_settings_values_from_cookies_garbage(self):
        self.client.cookies = SimpleCookie({'full_draft': 'foo', 'new_enough' : 'foo', 'expires_soon' : 'foo', 'left_menu': 'foo', })
        r = self.client.get(urlreverse("ietf.cookies.views.preferences"))
        self.assertEqual(r.status_code, 200)
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(), ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/off"]').contents(),   ['Off'])

    def test_settings_values_from_cookies_random(self):
        self.client.cookies = SimpleCookie({'full_draft': 'zappa', 'new_enough' : '365', 'expires_soon' : '5', 'left_menu': 'zappa', })
        r = self.client.get(urlreverse("ietf.cookies.views.preferences"))
        self.assertEqual(r.status_code, 200)
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href^="/accounts/settings/new_enough/"]').contents(),    [])
        self.assertEqual(q('div a.active[href^="/accounts/settings/expires_soon/"]').contents(),  [])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/off"]').contents(),   ['Off'])

# 
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertNotRegexpMatches(r.content, r'ietf-highlight-y.*new_enough')
#         self.assertNotRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon')

    def test_settings_values_from_cookies_1(self):
        self.client.cookies = SimpleCookie({'full_draft': 'on', 'new_enough' : '90', 'expires_soon' : 7, 'left_menu': 'off', })
        r = self.client.get(urlreverse("ietf.cookies.views.preferences"))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual([], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/on"]').contents(),  ['On'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/90"]').contents(),   ['90 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/7"]').contents(), ['7 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/off"]').contents(),    ['Off'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*on')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*90 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*7 days')

    def test_settings_values_from_cookies_2(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '60', 'expires_soon' : 14, 'left_menu': 'on', })
        r = self.client.get(urlreverse("ietf.cookies.views.preferences"))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual([], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/60"]').contents(),   ['60 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(), ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/on"]').contents(),    ['On'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*60 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*14 days')
       
    def test_settings_values_from_cookies_3(self):
        self.client.cookies = SimpleCookie({'full_draft': 'on', 'new_enough' : '30', 'expires_soon' : 21, 'left_menu': 'off'})
        r = self.client.get(urlreverse("ietf.cookies.views.preferences"))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual([], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/on"]').contents(),  ['On'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/30"]').contents(),   ['30 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/21"]').contents(), ['21 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/off"]').contents(),    ['Off'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*on')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*30 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*21 days')

    def test_settings_values_from_cookies_4(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '21', 'expires_soon' : 30, 'left_menu': 'on', })
        r = self.client.get(urlreverse("ietf.cookies.views.preferences"))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual([], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/21"]').contents(),   ['21 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/30"]').contents(), ['30 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/on"]').contents(),    ['On'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*21 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*30 days')

    def test_settings_values_from_cookies_5(self):
        self.client.cookies = SimpleCookie({'full_draft': 'on', 'new_enough' : '14', 'expires_soon' : 60, 'left_menu': 'off', })
        r = self.client.get(urlreverse("ietf.cookies.views.preferences"))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual([], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/on"]').contents(),  ['On'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/60"]').contents(), ['60 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/off"]').contents(),    ['Off'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*on')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*14 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*60 days')

    def test_settings_values_from_cookies_6(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '7', 'expires_soon' : 90, 'left_menu': 'on', })
        r = self.client.get(urlreverse("ietf.cookies.views.preferences"))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual([], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/7"]').contents(),   ['7 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/90"]').contents(), ['90 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/on"]').contents(),    ['On'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*7 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*90 days')

    def test_full_draft(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 14})
        r = self.client.get(urlreverse("ietf.cookies.views.full_draft")) # no value: reset
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['full_draft'].value, '')
        self.assertListEqual(['full_draft'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(), ['14 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*14 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*14 days')

    def test_full_draft_on(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 14})
        r = self.client.get(urlreverse("ietf.cookies.views.full_draft", kwargs=dict(enabled="on")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['full_draft'].value, 'on')
        self.assertListEqual(['full_draft'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/on"]').contents(),  ['On'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*on')

    def test_full_draft_off(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 14})
        r = self.client.get(urlreverse("ietf.cookies.views.full_draft", kwargs=dict(enabled="off")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['full_draft'].value, 'off')
        self.assertListEqual(['full_draft'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
#        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
#        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(), ['14 days'])
#        self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')

    def test_full_draft_foo(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 14})
        r = self.client.get(urlreverse("ietf.cookies.views.full_draft", kwargs=dict(enabled="foo")))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual([], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
#        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
#        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(), ['14 days'])
#        self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')

    def test_left_menu(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 14, 'left_menu': 'on', })
        r = self.client.get(urlreverse("ietf.cookies.views.left_menu")) # no value: reset
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['left_menu'].value, '')
        self.assertListEqual(['left_menu'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/off"]').contents(),   ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(), ['14 days'])

    def test_left_menu_on(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 14, 'left_menu': 'off', })
        r = self.client.get(urlreverse("ietf.cookies.views.left_menu", kwargs=dict(enabled="on")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['left_menu'].value, 'on')
        self.assertListEqual(['left_menu'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/on"]').contents(),  ['On'])

    def test_left_menu_off(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 14, 'left_menu': 'off', })
        r = self.client.get(urlreverse("ietf.cookies.views.left_menu", kwargs=dict(enabled="off")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['left_menu'].value, 'off')
        self.assertListEqual(['left_menu'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/off"]').contents(),  ['Off'])

    def test_left_menu_foo(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 14, 'left_menu': 'off', })
        r = self.client.get(urlreverse("ietf.cookies.views.left_menu", kwargs=dict(enabled="foo")))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual([], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/left_menu/off"]').contents(),  ['Off'])

    def test_new_enough(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 14})
        r = self.client.get(urlreverse("ietf.cookies.views.new_enough")) # no value: reset
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['new_enough'].value, '')
        self.assertListEqual(['new_enough'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(), ['14 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*14 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*14 days')

    def test_new_enough_7(self):
        self.client.cookies = SimpleCookie({'full_draft': 'on', 'new_enough' : '14', 'expires_soon' : 21})
        r = self.client.get(urlreverse("ietf.cookies.views.new_enough", kwargs=dict(days="7")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['new_enough'].value, '7')
        self.assertListEqual(['new_enough'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/on"]').contents(),  ['On'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/7"]').contents(),   ['7 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/21"]').contents(), ['21 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*on')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*7 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*21 days')

    def test_new_enough_14(self):
        self.client.cookies = SimpleCookie({'full_draft': 'on', 'new_enough' : '7', 'expires_soon' : 99})
        r = self.client.get(urlreverse("ietf.cookies.views.new_enough", kwargs=dict(days="14")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['new_enough'].value, '14')
        self.assertListEqual(['new_enough'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/on"]').contents(),  ['On'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
        self.assertEqual(q('div a.active[href^="/accounts/settings/expires_soon/14"]').contents(), [])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*on')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*14 days')
#         self.assertNotRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon')

    def test_new_enough_21(self):
        self.client.cookies = SimpleCookie({'full_draft': 'on', 'new_enough' : '14', 'expires_soon' : 90})
        r = self.client.get(urlreverse("ietf.cookies.views.new_enough", kwargs=dict(days="21")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['new_enough'].value, '21')
        self.assertListEqual(['new_enough'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/on"]').contents(),  ['On'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/21"]').contents(),   ['21 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/90"]').contents(), ['90 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*on')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*21 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*90 days')

    def test_new_enough_30(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 7})
        r = self.client.get(urlreverse("ietf.cookies.views.new_enough", kwargs=dict(days="30")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['new_enough'].value, '30')
        self.assertListEqual(['new_enough'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/30"]').contents(),   ['30 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/7"]').contents(),  ['7 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*30 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*7 days')

    def test_new_enough_60(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '14', 'expires_soon' : 14})
        r = self.client.get(urlreverse("ietf.cookies.views.new_enough", kwargs=dict(days="60")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['new_enough'].value, '60')
        self.assertListEqual(['new_enough'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/60"]').contents(),   ['60 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(), ['14 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*60 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*14 days')

    def test_new_enough_90(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'new_enough' : '22', 'expires_soon' : 60})
        r = self.client.get(urlreverse("ietf.cookies.views.new_enough", kwargs=dict(days="90")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['new_enough'].value, '90')
        self.assertListEqual(['new_enough'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/90"]').contents(),   ['90 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/60"]').contents(), ['60 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*90 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*60 days')

    def test_expires_soon(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'expires_soon' : '14', 'new_enough' : 14})
        r = self.client.get(urlreverse("ietf.cookies.views.expires_soon")) # no value: reset
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['expires_soon'].value, '')
        self.assertListEqual(['expires_soon'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(), ['14 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*14 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*14 days')

    def test_expires_soon_7(self):
        self.client.cookies = SimpleCookie({'full_draft': 'on', 'expires_soon' : '14', 'new_enough' : 21})
        r = self.client.get(urlreverse("ietf.cookies.views.expires_soon", kwargs=dict(days="7")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['expires_soon'].value, '7')
        self.assertListEqual(['expires_soon'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/on"]').contents(),  ['On'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/21"]').contents(),   ['21 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/7"]').contents(), ['7 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*on')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*7 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*21 days')

    def test_expires_soon_14(self):
        self.client.cookies = SimpleCookie({'full_draft': 'on', 'expires_soon' : '7', 'new_enough' : 99})
        r = self.client.get(urlreverse("ietf.cookies.views.expires_soon", kwargs=dict(days="14")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['expires_soon'].value, '14')
        self.assertListEqual(['expires_soon'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/on"]').contents(),  ['On'])
        self.assertEqual(q('div a.active[href^="/accounts/settings/new_enough/"]').contents(),   [])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/14"]').contents(),['14 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*on')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*14 days')
#         self.assertNotRegexpMatches(r.content, r'ietf-highlight-y.*new_enough')

    def test_expires_soon_21(self):
        self.client.cookies = SimpleCookie({'full_draft': 'on', 'expires_soon' : '14', 'new_enough' : 90})
        r = self.client.get(urlreverse("ietf.cookies.views.expires_soon", kwargs=dict(days="21")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['expires_soon'].value, '21')
        self.assertListEqual(['expires_soon'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/on"]').contents(),  ['On'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/90"]').contents(),   ['90 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/21"]').contents(), ['21 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*on')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*21 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*90 days')

    def test_expires_soon_30(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'expires_soon' : '14', 'new_enough' : 7})
        r = self.client.get(urlreverse("ietf.cookies.views.expires_soon", kwargs=dict(days="30")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['expires_soon'].value, '30')
        self.assertListEqual(['expires_soon'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/7"]').contents(),   ['7 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/30"]').contents(), ['30 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*30 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*7 days')

    def test_expires_soon_60(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'expires_soon' : '14', 'new_enough' : 14})
        r = self.client.get(urlreverse("ietf.cookies.views.expires_soon", kwargs=dict(days="60")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['expires_soon'].value, '60')
        self.assertListEqual(['expires_soon'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/14"]').contents(),   ['14 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/60"]').contents(), ['60 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*60 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*14 days')

    def test_expires_soon_90(self):
        self.client.cookies = SimpleCookie({'full_draft': 'off', 'expires_soon' : '22', 'new_enough' : 60})
        r = self.client.get(urlreverse("ietf.cookies.views.expires_soon", kwargs=dict(days="90")))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.cookies['expires_soon'].value, '90')
        self.assertListEqual(['expires_soon'], r.cookies.keys())
        q = PyQuery(r.content)
        self.assertEqual(q('div a.active[href="/accounts/settings/full_draft/off"]').contents(),  ['Off'])
        self.assertEqual(q('div a.active[href="/accounts/settings/new_enough/60"]').contents(),   ['60 days'])
        self.assertEqual(q('div a.active[href="/accounts/settings/expires_soon/90"]').contents(), ['90 days'])
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*full_draft.*off')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*expires_soon.*90 days')
#         self.assertRegexpMatches(r.content, r'ietf-highlight-y.*new_enough.*60 days')
