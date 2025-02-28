
### 1. Hoe is de ASM opgebouwd? Geef 2 verschillende types. Hoe kan je deze motor herkennen? Geef een andere naam voor de ASM.

Een ASM is opgebouwd uit een statisch gedeelte, *de stator* en een dynamisch gedeelte, *de rotor*. Beide zijn gescheiden door een kleine *luchtspleet*.
De *stator* is gemaakt uit gietstaal met gleuven waarin de $3f$ statorwikkelingen, regelmatig over de statoromtrek verdeeld, aangebracht zijn. In de *stator* bevind zich de *rotor* met een *luchtspleet tussen*. 
De *rotor* is opgebouwd uit koperen of Aluminium staven die op hun uiteinden zijn verbonden met koperen of Al staven met elkaar terug verbonden. Deze zitten in een stalen gelamineerde cylinder.

- Kooi anker machine
  wikkelingen zitten in de stator
  6 aansluitingen
- Sleepring machine
  Wikkelingen zitten in de rotor
  3 aansluitingen

Inductie motor

### 2. Vul in:

| **Toerental** |             | **Generatorwerking** | **Motorwerking** |
| ------------- | ----------- | -------------------- | ---------------- |
| $n<0$         | $M$         | +                    | -                |
| $n<0$         | $\cosφ_{1}$ | +                    | -                |
| $n>0$         | $M$         | -                    | +                |
| $n>0$         | $\cosφ_{1}$ | +                    | -                |
### 3. Geef de formule voor het toegevoegd vermogen en het nuttig vermogen bij een AS generator. Stel schematisch voor en duid de energiestroom aan.

$$
P_{toe}=M\cdot \omega
$$
$$
P_{L}=P_{toe}-P_{cu_{r}}-P_{Fe_{r}}-P_{v}
$$
$$
P_{nuttig}=P_{L}-P_{cu_{s}}-P_{Fe_{s}}
$$

### 4.Wat is een draaiveld?

Een magnetisch veld dat roteert in een ruimte. Gevoed door een 3f wisselstroom die door de statorwikkelingen v/d ASM vloeit. deze wikkelingen zijn geplaatste zodat de faseverschuiving tussen iedere wikkeling $120°$ is.

### 5.Welke waarden moeten voldaan zijn om binnen de stator van een ASM een draaiveld te bekomen?

- Een 3fasige voeding waar de faseverschuiving tussen iedere fase $120°$ is en een gelijke spanning
- De statorwikkelingen moeten geplaatst worden zodat ze onderling een fysieke hoekverschuiving hebben van $120°$ 
- De wikkelingen moeten een gelijke belasting hebben tov elkaar

### 6.Toon het ontstaan van een

1. tweepolig veld aan a.d.h.v één $(\omega t_{3}=180°)$ of meerdere figuren $(\omega t_{3}=180°$ en $\omega t_{4}=270°)$
2. vierpolig veld aan a.d.h.v één $(\omega t_{3}=180°)$ of meerdere figuren $(\omega t_{3}=180°$ en $\omega t_{4}=270°)$
3. tweepolig draaiveld aan a.d.h.v één $(\omega t_{3}=180°)$ of meerdere figuren $(\omega t_{3}=180°$ en $\omega t_{4}=270°)$, wijzerzin
4. vierpolig draaiveld a.d.h.v één $(\omega t_{3}=180°)$ of meerdere figuren $(\omega t_{3}=180°$ en $\omega t_{4}=270°)$, wijzerzin
5. tweepolig draaiveld a.d.h.v één $(\omega t_{3}=180°)$ of meerdere figuren $(\omega t_{3}=180°$ en $\omega t_{4}=270°)$, tegenwijzerzin

| grootheid | kleur |
| --------- | ----- |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
![[Pasted image 20250109124410.png]]
![[Pasted image 20250109141104.png]]
![[Pasted image 20250109141142.png]]
![[Pasted image 20241227145141.png|#invert]]

### 7.Bepaal wiskundig de grootte van het tweepolig draaiveld op $t=t_{3}$ en op $t=t_{4}$ . Geef hiervan de afleiding met bijhorend vectordiagram.

$$
\overline{\Phi_{t}}=\overline{\Phi_{1}}+\overline{\Phi_{2}}+\overline{\Phi_{3}}
$$
$$
|\Phi_{t}|=|\Phi_{1}|\cdot \sin\alpha+|\Phi_{2}|\cdot \sin(\alpha-120°)+|\Phi_{3}|\sin(\alpha-240°)
$$

### 8. Kan een AS motor op het synchroon toerental draaien?

**Theoretisch:** als ideale ASM kan dit wel want er zijn geen verliezen dus $M_{i}=M_{as}$ en op s=0 zal het inwendig moment ook 0 zijn en als er het tegenwerkend koppel ook 0 is dan kan de motor op zijn synchroon toerental draaien.

**Praktisch:** Neen maar kan wel streven naar het synchroon toerental dus $n_{r}\to n_{s}$ maar nooit $n_{r}\geq n_{s}$ tenzij er een uitwendig meedraaiend koppel is die de motor duwt tot $n_{s}$ of verder ($n_{r}>n_{s}$). De slip is essentieel voor de motorwerking ook al nadert de Slip naar 0 $(s\to0)$ Je kan enkel $s<0$ hebben als je de machine als generator gebruikt.

### 9. Beschouw de ideale AS motor. Teken het vectordiagram. In welke mate verschilt dit met die van de Ideale transformator?
![[Pasted image 20250109141851.png]]
De motor heeft een veel grotere $I_{\mu}$ dan de transformator dit komt door de luchtspleet tussen de stator en de rotor. En door de grotere magnetiseringsstroom zal de nullaststroom ook groter zijn.

### 10. Toon de werking aan van de AS motor voor: ... En voorzie de figuren van de nodige uitleg. Teken de verschillende grootheden $(I_{µ},\Phi,n_{s},n_{r},v,I_{2},\Phi_{2},\Phi_{1},I_{1}',F,M)$ in verschillende kleuren en noteer in de tabel naast de respectievelijke grootheid.

1. Een tweepolig veld aan io $\omega t_{3}=0°$ met draaizin in wijzerzin
2. Een tweepolig veld aan io $\omega t_{4}=90°$ met draaizin in wijzerzin
   
3. Een tweepolig veld aan io $\omega t_{3}=0°$ met draaizin in tegenwijzerzin
4. Een tweepolig veld aan io $\omega t_{3}=90°$ met draaizin in tegenwijzerzin


| grootheid | kleur |
| --------- | ----- |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
|           |       |
![[Pasted image 20241227143452.png|#invert]]
![[Pasted image 20250109142014.png]]
![[Pasted image 20241227150422.png|#invert]]


### 11. Toon de werking aan van de asynchrone generator voor: ... Voorzie de figuren van de nodige uitleg. Teken de verschillende grootheden $(I_{µ},\Phi,n_{s},n_{r},v,I_{2},\Phi_{2},\Phi_{1},I_{1}',F,M)$ in verschillende kleuren en noteer in de tabel naast de respectievelijke grootheid.
1. een tweepolig veld aan op $\omega t_{3}=180°$ met draaizin in wijzerzin
2. een tweepolig veld aan op $\omega t_{3}=270°$ met draaizin in wijzerzin
![[Pasted image 20241227150422.png|#invert]]


### 12. Teken vectordiagram van ideale generator a d h v besluiten van de vorige vraag. In welke mate verschilt deze van die van het motorprincipe

De EMK van de `Rotor` is omgepoolt, hierdoor is de `Rotorstroom` die verantwoordelijk is voor het genereren van de `rotorflux` ook omgepoold. Daardoor hebben we een $I'$ die ook $180°$ verdraaid is en dus hebben we een $\cos \varphi>90°$ . Die bij motorwerking kleiner dan $90°$ is.
![[Pasted image 20250109142316.png]]
### 13. Som de frequentieafhankelijke grootheden op bij de AS motor. Geef aan hoe ze wijzigen ifv de frequentie (formule). Geef voor elke grootheid een fysische duiding voor hun wijziging ifv de frequentie.

1. Machine
	1. Flux $\Phi$ = $\Phi \approx \frac{V}{X_{m}}=\frac{V}{2\pi fL_{m}}$
	   
	2. Stator
		1. EMK $E_{1}=4,44*f_{s}*n_{s}*\Phi$
		2. Rotorreactantie $X_{1}=2\pi f_{s}*L_{1}$
		   Als $f$ toeneemt, neemt de spanningsverandering ook toe en hierdoor gaat de reactantie stijgen van de spoel $f $
		3. Draaiveld $f_{s}=\frac{(n_{s}-0)*\eta}{60}$
		   De statorspoelen creëren het draaiveld als de frequentie hiervan stijgt gaat het veld rapper draaien door de snellere verandering van de stroom door ieder polenpaar $f\nearrow\implies X_{1}\nearrow$ 
	2. Rotor
		1. EMK $E_{2}=4,44*n_{r}*f_{r}*\Phi$
		2. Rotorreactantie $X_{2}=2\pi f_{r}*L_{2}$
		3. Rotor frequentie $f_{r}=f_{s}*s$
		4. koppel $M_{max}\approx \frac{v_{2}}{X_{tot}}$
		5. $s_{k}$ is afhankelijk van $X_{2}$ 

### 14. Een AS motor wordt nominaal belast. Teken de motorkarakteristiek. Duid het tegenwerkend koppel aan. Wat gebeurt er met de onderstaande grootheden indien de belasting toeneemt? Leg uit en geef een nauwkeurige verklaring. Duid ook aan op de voorziene grafiek.

- Het inwendig koppel:
  Zal stijgen tot het as koppel gelijk wordt met het tegenwerkend koppel van de belasting en als dit tegenwerkend koppel groter is dan het maximale koppel van de motor zal de motor tot stilstand geforceerd worden
- Het rotortoerental:
  Zal dalen tot het as koppel gelijk wordt met het tegenwerkend koppel van de belasting en als dit tegenwerkend koppel groter is dan het maximale koppel van de motor zal de motor tot stilstand geforceerd worden
- De slip:
  Zal stijgen tot het as koppel wordt met het tegenwerkend koppel van de belasting en als dit tegenwerkend koppel groter is dan het maximale koppel van de motor zal de motor tot stilstand geforceerd worden
- De rotorfrequentie:
  Zal stijgen tot het as koppel wordt met het tegenwerkend koppel van de belasting en als dit tegenwerkend koppel groter is dan het maximale koppel van de motor zal de motor tot stilstand geforceerd worden
- De rotor EMK:
  Zal stijgen tot het as koppel wordt met het tegenwerkend koppel van de belasting en als dit tegenwerkend koppel groter is dan het maximale koppel van de motor zal de motor tot stilstand geforceerd worden
- De rotorstroom $I_2$:
  Zal stijgen tot het as koppel wordt met het tegenwerkend koppel van de belasting en als dit tegenwerkend koppel groter is dan het maximale koppel van de motor zal de motor tot stilstand geforceerd worden

### 15.Vergelijk de arbeidsfactor van de rotor bij aanzetten van de niet ideale AS motor met deze bij nominaal draaien. Bewijs dit adhv vector diagramma's en voorzie dit van de nodige verklaringen, uitleg, formules, equivalente schema's. 

##### *Aanzetten-starten* - Equivalent schema
![[Pasted image 20241223185137.png]]
$$ 
Z=\sqrt{ \frac{R_{2}}{\underbrace{ s }_{ s=1=\text{MAX} }}^2+X_{st}^2 } \implies\cos \varphi \ll
$$
![[Pasted image 20241224093833.png]]
##### *Nominaal draaien/bedrijf* - Equivalent schema
![[Pasted image 20241224122011.png]]
![[Pasted image 20241224114338.png]]
$$
Z=\sqrt{ \frac{R_{2}}{\underbrace{ s }_{ s\ll }}^2+X_{st}^2 } \implies\cos \varphi \ll
$$
![[Pasted image 20241224104000.png]]
### 16. Verklaar de fysische betekenis van de weerstanden $R_{2},R_{2}/s,R_{2}(1-s)/s$
$R_{2}$: De weerstandswaarde van de statorstaven
$\frac{R_{2}}{s}$: De weerstandswaarde van de statorstaven plus de equivalente weerstandswaarde van de belasting op de as
$R_{2}\cdot \frac{1-s}{s}$: De equivalente weerstandswaarde van de belasting op de as van de motor

### 17. De nominaal draaiende AS motor (niet ideaal):
##### Geef het EQ schema

![[Pasted image 20241224122140.png]]

##### ==Welke actieve vermogens treden== er op in de draaiende AS motor en in ==welke onderdelen== van de machine treden deze vermogens op? Som ze één na één op. ==Bespreek ze uitgebreid== en leg uit wat hun ==fysische betekenis== is uitgaande van het ==EQ schema== van de ==nominaal draaiende AS motor== en geef de ==formule van dit vermogen==. Kan je de ==formules vlot omzetten==? Noteer tevens de ==formules van de resp. koppels.==
1. **Toegevoegd vermogen:**
   dit is het elektrische vermogen dat in de motor wordt gestuurd
   $P_{1}=\sqrt{ 3 }\cdot I_{L}\cdot U_{L}\cdot \cos \varphi_{1}$
1. **Primaire koperverliezen:**
   Dit is het verloren vermogen te danken aan de koper verliezen in de stator
   $P_{Cu_{1}}=3\cdot R_{1}\cdot I_{F_{S}}^2$
3. **Primaire ijzerverliezen:**
   Dit is het verloren vermogen te danken aan de wervelstromen in de stator is onafhankelijk van het toerental
   $P_{Fe_{S}}=P_{1}-3\cdot R_{1}\cdot I_{F_{S_{0}}}^2$
4. **Luchtspleetvermogen:**
   Het overgedragen vermogen van de stator naar de rotor dus dit vermogen is het toegevoegd vermogen zonder de prim Cu- en Fe-verliezen
   $P_{L}=3\cdot \frac{R_{2}}{s}\cdot I_{2}^2$
5. **Secundaire koperverliezen:**
   Het vermogen verloren door het Joule effect in de rotorstaven
   $P_{Cu_{R}}=3\cdot R_{2}\cdot I_{2}^2$
6. **Inwendig vermogen:**
   Het vermogen dat het inwendig koppel genereerd.
   $P_{i}=P_{L}\cdot (1-s)$
1. **Mechanische verliezen:**
   Het vermogen verloren aan factoren zoals wrijving van de rotor as en ventilatie.
   $/$
8. **Nuttig- of Asvermogen:**
   Het mechanisch vermogen op de rotor as.
   $P_{as}=P_{i}-P_{v}=M_{as}\cdot \omega$


- $P_{1}\implies P_{L},P_{v}(P_{Cu},P_{Fe})\implies P_{i},P_{Cu_{s}}\implies$

### 18. Van welke parameters is het inwendig koppel van de asynchrone motor afhankelijk?
$M_{as}$:
- Toerental
- Toegevoegd vermogen
- Tegenwerkend koppel
- Motorconstanten
- Rotorweerstanden en reactanties
- Statorweerstanden en reactanties
- Polenparen -> Toerental
- Statorfrequentie -> Toerental


### 19. Teken een realistische koppel-toerentalkarakteristiek samen met lineaire belastingskarakteristiek. Duid hierop de volgende punten/gebieden aan
- nullastkoppel $M_{i_{0}}$
- nominaal koppel $M_{i_{n}}$
- startkoppel $M_{i_{st}}$
- kipkoppel $M_{i_{k}}$
- nullast toerental $n_{r_{0}}$
- kipslip $s_{k}$
- synchroon toerental $n_{s}$
- maximale slip bij motorwerking $s_{n}$
- werkingsgebied motor
- onstabiel gebied motor
- generatorwerkingsgebied
- aanloopkoppel
#### Duid ook een zelfgekozen
- tegenwerkend koppel
- koppeloverschot
- inwendig koppel

##### 19.1 van welke parameters is de kipslip. Het kipkoppel afhankelijk, ifv het type motor
$s_{k}=\frac{R_{2}}{X_{2_{st}}}$
![[Pasted image 20250109152550.png]]
$R_2,\text{ }k\text{ en }X_{2}$ zijn motorafhankelijk
##### 19.2 Op welke wijze hebben deze parameters invloed op de koppel-toerentalkarakteristiek?




### 20 Betreffende $M_{J}$

##### 1. Leg de betekenis uit van het $M_{J}$ koppel.
$M_{J}$ is het koppel dat nodig is om de hoeksnelheid van het systeem te veranderen. Met andere woorden $M_{J}$ is de weerstand dat het roterend systeem biedt tegen een veranderijng in snelheid

##### 2. Kan $M_{J}>0$? Zo ja, situeer het gevolg vd. motorwerking
Ja, dit gebeurt als de hoeksnelheid toeneemt. 
Dit betekent dat de motor extra koppel moet geven om de traagheid te overwinnen en dus een versnelling kan veroorzaken

##### 3. Kan $M_{J}=0$? Zo ja, situeer het gevolg vd. motorwerking
Ja, dit gebeurt wanneer: $\frac{d\omega}{dt} = 0$  en dus het systeem dezelfde hoeksnelheid behoud. De motor moet geen extra koppel leveren om de hoeksnelheid te veranderen. De motor moet enkel het belasting koppel overwinnen. 

#### 4. Kan $M_{J}<0$? Zo ja, situeer het gevolg vd. motorwerking
Ja, dit gebeurt als de hoeksnelheid afneemt. Dit betekend dat het systeem een remmend effect heeft. de motor moet minder koppel leveren omdat het de traagheid al een deel van de vertraging veroorzaakt. In sommige gevallen kan de motor dan als generator werken, waarbij er energie wordt teruggewonnen.


### 21. Wat wort er verstaan onder de statische werking van de motor? Wat wordt verstaan onder de dynamische werking van de motor? Zijn aan beide modi voorwaarden gekoppeld?
1. Statische werking:
   De motor draait aan een constante hoeksnelheid, dus geen versnelling of vertraging:
	- $M_{J}=0$  omdat er geen verandering is in de hoeksnelheid
	- $M_{as}=M_{belasting}$ geleverde koppel is gelijk aan tegenwerkend koppel
	- De motor levert een constant koppel en verandert niet meer van snelheid 
	- Alle krachten opgeteld tellen op tot 0
1. Dynamische werking:
   Motor versneld, vertraagt of start op. Dit betekend dat het toerental vd motor veranderd
	- $\frac{d \omega}{dt} \neq 0$ er is een verandering van hoeksnelheid/toerental.
	- $M_{J}$ speelt een rol en wordt opgeteld of afgetrokken van het totale koppel
	- $M_{\text{motor}}=M_{\text{belasting}+}M_{J}$ 
	- Gebeurt bij opstarten van de motor en/of verandering in de belasting
	- De motor moet het extra koppel ($M_{J}$) kunnen leveren om de traagheid van het systeem te kunnen overwinnen.


### 22. Bespreek het statisch en dynamisch gedrag van de motor, onderhevig aan elk van deze belastingen.

**Gegeven**:
- onderstaand kopel-toerentalkarakteristiek
- statorstroom-toerentalkrarakteristiek van de motor
- twee belastingskarakteristieken van pomp 1 en pomp 2
- nominale stroom van de motor $I_{n}=1,75A$
![[Pasted image 20241227142126.png]]

De Motor zal overbelast zijn als deze pomp 2  moet aansturen en in het statisch punt komt, want de stator stroom zal groter zijn dan de nominale stroom en dus zal de motor oververhitten.
Bij pomp 1 is het wel mogelijk om deze constant aan te sturen, want de opgenomen statorstroom in het werkingspunt is lager dan de nominale stroom (vollast stroom) van de motor


