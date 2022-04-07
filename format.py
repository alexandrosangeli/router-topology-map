import os
import re

isIPv4 = lambda x: True if re.search("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$", x) else False

isIPv6 = lambda x: True if re.search("(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))", x) else False

def format(f, v):
    print("modifying " + f)
    with open(f"traceroute_out/{v}/{f}", "r") as f1:
        with open(f"traceroute_out/{v}/formatted/{f}" + "_f", "w") as f2:
            prev = ""
            for line in f1.readlines()[1:]:
                if line == "":
                    continue
                if line.strip()[-1] != '*':
                    lst = line.split(" ")
                    lst = [x for x in lst if x != ""]
                    if prev:
                        out = '"' + prev + '" -- "' + lst[1] + '"\n' 
                        f2.write(out)
                        prev = lst[1]
                    else:
                        prev = lst[1]


def main():

    files4 = list(filter(isIPv4, os.listdir("traceroute_out/v4/")))
    files6 = list(filter(isIPv6, os.listdir("traceroute_out/v6/")))

    for f in files4:
        format(f, "v4")

    for f in files6:
        format(f, "v6")

    
main()