"""
PINNA Serveur
console.py

Created by Shota Shimazu on 2018/2/14

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of PINNA Software License, see LICENSE for detail.
https://github.com/shotastage/pinna-music/blob/master/LICENSE
"""

import inspect
import textwrap
import sys


def log(string,
            withError = False, errorDetail = None,
            withInput = False, withConfirm = False, default = None):


    if withError:

        print('\033[31mPINNA Serveur: ' + str(string) + '\033[0m')

        if not errorDetail == None:
            separator_begin = "===== Error Detail =======================================================\n"
            separator_end   = "==========================================================================\n"
            print('\033[31m' + separator_begin + errorDetail + "\n" + separator_end + '\033[0m')


    elif withInput:
        string = str(input('\033[32m' + str(string) + ' >> \033[0m'))
        
        if string == "" and default != None:
            return default
        else:
            return string

    elif withConfirm:
        print('\033[31mPINNA Serveur: ' + str(string) + '\033[0m')

        while True:
            answer = input('\033[32m' + "Please respond with yes or no [Y/N/y/n]" + ' >> \033[0m').lower()

            if answer in [ "y", "Y", "yes", "Yes", "YES", "Yeah"]:
                return True
            elif answer in [ "n", "N", "no", "No", "NO", "Nope"]:
                return False        
    else:
        print('\033[32mPINNA Serveur: \033[0m' + str(string))



def raise_error_message(func):

    try:
        errored_func = func.__name__
    except:
        errored_func = "Failed to get func information!"

    try:
        errored_obj  = str(func)
    except:
        errored_obj  = "Failed to get errored object information!"

    try:
        func_sig     = inspect.signature(func)
    except:
        func_sig     = "Failed to get functino signature!"

    try:
        exec_info    = str(sys.exc_info())
    except:
        exec_info    = "Failed to get exec info!"


    return textwrap.dedent("""
Python Information:
Exceute func name : {func_name}
Exec Information  : {exec_info}
Object Info       : {obj_inf}
Signature         : {func_signature}
    """).format(
        func_name = errored_func,
        exec_info = exec_info,
        obj_inf   = errored_obj,
        func_signature = func_sig
    ).strip()
