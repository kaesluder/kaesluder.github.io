# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1669781660.0723772
_enable_loop = True
_template_filename = 'themes/blogtxt/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        post = context.get('post', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        messages = context.get('messages', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        title = context.get('title', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        permalink = context.get('permalink', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def extra_head():
            return render_extra_head(context)
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        messages = context.get('messages', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        title = context.get('title', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        permalink = context.get('permalink', UNDEFINED)
        def content():
            return render_content(context)
        def sourcelink():
            return render_sourcelink(context)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="post-')
        __M_writer(str(post.meta('slug')))
        __M_writer('" class="post hfeed">\n        <h2 class="entry-title"><a href=\'')
        __M_writer(str(permalink))
        __M_writer("'>")
        __M_writer(str(title))
        __M_writer('</a></h2>\n        <div class="entry-content">\n            ')
        __M_writer(str(post.text()))
        __M_writer('\n        </div>\n        <div class="archive-meta">\n            ')
        __M_writer(str(messages("Posted:")))
        __M_writer(' <time class="published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time>\n            <span class="meta-sep">|</span>\n            ')
        __M_writer(str(pheader.html_translations(post)))
        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n                ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n            <span class="entry-tags">\n            </span>\n        </div>\n    </div>\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n')
        if not post.meta('nocomments'):
            __M_writer('        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer('\n')
        __M_writer('    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if not post.meta('password'):
            __M_writer('                <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n')
        __M_writer('            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/blogtxt/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "58": 2, "59": 3, "60": 4, "61": 5, "62": 6, "67": 13, "72": 40, "78": 7, "87": 7, "88": 8, "89": 8, "90": 9, "91": 10, "92": 10, "93": 10, "94": 12, "95": 12, "101": 14, "118": 14, "119": 15, "120": 15, "121": 16, "122": 16, "123": 16, "124": 16, "125": 18, "126": 18, "127": 21, "128": 21, "129": 21, "130": 21, "131": 21, "132": 21, "133": 23, "134": 23, "139": 28, "140": 29, "141": 29, "142": 34, "143": 34, "144": 35, "145": 36, "146": 36, "147": 36, "148": 38, "149": 38, "150": 38, "156": 24, "164": 24, "165": 25, "166": 26, "167": 26, "168": 26, "169": 26, "170": 26, "171": 28, "177": 171}}
__M_END_METADATA
"""
