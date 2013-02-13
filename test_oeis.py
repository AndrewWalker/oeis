"""Test suite for oeis.py

This code is copyright 2013 Andrew Walker
See the end of the source file for the license of use.
"""
import unittest
import oeis
import os
import tempfile

# Monkey patch the oeis query, so that we don't have to
# keep talking to the server (which is reasonably slow).

orig_raw = oeis.raw_query

def _cached_query(sequence, n=1):
    cache_hash = hash((tuple(sequence), n))
    cache_file = 'oeis_cache_%s' % str(cache_hash)
    cache_file = os.path.join(tempfile.gettempdir(), cache_file)
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as fh:
            return fh.read()
    else:
        content = orig_raw(sequence, n)
        with open(cache_file, 'w') as fh:
            fh.write(content)
        return content

oeis.raw_query = _cached_query

class TestOEIS(unittest.TestCase):
    def setUp(self):
        self.seq = [1, 2, 3, 4]
        self.n = 5

    def test_split(self):
        content = oeis.raw_query(self.seq, self.n)
        blks = oeis.split_blocks(content)
        self.assertTrue(len(blks) <= self.n)

    def test_names(self):
        seqs = oeis.query(self.seq, self.n)
        self.assertEquals(seqs[0].id, 'A000027')
        self.assertEquals(seqs[1].id, 'A007953')
        self.assertEquals(seqs[2].id, 'A001477')
        self.assertEquals(seqs[3].id, 'A000961')
        self.assertEquals(seqs[4].id, 'A004086')

    def test_sequences(self):
        seqs = oeis.query(self.seq, self.n)
        self.assertEquals(seqs[0].sequence[0], 1)
        self.assertEquals(seqs[0].sequence[-1], 26)
        self.assertEquals(seqs[3].sequence[0], 1)
        self.assertEquals(seqs[3].sequence[-1], 53)


# Copyright (c) 2012 Andrew Walker <walker.ab@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# vim: set filetype=python ts=4 sw=4 et si tw=75
