
import os
files = os.listdir('./blog')

for f in sorted(files, reverse=True):
    name = f[:-3]
    print f
    #print '[' + name + ']' + '(blog/' + f + ')' + '<br><br>'
