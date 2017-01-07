#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for the pyncrypt module."""

import os

import pytest

from src.pyncrypt import KeyStore


@pytest.fixture(scope='function')
def myks(passphrase=r'dl34bas&'):
    ks = KeyStore(passphrase, passphrase_file='.secrets_p_pytest',
                  secretsdb_file='.secrets_pytest')
    yield ks
    # teardown code
    secretfiles = [os.path.join('.secrets_p_pytest'),
                   os.path.join('.secrets_pytest')]
    for fil in secretfiles:
        if os.path.exists(fil):
            os.remove(fil)

def test_store_require_str(myks):
    mykey = 'abc123'
    myks.store('mykey', mykey)
    assert myks.require('mykey') == mykey

def test_store_require_raw_str(myks):
    mykey = r'ks82998^#^#@_?'
    myks.store('mykey', mykey)
    assert myks.require('mykey') == mykey

def test_store_require_byte_salt(myks):
    mykey = r'nvnbYGTOksdeuw98^#^#@_?'
    myks.store('mykey', mykey)
    assert myks.require('mykey') == mykey

def test_store_require_byte_key(myks):
    mykey = b'nvnbY^*!GTOkeuw9^#?'
    with pytest.raises(TypeError):
        myks.store('mykey', mykey)

def test_remove_nonexist(myks):
    """Remove non-existent key returns None"""
    mykey = r'nvnbYGTOksdeuw98^#^#@_?'
    myks.store('mykey', mykey)
    assert myks.remove('nonkey') == None

def test_remove(myks):
    mykey = r'owidn83YUG203BDdkks'
    myks.store('mykey', mykey)
    myks.remove('mykey')
    with pytest.raises(OSError):
        myks.require('mykey')  # Should force a prompt to enter a value

def test_clear(myks):
    mykey = r',cnxsk3#SDFA*()'
    myks.store('mykey', mykey)
    myks.clear()
    with pytest.raises(OSError):
        myks.require('mykey')  # Should force a prompt to enter a value

# def test_one_time_instantiation():
#     ks = myks()
#     mykey = r',cnuedbk3#DSFA(*)'
#     ks.store('mykey', mykey)
#     del ks  # delete the KeyStore object, not the filesystem files
#     newks = myks()
#     with pytest.raises(ValueError):
#         newks.require('mykey')
