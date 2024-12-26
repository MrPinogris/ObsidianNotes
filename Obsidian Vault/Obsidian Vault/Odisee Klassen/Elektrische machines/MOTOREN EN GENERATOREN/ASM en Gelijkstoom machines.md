## Slip
### Absolute slip
Ontstaat door toerental verschil tussen het draaiveld ($n_{s}$)(synchrone toerental) en het rotor toerental ($n_{r}$).
De absolute slip ($s_{a}$) is het toerental verschil tussen $n_{s}$  $n_{r}$ kan berekend worden met deze formule:
$$s_{a}=n_{s}-n_{r}=\frac{60}{2\pi}*(\omega_{s}-\omega_{r})$$
### Relative slip
De relatieve slip $s$ wordt gedefinieerd als de verhouding tussen de absolute slip het synchrone toerental:
 $$s=\left( \frac{n_{s}-n_{r}}{n_{s}} \right)=\left(\frac{\omega_{s}-\omega_{r}}{\omega_{s}}\right)$$
De relatieve slip wordt $s$ genoemd en heeft geen eenheid
### Procentuele slip
Relatieve slip die in '%' word uitgeschreven. ==De nominale slip binnen het werkingsgebied van een ASM ligt tussen 2% en 8%.==
### Formules
$$n_r=n_{s}(1-s)$$
 $$\omega_{r}=\omega_{s}(1-s)$$
### Bijzondere punten gevisualiseerd
![[Pasted image 20241223163810.png]]
- Klein werkingsgebied $n_{r}^n\to n_{r}^0$
### Formules en Concepten

#### 1. Definitie van slip ($s$):
$$s = \frac{n_s - n_r}{n_s}$$

Waarbij:
- $n_s$ = Synchrone snelheid
- $n_r$ = Rotorsnelheid

#### 2. Bijzondere punten:

- **Wanneer $n_r = 0$ (stilstaande rotor):**
  $$
  s = \frac{n_s - 0}{n_s} = 1
  $$
  (Maximale slip, motor in opstartfase.)

- **Wanneer $n_r = n_s$ (synchrone snelheid):**
  $$
  s = \frac{n_s - n_s}{n_s} = 0
  $$
  (Geen slip, theoretisch ideaal punt voor motorwerking, maar niet realistisch voor ASM.)

- **Wanneer $n_r > n_s$ (rotor sneller dan het draaiveld):**
  $$
  s < 0
  $$
  (Negatieve slip, wat duidt op **generatorwerking**.)

- **Wanneer $n_r < 0$ (rotor draait in tegengestelde richting van het draaiveld):**
  $$
  s > 1
  $$
  (Motor onder extreme belasting of andere remwerking.)

#### 3. Typische waarden voor motorwerking:
- Voor een goed werkende ASM in **motorwerking** ligt de slip bij nominale belasting meestal tussen:
  $$
  s = 0.03 \text{ (3\%) en } s = 0.07 \text{ (7\%)}
  $$

- Voor de nominale slip:
  $$
  s_n \approx 4\% \quad \text{(voorbeeldwaarde afhankelijk van de machine).}
  $$

## Frequentieafhankelijke grootheden
#### Stator
$$E_{1}=4,44*f_{s}*n_{s}*\Phi$$
$$x_{1}=\omega_{s}*L_{1}$$
- Draaiveld 
$$n_{s}=\frac{60*f_{s}}{\eta}\implies f_{s}=\frac{(n_{s}-0)*\eta}
{60}$$
#### Rotor
$$f_r=\frac{(n_{s}-n_{r})*p}{60}
=\frac{(n_{s}-n_{r})*p*n_{s}}{60*n_{s}}
=s*f_{s}\implies f_{s}=\frac{(n_{s}-0)*p}{60}$$
### EMK
#### Stator
- Stilstand$$E_{1}=4,44*n_{s}*f_{s}*\Phi$$
#### Rotor
- Stilstand
$$E_{2(st)}=4,44*n_{r}*f_{s}*\Phi$$
- Draaiend
$$E_{2}=4,44*n_{r}*f_{r}*\Phi$$
- Met $n_{r}\to Draaien$
$$E_{2}=4,44*n_{r}*s*f_{r}*\Phi$$$$E_{2}=s*E_{2(st)}=s*\frac{E_{1}}{k}$$
#### Vergelijking
- Stilstand$$\frac{E_{1}}{E_{2(st)}}=\frac{N_{s}}{N_{r}}=k\to E_{2(st)}=\frac{E_{1}}{k}$$
- Draaiend
	- $E_{2}$ stijgt als de slip stijgt de dichter s bij 1 de groter $E_{2}$ als $s = 1$ dan $E_{2(st)}=\frac{E_{1}}{k}=MAX$ 

### Rotorreactantie $X_{2}$
De lekfluxen sluiten zich vooral over de lucht, zijn recht evenredig met hun stromen. In fase met de hun opgewekte stromen. De reactantie is max bij stilstand.

Stilstand$$X_{2(st)}=\omega_{s}L_{2}=2\pi f_{s}L_{2}$$Draaiend$$X_{2}=\omega_{r}L_{2}=2\pi f_{r}L_{2}=s*X_{2(st)}$$
Bij nominaal toerental zal $X_{2(n)}$ een fractie zijn van $X_{2(st)}$, namelijk $s_{n}$.
## Inwendig koppel
Start formule afgeleid van het luchtspleetvermogen
$$
P_{L}=3\cdot \frac{R_{2}}{s}\cdot I^2_{2}
$$
$$
\begin{align}
M_{i}\\
\approx\frac{P_{i}}{\omega} \implies P_{i}=3*\frac{1-s}{s}*R_{2}*I^2_{F_{2}} \\
\implies I_{2}=\frac{E_{2(st)}}{\sqrt{\left( \frac{ R_{2}}{s} \right)^2+X_{2(st)}^2 }}  \\

\implies M_{i}\approx3\cdot\frac{R_{2}}{\omega_{s}}\cdot \frac{U^2_{1}}{k^2}\cdot \frac{s}{R^2+s^2\cdot X^2_{2_{st}}} \\
\approx \frac{1}{\omega_{s}}\cdot3\cdot \frac{U^2_{1}}{k^2}\cdot \frac{s\cdot R_{2}}{R_{2}^2+s^2\cdot X_{2_{st}}^2}
\end{align}
$$
==**Hier zijn de stator weerstand en -reactantie verwaarloost zodat de aangelegde spanning gelijk kon gesteld worden aan de regen EMK**==
##### Enkele parameters die vast zijn
- $\omega _s\implies f_{s}$
- $U_{1}^2$
- $R_{2}$
- $X_{2_{st}}$
##### Variabele parameter
- $s\to f(s)$
### Formule
$$
M_{i}=f(s)
$$
of
$$
M_{i}=f(n_{r})
$$
$$
M_{i}\approx \cancel{ \frac{1}{\omega_{s}}\cdot3\cdot \frac{U^2_{1}}{k^2} }\cdot \frac{s\cdot \cancel{ R_{2} }}{R_{2}^2+s^2\cdot X_{2_{st}}^2}
$$
Vervangen door een constante
$$
M_{i}\approx C^{te}\cdot \frac{s}{R_{2}^2+s^2\cdot X_{2_{st}}^2}
$$
Het inwendig koppel is het tegenwerkend koppel of het werktuig plus het verlieskoppel aan wrijvings- en  de ventielatie verliezen
$$
M_{i}=M_{v}+M_{W}\underbrace{ \implies }_{ \text{als de machiene in statische toestand is} } M_{i}=M_{T}
$$
### Belangrijke punten

#### Uitleg
- Het werkingsgebied is Tussen $M_{i_{n}}$ en $M_{i_{0}}$
- Als de motor teveel belast wordt, wordt de motor overbelast en dus zal er een overstroom vloeien die niet goed is voor de motor.
#### Slip moment karakteristiek
- $M_{i}=0\implies s=0\implies n_{r}=n_{s}\implies v_{rel}=0$
- $M_{i}\to{0}\implies s\to \pm\infty$
- $M_{i}>0$
- $\pm M_{i_{st}}\implies s=\pm1$
- $M_{i}=max\implies s=s_{k}$
![[Pasted image 20241225091939.png]]

### Kipslip
#### Kenmerken
##### Betekenis
- Bij $s_{k}$ bereikt de motor zijn maximale koppel
- Belangrijk voor de stabiliteit van de motorwerking; als de slip groter wordt dan $s_k$, zal de motor te traag draaien of zelfs stilvallen.
##### Belangrijke parameters
- Als de rotorweerstand $R_{2}$ zal de kipslip verschuiven naar een hogere waarde
##### Formule
$$
s_{k}=\frac{R_{2}}{X_{2_{st}}}
$$
##### Afgeleid
Kipslip is de behaald door het afgeleide te nemen van de formule van het moment
$$
M_i = C^{te} \cdot \frac{s \cdot R_2}{R_2^2 + (s \cdot X_{2,ST})^2}
$$
$$
\frac{\partial}{\partial s} \left( \frac{s \cdot R_2}{R_2^2 + (s \cdot X_{2,ST})^2} \right) = 
\frac{R_2 \cdot \left( R_2^2 + (s \cdot X_{2,ST})^2 \right) - s \cdot R_2 \cdot 2 \cdot s \cdot X_{2,ST}^2}{\left( R_2^2 + (s \cdot X_{2,ST})^2 \right)^2}
$$
$$
R_2 \cdot (R_2^2 + (s \cdot X_{2,ST})^2) = s \cdot R_2 \cdot 2 \cdot s \cdot X_{2,ST}^2
$$
$$
R_2^2 + (s \cdot X_{2,ST})^2 = 2 \cdot s^2 \cdot X_{2,ST}^2
$$
$$
R_2^2 = s^2 \cdot X_{2,ST}^2
$$
$$
s_k = \frac{R_2}{X_{2,ST}}
$$

##### In het kort
De kipslip is de slipwaarde bij maximaal koppel. Het is cruciaal voor het ontwerpen en begrijpen van de belasting die een ASM aankan zonder in instabiliteit te raken.

### Statische werking ASM $n_{r}=C^{te}$
#### Alegemeen
Toerental motor is constant en in het werkingsgebied dan is de motor bruikbaar voor het werktuig.
==Het statisch werktuig moet gelegen zijn in het werkingsgebied van de motor==
![[Pasted image 20241225102509.png]]
#### Beste motor voor statisch werktuig
Je kiest best een motor die een koppel nodig heeft ==net onder het nominaal koppel== en boven de nullast koppel
### Dynamische werking ASM $n_r \neq C_{te}$
#### Algemeen
$$
M_i = M_T + M_J = M_T + J \cdot \frac{d\omega}{dt} = M_T + J \cdot \alpha
$$

- $M_T$ als het tegenwerkend koppel $[\text{Nm}]$
- $J$ als het traagheidsmoment $[\text{kg} \cdot \text{m}^2]$
- $\alpha$ als de hoekversnelling $[\text{rad/s}^2]$: 
  $$
  \alpha = \frac{\Delta \omega_r}{\Delta t}
  $$

---

#### Uitleg over dynamische werking
Een aandrijving (combinatie motor en belasting) bevindt zich in een **dynamische toestand** wanneer het rotortoerental ($n_r$) niet constant is. Dit betekent dat de motor versnelt of vertraagt, afhankelijk van:
- Het verschil tussen het intern gegenereerd koppel ($M_i$) en het tegenwerkend koppel ($M_T$).
- De hoeksnelheidsverandering $\alpha$, die het effect van het traagheidsmoment ($J$) bepaalt.

---

#### Versnellingsmoment
Het **versnellingsmoment** $M_J$ beschrijft de dynamische reactie van het systeem:
$$
M_J = J \cdot \alpha = J \cdot \frac{d\omega}{dt}
$$

Het totale intern gegenereerde koppel $M_i$ wordt gegeven door:
$$
M_i = M_T + M_J
$$
Hieruit volgt:
$$
M_i = M_T + J \cdot \alpha
$$

---

#### Belang van versnellingskoppel
- Het verschil tussen het **motorkoppel** en het **belastingkoppel** bepaalt de versnelling of vertraging van de rotor.
- Wanneer $M_T > M_i$, zal de rotor vertragen.
- Wanneer $M_i > M_T$, zal de rotor versnellen.

---

#### Opmerking
- Als het belastingkoppel op een bepaald moment groter is dan het maximaal beschikbare motorkoppel (bijvoorbeeld bij een te hoge belasting of bij stilstand), kan de motor niet starten.
- Dit wordt ook wel het **losbreekkoppel** genoemd.![[Pasted image 20241225113115.png]]
#### Dynamische werking ASM $n_r \neq C_{te}$
##### Grafische voorbeelden

Hieronder worden twee voorbeelden van de dynamische werking van een asynchrone motor grafisch weergegeven. Deze laten zien hoe het intern gegenereerde koppel ($M_i$), het belastingkoppel ($M_T$), en het versnellingsmoment ($M_J$) zich gedragen in verschillende situaties.

---

##### Voorbeeld 1: Dynamische werking bij statische en dynamische situaties
![[Pasted image 20241225113409.png]]

- **Statisch punt**:
  - Het systeem is in evenwicht als $M_i = M_T$.
  - Geen versnelling: $\alpha = 0$.

- **Dynamische punten**:
  - Wanneer $M_i > M_T$, is $M_J > 0$ en versnelt de motor ($\alpha > 0$).
  - Wanneer $M_i < M_T$, is $M_J < 0$ en vertraagt de motor ($\alpha < 0$).

---

##### Voorbeeld 2: Dynamische werking bij starten en overbelasting
![[Pasted image 20241225113424.png]]

- **Opstartfase**:
  - Bij stilstand ($n_r = 0$), moet $M_i > M_T$ om de motor te laten starten.
  - Als $M_i < M_T$, zal de motor niet starten ($\alpha = 0$).

- **Overbelasting**:
  - Als het belastingkoppel ($M_T$) groter is dan het maximale motorkoppel ($M_{i,\text{max}}$), kan de motor niet accelereren of zelfs volledig stilvallen.

---

#### Toelichting
Deze grafieken illustreren de relatie tussen de verschillende koppels en de resulterende hoeksnelheid. Het verschil tussen $M_i$ en $M_T$ bepaalt of de motor versnelt of vertraagt.
### Toerentalvariatie

#### Algemeen
De formule voor het rotortoerental van een asynchrone motor:
$$
n_r = n_s \cdot (1 - s) = \frac{60 \cdot f_s}{p} \cdot (1 - s)
$$

Hieruit volgen drie methoden om het rotortoerental te beïnvloeden:
1. **Aantal polen ($p$) aanpassen.**
2. **Frequentie ($f_s$) van de netspanning wijzigen.**
3. **Slip ($s$) aanpassen:**
   - Door wijziging van de rotorweerstand ($R_2$).
   - Door wijziging van de statorspanning ($U_1$).

---

#### 2.13.1 Poolomschakelbare motoren

##### 2.13.1.1 Meervoudige statorwikkelingen
- Elke statorwikkeling heeft een vast aantal polen.
- Meerdere statorwikkelingen maken verschillende rotatiesnelheden mogelijk:
  - Bijvoorbeeld 2p = 4/6, 6/8, of 8/10.
- Dit zorgt voor meerdere synchrone toerentallen.
![[Pasted image 20241225115817.png]]
![[Pasted image 20241225114750.png]]

##### 2.13.1.2 Dahlandermotor
- Dahlander-motor gebruikt één statorwikkeling.
- De statorwikkeling kan in verschillende schakelingen worden gezet:
  - **Driehoekschakeling:** Voor lage snelheid.
  - **Dubbelsterschakeling:** Voor hoge snelheid.
- Dit zorgt voor een factor-2 verschil in rotatiesnelheid.

![[Pasted image 20241225114853.png]]

---

#### 2.13.2 Frequentieregeling
- Door de frequentie van de netspanning te variëren, verandert de synchrone snelheid:
  $$
  n_s = \frac{60 \cdot f_s}{p}
  $$
- Regelbereik:
  - **Frequenties kleiner dan nominale frequentie:** Constant veld, behoud van nominaal koppel.
  - **Frequenties groter dan nominale frequentie:** Gebied met veldverzwakking; koppel vermindert.

![[Pasted image 20241225115150.png]]

---

#### 2.13.3 Variatie van de slip

##### 2.13.3.1 Variatie van de statorspanning
- Verlagen van de statorspanning ($U_1$) verlaagt het koppel.
- Formule kipkoppel ($M_k$):
  $$
  M_k \propto \frac{U_1^2}{f_s^2}
  $$
- Het toerental van de motor daalt naarmate het koppel afneemt.

![[Pasted image 20241225115422.png]]

##### 2.13.3.2 Variatie van de rotorweerstand
- Vergroting van de rotorweerstand ($R_2$) verhoogt de slip bij het maximum koppel:
  $$
  s_k = \frac{R_2}{X_{2,ST}}
  $$
- Hierdoor kan het aanloopkoppel worden verbeterd.

![[Pasted image 20241225115442.png]]

---

#### Grafieken en tabellen
- Diverse grafieken en schema's worden gebruikt om de invloed van bovenstaande methoden te visualiseren.
- Bekijk grafieken voor:
  - Relatie tussen statorspanning en koppel.
  - Invloed van rotorweerstand op slip en koppel.

---

### 2.14 Stroom-toerentalkarakteristiek

#### Inleiding
Bij het starten van een asynchrone motor vloeit er een stroom door de stator die veel groter is dan de nominale stroom. Deze grote aanloopstroom heeft gevolgen:
- **Netspanning:** Spanning in het net kan aanzienlijk dalen.
- **Motorwikkelingen:** Kans op schade door hoge temperaturen.

Om dit te beperken worden methoden gebruikt, zoals verlaging van de statorspanning of verhoging van de rotorweerstand.

#### Rotorstroom en slip
De rotorstroom $I_2$ in functie van de slip $s$ wordt gegeven door:
$$
I_2 = \frac{E_{2,ST}}{\sqrt{\left( \frac{R_2}{s} \right)^2 + X_{2,ST}^2}}
$$

![[Pasted image 20241226092138.png]]

---

#### Equivalentieschema in context van stroom-toerentalkarakteristiek
Het equivalentieschema van de asynchrone motor is essentieel om:
1. **Stromen en spanningen te berekenen** bij verschillende punten van de slip ($s$).
2. **Reflectie versus geen reflectie**:
   - **Met reflectie:** Rotorimpedantie ($R_2$ en $X_{2,ST}$) wordt omgerekend naar de statorgrootheden.
   - **Zonder reflectie:** Rotor- en statorgrootheden blijven afzonderlijk, wat een directe analyse van $I_2$ mogelijk maakt.

Het equivalentieschema wordt als volgt gebruikt in deze context:
- **Reflectie:** Toegepast om stroomwaarden in de stator ($I_1$) en rotor ($I_2$) te koppelen.
- **Geen reflectie:** Nuttig om de rotorparameters onafhankelijk te analyseren.

#### Toepassing van het schema
- **Bij s = 0** (synchrone snelheid): Impedantie van de rotor is oneindig groot ($I_2 = 0$).
- **Bij s = 1** (aanloopfase): Rotorimpedantie is minimaal, maximale stroom.

![[Pasted image 20241226094315.png]]

---

#### Statorstroom en slip
Voor de statorstroom $I_1$ geldt de formule:
$$
\overline{I_1} = \overline{I_0} + \left(- \frac{1}{k}\right) \cdot \overline{I_2}
$$

De aanloopstroom ($I_{1,ST}$) wordt uitgedrukt als:
$$
I_{1,ST} = \frac{U_1}{\sqrt{(R_1 + k^2 \cdot R_2)^2 + (X_1 + k^2 \cdot X_{2,ST})^2}}
$$

![[Pasted image 20241226092212.png]]

---

#### Bijzondere punten
- **$s = 0$ (synchrone snelheid):**
  - $I_2 = 0$
  - $I_1 = I_0$

- **$s = 1$ (stilstand):**
  - $I_2 = I_{2,ST}$
  - $I_1 = I_{1,ST}$

- **$s \to -\infty$ (tegengestelde rotatie):**
  - Maximale $I_2$ en $I_1$.

| Slip ($s$)       | Situatie                                   | Rotorstroom ($I_2$)                       | Statorstroom ($I_1$)                   |
|-------------------|-------------------------------------------|-------------------------------------------|----------------------------------------|
| $s = 0$          | Synchrone snelheid                        | $I_2 = 0$                                 | $I_1 = I_0$                            |
| $s = 1$          | Stilstand (aanloopfase)                   | $I_2 = I_{2,ST}$                          | $I_1 = I_{1,ST}$                       |
| $s = -1$         | Tegengestelde rotatie                     | Maximale $I_2$                            | Maximale $I_1$                         |
| $s \to +\infty$  | Rotor draait oneindig traag               | $I_2 \to 0$                               | $I_1 \to I_0$                          |
| $s \to -\infty$  | Rotor draait oneindig snel in tegengestelde richting | Maximale $I_2$                            | Maximale $I_1$                         |

---

#### Beperken van de aanloopstroom
Manieren om de aanloopstroom te beperken:
1. Verlagen van de statorspanning.
2. Verhogen van de stator- of rotorweerstand.
3. Gebruik van reactantie.
![[Pasted image 20241226092541.png]]


---
### 2.15 Aanloopmethodes

#### Inleiding
Aanloopmethodes worden gebruikt om de aanloopstroom en het aanloopkoppel van asynchrone motoren te beheersen. Verschillende methodes worden ingezet afhankelijk van het type motor en de toepassingsvereisten.

---

#### 2.15.1 Directe aanloop
- **Toepassing**: Geschikt voor motoren met klein vermogen of motoren aangesloten op een net met lage impedantie.
- **Kenmerken**:
  - Motor wordt direct verbonden met de netspanning.
  - Maximale aanzetkoppel ($M_{i,ST}$).
  - Aanloopstroom ($I_{1,ST}$) wordt niet beperkt.
- **Werking**:
  - Driepolige handschakelaar of automatische start-stop schakeling wordt gebruikt.
  - Beveiligingen (zoals thermische beveiliging) worden toegepast om de motor te beschermen.

![[Pasted image 20241226094415.png]]

---

#### 2.15.2 Verlaagde spanning

#### 2.15.2.1 Ster-driehoek aanloop
- **Toepassing**: Alleen geschikt voor motoren die in bedrijfstoestand in driehoek geschakeld worden.
- **Werking**:
  1. Start in sterconfiguratie om spanning en stroom te verlagen.
  2. Overschakeling naar driehoek bij ongeveer $0,8 \cdot n_n$.

- **Kenmerken**:
  - Aanloopstroom wordt verlaagd met een factor $\sqrt{3}$.
  - Aanloopkoppel is beperkt tot 1/3 van het nominale koppel.
![[Pasted image 20241226094439.png]]
##### Belangrijke opmerking (mogelijke examenvraag)
- **Vraag**: Waarom moet de omschakeling van ster naar driehoek bij $0,8 \cdot n_n$ gebeuren?
- **Antwoord**: Om stroompieken en activering van thermische beveiligingen te voorkomen.

##### 2.15.2.2 Spaartransformator
- **Werking**: Gebruik van een regelbare transformator om de motorspanning tijdens aanloop te verlagen.
- **Kenmerken**:
  - Verlaagd de aanloopstroom ($I_1 \propto k^2$).
  - Verlaagd aanloopkoppel evenredig met de spanningsreductie.

---

##### 2.15.2.3 Stator aanzetweerstanden
- **Toepassing**: Impedanties in serie met de statorwikkelingen verminderen de aanloopstroom.
- **Kenmerken**:
  - Vermindert aanloopkoppel sterk.
  - Alleen geschikt voor onbelaste aanloop.
  - Weerstanden worden trapsgewijs uitgeschakeld.

---

#### 2.15.3 Rotorweerstanden
- **Toepassing**: Bij motoren met een bewikkelde rotor (sleepringmotoren).
- **Kenmerken**:
  - Verhoogt de slip bij maximaal koppel.
  - Verhoogt aanloopkoppel.
  - Wordt trapsgewijs uitgeschakeld naarmate de motor accelereert.

![[Pasted image 20241226094629.png]]

---

#### Conclusie
De keuze van de aanloopmethode hangt af van de toepassing, het gewenste aanloopkoppel, en de stroombeperkingen. Directe aanloop is geschikt voor kleine motoren, terwijl geavanceerde methodes zoals ster-driehoek en spaartransformatoren worden gebruikt bij grotere belastingen.

---

Gebruik de genoemde plaatsen om de relevante figuren en grafieken toe te voegen. Laat me weten als je meer verduidelijking nodig hebt of een andere sectie wilt uitbreiden! 😊

#### Conclusie
- De stroom-toerentalkarakteristiek is essentieel voor het analyseren van het gedrag van de ASM bij verschillende slips.
- Bijzonder belangrijk bij de startfase om schade te voorkomen en een efficiënte werking te garanderen.
## Links
- [[ASM motorprincipe]]
- [[ASM Generatorprincipe]]
