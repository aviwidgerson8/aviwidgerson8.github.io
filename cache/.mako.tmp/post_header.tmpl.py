# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569138391.2543635
_enable_loop = True
_template_filename = '/home/random8dots/site/lib/python3.5/site-packages/nikola/data/themes/base/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_title', 'html_sourcelink', 'html_post_header', 'html_translations']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

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
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        <p class="sourceline"><a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" class="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        def html_translations(post):
            return render_html_translations(context,post)
        messages = context.get('messages', UNDEFINED)
        def html_title():
            return render_html_title(context)
        comments = _mako_get_namespace(context, 'comments')
        _link = context.get('_link', UNDEFINED)
        post = context.get('post', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <header>\n        ')
        __M_writer(str(html_title()))
        __M_writer('\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
        if author_pages_generated:
            __M_writer('                    <a href="')
            __M_writer(str(_link('author', post.author())))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('</a>\n')
        else:
            __M_writer('                    ')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('\n')
        __M_writer('            </span></p>\n            <p class="dateline">\n            <a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark">\n            <time class="published dt-published" datetime="')
        __M_writer(str(post.formatted_date('webiso')))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('">')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('</time>\n')
        if post.updated and post.updated != post.date:
            __M_writer('                <span class="updated"> (')
            __M_writer(str(messages("updated")))
            __M_writer('\n                    <time class="updated dt-updated" datetime="')
            __M_writer(str(post.formatted_updated('webiso')))
            __M_writer('" itemprop="dateUpdated" title="')
            __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
            __M_writer('</time>)</span>\n')
        __M_writer('            </a>\n            </p>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('                <p class="commentline">')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('\n')
        __M_writer('            ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\n')
        if post.meta('link'):
            __M_writer('                    <p class="linkline"><a href="')
            __M_writer(str(post.meta('link')))
            __M_writer('">')
            __M_writer(str(messages("Original site")))
            __M_writer('</a></p>\n')
        __M_writer('        </div>\n        ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(post.translated_to) > 1:
            __M_writer('        <div class="metadata posttranslations translations">\n            <h3 class="posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"23": 3, "26": 2, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 60, "45": 5, "51": 5, "52": 6, "53": 7, "54": 7, "55": 7, "56": 7, "57": 7, "63": 24, "70": 24, "71": 25, "72": 26, "73": 26, "74": 26, "75": 26, "76": 26, "82": 30, "99": 30, "100": 32, "101": 32, "102": 35, "103": 36, "104": 36, "105": 36, "106": 36, "107": 36, "108": 37, "109": 38, "110": 38, "111": 38, "112": 40, "113": 42, "114": 42, "115": 43, "116": 43, "117": 43, "118": 43, "119": 43, "120": 43, "121": 44, "122": 45, "123": 45, "124": 45, "125": 46, "126": 46, "127": 46, "128": 46, "129": 46, "130": 46, "131": 48, "132": 50, "133": 51, "134": 51, "135": 51, "136": 53, "137": 53, "138": 53, "139": 54, "140": 55, "141": 55, "142": 55, "143": 55, "144": 55, "145": 57, "146": 58, "147": 58, "153": 11, "162": 11, "163": 12, "164": 13, "165": 14, "166": 14, "167": 15, "168": 16, "169": 17, "170": 17, "171": 17, "172": 17, "173": 17, "174": 17, "175": 17, "176": 20, "182": 176}, "uri": "post_header.tmpl", "source_encoding": "utf-8", "filename": "/home/random8dots/site/lib/python3.5/site-packages/nikola/data/themes/base/templates/post_header.tmpl"}
__M_END_METADATA
"""
