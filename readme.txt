﻿Uždavinis surušiuoti  grafą topologinę tvarką jei neįmanona
paskayti tai. Pateikti viršunes ir jų vaikus, kai surušiuota 
nurodyt viršunių tėvus.

programos įėjimo failas sudaromas taip:
	nurodoma viršunė ir kitą viršunė į kurią galima patekti
iš pirmosios pav failo
	
	input.txt
	1 2
	2 3 
 kai baigiama vardinti grafo briaunos gale neturėtų 
 būti tuščios
 eilutės  1) failo eilutė atstovauja briaunai 1 ----> 2

 programos naudojimas turi būti sukurtas objektas 
 Topological_sort() typo ir kviečiams jo metodas sort(file_name)
rezultatas parodomas konsolėje jei įmanoma išrušiuot grafą kitų
atveju pasako, kad to padaryti neįmanoma
