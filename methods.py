import os
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def get_sizeFolder(d):
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(d):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size
    except:            
        return total_size

def get_sizeFile(f):
    total_size = 0
    try:
        total_size = os.stat(f).st_size
        return total_size
    except:
        return total_size