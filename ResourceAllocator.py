#techtinium assessment
#Arjunan TJ
#arjunantjdeveloper@gmail.com

"""Resource	    Units	  NY	    India	   China
        l	      10	    120	     140	    110
        xl	    20	    230	      -	      200
        2xl	    40	    450	     413	     -
        4xl	    80	    774	     890	    670
        8xl	    160	    1400	  1300	   1180
        10xl	  320	    2820	  2970	     -  """
        
class allocator():
    dNy = {320:2820, 160:1400, 80:774, 40:450, 20:230, 10:120}
    dIn = {320:2970, 160:1300, 80:890, 40:413, 20:0,   10:140}
    dCh = {320:0,    160:1180, 80:670, 40:0,   20:200, 10:110}
    dcodes = {320:"10xLarge", 160:"8xLarge", 80:"4xLarge", 40:"2xLarge", 20:"xLarge", 10:"Large"}
 
    #def __init__(self):
        #pass

    def check(self,cap, xl, hr, d):
        rem = cap%xl
        count = int(cap/xl)
        val = count*d[xl]*hr
        return int(rem),int(val),int(count)

    def machinescheck(self, rem, xl, hr, d, ms):
        dans = list()
        cs = 0
        while rem > 0:
                reme,val,count = self.check(rem, int(xl/2), hr, d)
                if ms!=0:
                    if ms < val:
                        return None,None
                if val!=0:
                    #dchans[xl/2] = count
                    dans.append((self.dcodes[xl/2],count))
                    cs+=val
                    rem = reme
                xl = xl/2
        return cs,dans
        
    def countryBased(self, region, cap, hr):
        ms = 0
        cs = 0
        rem = cap
        
        if region == "NY":
            dnyans = list()
            xl = 640
            while xl > 10:
                cs,dans = self.machinescheck(rem, xl, hr, self.dNy, ms)
                if cs != None and dans != None:       
                    if ms==0:
                        ms = cs
                        dnyans = dans
                    else:
                        if ms > cs:
                            ms = cs
                            dnyans = dans
                xl = xl/2
            
            
            return ms,dnyans
        if region == "IN":
            dinans = list()
            xl = 640
            while xl >10:
                cs,dans = self.machinescheck(rem, xl, hr, self.dIn, ms)
                if cs != None and dans != None: 
                    if ms==0:
                        ms = cs
                        dinans=dans
                    else:
                        if ms > cs:
                            ms = cs
                            dinans = dans
                xl = xl/2

            return ms,dinans
        
        if region == "CH":
            dchans = list()
            xl = 640
            while xl > 10:
                cs, dans = self.machinescheck(rem, xl, hr, self.dCh, ms) 
                if cs != None and dans != None:
                    if ms==0:
                        ms = cs
                        dchans = dans
                    else:
                        if ms > cs:
                            ms = cs
                            dchans = dans
                xl = xl/2

            return ms,dchans


def main():
    cap = int(input("Enter the capacity"))
    hr = int(input("Enter hours"))
    al = allocator()
    nycost, nymachines = al.countryBased("NY", cap, hr)
    incost, inmachines = al.countryBased("IN", cap, hr)
    chcost, chmachines = al.countryBased("CH", cap, hr)
    doutput = dict()
    doutput['Output'] = [{"region":"NewYork", "total_cost":nycost, "machines":nymachines},{"region":"India", "total_cost":incost, "machines":inmachines}, {"region":"China", "total_cost":chcost, "machines":chmachines}]
    print(doutput)
    
main()
