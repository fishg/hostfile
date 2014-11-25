hostfile
========

严格来讲这不是一个hosts文件,这是用来给极路由的hosts插件用的,支持通配符,比如: *.twitter.com  
用来访问配合极路由的VPN智能模式,加速google\twitter\facebook访问.主要是通过以下两点改善速度:  
1. 常用国外网站的DNS解析速度
2. 如果有国内ip使用国内ip替换

适合国内极路由用户使用:  
1.屏蔽部分广告，如部分百度推广  
2.加速google部分资源载入（部分使用国内ip） 
3.印象笔记更新使用国内CDN  

ip更新方式:   

``python update_hosts.py``

脚本最好在海外vps上运行获得新的new_hosts文件，本地运行确保dns走的vpn线路,用自己使用的vpn获取ip理论上能得到你的vpn能最快访问的ip.

