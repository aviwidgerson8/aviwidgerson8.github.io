# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1567900197.1358724
_enable_loop = True
_template_filename = 'themes/custom/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content_header', 'extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('archive_nav', context._clean_inheritance_tokens(), templateuri='archive_navigation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'archive_nav')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def content_header():
            return render_content_header(context)
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        def content():
            return render_content(context)
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        def content_header():
            return render_content_header(context)
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        __M_writer('<div class="row">\n<div class="col-md-12 blog-main">\n<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('" itemscope="itemscope" itemtype="http://schema.org/Article">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
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
                __M_writer('\n                    <time class="dt-updated" datetime="')
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
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('</div>\n</div>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"258": 252, "23": 2, "26": 3, "29": 4, "32": 6, "35": 5, "38": 7, "44": 0, "80": 2, "81": 3, "82": 4, "83": 5, "84": 6, "85": 7, "86": 8, "91": 16, "96": 72, "102": 19, "113": 19, "114": 20, "115": 20, "121": 10, "135": 10, "136": 11, "137": 11, "138": 12, "139": 13, "140": 13, "141": 13, "142": 15, "143": 15, "144": 15, "150": 18, "180": 18, "185": 21, "186": 22, "187": 23, "188": 23, "189": 23, "190": 25, "191": 28, "192": 29, "193": 29, "194": 29, "195": 31, "196": 31, "197": 31, "198": 31, "199": 34, "200": 35, "201": 35, "202": 35, "203": 35, "204": 35, "205": 36, "206": 37, "207": 37, "208": 37, "209": 39, "210": 41, "211": 41, "212": 42, "213": 42, "214": 42, "215": 42, "216": 42, "217": 42, "218": 43, "219": 44, "220": 44, "221": 44, "222": 45, "223": 45, "224": 45, "225": 45, "226": 45, "227": 45, "228": 47, "229": 49, "230": 50, "231": 50, "232": 50, "233": 52, "234": 54, "235": 55, "236": 56, "237": 56, "238": 57, "239": 58, "240": 59, "241": 59, "242": 61, "243": 64, "244": 65, "245": 66, "246": 66, "247": 66, "248": 68, "249": 70, "250": 70, "251": 71, "252": 71}, "uri": "index.tmpl", "filename": "themes/custom/templates/index.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
