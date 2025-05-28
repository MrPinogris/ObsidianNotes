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

