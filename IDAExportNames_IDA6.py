import idaapi
import idautils
import idc

def GetFilePath():
    return "C:\\Games\\SkyrimMods\\RETools\\Data\\"
    
def IsUserName(ea):
    # has_user_name since IDA 7.0
    return idc.hasUserName(idc.GetFlags(ea))

def GetStr(num):
    return "%X" % num

print "Beginning export\n"

handle = open(GetFilePath() + "idanames.txt", "w")
handle.truncate()
for key, value in Names():
    if IsUserName(key) != True:
        continue
    handle.write(GetStr(key))
    handle.write("\t")
    handle.write(value)
    handle.write("\t")
    name_str = Demangle(value, GetLongPrm(INF_SHORT_DN))
    if name_str:
        handle.write(name_str)
    handle.write("\n")
handle.close()

print "Done with export\n"