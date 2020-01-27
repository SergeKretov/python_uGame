from setuptools import setup

APP = ['ugame.py']
DATA_FILES = ['advokat.png','bg.png','bgame.png','bgames.png','box.png','boxbg.png','chc.png','cho.png','coin.ogg','colonna.png','dela.png','doorc.png','dooro.png','exit.png','exits.png','fireball.ogg','fireball.png','gover.png','gulp.ogg','hdie.ogg','holst.png','holst2.png','info.png','level01.map','level02.map','level03.map','level04.map','level05.map','level06.map','level07.map','level08.map','level09.map','level10.map','level11.map','level12.map','level13.map','level14.map','level15.map','level16.map','level17.map','level18.map','level19.map','level20.map','level21.map','level22.map','level23.map','level24.map','level25.map','level26.map','level27.map','level28.map','level29.map','level30.map','level31.map','level32.map','level33.map','lup.png','mmm.ogg','nlev.ogg','pdie.ogg','pleft.png','police.png','pright.png','rule.png','rules.png','rules.txt','setting.png','settings.png','sud.png','title.png','tlc.png','ugame.ico','ulika.png','win.png','wl1.png','wl2.png','wl3.png','wl4.png','yw.ogg','yww.png','znan.png']
OPTIONS = {
    'iconfile':'ugame.icns',
    'argv_emulation': False,
    'packages': ['pygame','tkinter','timer','threading','random'],
    }
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    )
    
