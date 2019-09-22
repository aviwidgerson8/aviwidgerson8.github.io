# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569160587.8224988
_enable_loop = True
_template_filename = '/home/random8dots/site/lib/python3.5/site-packages/nikola/data/themes/bootstrap4/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_stylesheets', 'html_translations', 'html_headstart', 'html_feedlinks', 'late_load_js', 'html_navigation_links', 'html_navigation_links_entries']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\n        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.11.0/baguetteBox.min.css" integrity="sha256-cKiyvRKpm8RaTdU71Oq2RUVgvfWrdIXjvVdQF2oZ1Y4=" crossorigin="anonymous" />\n')
        if use_bundles and use_cdn:
            __M_writer('        <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
        elif use_bundles:
            __M_writer('        <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if not use_cdn:
                __M_writer('            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n            <link href="/assets/css/baguetteBox.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li class="nav-item"><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('" class="nav-link">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        nextlink = context.get('nextlink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        permalink = context.get('permalink', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        title = context.get('title', UNDEFINED)
        meta_generator_tag = context.get('meta_generator_tag', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        __M_writer("prefix='")
        __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article#\n')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb# ')
        __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width, initial-scale=1">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n')
        if meta_generator_tag:
            __M_writer('    <meta name="generator" content="Nikola (getnikola.com)">\n')
        __M_writer('    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_atom = context.get('generate_atom', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        date_fanciness = context.get('date_fanciness', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha256-ZvOgfh+ptkpoa2Y4HkRY28ir89u/+VRyDE7sB7hEEcI=" crossorigin="anonymous"></script>\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.11.0/baguetteBox.min.js" integrity="sha256-yQGjQhFs3LtyiN5hhr3k9s9TWZOh/RzCkD3gwwCKlkg=" crossorigin="anonymous"></script>\n')
        if use_bundles and use_cdn:
            __M_writer('        <script src="/assets/js/all.js"></script>\n')
        elif use_bundles:
            __M_writer('        <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if not use_cdn:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/popper.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/baguetteBox.min.js"></script>\n')
        if date_fanciness != 0:
            if use_cdn:
                __M_writer('            <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment-with-locales.min.js" integrity="sha256-AdQN98MVZs44Eq2yTwtoKufhnU+uZ7v2kXnD5vqzZVo=" crossorigin="anonymous"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/moment-with-locales.min.js"></script>\n')
            if not use_bundles:
                __M_writer('            <script src="/assets/js/fancydates.min.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        navigation_links = context.get('navigation_links', UNDEFINED)
        def html_navigation_links_entries(navigation_links_source):
            return render_html_navigation_links_entries(context,navigation_links_source)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(html_navigation_links_entries(navigation_links)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links_entries(context,navigation_links_source):
    __M_caller = context.caller_stack._push_frame()
    try:
        permalink = context.get('permalink', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links_source[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li class="nav-item dropdown"><a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
                __M_writer(str(text))
                __M_writer('</a>\n            <div class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <a href="')
                        __M_writer(str(permalink))
                        __M_writer('" class="dropdown-item active">')
                        __M_writer(str(text))
                        __M_writer(' <span class="sr-only">')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a>\n')
                    else:
                        __M_writer('                    <a href="')
                        __M_writer(str(suburl))
                        __M_writer('" class="dropdown-item">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                __M_writer('            </div>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="nav-item active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('" class="nav-link">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a>\n')
                else:
                    __M_writer('                <li class="nav-item"><a href="')
                    __M_writer(str(url))
                    __M_writer('" class="nav-link">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base_helper.tmpl", "filename": "/home/random8dots/site/lib/python3.5/site-packages/nikola/data/themes/bootstrap4/templates/base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 62, "22": 94, "23": 122, "24": 126, "25": 149, "26": 172, "27": 180, "33": 97, "41": 97, "42": 98, "43": 99, "44": 102, "45": 103, "46": 104, "47": 105, "48": 106, "49": 107, "50": 108, "51": 111, "52": 114, "53": 115, "54": 118, "55": 119, "61": 174, "71": 174, "72": 175, "73": 176, "74": 177, "75": 177, "76": 177, "77": 177, "78": 177, "79": 177, "80": 177, "86": 2, "113": 2, "114": 6, "115": 7, "116": 8, "117": 9, "118": 11, "119": 12, "120": 13, "121": 16, "122": 16, "123": 16, "124": 19, "125": 20, "126": 20, "127": 20, "128": 22, "129": 23, "130": 24, "131": 24, "132": 24, "133": 25, "134": 26, "135": 26, "136": 26, "137": 26, "138": 26, "139": 28, "140": 29, "141": 29, "142": 30, "143": 30, "144": 31, "145": 32, "146": 34, "147": 34, "148": 34, "149": 35, "150": 35, "151": 37, "152": 38, "153": 39, "154": 39, "155": 39, "156": 39, "157": 39, "158": 39, "159": 39, "160": 42, "161": 43, "162": 44, "163": 44, "164": 44, "165": 46, "166": 47, "167": 48, "168": 48, "169": 48, "170": 50, "171": 51, "172": 51, "173": 51, "174": 53, "175": 54, "176": 54, "177": 55, "178": 56, "179": 57, "180": 58, "181": 58, "182": 58, "183": 60, "184": 61, "185": 61, "191": 151, "202": 151, "203": 152, "204": 153, "205": 153, "206": 153, "207": 154, "208": 155, "209": 156, "210": 157, "211": 157, "212": 157, "213": 157, "214": 157, "215": 159, "216": 160, "217": 160, "218": 160, "219": 163, "220": 164, "221": 165, "222": 166, "223": 166, "224": 166, "225": 166, "226": 166, "227": 168, "228": 169, "229": 169, "230": 169, "236": 64, "244": 64, "245": 65, "246": 66, "247": 71, "248": 72, "249": 73, "250": 74, "251": 75, "252": 76, "253": 77, "254": 83, "255": 84, "256": 85, "257": 86, "258": 87, "259": 89, "260": 90, "261": 93, "262": 93, "263": 93, "269": 124, "276": 124, "277": 125, "278": 125, "284": 128, "294": 128, "295": 129, "296": 130, "297": 131, "298": 131, "299": 131, "300": 133, "301": 134, "302": 135, "303": 135, "304": 135, "305": 135, "306": 135, "307": 135, "308": 135, "309": 136, "310": 137, "311": 137, "312": 137, "313": 137, "314": 137, "315": 140, "316": 141, "317": 142, "318": 143, "319": 143, "320": 143, "321": 143, "322": 143, "323": 143, "324": 143, "325": 144, "326": 145, "327": 145, "328": 145, "329": 145, "330": 145, "336": 330}}
__M_END_METADATA
"""
