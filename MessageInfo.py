class MessageInfo:
    idx = None
    nama = ''
    kelas = ''
    pesan = ''

    @staticmethod
    def setIdx(num):
        idx = num

    @staticmethod
    def getIdx():
        return idx
    
    @staticmethod
    def setNama(strNama):
        nama = strNama
    
    @staticmethod
    def getNama():
        return nama
    
    @staticmethod
    def setKelas(strKelas):
        kelas = strKelas
    
    @staticmethod
    def getKelas():
        return kelas
    
    @staticmethod
    def setPesan(strPesan):
        pesan = strPesan

    @staticmethod
    def getPesan():
        return pesan

