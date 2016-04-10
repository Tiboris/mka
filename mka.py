#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#MKA:xdudla00
#------------------------------------------------------------------------------
import re                           # to searching by regex
import os                           # to work with filesystem
import sys                          # to get arguments
import argparse                     # to parse arguments
#------------------------------------------------------------------------------
PROG_OK  = 0
ARGS_ERR = 1
READ_ERR = 2
WRIT_ERR = 3
FORM_ERR = 60
SEMS_ERR = 61
DSKA_ERR = 62
#------------------------------FUNCTIONS---------------------------------------
#------------------------------------------------------------------------------
def check_args(): # TODO fix duplicated params
    parser = argparse.ArgumentParser(add_help=False, 
                description='Script for processing finite state machines')
    parser.add_argument('--help', help='show this help message and exit', 
                required=False, action="store_true")
    parser.add_argument('--input', required=False,
                help='if not set it takes STDIN', 
                default=sys.stdin)
    parser.add_argument('--output', required=False,
                help='if not set output will be at STDOUT', 
                default=sys.stdout)
    parser.add_argument('-m','--minimize', required=False,
                help='minimizes finite state machine', 
                action="store_true")
    parser.add_argument('-f','--find-non-finishing', required=False,
                help='find states and prints them otherwise \'0\'',
                action="store_true")
    parser.add_argument('-i','--case-insensitive', required=False, 
                help='ignoring input states strings case', 
                action="store_true")
    try :       # not working still on stderr
        args = parser.parse_args()
    except :
        print_err("", ARGS_ERR)
    if args.find_non_finishing == args.minimize and args.minimize == True :
        print_err("Wrong combination of arguments", ARGS_ERR)
    if args.help : 
        print(parser.format_help())
    return args
#------------------------------------------------------------------------------
def read_input(input_file):
    if input_file != sys.stdin :
        try:
            with open(input_file,'r') as file :
                input_file = file.read()
        except:
            print_err("Can not open file", READ_ERR)
    else :
        input_file = input_file.read()
    return input_file
#------------------------------------------------------------------------------
def empty_alphabet(alphabet): #TODO
    return True
#------------------------------------------------------------------------------
def invalid_rules(input_str,states): #TODO 
#pravidlo obsahuje stav resp. symbol, který není v množině stavů resp. vstupní abecedě,
    return True
#------------------------------------------------------------------------------
def in_states(start,states): #TODO počáteční stav nepatří do množiny stavů,
    return True
#------------------------------------------------------------------------------
def fin_states(fin_states,states): #TODO množina koncových stavů není podmnožinou množiny stavů.
    return True
#------------------------------------------------------------------------------
def valid_format(input_str): #TODO Kontrola spr8vnosti vstupu 
    return True
#------------------------------------------------------------------------------
def is_dska(M): #TODO 
# Pokud vstup nereprezentuje dobře specifikovaný konečný automat, skončí skript
# s chybou a vrátí návratový kód 62
    return True
#------------------------------------------------------------------------------
def print_err(msg,code):
    print(msg,file=sys.stderr)
    exit(code)
#------------------------------------------------------------------------------
#-----------------------------MAIN-FUNCTION------------------------------------
def main():
    args = check_args()
    if not valid_format(read_input(args.input)) :
        print_err("Input file is not in valid format", FORM_ERR)
    if not True :
        pass
    return PROG_OK
#------------------------------------------------------------------------------
if __name__ == "__main__":
    exit(main())    
#------------------------------------------------------------------------------

# -f, --find-non-finishing -> hledá neukončující stav zadaného dobře specifikovaného
# konečného automatu (automat se nevypisuje). Nalezne-li jej, bez odřádkování jej vypíše na
# výstup; jinak vypíše pouze číslici 0. (Před hledáním se provede validace na dobrou specifiko-
# vanost automatu.) Parametr nelze kombinovat s parametrem -m (resp. --minimize).

# -m, --minimize -> provede minimalizaci dobře specifikovaného konečného automatu (viz algo-
# ritmus IFJ, přednáška 11, snímek 23/35). Parametr nelze kombinovat s parametrem -f (resp.
# --find-non-finishing).

# -i, --case-insensitive -> nebude brán ohled na velikost znaků při porovnávání symbolů či
# stavů (tj. a = A, ahoj = AhOj nebo A b = a B); ve výstupu potom budou všechna velká písmena
# převedena na malá.

# bonus 
# -w, --white-char
# -r, --rules-only
# --analyze-string="retezec"
# --wsfa