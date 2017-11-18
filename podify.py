#!/usr/bin/env python3

import os
import pafy

try: os.mkdir('pods')
except: pass
downloaded = eval(open('downloaded.set').read()) # never download same file twice

for url in open('urls.txt'):
    url = url.strip()
    if not url or url in downloaded or url.startswith('#'):
        continue
    downloaded.add(url)
    video = pafy.new(url)
    audiostream = max(video.audiostreams, key=lambda audio: abs(audio.rawbitrate-131072))
    filename = audiostream.download()
    os.rename(filename, 'pods/'+filename)
    print(filename)
    open('downloaded.set', 'wt').write(str(downloaded))
