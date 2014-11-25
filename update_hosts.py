#!/usr/bin/python
#-*-coding:utf-8-*-

def getIp(domain):
    import socket
    domain = domain.strip("*.")
    if domain.endswith(".adobe.com"):
        print("%s:%s"%(domain,"127.0.0.1"))
        return "127.0.0.1"
    elif domain == "dl-ssl.google.com" or domain == "dl.google.com":
        print("%s:%s"%(domain,"203.208.46.200"))
        return "203.208.46.200"
    elif domain == "jdk.dev":
        print("%s:%s"%(domain,"192.168.1.8"))
        return "192.168.1.8"
    elif domain == "e7813.ca.s.tl88.net" or domain == "cdn1.evernote.com":
        print("%s:%s"%(domain,"122.228.222.49"))
        return "122.228.222.49"
    else:
        myaddr = socket.getaddrinfo(domain,'http')[0][4][0]
        print("%s:%s"%(domain,myaddr))
        return myaddr

if __name__ == "__main__":
    fp = open("hosts_template","r")
    host_lines = fp.readlines()
    fp.close()
    hosts = ""
    for line in host_lines:
        line = line.strip('\n')
        line = line.strip()
        if not line.startswith("#") and line!="":
            try:
                ip = getIp(line)
            except Exception, e:
                hosts += "127.0.0.1 " + line + "\n"
                print("error:"+line)
                print(e)
            else:
                hosts += ip + " " + line + "\n"
            finally:
                pass
    fpw = open("new_hosts","w")
    fpw.write(hosts)
    fpw.close()
    print(hosts)
    print("Write host to file: new_hosts")
