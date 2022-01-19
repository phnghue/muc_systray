# icon in systray : infi.systray (https://github.com/Infinidat/infi.systray and https://stackoverflow.com/a/54082417/3154274)
# install PIL :  pip install Pillow
# install infi.systray : pip install infi.systray
from infi.systray import SysTrayIcon
import time;
import webbrowser;

n=1; k=0;
AUrl=["https://icedrive.net/s/TxvVDigygFA2FF5hThPyhGTwSgYZ"
    ,"https://www.deviantart.com/hiperrine/art/Meme-Brown-Nau-Can-you-make-a-caption-for-this-894933781"
    ,"https://www.deviantart.com/hiperrine/art/Muc-Ink-Fractal-893014966"
    ,"https://www.deviantart.com/hiperrine/art/Muc-Ink-Fibonacci-Tree-893183741"
    ,"https://www.deviantart.com/hiperrine/art/Muc-Ink-Sierpinski-893195392"
];
def open(id): return lambda i:webbrowser.open(AUrl[id], new = 2);
menu_options = (
    ("Gimme some more food!!!", None, open(0))
    ,("My sons", None, open(1))
    ,("Me in fractal", None, open(2))
    ,("Me and Fibonacci", None, open(3))
    ,("Me and Sierpinski", None, open(4))
);
systray = SysTrayIcon("./muc_s.ico", "Muc Systray", menu_options)
systray.start();
cFirst=0;
while cFirst==0 or not systray._hwnd is None:
    cFirst=1;
    n+=1; k=n%4;
    if k==0:systray.update(icon="./muc_s.ico");
    elif k==1:systray.update(icon="./muc_m.ico");
    elif k==2:systray.update(icon="./muc_l.ico");
    elif k==3:systray.update(icon="./muc_m.ico");
    time.sleep(50/1000);
systray.shutdown()
