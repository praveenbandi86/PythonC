# This Python file uses the following encoding: utf-8
# coding=UTF-8

import json

file = open("//HOFILE04//USERS_M//T032160//Amica//Digital Marketing//mixpanel_android_01.json", 'r')
example = json.load(file)
# print(len(iterable))

def iterate_all(iterable, returned="key"):
    
    """Returns an iterator that returns all keys or values
       of a (nested) iterable.
       
       Arguments:
           - iterable: <list> or <dictionary>
           - returned: <string> "key" or "value"
           
       Returns:
           - <iterator>
    """
  
    if isinstance(iterable, dict):
        for key, value in iterable.items():
            if returned == "key":
                yield key
            elif returned == "value":
                if not (isinstance(value, dict) or isinstance(value, list)):
                    yield value
            else:
                raise ValueError("'returned' keyword only accepts 'key' or 'value'.")
            for ret in iterate_all(value, returned=returned):
                yield ret
    elif isinstance(iterable, list):
        for el in iterable:
            for ret in iterate_all(el, returned=returned):
                yield ret

# example = {'app_url': '', 'models': [{'perms': {'add': True, 'change': True, 'delete': True}, 'add_url': '/admin/cms/news/add/', 'admin_url': '/admin/cms/news/', 'name': ''}], 'has_module_perms': True, 'name': u'CMS'}

print(list(iterate_all(example, "key")))