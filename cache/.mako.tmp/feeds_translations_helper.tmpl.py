# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1570044476.6096184
_enable_loop = True
_template_filename = '/home/nudginghead/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl'
_template_uri = 'feeds_translations_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['_head_feed_link', '_html_feed_link', 'feed_link', '_head_atom', 'translation_link', '_html_translation_link', '_head_rss', 'head']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <link rel="alternate" type="')
            __M_writer(str(link_type))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(link_name)))
            __M_writer(' (')
            __M_writer(str(language))
            __M_writer(')" hreflang="')
            __M_writer(str(language))
            __M_writer('" href="')
            __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
            __M_writer('">\n')
        else:
            __M_writer('        <link rel="alternate" type="')
            __M_writer(str(link_type))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(link_name)))
            __M_writer('" hreflang="')
            __M_writer(str(language))
            __M_writer('" href="')
            __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__html_feed_link(context,link_type,link_name,link_postfix,classification,kind,language,name=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            if name and kind != "archive" and kind != "author":
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer(' (')
                __M_writer(filters.html_escape(str(name)))
                __M_writer(', ')
                __M_writer(str(language))
                __M_writer(')</a>\n')
            else:
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')</a>\n')
        else:
            if name and kind != "archive" and kind != "author":
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer(' (')
                __M_writer(filters.html_escape(str(name)))
                __M_writer(')</a>\n')
            else:
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_feed_link(context,classification,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _html_feed_link(link_type,link_name,link_postfix,classification,kind,language,name=None):
            return render__html_feed_link(context,link_type,link_name,link_postfix,classification,kind,language,name)
        generate_atom = context.get('generate_atom', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if generate_atom or generate_rss:
            if len(translations) > 1 and has_other_languages and kind != 'index':
                for language, classification, name in all_languages:
                    __M_writer('                <p class="feedlink">\n')
                    if generate_atom:
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/atom+xml', 'Atom feed', 'atom', classification, kind, language, name)))
                        __M_writer('\n')
                    if generate_rss and kind != 'archive':
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/rss+xml', 'RSS feed', 'rss', classification, kind, language, name)))
                        __M_writer('\n')
                    __M_writer('                </p>\n')
            else:
                for language in sorted(translations):
                    __M_writer('                <p class="feedlink">\n')
                    if generate_atom:
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/atom+xml', 'Atom feed', 'atom', classification, kind, language)))
                        __M_writer('\n')
                    if generate_rss and kind != 'archive':
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/rss+xml', 'RSS feed', 'rss', classification, kind, language)))
                        __M_writer('\n')
                    __M_writer('                </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__head_atom(context,classification=None,kind='index'):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _head_feed_link(link_type,link_name,link_postfix,classification,kind,language):
            return render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language)
        generate_atom = context.get('generate_atom', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if generate_atom:
            if len(translations) > 1 and has_other_languages and classification and kind != 'index':
                for language, classification, name in all_languages:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom for ')
                    __M_writer(str(kind))
                    __M_writer(' ')
                    __M_writer(filters.html_escape(str(name)))
                    __M_writer(' (')
                    __M_writer(str(language))
                    __M_writer(')" hreflang="')
                    __M_writer(str(language))
                    __M_writer('" href="')
                    __M_writer(str(_link(kind + "_atom", classification, language)))
                    __M_writer('">\n')
            else:
                for language in sorted(translations):
                    if (classification or classification == '') and kind != 'index':
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/atom+xml', 'Atom for ' + kind + ' ' + classification, 'atom', classification, kind, language)))
                        __M_writer('\n')
                    else:
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/atom+xml', 'Atom', 'atom', classification, 'index', language)))
                        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_translation_link(context,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        def _html_translation_link(classification,kind,language,name=None):
            return render__html_translation_link(context,classification,kind,language,name)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if has_other_languages and other_languages:
            __M_writer('        <div class="translationslist translations">\n            <h3 class="translationslist-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for language, classification, name in other_languages:
                __M_writer('            <p>')
                __M_writer(str(_html_translation_link(classification, kind, language, name)))
                __M_writer('</p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__html_translation_link(context,classification,kind,language,name=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if name and kind != "archive" and kind != "author":
            __M_writer('        <a href="')
            __M_writer(str(_link(kind, classification, language)))
            __M_writer('" hreflang="')
            __M_writer(str(language))
            __M_writer('" rel="alternate">')
            __M_writer(str(messages("LANGUAGE", language)))
            __M_writer(' (')
            __M_writer(filters.html_escape(str(name)))
            __M_writer(')</a>\n')
        else:
            __M_writer('        <a href="')
            __M_writer(str(_link(kind, classification, language)))
            __M_writer('" hreflang="')
            __M_writer(str(language))
            __M_writer('" rel="alternate">')
            __M_writer(str(messages("LANGUAGE", language)))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__head_rss(context,classification=None,kind='index',rss_override=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _head_feed_link(link_type,link_name,link_postfix,classification,kind,language):
            return render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language)
        rss_link = context.get('rss_link', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link and rss_override:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        if generate_rss and not (rss_link and rss_override) and kind != 'archive':
            if len(translations) > 1 and has_other_languages and classification and kind != 'index':
                for language, classification, name in all_languages:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS for ')
                    __M_writer(str(kind))
                    __M_writer(' ')
                    __M_writer(filters.html_escape(str(name)))
                    __M_writer(' (')
                    __M_writer(str(language))
                    __M_writer(')" hreflang="')
                    __M_writer(str(language))
                    __M_writer('" href="')
                    __M_writer(str(_link(kind + "_rss", classification, language)))
                    __M_writer('">\n')
            else:
                for language in sorted(translations):
                    if (classification or classification == '') and kind != 'index':
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/rss+xml', 'RSS for ' + kind + ' ' + classification, 'rss', classification, kind, language)))
                        __M_writer('\n')
                    else:
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/rss+xml', 'RSS', 'rss', classification, 'index', language)))
                        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,classification=None,kind='index',feeds=True,other=True,rss_override=True,has_no_feeds=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _head_rss(classification=None,kind='index',rss_override=True):
            return render__head_rss(context,classification,kind,rss_override)
        _link = context.get('_link', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        def _head_atom(classification=None,kind='index'):
            return render__head_atom(context,classification,kind)
        other_languages = context.get('other_languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if feeds and not has_no_feeds:
            __M_writer('        ')
            __M_writer(str(_head_rss(classification, 'index' if (kind == 'archive' and rss_override) else kind, rss_override)))
            __M_writer('\n        ')
            __M_writer(str(_head_atom(classification, kind)))
            __M_writer('\n')
        if other and has_other_languages and other_languages:
            for language, classification, _ in other_languages:
                __M_writer('            <link rel="alternate" hreflang="')
                __M_writer(str(language))
                __M_writer('" href="')
                __M_writer(str(_link(kind, classification, language)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "feeds_translations_helper.tmpl", "filename": "/home/nudginghead/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 9, "23": 25, "24": 33, "25": 54, "26": 72, "27": 85, "28": 113, "29": 124, "35": 3, "42": 3, "43": 4, "44": 5, "45": 5, "46": 5, "47": 5, "48": 5, "49": 5, "50": 5, "51": 5, "52": 5, "53": 5, "54": 5, "55": 6, "56": 7, "57": 7, "58": 7, "59": 7, "60": 7, "61": 7, "62": 7, "63": 7, "64": 7, "70": 11, "78": 11, "79": 12, "80": 13, "81": 14, "82": 14, "83": 14, "84": 14, "85": 14, "86": 14, "87": 14, "88": 14, "89": 14, "90": 14, "91": 14, "92": 14, "93": 14, "94": 15, "95": 16, "96": 16, "97": 16, "98": 16, "99": 16, "100": 16, "101": 16, "102": 16, "103": 16, "104": 16, "105": 16, "106": 18, "107": 19, "108": 20, "109": 20, "110": 20, "111": 20, "112": 20, "113": 20, "114": 20, "115": 20, "116": 20, "117": 20, "118": 20, "119": 21, "120": 22, "121": 22, "122": 22, "123": 22, "124": 22, "125": 22, "126": 22, "127": 22, "128": 22, "134": 87, "147": 87, "148": 88, "149": 89, "150": 90, "151": 91, "152": 92, "153": 93, "154": 93, "155": 93, "156": 95, "157": 96, "158": 96, "159": 96, "160": 98, "161": 100, "162": 101, "163": 102, "164": 103, "165": 104, "166": 104, "167": 104, "168": 106, "169": 107, "170": 107, "171": 107, "172": 109, "178": 56, "191": 56, "192": 57, "193": 58, "194": 59, "195": 60, "196": 60, "197": 60, "198": 60, "199": 60, "200": 60, "201": 60, "202": 60, "203": 60, "204": 60, "205": 60, "206": 62, "207": 63, "208": 64, "209": 65, "210": 65, "211": 65, "212": 66, "213": 67, "214": 67, "215": 67, "221": 115, "230": 115, "231": 116, "232": 117, "233": 118, "234": 118, "235": 119, "236": 120, "237": 120, "238": 120, "239": 122, "245": 27, "251": 27, "252": 28, "253": 29, "254": 29, "255": 29, "256": 29, "257": 29, "258": 29, "259": 29, "260": 29, "261": 29, "262": 30, "263": 31, "264": 31, "265": 31, "266": 31, "267": 31, "268": 31, "269": 31, "275": 35, "289": 35, "290": 36, "291": 37, "292": 37, "293": 37, "294": 39, "295": 40, "296": 41, "297": 42, "298": 42, "299": 42, "300": 42, "301": 42, "302": 42, "303": 42, "304": 42, "305": 42, "306": 42, "307": 42, "308": 44, "309": 45, "310": 46, "311": 47, "312": 47, "313": 47, "314": 48, "315": 49, "316": 49, "317": 49, "323": 75, "334": 75, "335": 76, "336": 77, "337": 77, "338": 77, "339": 78, "340": 78, "341": 80, "342": 81, "343": 82, "344": 82, "345": 82, "346": 82, "347": 82, "353": 347}}
__M_END_METADATA
"""
