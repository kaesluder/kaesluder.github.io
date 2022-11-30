# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1669781773.920097
_enable_loop = True
_template_filename = 'themes/blogtxt/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'belowtitle', 'content', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        license = _import_ns.get('license', context.get('license', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n<div id="wrapper">\n    <div id="container">\n        <div id="content">\n            <div id="header">\n                <h1 id="blog-title">\n                    <a href="')
        __M_writer(str(blog_url))
        __M_writer('" title="')
        __M_writer(str(blog_title))
        __M_writer('">')
        __M_writer(str(blog_title))
        __M_writer('</a>\n                </h1>\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\n            </div>\n        <div class="hfeed">\n            <!--Body content-->\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n            <!--End of body content-->\n        </div><!-- .hfeed -->\n    </div><!-- #content -->\n</div><!-- #container -->\n\n<div id="primary" class="theme_sidebar">\n    <ul>\n')
        for url, text in navigation_links[lang]:
            __M_writer('            <li><h3><a href="')
            __M_writer(str(rel_link(permalink, url)))
            __M_writer('">')
            __M_writer(str(text))
            __M_writer('</a></h3>\n            ')
            __M_writer(str(template_hooks['menu']()))
            __M_writer('\n            ')
            __M_writer(str(template_hooks['menu_alt']()))
            __M_writer('\n')
        __M_writer('        <li>')
        __M_writer(str(license))
        __M_writer('\n        <li>')
        __M_writer(str(search_form))
        __M_writer('\n    </ul>\n</div><!-- #primary .theme_sidebar -->\n\n<div id="footer">\n    <span id="theme-link"><a href="http://www.plaintxt.org/themes/blogtxt/" title="blog.txt theme for WordPress" rel="follow designer">blog.txt</a> \'theme by <span class="vcard"><a class="url fn n" href="http://scottwallick.com/" title="scottwallick.com" rel="follow designer"><span class="given-name">Scott</span><span class="additional-name"> Allan</span><span class="family-name"> Wallick</span></a></span></span>\n    <small>')
        __M_writer(str(content_footer))
        __M_writer('\n            ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n </small><p>\n</div><!-- #footer -->\n\n</div><!-- #wrapper -->\n    ')
        __M_writer(str(body_end))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context)
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('                <small>\n                    ')
            __M_writer(str(messages("Also available in:")))
            __M_writer('&nbsp;\n')
            for langname in translations.keys():
                if langname != lang:
                    __M_writer('                            <a href="')
                    __M_writer(str(_link("index", None, langname)))
                    __M_writer('">')
                    __M_writer(str(messages[langname]["LANGUAGE"]))
                    __M_writer('</a>\n')
            __M_writer('                </small>\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/blogtxt/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "58": 2, "59": 3, "60": 3, "61": 4, "62": 4, "67": 7, "68": 8, "69": 8, "70": 16, "71": 16, "72": 16, "73": 16, "74": 16, "75": 16, "80": 29, "85": 33, "86": 41, "87": 42, "88": 42, "89": 42, "90": 42, "91": 42, "92": 43, "93": 43, "94": 44, "95": 44, "96": 46, "97": 46, "98": 46, "99": 47, "100": 47, "101": 53, "102": 53, "103": 54, "104": 54, "105": 59, "106": 59, "107": 60, "108": 60, "113": 61, "114": 62, "115": 62, "121": 5, "129": 5, "135": 18, "148": 18, "149": 19, "150": 20, "151": 21, "152": 21, "153": 22, "154": 23, "155": 24, "156": 24, "157": 24, "158": 24, "159": 24, "160": 27, "161": 29, "167": 33, "180": 61, "193": 180}}
__M_END_METADATA
"""
