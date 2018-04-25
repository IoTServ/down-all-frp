if __name__ == '__main__':
    def downloadFile(url,path):
        import os, urllib
        def Schedule(a, b, c):
            per = 100.0 * a * b / c
            if per > 100:
                per = 100
            print('%.2f% %' % per)

        filename = url.split("/")[-1]
        local = os.path.join(path, filename)
        urllib.urlretrieve(url, local, Schedule)


    def mkdir(path):
        import os
        path = path.strip()
        path = path.rstrip("\\")
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)

    version = ["0.17.0","0.16.1","0.16.0","0.15.1","0.15.0","0.14.1","0.13.0","0.12.0","0.11.0","0.10.0","0.9.3","0.8.1"]
    arch = ["darwin_amd64","freebsd_386","freebsd_amd64","linux_386","linux_amd64",
      "linux_arm","linux_mips","linux_mips64","linux_mips64le","linux_mipsle","windows_386","windows_amd64"]
    for v in version:
        mkdir(v)
        for a in arch:
            if "windows" in a:
                url = "https://github.com/fatedier/frp/releases/download/v%s/frp_%s_%s.zip"%(v,v,a)
            else:
                url = "https://github.com/fatedier/frp/releases/download/v%s/frp_%s_%s.tar.gz" % (v, v, a)
            print url
            downloadFile(url,v)

    print("download complete!")