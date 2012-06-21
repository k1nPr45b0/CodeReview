#! /usr/bin/env python

####################################################################################################
# 
# - 
# Copyright (C) 2012 
# 
####################################################################################################

import Git

####################################################################################################

import os
import sys

####################################################################################################

if len(sys.argv) != 2:
    print("Give a repository path")
    sys.exit(1)

repository_path = sys.argv[1]

repository_path = os.path.expandvars(repository_path)
repository_path = os.path.abspath(repository_path)
repository_path = os.path.normpath(repository_path)

print("Repository:", repository_path)

####################################################################################################

repository = Git.Repository(repository_path)

head = repository.head
print str(head)
head.top_down_visitor(max_level=2)

####################################################################################################
# 
# End
# 
####################################################################################################