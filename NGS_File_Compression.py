##This code helps reduce the file size of raw NGS data by aligning exact-match reads and obtaining a count from each one. It creates a file that should be fed directly into the ruby script.
ngs_data_file = open ("NGS_file_name.fastq", "r") ##Opens to read de-compressed raw reads file (direct this to your NGS file)

compressed_data_file = open ("compare.txt","w+") ##opens new text file to write "compressed" file to

line_num = 0

ngs_dictionary = {}

name = None
sequence = None
quality = None

for line in ngs_data_file:

  line  = line.strip()

  ##print(line.strip())
  ##line_num += 1
  ##if line_num == 20: 
    ##break

  if line[0] == "@" : 
    name = line
  elif line[0] == "+" :
    if sequence in ngs_dictionary : 
      ngs_dictionary[sequence].append((name,quality))
    else : 
      ngs_dictionary[sequence] = [(name,quality)]
    name = None
    sequence = None
    quality = None
  else : 
    if name : 
      sequence = line
    else : 
      quality = line

ngs_data_file.close()

for sequence in ngs_dictionary : 
  compressed_data_file.write("{} :  {}".format(sequence,len(ngs_dictionary[sequence])))

##print statements to check

##using @ symbol for name, if no name, it's the quality score, if have name, it's the sequence for every line starting with +, save to dictionary


