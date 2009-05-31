#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright © 2009 Pierre Raybaut
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#    
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
Simple formlayout example

Please take a look at formlayout.py for more examples
(at the end of the script, after the 'if __name__ == "__main__":' line)
"""

from formlayout import fedit

def create_datalist_example():
    return [('str', 'this is a string'),
            ('list', [0, '1', '3', '4']),
            ('list2', ['--', ('none', 'None'), ('--', 'Dashed'),
                       ('-.', 'DashDot'), ('-', 'Solid'),
                       ('steps', 'Steps'), (':', 'Dotted')]),
            ('float', 1.2),
            (None, 'Other:'),
            ('int', 12),
            ('color', '#123409'),
            ('bool', True),
            ]
    
def create_datagroup_example():
    datalist = create_datalist_example()
    return ((datalist, "Category 1", "Category 1 comment"),
            (datalist, "Category 2", "Category 2 comment"),
            (datalist, "Category 3", "Category 3 comment"))

#--------- datalist example
datalist = create_datalist_example()
print "result:", fedit(datalist, title="Example",
                       comment="This is just an <b>example</b>.")

#--------- datagroup example
datagroup = create_datagroup_example()
print "result:", fedit(datagroup, "Global title")
    
#--------- datagroup inside a datagroup example
datalist = create_datalist_example()
datagroup = create_datagroup_example()
print "result:", fedit(((datagroup, "Title 1", "Tab 1 comment"),
                        (datalist, "Title 2", "Tab 2 comment"),
                        (datalist, "Title 3", "Tab 3 comment")),
                        "Global title")
