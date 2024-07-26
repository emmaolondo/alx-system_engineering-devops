#!/usr/bin/env ruby
# Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/(hbt{1,}n)/).join
