Unpack software archive into some folder, e.g. C:\fm2txt

Go to https://www.anaconda.com/download/ and choose Python 3.6 version, 64-Bit Graphical Installer
or download directly: https://repo.continuum.io/archive/Anaconda3-5.0.1-Windows-x86_64.exe

Run anaconda prompt, change dir to C:\fm2txt [c:] [cd \fm2txt], then run:
```
pip install -r requirements.txt
```
Ubuntu 18 <br>
sudo pip3 install --upgrade speechrecognition<br>


Last step is to copy 2 files from x64!!! osmocom rtl-sdr drivers: https://osmocom.org/attachments/download/2242/RelWithDebInfo.zip

Copy these [rtl-sdr-release/x64/]: rtlsdr.dll & libusb-1.0.dll into C:\Windows folder.

Now we may run, this will produce text recognition results file [radio_log.txt]:
```
python listen.py --freq=95000000 --gain=20 --ppm=56 --lang=ru-RU
The following was change as most laptops is to slow and get under run
sample_rate_fm = 240000 was changed to 180000
if you get this error
OSError: Error code -6 when opening SDR (device index = 0)
it means there is still a process holding onto rtl_dongle

Some unnecessary help available:
```
python listen.py --help
```

To mute audio output use verbose key:
```
python listen.py --verbose
```

If you experiencing some audio gaps due to high CPU usage, try to lower down digitising frequency, for example:
```
sdr.rs = 1024000
```

List of supported languages and their codes: https://cloud.google.com/speech/docs/languages

Recognition quality can be improved using paid Google, Microsoft, IBM or other services.
