#!/usr/bin/env ruby
#regular expression must match a 10 digit phone number
puts ARGV[0].scan(/\[from:(.?*)\]\s\[to:(.?*)\]\s\[flags:(.?*)\]/).join
