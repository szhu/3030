#!/usr/bin/env python
# coding: utf-8

SEP = '\n<!-- GAME -->\n'

def get_between_sep(fname, sep):
    with open(fname, 'rb') as f:
        contents = f.read()
    parts = contents.split(sep)
    assert len(parts) == 3
    return parts

table = {
    ' ': ' 🍫        ',
    '.': '[🌲][dead] ',
}

def make_game(fname):
    gmap = open(fname, 'rb').read()
    gmap = gmap.replace(' ', table[' '])
    gmap = gmap.replace('.', table['.'])
    return ' \n'.join(gmap.split('\n')) + '[dead]: http://github.com/%%30%30'

def main(game_fname, doc_fname):
    doc_parts = get_between_sep(doc_fname, SEP)
    game = make_game(game_fname)
    doc_parts[1] = game
    contents = SEP.join(doc_parts)
    with open(doc_fname, 'wb') as f:
        f.write(contents)
    return 0


class ProgramError(Exception):
    pass


def run():
    from sys import argv, stderr
    try:
        exit(main(*argv[1:]) or 0)
    except ProgramError, exc:
        print >> stderr, exc
    except TypeError, exc:
        if exc.message.startswith("main() takes"):
            print >> stderr, exc
        else:
            raise

if __name__ == '__main__':
    run()
