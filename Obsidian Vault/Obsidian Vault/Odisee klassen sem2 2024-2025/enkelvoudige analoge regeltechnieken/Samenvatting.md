## Hoofdstuk 1: Opbouw en indeling van regelaars
### Korte samenvatting  
Een regelkring bestaat uit sensoren, een regelaar en een corrigerend orgaan. Regelaars worden ingedeeld in lineaire (P, PI, PD, PID) en niet-lineaire (meerstanden-, tijd-proportionele) regelaars. De keuze hangt af van vereiste nauwkeurigheid, procesdynamiek en kosten.

### Kernbegrippen & Theorie  
- **Foutsignaal**: $\varepsilon(t)=\text{SW}-\text{GW}$  
- **Direct/Indirect** werkend: uitgang steigt resp. daalt bij positieve $\varepsilon$.  
- **Lineaire regelaars**: continue, transferfunctie toepasbaar.  
- **Niet-lineaire regelaars**: discrete standen; analyse via graaf- of tijds­gebied.  
- **Hysteresis (dode zone)**: band waarin de uitgangsstand niet wisselt; verlaagt schakel­frequentie.  

### Formules  
| Grootheid | Definitie | Toepassing |
|-----------|-----------|-----------|
| Fout | $\varepsilon(t)=\text{SW}-\text{GW}$ | Basis voor alle regelaars |
| Transfer open-lus | $H(s)=\dfrac{Y(s)}{E(s)}$ | Analyse stabiliteit |
| Hysteresegebied | $h=V_\text{sat}\dfrac{R_2}{R_1+R_2}$ | Comparator in tweestandenregelaar |

### Mogelijke examenvragen  
1. Teken en benoem alle blokken van een gesloten regelkring.  
2. Verschil tussen lineaire en niet-lineaire regelaar; voor- en nadelen.  
3. Verklaar invloed van hysteresisbreedte op regeling en levensduur van het corrigerend orgaan.

### Studietips  
- Memoriseer de basisblokschema’s.  
- Oefen het herkennen van direct vs. indirect werkend uit karakteristieken.  
- Begrijp waarom hysteresis nodig is om contactslijtage te beperken.

---

## Hoofdstuk 2: De meerstanden-regelaar
### Korte samenvatting  
Meerstanden-regelaars (twee- en driestanden) schakelen slechts vaste uitgangswaarden. Ze zijn eenvoudig, robuust en geschikt voor trage processen met beperkte nauwkeurigheid.

### Kernbegrippen & Theorie  
- **Tweestanden-regelaar**: uitgang “aan/uit”; karakteristiek met hysterese.  
- **Driestanden-regelaar**: uitgang “koud–uit–warm” of “retour–stop–aan”.  
- **Schakelfrequentie** daalt bij grotere hysterese, maar foutband groeit.  
- **Elektronische implementatie**: comparator met positieve terugkoppeling; hysterese instelbaar via $R_2$.  

### Formules  
| Situatie | Procesuitgang $y(t)$ (1e orde) |
|----------|--------------------------------|
| Stijgen $(0\!\to\!t_1)$ | $y(t)=C_\text{max}-\big(C_\text{max}-C_\text{min}\big)e^{-t/\tau}$ |
| Dalen $(t_1\!\to\!t_2)$ | $y(t)=C_\text{min}+\big(\text{SW}+\tfrac{h}{2}-C_\text{min}\big)e^{-(t-t_1)/\tau}$ |
| Periode | $T = t_3-t_1,\; f_\text{sch}=1/T$ |

### Mogelijke examenvragen  
1. Leg uit hoe hysteresis doorschot en relais­slijtage beïnvloedt.  
2. Bereken de schakelfrequentie voor gegeven $\tau$, $h$, SW.  
3. Vergelijk twee- en driestanden-regeling bij klimaatbeheersing.

### Studietips  
- Teken telkens ingang-uitgangs­diagrammen om schakelpunten te zien.  
- Automatiseer berekening van $t_1,t_2$ in een spreadsheet voor oefenopgaven.

---

## Hoofdstuk 3: De P-regelaar
### Korte samenvatting  
Een proportionele regelaar levert een uitgang evenredig met de fout. Hij verkleint maar elimineert de statische afwijking niet.

### Kernbegrippen & Theorie  
- **Regelwet**: $y(t)=M+K_p\,\varepsilon(t)$  
- **Proportionele band**: $\text{PB}=100\,\%/(K_p K_\text{proc})$  
- **Statische fout (offset)** blijft: $\varepsilon_\infty=\dfrac{\text{SW}}{1+K_pK_\text{proc}}$  
- **Invloed $K_p$**: groter ⇒ sneller, kleiner offset, maar kans op overshoot.

### Formules  
| Grootheid | Uitdrukking |
|-----------|-------------|
| PB – signaal­eenheden | $\text{PB} = \dfrac{100\,\%\; \Delta x_\text{in}}{K_p\,\Delta y_\text{out}}$ |
| 1e orde kringtijd­constante | $\tau'=\dfrac{\tau}{1+K_p K_\text{proc}}$ |
| Statische fout | $\varepsilon_\infty=\dfrac{\text{SW}}{1+K_pK_\text{proc}}$ |

### Mogelijke examenvragen  
1. Bereken PB voor gegeven $K_p$ en ranges.  
2. Toon effect van $K_p$-vergroting op tijdconstante en offset bij 1e orde proces.  
3. Schets proceskarakteristiek en regelkarakteristiek voor douchemengkraan.

### Studietips  
- Leer PB↔$K_p$ omrekenen in verschillende eenheden.  
- Oefen grafische bepaling van offset uit karakteristieken.

---

## Hoofdstuk 4: De I-regelactie en PI‐regelaar
### Korte samenvatting  
Integrale actie somt de fout op, elimineert de statische fout maar kan bij te korte integratietijd oscillaties veroorzaken. De PI‐regelaar combineert snelle P-correctie met langzame foutuitdoving.

### Kernbegrippen & Theorie  
- **I-wet**: $y(t)=\dfrac{1}{\tau_i}\int_0^t \varepsilon(\xi)\,d\xi$  
- **Integratietijd** $\tau_i$: kleiner ⇒ agressiever.  
- **Anti-reset-wind-up (ARW)**: begrenst I-uitgang binnen $\pm$ band.  
- **PI-transfer (serie)**: $H(s)=K_p\!\left(1+\dfrac{1}{\tau_i s}\right)$.

### Formules  
| Grootheid | Formule |
|-----------|---------|
| Na-insteltijd | $\tau_n=\tau_i$ (PI-serie) |
| Reset-rate | $r=1/\tau_i\;[\text{repeats/min}]$ |
| PI-uitgang | $y(t)=K_p\big(\varepsilon + \dfrac{1}{\tau_i}\int\varepsilon dt\big)$ |

### Mogelijke examenvragen  
1. Beschrijf reset-wind-up en ARW-oplossing.  
2. Bereken $\tau_i$ uit opgegeven reset-rate.  
3. Analyseer PI-gedrag voor 1e orde proces met stap in SW.

### Studietips  
- Gebruik simulatie om invloed van $\tau_i$ visueel te zien.  
- Controleer steeds verzadiging bij grote storingen.

---

## Hoofdstuk 5: De D-regelactie en PD‐regelaar
### Korte samenvatting  
De D-actie anticipeert op foutverandering, versnelt reactie maar reageert op meetruis. In praktijk wordt een «tamme» differentiator gebruikt.

### Kernbegrippen & Theorie  
- **D-wet**: $y(t)=K_p\big(\varepsilon+\tau_d\,\dot\varepsilon\big)$  
- **Differentiatietijd** $\tau_d$: typisch $\le 0.25\,\tau_\text{proces}$.  
- **Tamme differentiator**: $H(s)=\dfrac{\tau_d s}{\tau_d s+1}$ (hoog-frequent begrensd).  
- **PD-parallel**: $H(s)=K_p+\tau_d s$.

### Formules  
| Grootheid | Uitleg |
|-----------|--------|
| Reële differentiator | $H(s)=\dfrac{R_2}{R_1}\dfrac{s\tau_d}{1+s\tau_f}$ met $\tau_f=R_4C$ |
| PD-uitgang na stap | P-piek $=K_p\Delta\varepsilon$, D-piek $=K_p\tau_d\delta(t)$ (ideal) |

### Mogelijke examenvragen  
1. Waarom beperkt men de D-bandbreedte?  
2. Ontwerp een inverte­rende PD-schakeling met gegeven $K_p$, $\tau_d$.  
3. Bespreek effect van ruis op D-actie.

### Studietips  
- Pas D-actie enkel toe als meetsignaal voldoende gefilterd is.  
- Simuleer tamme vs. ideale differentiator voor begrip.

---

## Hoofdstuk 6: De PID-regelaar
### Korte samenvatting  
PID combineert P-, I- en D-actie zodat het snel reageert, foutvrij uitregelt en overshoot tempert. Er bestaan standaard (non-interactive), serie (interactive) en parallel vormen.

### Kernbegrippen & Theorie  
- **Parallel-vorm**: $u(t)=k_p\!\big(\varepsilon + \dfrac{1}{T_i}\!\int\varepsilon dt + T_d\dot\varepsilon\big)$  
- **Bode-diagram**: integrerend voor lage ω, proportioneel middensectie, differentie­rend hoge ω.  
- **Tuning**: Ku, Tu (Ziegler–Nichols), CHR, Strejc, etc.  
- **Implementatie**: één-opamp (beperkte onafhankelijkheid), opamps cascade (volledig instelbaar).

### Formules  
| Parameterconversie | Relatie |
|--------------------|---------|
| Standaard → parallel | $k_p=K_p$ , $k_i=K_p/\tau_i$ , $k_d=K_p\tau_d$ |
| Interactief (serie) | zie conversietabellen (omrekening nodig) |

### Mogelijke examenvragen  
1. Vergelijk parallel- en interactive-PID.  
2. Geef Bode-schets en verklaar vorm.  
3. Pas CHR-regels toe voor 0 % overshoot.

### Studietips  
- Teken blokschema met afzonderlijke P, I, D paden om structuur te onthouden.  
- Oefen omrekenen van parameters tussen vormen.

---

## Hoofdstuk 7: Stabiliteit
### Korte samenvatting  
Een systeem is stabiel als de impuls­respons naar nul tendeert. Stabiliteit wordt beoordeeld in het $s$-vlak (polen links) of met frequentiemethoden (Nyquist, Bode-marges).

### Kernbegrippen & Theorie  
- **Routh–Hurwitz**: tekenwissels in eerste kolom ↔ polen in rechter halfvlak.  
- **Nyquist-criterium**: rondgaande versterking $GH(j\omega)$ mag het punt –1 niet omsluiten.  
- **Fasemarge** $\varphi_m$: afstand tot –180° bij $|GH|=1$.  
- **Versterkingsmarge** $G_m$: reciproke van $|GH|$ bij fase –180°.

### Formules  
| Beoordeling | Voorwaarde |
|-------------|-----------|
| Absolute stabiliteit | Alle Routh hoofdcoëfficiënten $>0$ |
| Kritisch oscilleren | $GH(j\omega_c)=-1 \;\Rightarrow\; \omega_c,\,K_u$ |
| Fase-/gain-marge | $\varphi_m=\angle GH|_{|GH|=1}+180^\circ$,  $G_m=1/|GH|_{\,\angle GH=-180^\circ}$ |

### Mogelijke examenvragen  
1. Construeer Routh-tabel voor 4e-orde polynoom en bepaal stabiliteit.  
2. Definieer fase- en versterkingsmarge en interpreteer hun belang.  
3. Bepaal met Nyquist of een PID-tuned kring voldoende marge bezit.

### Studietips  
- Automatiseer Routh-tabelberekening met een script.  
- Oefen lezen van Bode-diagrammen om marges snel af te leiden.

---

## Hoofdstuk 8: Instelregels (tuning)
### Korte samenvatting  
Tuningregels geven startwaarden voor $K_p$, $T_i$, $T_d$ op basis van proces­tests. Bekend zijn Ziegler–Nichols, Chien-Hrones-Reswick, Strejc, Good Gain, bedrags- en symmetrisch optimum.

### Kernbegrippen & Theorie  
- **Proceskarakteristiek**: reactie op stap (S-curve) ⇒ $K$, $T$, $L$.  
- **Z-N open-loop**: $K_p=\tfrac{T}{K L}$ (P); PI/PID volgens tabelwaarden.  
- **Z-N closed-loop**: ultieme gain $K_u$, periode $T_u$.  
- **CHR**: aparte tabellen voor 0 % of 20 % overshoot.  
- **Strejc**: niet-gehele orde $n$, grafieken voor $K_pT_i$, $T_i/T$, $T_d/T_i$.  
- **Good Gain**: bepaal $K_{p,\text{GG}}$, oscillatie-interval $T_{ou}$, zet $K_p=0.8K_{p,\text{GG}}$, $T_i=1.5T_{ou}$, $T_d=T_i/4$.  
- **Bedragsoptimum**: instelregels gebaseerd op som van tij constanten; snelle opstijgtijd met beperkt overshoot.  
- **Symmetrisch optimum**: verbeterde stabiliteit bij integrator in proces; $\tau_i=4\sigma$.

### Formules  
| Regel | Hoofdrelaties |
|-------|---------------|
| Z-N (closed) | $K_p=0.6K_u,\;T_i=0.5T_u,\;T_d=0.125T_u$ |
| CHR (0 % OS, PI) | $K_p=0.35K\,T/L,\;T_i=1.2T$ |
| Bedragsoptimum | $\tau_i=2\sigma,\;K_p=\dfrac{1}{2K}\dfrac{\tau}{\sigma}$ |
| Symm. optimum | $\tau_i=4\sigma,\;K_p=\dfrac{\tau_1}{2K\sigma}$ |

### Mogelijke examenvragen  
1. Pas Z-N open-loop toe op gegeven S-curve.  
2. Bepaal Strejc-orde en lees PI-instellingen af.  
3. Vergelijk Good Gain met Z-N m.b.t. settle- en overshoot.

### Studietips  
- Leer telkens testprocedure (open-/closed-loop) stap-voor-stap.  
- Onthoud welke regels overshoot minimaliseren (CHR 0 %, bedragsoptimum).  
- Gebruik simulatie om effect van elke regel snel te beoordelen.  
