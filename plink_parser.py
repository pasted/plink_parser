from pprint import pprint
import argparse, csv, string
import multiprocessing as mp

class PlinkAssoc(object):
   def __init__(self, row):
      self.rsid = row['SNP']
      self.chr = row['CHR']
      self.position = row['BP']
      self.effect_allele = row['A1']
      self.test_type = row['TEST']
      self.number_missing = row['NMISS']
      self.odds_ratio = row['OR']
      self.standard_error = row['SE']
      self.upper_95_ci = row['U95']
      self.lower_95_ci = row['L95']
      self.stat = row['STAT']
      self.p_value = row['P']

def process_wrapper(chunk_start, chunk_size, file_name):
   with open(file_name) as f:
      f.seek(chunk_start)
      lines = f.read(chunk_size).splitlines()
      for line in lines:
         process(line)

def chunkify(file_name, size=1024*1024):
   file_end = os.pth.getsize(file_name)
   with open(file_name, 'r') as f:
      chunk_end = f.tell()
   while True:
      chunk_start = chunk_end
      f.seek(size, 1)
      f.readline()
      chunk_end = f.tell()
      yield chunk_start, chunk_end - chunk_start
      if chunk_end > file_end:
         break
