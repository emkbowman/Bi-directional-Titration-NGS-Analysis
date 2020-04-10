##This code aligns the compressed NGS file to the sgRNA library-this ensures only exact matches, and results in the sgRNA name, sequence and total read counts for each file
##Code written by Cole Musselman and adapted for NGS alignment by Daniel Pogue
require 'json'
require 'fileutils'
require 'roo'



#inputs
source_filename = ARGV[0]
compare_filename = ARGV[1]

#initialize output file and vars
File.open('NGS_output_name.csv', "wb") do |file|
    file.puts "Gene Name and guide Positions|Guide|Count"
end
count = 0

source_file = Roo::Excelx.new(source_filename)
    source_file.each_row_streaming do |row|
        count = 0
        gene_name = row[0].to_s
        guide = row[1].to_s
        File.open(compare_filename, "r") do |compare_file|
            compare_file.each_line do |compare_string|
            if compare_string.to_s.include? guide
                count += compare_string.split(":")[1].to_i
            end
        end
        File.open('output.csv', "ab") do |file|
            file.puts gene_name.inspect+"|"+guide.to_s.inspect+"|"+count.to_s.inspect
        end
    end
end
