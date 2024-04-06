class gps(object):
    def __init__(self,uart):
        self.uart=uart
        self.gps=False
        self.speed=False
        self.jd=False
        self.Lat = False
        self.Tn=False
        self.Lng = False
        self.Gn=False
        self.date=False
        self.year=False
        self.month=False
        self.day=False
    def gll(self):
        i=self.uart.readline()
        try:
            if i.startswith(b"$GNGLL"):
                line = str(i).split(',')
                if (len(line[1][:2])!=0 and len(line[1][2:])!=0):
                    self.Lat = float(line[1][:2])+float(line[1][2:])/60
                    self.Tn=line[2]
                    self.Lng = float(line[3][:3])+float(line[3][3:])/60
                    self.Gn=line[4]
                    self.hh=line[5][0:2]
                    self.mm=line[5][2:4]
                    self.ss=line[5][4:6]
                    self.gps=[self.Lat,self.Tn,self.Lng,self.Gn,[self.hh,self.mm,self.ss]]
                    return self.gps
            else:
                return False
        except:
            return False
    def rmc(self):
        i=self.uart.readline()
        try:
            if i.startswith(b"$GNRMC"):
                line = str(i).split(',')
                if len(line)==14:
                    return self.info(line)
                elif len(line)>=7:
                    return self.info_gps(line)
            return False
        except:
            return False
    def info(self,line):
        self.hh=line[1][0:2]
        self.mm=line[1][2:4]
        self.ss=line[1][4:6]
        self.Lat = float(line[3][:2])+float(line[3][2:])/60
        self.Tn=line[2]
        self.Lng = float(line[5][:3])+float(line[5][3:])/60
        self.Gn=line[4]
        self.gps=[self.Lat,self.Tn,self.Lng,self.Gn,(self.hh,self.mm,self.ss)]
        self.speed=float(line[7])*1.852
        self.date=[line[9][4:6],line[9][2:4],line[9][0:2]]
        self.jd=line[8]
        self.year=line[9][4:6]
        self.month=line[9][2:4]
        self.day=line[9][0:2]
        return [self.Lat,self.Tn,self.Lng,self.Gn,[self.hh,self.mm,self.ss],[self.year,self.month,self.day],self.speed,self.jd]
    def info_gps(self,line):
        self.hh=line[1][0:2]
        self.mm=line[1][2:4]
        self.ss=line[1][4:6]
        self.Lat = float(line[3][:2])+float(line[3][2:])/60
        self.Tn=line[2]
        self.Lng = float(line[5][:3])+float(line[5][3:])/60
        self.Gn=line[4]
        self.gps=[self.Lat,self.Tn,self.Lng,self.Gn,[self.hh,self.mm,self.ss]]
        return self.gps

