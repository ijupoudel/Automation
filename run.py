from subprocess import call
import glob
import sys
path = glob.glob("/mnt/e/sijanprojects/zite-tests/status-test.py")
# testdata = filter(lambda x: x.endswith('/run.py'),path)
# for v in testdata:
#     path.remove(v)


scr,domain,token = sys.argv

class CallPy(object):
    def __init__(self,path):
        self.path = path

    def call_python_file(self):
        for p in self.path:
            call(["python3","{}".format(p),domain,token])

if __name__ == '__main__':
    c = CallPy(path)
    c.call_python_file()
    
