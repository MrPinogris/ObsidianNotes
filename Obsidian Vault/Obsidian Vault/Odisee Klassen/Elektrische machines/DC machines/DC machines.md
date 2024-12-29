# Gelijkstroommachines

## 3.1 Inleiding

De term *elektrische machine* verwijst naar een apparaat waarbij elektrische energie wordt omgezet in mechanische energie of omgekeerd. Deze machines zijn elektromechanische omzetters van energie. Gelijkstroommachines kunnen worden onderverdeeld in:

- **Dynamo's**: zetten mechanische energie om in elektrische energie.
- **Motoren**: zetten elektrische energie om in mechanische energie.

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
## 3.3.2 De types bekrachtiging

Gelijkstroommachines worden verder ingedeeld op basis van de methode waarmee de veldstroom wordt opgewekt:

1. **Onafhankelijke bekrachtiging**:
   - De veldstroom wordt geleverd door een externe spanningsbron.
   - Deze machines worden OB-machines genoemd.
   - Aanduidingen:
     - **Ankerwikkeling**: $A_1 - A_2$
     - **Veldwikkeling**: $F_1 - F_2$

2. **Eigen of zelfbekrachtiging**:
   - De veldstroom wordt opgewekt door de machine zelf.
   - Onderverdeling:
     - **Seriemotor**: veldwikkeling in serie met ankerwikkeling ($D_1 - D_2$).
     - **Shuntmotor**: veldwikkeling in parallel met ankerwikkeling ($E_1 - E_2$).
     - **Compoundmotor**: combinatie van serie- en shuntwikkeling.

### Klemmaanduidingen

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
Een gelijkstroommotor werkt op basis van het effect van een magnetische flux $\phi$ op een stroom voerende geleider. Dit genereert een lorentzkracht, gegeven door: $$ F = B \cdot l \cdot I_a $$ waarbij: - $B$: inductie (in het magnetisch veld), - $l$: effectieve lengte van de geleider, - $I_a$: ankerstroom. Wanneer de hoek tussen $B$ en $I_a$ niet loodrecht is, wordt de kracht: $$ F = B \cdot l \cdot I_a \cdot \cos{\alpha} $$ 
### 3.4.2 Motorwerking Het anker draait in het magnetisch veld door het resulterende koppel: 
$$ M = F \cdot d = k_2 \cdot \phi \cdot I_a $$
waarbij $k_2$ de tweede machineconstante is. ### 3.4.3 Tegen-EMK en toerental De opwekking van de tegen-EMK $E$ is recht evenredig met het toerental $n$ en de flux $\phi$: 
$$ E = k_1 \cdot \phi \cdot n $$
waarbij $k_1$ de eerste machineconstante is. De ankerstroom bij stilstand is: 
$$ I_{a,\text{aan}} = \frac{U_a}{R_a + R_{\text{aan}}} $$

---
## 3.5 Ankerreactie

### 3.5.1 Onbelast

Bij een onbelaste twee-polige gelijkstroommachine is de ankerstroom $I_{a,0}$ vrijwel nul, omdat de motor in nullast werkt. Het magnetisch veld, het hoofdveld $\phi_h$, wordt gegenereerd door de statorpolen. De neutrale lijn ($AB$) staat loodrecht op het hoofdveld en stroomwisselingen kunnen daar plaatsvinden.

### 3.5.2 Belast

Wanneer de gelijkstroommachine belast wordt, ontstaat er een ankerstroom $I_a$. Deze stroom genereert een ankerveld $\phi_a$, dat invloed heeft op het hoofdveld $\phi_h$. Het resulterende veld $\phi_\text{res}$ is de som van het hoofdveld en het ankerveld. Dit veroorzaakt:
- Verplaatsing van de neutrale lijn.
- Lokale verzadiging in de poolschoenen, wat de flux verzwakt.

De nadelige effecten van ankerreactie zijn:
1. Fluxvermindering, wat leidt tot verminderde prestaties van de machine.
2. Vervorming van de neutrale lijn, wat commutatie bemoeilijkt en vonkvorming veroorzaakt.
3. Veranderingen in de ankerreactie bij wisselende belasting.

### 3.5.3 Oplossingen voor ankerreactie

#### Compensatiewikkeling
- Deze wikkeling wordt aangebracht in de poolschoenen en staat in serie met het anker.
- Het opgewekte compensatieveld is tegengesteld aan het ankerveld.
- Toegepast bij zwaar belaste gelijkstroommachines.

#### Hulppolen
- Geplaatst tussen de hoofdpolen.
- Genereren een veld om de ankerreactie lokaal te compenseren.
- Toegepast bij gelijkstroommachines met een klein vermogen.

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
M = k_2 \cdot \phi \cdot I_a
$$

Met:
- $k_2$: tweede machineconstante,
- $\phi$: flux,
- $I_a$: ankerstroom.

Het koppel is evenredig met de flux en de ankerstroom.

---
## 3.7 Vermogenverdeling motor

### Inleiding

Bij de werking van een motor wordt elektrische energie omgezet in mechanische energie. Deze omzetting is echter niet volledig efficiënt. Een deel van de elektrische energie gaat verloren als warmte of mechanische verliezen.

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
P_i = P_t - P_{Cu} = E \cdot I_a
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
