#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Small python script to brute force a SHA512 hash
'''

__author__ = "C4rt"
__date__ = "11/05/2013"
__version__ = "1.0"
__maintainer__ = "C4rt"
__email__ = "eric.c4rtman@gmail.com"
__status__ = "Production"

try:
    import hashlib
    import optparse
    from threading import Thread
except ImportError, err:
    raise
    print >>sys.stderr, "[X] Unable to import : %s\n" % err
    sys.exit(1)


def testPass(hashPass, word):
    try:
            hash = hashlib.sha512(word)
            hashWord = hash.hexdigest()
            if hashWord == hashPass:
                print '[+] Found Password: ' + word + '\n'
                exit(0)
    except:
        pass


def main():
    parser = optparse.OptionParser("usage%prog "+\
        "-f <hashPass> -d <dictionary>")
    parser.add_option('-f', dest='cname', type='string',\
        help='specify hashed password')
    parser.add_option('-d', dest='dname', type='string',\
        help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.cname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else :
        cname = options.cname
        dname = options.dname
    hashPass = cname
    dico = open(dname)
    for line in dico.readlines():
        word = line.strip('\n')
        t = Thread(target=testPass, args=(hashPass, word))
        t.start()

if __name__ == '__main__':
    try:
        main()
    except:
        print "\n\n\n\n", traceback.format_exc()
