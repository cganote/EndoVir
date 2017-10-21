#  flanker.py
#
#  Author: Jan Piotr Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0.0

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../'))
import lib.fasta.parser

class Flanker(lib.fasta.parser.FastaParser):

  def __init__(self, flank_len=500):
    super().__init__()
    self.len_flank = flank_len
    self.lhs_count = 0
    self.rhs_count = 0

  def add_sequence(self, seq, stream=False):
    if seq.length <= self.len_flank:
      seq.name += "_lhs"
      self.sequences[seq.hader] = (seq)
      self.lhs_count += 1
      if stream == True:
        return seq.get_sequence()
    else:
      subseql = seq.subseq(0, self.len_flank, seq.name+"_lhs")
      self.sequences[subseql.header] = subseql
      self.lhs_count += 1
      subseqr = seq.subseq(seq.length-self.len_flank, self.len_flank, seq.name+"_rhs")
      self.sequences[subseqr.header] = subseqr
      self.rhs_count += 1
      if stream == True:
        return subseql.get_sequence() + subseqr.get_sequence()
