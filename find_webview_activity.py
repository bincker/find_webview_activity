__author__ = 'kotz'
import xml.dom.minidom as md
import sys
import os


UNZIP_DIR = "/home/kotz/unzip/"
PROJ_DIR = '/home/kotz/unzip/'
PROJ_DIR1 = '/home/kotz/apk_zip/'
PROJ_DIR2 = '/home/kotz/apk_zip/smali/'

s = os.system('apktool d -f /home/kotz/unzip/360browser_phone.apk ./apk_zip')


#print(s)

ManFileName = os.path.join(PROJ_DIR1, "AndroidManifest.xml")
OUT = os.path.join(PROJ_DIR, "man_perms.txt")

PermElemName = 'activity'
PermAttrName = 'android:name'


PERMS = []

of = open(OUT, 'w+')
#of.write("(")

def getActivity():
    man_dom = md.parse(ManFileName)

    perms_lst = man_dom.getElementsByTagName(PermElemName)
    if perms_lst.length == 0 :
        print "empty Activity"
        #of.write(")")
        of.close()
        return
# print perms_lst
    for perm_dom in perms_lst:
        if perm_dom.hasAttribute(PermAttrName):
 # print "has"
            PERMS.append(str(perm_dom.getAttribute(PermAttrName)))
            of.write(str(perm_dom.getAttribute(PermAttrName)))
            of.write ('\n')
# of.write(")")
    of.write("\n")
    of.close()



def find_str(s_str):
    r = []
    for fname in PERMS:
        f = PROJ_DIR2 + '/'.join(fname.split('.')) + ".smali"
        #print f
        try:
            ff = open(f, 'r')
            ss = ff.read()
            ff.close()
            if s_str in ss:
                #print "Find in ",fname
                r.append(fname)
        except Exception,e:
            print e
    return r

getActivity()

#print PERMS

dd = find_str("WebView")
print dd
