# Gelijkstroommachines

[[ASM en Gelijkstoom machines]]
[[Oefeningen DC]]
## 3.1 Inleiding

==De term *elektrische machine* verwijst naar een apparaat waarbij elektrische energie wordt omgezet in mechanische energie of omgekeerd. Deze machines zijn elektromechanische omzetters van energie. Gelijkstroommachines kunnen worden onderverdeeld in:==

- **Dynamo's**: zetten mechanische energie om in elektrische energie.
- **Motoren**: zetten elektrische energie om in mechanische energie.

### 3.1.2 de vergelijking

| Transformator | ASM       | DC-machine    |
| ------------- | --------- | ------------- |
| Sinusoidal    | Draaiveld | Vast mag veld |
| Primaire      | Stator    | Stator        |
| Secundair     | Rotor     | Anker         |

---
## 3.2 De bouw van de gelijkstroommachine

### 3.2.1 De onderdelen

Een gelijkstroommachine bestaat uit de volgende hoofdonderdelen:

1. **De stator**: de vaste behuizing van de machine.
2. **De statorwikkeling**: zorgt voor de opwekking van het magnetisch veld.
3. **De ankerwikkeling**: geleidt de stroom in de rotor.
4. **De collector/commutator**: wisselt de stroomrichting in het anker.
5. **De koolstofborstels**: zorgen voor elektrisch contact tussen de rotor en het externe circuit.
![[Pasted image 20241228125152.png]]
### 3.2.2 De stator

De stator dient om een magnetisch veld te genereren. Dit kan op twee manieren gebeuren:

- **Permanent magneet**: gebruikt een permanente magneet om een constant magnetisch veld te creëren.
- **Elektromagneet**: gebruikt een veldwikkeling (*bekrachtigingswikkeling*) om een variabel magnetisch veld te genereren. Deze bestaat uit:
  - **Juk**: het ijzeren deel dat het magnetisch veld geleidt.
  - **Poolkern** en **poolschoen**: concentreren het magnetisch veld.

Het magnetisch veld stroomt door de veldwikkeling, de polen, de luchtspeling en het anker. Het aantal polen bepaalt de specificatie van de machine:
- **Tweepolige machine**
- **Vierpolige machine**
![[Pasted image 20241228125242.png]]

### 3.2.3 Het anker

Het anker is de draaiende rotor van de machine. Bij de meeste gelijkstroommachines wordt een *trommelanker* gebruikt, bestaande uit:

- **Ankerblikken**: dunne, geïsoleerde lamellen om wervelstromen te minimaliseren.
- **Gleuven**: bevatten de ankergeleiders.
- **Collector/commutator**: verbonden met de uiteinden van de ankergeleiders via koolstofborstels.
![[Pasted image 20241228125321.png]]

De **draaizin** wordt bepaald door de richting van de stroom door het anker en het statorveld.

---

## 3.3 De verschillende types gelijkstroommachines

### 3.3.1 De permanente magneet motor

**Stator:**
- **Primair veld:** bestaat uit permanente magneten
**Anker:**
- Gelijk als gewone DC-motor
**Kenmerken:**
- Kleine vermogens
- Hoger rendement 

### 3.3.2 De types bekrachtiging

Gelijkstroommachines worden verder ingedeeld op basis van de methode waarmee de veldstroom wordt opgewekt:

1. **Onafhankelijke bekrachtiging**:
   - De veldstroom wordt geleverd door een externe spanningsbron.
   - Deze machines worden OB-machines (Onafhankelijke Bekrachtiging machines) genoemd.
   - Aanduidingen:
     - **Ankerwikkeling**: $A_1 - A_2$
     - **Veldwikkeling**: $F_1 - F_2$

2. **Eigen of zelfbekrachtiging**:
   - De veldstroom wordt opgewekt door de machine zelf.
   - Onderverdeling:
     - **Seriemotor**: veldwikkeling in serie met ankerwikkeling ($D_1 - D_2$).
     - **Shuntmotor**: veldwikkeling in parallel met ankerwikkeling ($E_1 - E_2$).
     - **Compoundmotor**: combinatie van serie- en shuntwikkeling.


#### Klemmaanduidingen

| **Benaming**                 | **Klemmaanduiding** |
|------------------------------|---------------------|
| Ankerwikkeling               | $A_1 - A_2$         |
| Hulppoolwikkeling            | $B_1 - B_2$         |
| Compensatiewikkeling         | $C_1 - C_2$         |
| Seriewikkeling               | $D_1 - D_2$         |
| Shuntwikkeling               | $E_1 - E_2$         |
| Onafhankelijke bekrachtiging | $F_1 - F_2$         |

---
## 3.4 Principe van de motorwerking
### 3.4.1 Algemene werking
Een gelijkstroommotor werkt op basis van het effect van een magnetische flux $\phi$ op een stroom voerende geleider. Dit genereert een lorentzkracht, gegeven door: 
$$
F = B \cdot l \cdot I_a 
$$
![[Pasted image 20241229124134.png]]
waarbij: - $B$: inductie (in het magnetisch veld), - $l$: effectieve lengte van de geleider, - $I_a$: ankerstroom. Wanneer de hoek tussen $B$ en $I_a$ niet loodrecht is, wordt de kracht: 
$$
F = B \cdot l \cdot I_a \cdot \cos{\alpha} 
$$
Met:
- $B \text{ de inductie}$
- $l \text{ de nuttige lengte}$
- $I_{a} \text{ de stroomvoerende gelijder}$
- $\alpha \text{ de hoek van waar de gelijder zich bevind tov het veld}$
![[Pasted image 20241229124155.png]]
![[Pasted image 20241229124358.png]]

### 3.4.2 Motorwerking
Het anker draait in het magnetisch veld door het resulterende koppel: 
$$
M = F \cdot d = k_2 \cdot \phi \cdot I_a 
$$
waarbij:
- $d \text{ de diameter van het anker}[m]$
- $k_2$ de tweede machineconstante is.
$$
M=F\cdot d=\frac{\Phi}{S}\cdot l\cdot I_{a}\cdot d=k_{2}\cdot \Phi\cdot I_{a}
$$
Met: $B \text{ wordt vervangen door }\frac{\Phi}{S} \implies k_{2}=\frac{l*d}{S}$

waarbij:
- $\Phi[Wb]$
- $I_{a}[A]$
- $M[Nm]$
- $S[m^2]$

#### 3.4.2.0 Motorwerking

Om het gewenste magnetische veld in de luchtspeling te bekomen:
- Het veld wordt opgebouwd door poolschoenen dicht bij het cirkelvormige anker.
- Lorentzkrachten werken radiaal op actieve geleiders (loodrecht op de straal).
- Nabij de neutrale lijn neemt de kracht af tot nul.

Wanneer het anker roteert:
- Opvolgende wikkelingen moeten van elektrische stroom worden voorzien.
- De stroomrichting wordt omgepoold door koolstofborstels en de commutator.
- Geleiders op de neutrale lijn dragen niet bij aan het koppel door een tangentiële krachtcomponent.

**Koolstofborstels en commutator:**
- Koolstofborstels maken contact met het anker via een commutator.
- De commutator bestaat uit koperen lamellen gescheiden door isolatiemateriaal.
- Koolstofborstels zorgen voor een continue stroom naar de wikkelingen.
- Door rotatie schakelt de commutator de stroomrichting, waardoor een constant koppel ontstaat.

De combinatie van koolstofborstels en commutator:
- Zorgt voor stroomtoevoer naar het anker.
- Schakelt de stroomrichting, zodat het magnetische veld een constante richting behoudt en rotatie ondersteunt.

### 3.4.3 Primair verschijnsel bij motorwerking

**Oorzaak toerental:**
1. Inductie
2. Stroom voerende geleiders
3. Lorentzkracht
4. Cylinder dus Lorentzkracht omgezet in koppel
5. Koppel veroorzaakt draaiende beweging
6. Toerental

### 3.4.4 Secundair verschijnsel bij motorwerking
De opwekking van de tegen-EMK $E$ is recht evenredig met het toerental $n$ en de flux $\phi$: 
$$
E = k_1 \cdot \phi \cdot n 
$$

waarbij $k_1$ de eerste machineconstante is. 
$$
k_{1}=s\cdot \frac{1}{S}\cdot l\cdot R\cdot \frac{2\pi}{60}
$$
De ankerstroom bij stilstand is: 
$$
I_{a,\text{aan}} = \frac{U_a}{R_a + R_{\text{aan}}} 
$$
De tegen EMK OB-machine
$$
E=U_{a}-R_{a_{tot}}\cdot I_{a}
$$
$$
k_{1}\cdot n\cdot \Phi=U_{a}-R_{a_{tot}}\cdot I_{a}
$$
$$
n=\frac{U_{a}-R_{a_{tot}}\cdot I_{a}}{k_{1}*\Phi}
$$

---
## 3.5 Anker reactie

### 3.5.1 Onbelast

Bij een onbelaste twee-polige gelijkstroommachine is de ankerstroom $I_{a,0}$ vrijwel nul, omdat de motor in nullast werkt. Het magnetisch veld, het hoofdveld $\phi_h$, wordt gegenereerd door de statorpolen. De neutrale lijn ($AB$) staat loodrecht op het hoofdveld en stroomwisselingen kunnen daar plaatsvinden.
![[Pasted image 20241229141347.png]]

### 3.5.2 Belast

Wanneer de gelijkstroommachine belast wordt, ontstaat er een ankerstroom $I_a$. Deze stroom genereert een ankerveld $\phi_a$, dat invloed heeft op het hoofdveld $\phi_h$. Het resulterende veld $\phi_\text{res}$ is de som van het hoofdveld en het ankerveld. Dit veroorzaakt:
- Verplaatsing van de neutrale lijn(loodrecht op het hoofdveld).
- Lokale verzadiging in de poolschoenen, wat de flux verzwakt.

De nadelige effecten van anker reactie zijn:
1. Fluxvermindering, wat leidt tot verminderde prestaties van de machine.
2. Vervorming van de neutrale lijn, wat commutatie bemoeilijkt en vonkvorming veroorzaakt.
3. Veranderingen in de anker reactie bij wisselende belasting.
![[Pasted image 20241229141737.png]]

**Ankerreactie**
![[Pasted image 20241229143115.png]]

### 3.5.3 Oplossingen voor anker reactie

#### Borstelverschuiving
- De borstels op de hoogte zetten van de verwachte verschoven neutrale lijn.
![[Pasted image 20241229143418.png]]

#### Compensatiewikkeling
- Deze wikkeling wordt aangebracht in de poolschoenen en staat in serie met het anker.
- Het opgewekte compensatieveld is tegengesteld aan het ankerveld.
- Toegepast bij zwaar belaste gelijkstroommachines.
![[Pasted image 20241229143432.png]]

#### Hulppolen
- Geplaatst tussen de hoofdpolen.
- Genereren een veld om de anker reactie lokaal te compenseren.
- Toegepast bij gelijkstroommachines met een klein vermogen.
![[Pasted image 20241229143443.png]]

---
## 3.6 Principe gelijkstroomdynamo

### 3.6.1 Principe

De werking van een dynamo is gebaseerd op de **Blv-regel**, die stelt dat wanneer een geleider een magnetisch veld snijdt, er een elektromotorische kracht (emk) wordt opgewekt. De grootte van de opgewekte spanning $E_{PQ}$ hangt af van:
- De magnetische flux $\phi$ of inductie $B$.
- De rotatiesnelheid $n$ (in toeren/min).
- De machineconstante $k_1$.

De formule voor de opgewekte spanning is:
$$
E_{PQ} = 2 \cdot B \cdot l \cdot v \cdot \sin{\alpha}
$$

Met:
- $B$: magnetische inductie,
- $l$: effectieve lengte van de geleider,
- $v$: snelheid van de geleider,
- $\alpha$: hoek tussen $v$ en $B$.
![[Pasted image 20241229143648.png]]

### 3.6.2 Dynamowerking

Wanneer een winding roteert in een homogeen magnetisch veld:
- Wordt de opgewekte spanning sinusvormig als functie van de positie van de winding in het veld.
- De polariteit van de spanning kan worden aangepast door de rotatierichting of veldpolariteit te veranderen.

De opgewekte spanning wordt gegeven door:
$$
E = k_1 \cdot \phi \cdot n
$$

Hierbij:
- $k_1$: machineconstante,
- $\phi$: flux in weber (Wb),
- $n$: toerental (t/min).

### 3.6.3 Primair verschijnsel

Het primaire effect is de opwekking van een spanning in de ankergeleiders door het snijden van de veldlijnen. De formule voor de opgewekte spanning is hetzelfde als hierboven.

### 3.6.4 Secundair verschijnsel

De opgewekte stroom $I_a$ in de ankergeleiders bevindt zich in een magnetisch veld en veroorzaakt een lorentzkracht:
$$
F = B \cdot l \cdot I_a
$$
Dit resulteert in een tegenwerkend koppel:
$$
M_{tot}=z'\cdot B\cdot l\cdot I_{a}\cdot_{2}R = z'\cdot l\cdot 2R\cdot \frac{1}{S}\cdot \Phi\cdot I_{a}
$$

---

- $F=B\cdot l\cdot I_{a}$
- $B=\frac{\Phi}{S}$


----

$$
M = k_2 \cdot \phi \cdot I_a
$$

---

- $k_{2}=z'\cdot l\cdot 2R\cdot \frac{1}{S}$

---

Met:
- $k_2$: tweede machineconstante,
- $\phi$: flux,
- $I_a$: ankerstroom.

Het koppel is evenredig met de flux en de ankerstroom.

![[Pasted image 20241229144444.png]]
$R_{a_{tot}}=R_{a}+R_{b}+R_{c}$


---
## 3.7 Vermogensverdeling OB-motor

### Inleiding

Bij de werking van een motor wordt elektrische energie omgezet in mechanische energie. Deze omzetting is echter niet volledig efficiënt. Een deel van de elektrische energie gaat verloren als warmte of mechanische verliezen.

![[Pasted image 20241229144628.png]]

### 3.7.1 Toegevoegd vermogen

Het toegevoegde vermogen aan de motor wordt gegeven door:
$$
P_t = U_a \cdot I_a
$$
Waarbij:
- $U_a$: aangelegde spanning,
- $I_a$: ankerstroom.

### 3.7.2 Koperen verliezen

De koperen verliezen ontstaan door weerstand in de wikkelingen. Het totale koperverlies is:
$$
P_{Cu} = R_{a,\text{tot}} \cdot I_a^2
$$
Waarbij $R_{a,\text{tot}}$ de totale weerstand van de wikkelingen omvat, inclusief eventuele hulppolen en compensatiewikkelingen.

### 3.7.3 Inwendig vermogen

Het inwendig vermogen, na aftrek van de koperen verliezen, wordt berekend als:
$$
P_i = P_t - P_{Cu} = U_{a}\cdot I_{a}-R_{a_{tot}}\cdot I_{a}^2 = E \cdot I_a
$$
Het overeenkomende inwendige koppel is:
$$
M_i = \frac{P_i}{\omega}
$$
Waarbij:
- $E$: gegenereerde tegen-emk,
- $\omega$: hoeksnelheid.

### 3.7.4 Mechanische verliezen

Mechanische verliezen omvatten:
- **Ventilatieverliezen** ($P_{\text{vent}}$): veroorzaakt door luchtverplaatsing,
- **Wrijvingsverliezen** ($P_{\text{wrij}}$): door lagers, borstels en commutator.

### 3.7.5 IJzerverliezen

IJzerverliezen zijn afhankelijk van de inductie en het toerental:
1. **Hysteresisverliezen**: energieverlies door magnetisatie en demagnetisatie.
2. **Wervelstroomverliezen**: geïnduceerde stromen in het ijzer, afhankelijk van het toerental.

Het totaal aan mechanische en ijzerverliezen wordt uitgedrukt als:
$$
P_v = P_{\text{Fe}} + P_{\text{vent}} + P_{\text{wrij}}
$$

### 3.7.6 Nuttig vermogen

Het nuttige vermogen dat beschikbaar is als mechanische energie wordt berekend met:
$$
P_n = P_i - P_v
$$
Het corresponderende nuttige koppel:
$$
M_n = \frac{P_n}{\omega}
$$

### 3.7.7 Rendement

Het rendement van de motor wordt bepaald door de verhouding tussen het nuttige vermogen en het toegevoegde vermogen:
$$
\eta = \frac{P_n}{P_t} \cdot 100\%
$$

Dit rendement is afhankelijk van de belasting en de ontwerpkenmerken van de motor.

---
## 3.8 Vermogensverdeling dynamo

![[Pasted image 20241229172108.png]]

Wanneer een gelijkstroommachine als dynamo werkt, wordt mechanisch vermogen ($P_t$) aan de as toegevoegd. Tijdens het draaien treden er verliezen op:
- **IJzerverliezen** ($P_{\text{Fe}}$),
- **Mechanische verliezen** ($P_{\text{vent+wrij}}$): ventilatie- en wrijvingsverliezen.

Het totaal van deze verliezen wordt aangegeven als $P_v$.

### Inwendig vermogen
Het inwendig vermogen van de dynamo wordt berekend door het mechanisch toegevoegd vermogen te verminderen met de verliezen:
$$
P_i = P_t - P_v = P_t - (P_{\text{Fe}} + P_{\text{vent+wrij}})
$$
Ook kan dit uitgedrukt worden als:
$$
P_i = E \cdot I_a
$$
waarbij:
- $E$: opgewekte spanning,
- $I_a$: ankerstroom.

### Nuttig vermogen
Het afgegeven of nuttig vermogen (nu elektrisch vermogen) wordt berekend als:
$$
P_n = P_i - P_{\text{Cu,anker}} = U_a \cdot I_a
$$
waarbij:
- $U_a$: klemspanning.

### Rendement
Het rendement van de dynamo wordt berekend door het nuttige vermogen te delen door het toegevoegde vermogen:
$$
\eta = \frac{P_n}{P_t} \cdot 100\%
$$

### Opmerkingen
- Bij de dynamo geldt dat $P_t$ mechanisch vermogen is, terwijl $P_n$ elektrisch vermogen is.
- De respectieve koppels kunnen worden afgeleid door de vermogens te delen door de hoeksnelheid $\omega$.

---

## 3.9 Kwadrantenwerking

De gelijkstroommachine kan zowel als motor als dynamo werken, afhankelijk van de richting van de stroom ($I_a$) en de opgewekte spanning ($E$). De werking wordt onderverdeeld in vier kwadranten, afhankelijk van:
- Het toerental ($n$),
- Het koppel ($M$),
- De energiestroom (positief of negatief).

### Kwadrantindeling
De kwadranten worden als volgt beschreven:

1. **Kwadrant I**: 
   - **Motorwerking**: De machine werkt als motor en neemt energie op.
   - $M > 0$, $n > 0$, energiestroom positief.
   - $E < U_a$ (opgewekte EMK kleiner dan de klemspanning).
   - Voorbeeld: normaal bedrijf van een motor.

2. **Kwadrant II**:
   - **Dynamowerking (genererend)**: De machine genereert energie met een positief toerental maar negatief koppel.
   - $M < 0$, $n > 0$, energiestroom negatief.
   - Voorbeeld: remmen via regeneratie in voertuigen.

3. **Kwadrant III**:
   - **Motorwerking (omgekeerd)**: De machine werkt als motor, maar met omgekeerde draairichting.
   - $M < 0$, $n < 0$, energiestroom positief.
   - Voorbeeld: achteruitrijden met een elektrisch aangedreven voertuig.

4. **Kwadrant IV**:
   - **Dynamowerking (genererend)**: De machine genereert energie met een negatief toerental en negatief koppel.
   - $M > 0$, $n < 0$, energiestroom negatief.
   - Voorbeeld: regeneratief remmen bij omgekeerde draairichting.

### Overzichtstabel
| **Kwadrant** | **M** | **n** | **Energiestroom** | **$U_a$** | **$E$** | **$I_a$** | **Verduidelijking** |
|--------------|--------|-------|-------------------|-----------|----------|----------|----------------------|
| I            | +      | +     | +                 | +         | $E < U_a$| +        | Motorwerking, energieopname |
| II           | -      | +     | -                 | +         | $E > U_a$| -        | Dynamowerking, energieafgifte |
| III          | -      | -     | +                 | -         | $E < U_a$| +        | Motorwerking, omgekeerde draairichting |
| IV           | +      | -     | -                 | -         | $E > U_a$| -        | Dynamowerking, energieafgifte bij omgekeerde draairichting |

![[Pasted image 20241229150838.png]]

### Conclusie
De kwadrantenwerking maakt het mogelijk om een gelijkstroommachine flexibel in te zetten als motor of dynamo, afhankelijk van de toepassingsvereisten.

---

## 3.10 Onafhankelijk bekrachtigde gelijkstroommotor

### 3.10.1 Equivalent schema
Het equivalent schema van de onafhankelijk bekrachtigde motor omvat een voorschakelweerstand $R_{\text{aan}}$, die dient om de ankerstroom te beperken tijdens het starten. 

![[Pasted image 20241229151111.png]]

### 3.10.2 Veldstroom
De veldwikkeling is aangesloten op een externe spanningsbron $U_v$. De veldstroom wordt berekend met:
$$
I_v = \frac{U_v}{R_v}
$$
Hierbij:
- $R_v$: weerstand van de veldwikkeling,
- $U_v$: spanning over de veldwikkeling.

Door het grote aantal windingen in de veldwikkeling is $I_v$ klein, maar het opgewekte magnetisch veld is relatief groot.

### 3.10.3 Ankerstroom
De ankerstroom wordt gegeven door:
$$
I_a = \frac{\overbrace{ U_a }^{ C^{te} } - \overbrace{ E }^{ Var }}{R_{a_{tot}}}
$$
Waarbij:
- $U_a$: klemspanning,
- $E$: tegen-emk,
- $R_{a,\text{tot}}$: totale weerstand van de ankerkring.

### 3.10.4 Koppelkarakteristiek
Het koppel wordt berekend met:
$$
M = \overbrace{ k_2 }^{ C^{te} } \cdot \overbrace{ \Phi }^{ C^{te} } \cdot I_a
$$
Bij een constante flux $\phi$ is het koppel evenredig met $I_a$. De koppelkarakteristiek is een rechte lijn door de oorsprong, waarbij een hogere ankerstroom resulteert in een groter koppel.
![[Pasted image 20241229151352.png]]

### 3.10.5 Toerentalkarakteristiek
Het toerental wordt gegeven door:
$$
n = \frac{U_a - R_{a,\text{tot}} \cdot I_a}{k_1 \cdot \phi}
$$
Bij een constante flux verloopt het toerental lineair met $I_a$. Belangrijke punten:
- Bij een kleine belasting blijft het toerental relatief constant.
- Bij een grote belasting daalt het toerental door de toenemende spanningsval over $R_{a,\text{tot}}$.

In nullast bereikt het toerental theoretisch:
$$
n_{\text{max}} = \frac{U_a}{k_1 \cdot \phi}
$$
Bij verlies van flux ($\phi = 0$) kan de motor "op hol slaan." Dit wordt voorkomen door veldbewaking in de stuurkring.

## 3.11 Shunt motor
Kan nooit op hol slaan, tenzij de flux wegvalt.
### 3.11.1 EQ Schema
![[Pasted image 20250109153407.png]]
### 3.11.2 Veldstroom
**Veldwikkeling:**
- veel wikkelingen
- aangesloten op ankerspanning
- hoge ohmse weerstand
- sterk inductief
- kleine veldstroom
- groot veld
- $I_{v}=\frac{U_{a}}{R_{v}}$
### 3.11.3 Ankerstroom
- $I_{a}=\frac{U_{a}-E}{R_{a_{tot}}}$
- Aanloopweerstand voor start stroom te beperken
- $I_{tot}=I_{a}+I_{v}$
- Grootste deel ankerstroom
### 3.11.4 Koppelkarakteristiek
- Constant Veld dus koppel recht evenredig met stroom $M=k_{2}\cdot \phi\cdot I_{a}$
### 3.11.5 Toerentalkarakteristiek
- $n=\frac{U_{a}-R_{a_{tot}}\cdot I_{a}}{k_{1}\cdot \phi}$
## 3.12 Seriemotor
### 3.12.1 EQ schema
![[Pasted image 20250109160313.png]]
### 3.12.2 Ankerstroom
- veldwikkeling in serie met anker
- ankerstroom is gelijk als e verldstroom
- veldwikkeling weinig wikkelingen en grote diameter
### 3.12.3 Koppelkarakteristiek
- $M=k_{2}\cdot \phi\cdot I_{a} \approx k_{2}'\cdot I_{a}^2$
- koppel kwadratisch afhankelijk van ankerstroom
### 3.12.4 Toerentalkarakteristiek
- $n=\frac{U_{a}-R_{a_{tot}}\cdot I_{a}}{k_{1}\cdot \phi}$
- $n=\frac{U_{a}-R_{a_{tot}}\cdot I_{a}}{k_{1}'\cdot I_{a}}$
- Motor kan op hol slaan als de ankerstroom daalt
- toerental is sterk afhankelijk van de belasting
- als er geen belasting is dan zal de motor op hol slaan
## 3.13 Toerentalvariatie van de OB-motor
$$
n=\frac{U_{a}-R_{a_{tot}}\cdot I_{a}}{k_{1}\cdot \phi}=n=\frac{U_{a}-R_{a_{tot}}\cdot I_{a}}{}
$$