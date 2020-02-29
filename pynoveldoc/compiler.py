from rbnf_rts.routine import DQString
from rbnf_rts.rts import Tokens, State
from pynoveldoc import docast
from pynoveldoc.grammar import run_lexer, mk_parser
from prettyprinter import pprint, install_extras

ctx = {'Str': DQString}
co = mk_parser.__code__
requires = co.co_varnames[:co.co_argcount]

for each in requires:
    if each not in ctx:
        ctx[each] = getattr(docast, each)


parse = mk_parser(**ctx)

tokens = list(run_lexer("<current file>", r"""
Story Start

SET lfkdsk = 100  
SET v = "lfkdsk"

SAY 「lfkdsklfkdskfuck 」

# comment test

A SAY 「dsk」
A [Angry] SAY 「dsk」

START STORY novel1
END novel1

> BGMStop
> BGM Eff.music 

Choice :
「1.」  -> 「novel1」
「2.」  -> 「novel2」
「3.」  -> 「novel3」

- []
+ []
+ [ A ]
+ [ A, B, C ]

[] -> Hello
[ A ] -> Hello 

===== Chapter One =====

Story End

"""))

pprint(tokens)
install_extras(exclude=['django', 'ipython'])
got = parse(State(), Tokens(tokens))
pprint(got)
