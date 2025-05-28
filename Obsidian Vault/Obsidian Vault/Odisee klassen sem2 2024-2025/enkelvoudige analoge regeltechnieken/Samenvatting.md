## Hoofdstuk 2: De meerstanden-regelaar

### Korte samenvatting
In dit hoofdstuk wordt de meerstanden-regelaar behandeld: een eenvoudige regelaar die werkt met meerdere ingestelde spanningsniveaus (trappen). De uitgang verandert sprongsgewijs afhankelijk van de grootte van het meetsignaal. De regelaar is niet continu maar werkt volgens vaste drempelwaarden.

---

### Kernbegrippen en theorie

#### Meerstanden-regelaar
Een meerstanden-regelaar (of stappenregelaar) is een regelaar waarvan de uitgang slechts een beperkt aantal discrete standen kan aannemen. Deze standen zijn afhankelijk van het meetsignaal en vaste grenswaarden.

Er bestaan:
- **2-standen regelaars** (binaire regeling: enkel aan/uit),
- **3-standen regelaars** (b.v. verwarmen–niets–koelen),
- **n-standen regelaars** (waarbij de uitgang n discrete waarden kan aannemen).

#### Toepassing
Dergelijke regelaars worden gebruikt in systemen waar een continu regelgedrag niet noodzakelijk is of te complex is. Typische voorbeelden zijn elektrische verwarmingselementen met meerdere vermogensniveaus, of ventilatoren met drie snelheden.

#### Hysteresis
Om te vermijden dat een regelaar continu aan en uit schakelt bij kleine schommelingen rond een drempelwaarde, wordt vaak hysteresis toegevoegd. Dat betekent dat er een verschil is tussen de inschakel- en uitschakeldrempel.

---

### Formules

#### 1. 2-standen regelgedrag:
Er is geen expliciete wiskundige formule opgegeven, maar het gedrag kan als volgt beschreven worden:

- Als $e(t) > d$ → $u(t) = U_{max}$
- Als $e(t) < -d$ → $u(t) = U_{min}$

**Uitleg:**
- $e(t)$: het regelsignaal op tijdstip $t$ (meetsignaal – referentie)
- $d$: drempelwaarde (positieve waarde)
- $u(t)$: uitgangssignaal op tijdstip $t$
- $U_{max}$ en $U_{min}$: maximale en minimale uitgangswaarden

**Herkomst:** afkomstig uit praktische implementatie van 2-standen regelaars met hysteresis

**Belang:** deze logica is cruciaal om ongewenst pendelgedrag rond de nul te voorkomen.

**Voorbeeld:**
Stel dat een thermostaat in een oven werkt met:
- $d = 1\ ^\circ$C
- $U_{max}$ = verwarming aan
- $U_{min}$ = verwarming uit

Als de temperatuur onder de gewenste temperatuur - 1°C zakt, gaat de verwarming aan. Als hij boven gewenste +1°C komt, gaat hij uit.

---

### Mogelijke examenvragen

1. Leg uit wat een meerstanden-regelaar is en geef een voorbeeld van een toepassing.
2. Wat is het nut van hysteresis in een 2-standen-regelaar?
3. Schets het uitgangsgedrag van een 3-standen-regelaar en leg uit hoe de drempelwaarden worden ingesteld.
4. Waarom is een meerstanden-regelaar geen continue regelaar?

---

### Studietips

- Begrijp het verschil tussen continue en discrete regeling.
- Focus op het grafisch gedrag van de uitgang in functie van het regelsignaal.
- Oefen met praktische toepassingen: stel zelf een 2- of 3-standen regeling op voor een systeem naar keuze.
- Begrijp het belang van hysteresis en hoe dit pendelen voorkomt.

---
## Hoofdstuk 4: De I-regelactie

De I-regelactie (integrerende regelaar) wordt gebruikt wanneer er geen statische fout mag zijn in de regeling. Dit hoofdstuk behandelt de werking, kenmerken en beperkingen van de I-regelaar en hoe deze zich gedraagt in combinatie met een eerste orde systeem. Ook de praktische implementatie en typische toepassingen worden besproken.

---

### Kernbegrippen en theorie

#### I-regelactie (Integrerende regelaar)
Een I-regelaar produceert een uitgangssignaal dat evenredig is met de **geïntegreerde waarde van het ingangssignaal** (de fout). Dit betekent dat zelfs een kleine constante fout op termijn een steeds groter regelaarsignaal zal veroorzaken, wat leidt tot nul statische fout.

- **Eigenschap**: een I-regelaar elimineert de statische fout volledig.
- **Traagheid**: de integratie veroorzaakt traag gedrag; de reactie op verstoringen is langzaam.
- **Nadeel**: gevoeliger voor overshoot en instabiliteit, vooral bij snelle processen.

#### Overdrachtsfunctie van een I-regelaar
De standaard overdrachtsfunctie in het Laplace-domein is:

$$
G_R(s) = \frac{K_I}{s}
$$

waarbij:
- $G_R(s)$: overdrachtsfunctie van de regelaar
- $K_I$: integratieversterking (proportionaliteitsfactor voor de integratie)
- $s$: Laplace-variabele
- $\frac{1}{s}$: integratieoperator in het Laplace-domein

---

### Formules

#### 1. Overdrachtsfunctie I-regelaar

**Formule**:  
$$
G_R(s) = \frac{K_I}{s}
$$

**Uitleg**:  
Deze formule geeft de relatie weer tussen de fout (input van de regelaar) en het regelsignaal (output van de regelaar). Ze beschrijft hoe de fout wordt geïntegreerd over de tijd en vermenigvuldigd met de versterking $K_I$.

**Symbolen**:
- $G_R(s)$ = Output / Input van de regelaar in Laplace-domein
- $K_I$ = Integratieversterking (dimensie: 1/s)
- $s$ = Laplace-variabele (complexe frequentie)

**Afkomst**: Deze formule volgt rechtstreeks uit de definitie van een integrerende regelaar in het frequentiedomein.

**Belang**: Deze overdrachtsfunctie toont dat de I-regelaar een oneindige versterking heeft bij $s = 0$ (statische fout = 0).

**Voorbeeld**: Stel $K_I = 5$, dan wordt een constante fout van 0.2 op lange termijn omgezet in een toenemend regelsignaal, dat met een helling van $K_I \cdot fout = 5 \cdot 0.2 = 1$ per seconde stijgt.

---

### Toepassing op een eerste orde systeem

Als een I-regelaar een systeem van eerste orde aanstuurt:

- Het gesloten regelsysteem wordt **tweede orde zonder demping**.
- De uitgang reageert traag op veranderingen.
- De respons heeft **permanente oscillaties** (als er geen extra correctie is, zoals een D-component).

---

### PI-regelaar (kort aangestipt)
Een **PI-regelaar** combineert een proportionele actie ($P$) met een integrerende actie ($I$), wat een snellere respons mogelijk maakt zonder de statische fout toe te laten. Wordt verder uitgewerkt in een later hoofdstuk.

---

### Mogelijke examenvragen

- Wat is de overdrachtsfunctie van een I-regelaar?
- Waarom is een I-regelaar geschikt voor systemen waarbij geen statische fout mag voorkomen?
- Wat gebeurt er als je een I-regelaar koppelt aan een eerste orde systeem?
- Wat zijn de nadelen van een puur integrerende regelaar?
- Hoe kan je overshoot beperken bij gebruik van een I-regelaar?

---

### Studietips

- Zorg dat je de invloed van de I-regelaar op de foutanalyse begrijpt.
- Oefen het tekenen van het blokdiagram met een I-regelaar en eerste orde proces.
- Begrijp waarom een I-regelaar kan leiden tot instabiliteit zonder aanvullende maatregelen.
- Ken het onderscheid tussen $K_I$ en $K_P$ (komt later bij PI).

---


## Hoofdstuk 4: De I-regelactie

### Korte samenvatting
Hoofdstuk 4 behandelt de werking en toepassing van de integrerende regelaar (I-regelaar). Er wordt uitgelegd hoe de integratiecomponent reageert op een foutsignaal, welke invloed dit heeft op het systeemgedrag, en wat de voordelen en beperkingen zijn. Ook wordt de combinatie van een P-regelaar met een I-regelaar besproken in de vorm van een PI-regelaar.

---

### Kernbegrippen en theorie

#### I-regelactie (integrerende actie)
De I-regelactie zorgt ervoor dat het regelsignaal stijgt (of daalt) zolang het foutsignaal verschillend is van nul. Dit betekent dat het regelsignaal de fout in de tijd blijft accumuleren, wat leidt tot eliminatie van een blijvende regelafwijking (steady-state error).

- **Voordeel**: Corrigeert blijvende fout (offset) volledig.
- **Nadeel**: Kan traag reageren; gevaar voor overshoot en instabiliteit bij snelle variaties.

#### Vergelijking met P-regelaar
Een P-regelaar reageert direct op de fout maar laat een blijvende fout na. De I-regelaar elimineert deze fout, maar doet dat trager.

#### PI-regelaar
Een combinatie van een proportionele en een integrerende regelaar. Dit type regelaar combineert snelle reactie (van de P) met het vermogen om offset te elimineren (van de I).

- Gebruikt in processen waar een snelle aanpassing gewenst is zonder blijvende fout.
- Wordt vaak ingezet bij temperatuurregeling, debietregeling, enz.

---

### Formules

#### Overdrachtsfunctie van een I-regelaar

$$
G(s) = \frac{K}{s}
$$

- **$G(s)$**: Overdrachtsfunctie van de regelaar in Laplace-domein
- **$K$**: Integratieversterking (gain), bepaalt hoe snel het regelsignaal oploopt
- **$s$**: Laplace-variabele
- **$\frac{1}{s}$**: Integratie in het Laplace-domein
- **$\frac{K}{s}$**: Geeft aan dat het regelsignaal de fout integreert in de tijd

**Herkomst**: Deze formule komt voort uit het feit dat integratie in het tijdsdomein overeenkomt met een deling door $s$ in het Laplace-domein.

**Belang**: Het toont hoe de I-regelaar de fout optelt in de tijd, wat leidt tot eliminatie van de stationaire fout.

**Typische waarden voor $K$**:
- Voor trage systemen: $K$ tussen $0.1$ en $1$
- Voor snellere systemen: $K$ tussen $1$ en $10$
  (hogere $K$-waarden verhogen de snelheid maar ook de kans op instabiliteit)

**Voorbeeldtoepassing**:
- Stel $K = 2$, en een constante fout van $e(t) = 1$.
- Dan wordt het regelsignaal:
  
  $$
  u(t) = K \int_0^t e(\tau) d\tau = 2 \cdot \int_0^t 1 \, d\tau = 2t
  $$

  Na 5 seconden is $u(t) = 10$

---

### Mogelijke examenvragen

- Leg het verschil uit tussen een P- en een I-regelaar. Wat zijn de voor- en nadelen van elk?
- Waarom elimineert een I-regelaar een blijvende fout, en hoe blijkt dat uit de formule?
- Teken het blokdiagram van een I-regelaar en leg de betekenis van elke component uit.
- Wat gebeurt er met het regelsignaal bij een constante fout van 1? Geef een wiskundige verklaring.

---

### Studietips

- Begrijp het concept van integratie in het tijdsdomein goed — visualiseer dat de uitgang blijft stijgen zolang de fout niet nul is.
- Oefen met het intekenen van tijdsverloop van foutsignaal en regelsignaal.
- Probeer zelf enkele voorbeelden uit te werken met verschillende $K$-waarden om het effect op het systeemgedrag te zien.
- Onthoud dat de I-regelaar offset elimineert maar trager reageert — dit komt vaak terug in examenvragen.

