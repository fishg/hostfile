#!/usr/bin/python
#-*-coding:utf-8-*-

def getIp(domain):
    import socket
    domain = domain.strip("*.")
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
                if " " in line:
                    hosts += line + "\n"
                else:
                    ip = getIp(line)
                    hosts += ip + " " + line + "\n"
            except Exception, e:
                hosts += "0.0.0.0 " + line + "\n"
                print("error:"+line)
                print(e)
            else:
                pass
            finally:
                pass
    fpw = open("new_hosts","w")
    fpw.write(hosts)
    fpw.close()
    print(hosts)
    print("Write host to file: new_hosts")
