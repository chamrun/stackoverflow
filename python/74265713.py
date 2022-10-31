import os
import threading


class Args:
    def __init__(self):
        self.dir = '.'


class Threader:
    def __init__(this):
        this.args = Args()

    def tfunc(this, folder):
        for file in os.listdir(folder):
            this.executeFile(os.path.join(this.args.dir, file))

    def executeFiles(this):
        for folders1 in os.listdir(this.args.dir):
            # for folders2 in os.listdir("downloaded/" + os.path.join(folders1)):
            t = threading.Thread(target=this.tfunc, args=(this, folders1))
            t.start()

    def executeFile(this, file):
        pass


if __name__ == '__main__':
    threader = Threader()
    threader.executeFiles()
