import sys

class f_opt:
    def __init__(self, checkArgs: dict):
        self.args = sys.argv
        self.cArgs = checkArgs
        self.check()

    def check(self):
        # check if args are supplied
        pos = []
        reqDist = []
        EndDist = len(self.args)
        for p, i in enumerate(self.args):
            if self.cArgs.get(i) != None:
                pos.append((p, i))
                reqDist.append(len(self.cArgs.get(i)[0]))
        Dist = [pos[i][0]-pos[i-1][0]-1 for i in range(1, len(pos))]
        Dist.append(EndDist-pos[len(pos)-1][0]-1)
        fault = False
        for p, i in enumerate(Dist):
            if i != reqDist[p]:
                print(f"The option {pos[p][1]} requires {reqDist[p]} arguments.  {i} option(s) has been supplied.")
                fault = True
        if fault == True:
            return
        #run and fallback
        funcOPT = [self.cArgs.get(i[1]) for i in pos]
        for i in range(0, len(funcOPT)):
            start = pos[i][0]+1
            funcOPT[i][1](*[funcOPT[i][0][p1](i1) for p1, i1 in enumerate(self.args[start: start+len(funcOPT[i][0])])])