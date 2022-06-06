
SZÍNFELISMERŐ PROGRAM

BMSZC Neumann Informatikai Technikum

INDUSTRIA PERITIA
Bodó Sándor, Kármán Szabolcs, Gulyás Csaba

-----------------

A programot úgy készítettük el, mintha ezt egy raktárban már gépek használnák automatikus szortírozásra. Szín alapján deríti ki, hogy az adott csomag törékeny, romlandó vagy aeroszolos. Későbbi bővítésként bekerülhet, hogy gépi tanulást használva automatikusan megkeresi a csomagon a színt.

(Ahhoz hogy működjön, a python 'cv2', 'Pillow' (vagy 'PIL') és 'pandas' moduljának telepítve kell lennie. A program könyvtárában lévő '\temp' könyvtárba menti a képeket a futás közben.)

-----------------

A 'szinfelismero.py' a fő program. Elindításkor a konzolon bekéri a kép nevét (kép_neve.kiterjesztése). Ezután feldolgozza a képet (medián elmosódás és kontrasztosítás), hogy könnyebbé tegye a munkát. Ezt az új képet fogja megjeleníteni, ahol dupla kattintással lehet kiválasztani, hogy hol ellenőrizze le a színt. Az eredményt kiírja a képernyőn is, és a konzolon is. Kilépni az ESC-pel lehet.

A 'csomag_1.png', 'csomag_2.png' és 'csomag_3.png' képek a demonstrációra szolgálnak (dupla katt a színes részre). A 'test.png'-vel opcionálisan lehet tesztelni az érzékenységet.

A 'szin_konvertalo.py'-val finomítottuk az érzékenységét a felismerőnek. A 'dataset.csv'-t - mely 900 színt tartalmaz -, átkonvertál 4 lehetőségre (pirosra, zöldre, kékre és ismeretlenre) a 'dataset_new.txt'-be.

