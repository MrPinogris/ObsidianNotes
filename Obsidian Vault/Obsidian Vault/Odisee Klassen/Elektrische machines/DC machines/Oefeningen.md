# Oefeningen [[DC machines]]

## Oef 1

Een gelijkspanningsdynamo met een klemspanning van 230V levert een ankerstroom van 100A. Het gedissipeerde kopervermogen bedraagt 3% van het afgegeven vermogen. Het aandrijvende werktuig geeft een vermogen af van 25,5kW.

**Gegeven:**
- $E_{1}=230V$
- $I_{a}=100A$
- $P_{Cu}=3\%P_{n}$
- $P_{n}=25.6kW$
**Gevraagd:**
0. Stel schematisch de vermogensverdeling voor
1. Het rendement
   $$
P_{elec}=230\cdot 100=23kW
$$
$$
\eta = \frac{23kW}{25,6kW}=89,84\%
$$

2. Het inwendig vermogen
   $$
 P_{i} = P_{elec}\cdot 103\% = 23,69kW
$$
3. De ijzer- en wrijvingsverliezen
   $$
P_{v}= P_{in}-P_{i}=25,6\cdot 23,69=1,69kW
$$

---
## Oef 2

Een dynamo wekt een emk op van 110 V en levert een ankerstroom van 50 A. Het actief vermogen te wijten aan de koperwikkeling bedraagt 4% van het inwendig vermogen. Het rendement van de machine is 84%.

**Gegeven:**
- $E = 110 \, \text{V}$
- $I_a = 50 \, \text{A}$
- $P_{Cu} = 4\% \, P_{in}$
- $\eta = 84\%$

**Gevraagd:**
0. Stel schematisch de vermogensverdeling voor.
1. Het inwendig vermogen (5,5 kW).
   $$
P_{i} = E\cdot I_{a}=110\cdot 50= 5500W
$$
2. Het nuttig vermogen (5,28 kW).
   $$
P_{n}= P_{i}-P_{Cu}=5500\cdot 0,96=5,28kW
$$
3. De mechanische verliezen (0,788 kW).
   $$
P_{v}=P_{as}-P_{i}=\frac{5280}{0,84}-5500=788W
$$

---

## Oef 3

Een 230 V-gelijkstroommotor van 10 kW neemt een ankerstroom op van 50 A. Het actief vermogen dat gedissipeerd wordt in de koperwikkeling bedraagt 600 W.

**Gegeven:**
- $U = 230 \, \text{V}$
- $P = 10 \, \text{kW}$
- $I_a = 50 \, \text{A}$
- $P_{Cu} = 600 \, \text{W}$

**Gevraagd:**
0. Stel schematisch de vermogensverdeling voor.
1. Het rendement $\eta = 86,96\%$.
   $$
\eta = \frac{P_{as}}{P_{elec}}=\frac{10kW}{230\cdot 50}=86,96 \%
$$
2. Het inwendig vermogen (10,9 kW).
   $$
P_{i}= P_{elec}-P_{cu}=230\cdot 50 - 600=10,9kW
$$
3. De ijzer- en wrijvingsverliezen (0,9 kW).
   $$
P_{v}=P_{i}-P_{as}=10,9-10=900W
$$

---

## Oef 4

Een 4 kW - 110 V-gelijkstroommotor neemt een ankerstroom op van 40 A. De tegenemk bedraagt 106 V.

**Gegeven:**
- $P = 4 \, \text{kW}$
- $U = 110 \, \text{V}$
- $I_a = 40 \, \text{A}$
- $E = 106 \, \text{V}$

**Gevraagd:**
0. Stel schematisch de vermogensverdeling voor.
1. De mechanische verliezen (0,24 kW).
   $$
P_{v}=P_{i}-P_{as}=40\cdot 106 - 4000=240W
$$
2. De koperverliezen (0,16 kW).
   $$
P_{Cu}=P_{elec}-P_{i}=110\cdot 40- 106\cdot 40=160
$$
3. Het rendement $\eta = 91\%$.
   $$
\eta=\frac{P_{as}}{P_{elec}}=\frac{4000}{110\cdot 40}=91\%
$$

---

## Oef 5

Een 110 V-gelijkstroommotor heeft een totale ankerweerstand van 0,2 ohm. Het vermogen is 8 kW terwijl het rendement 84% bedraagt.

**Gegeven:**
- $U = 110 \, \text{V}$
- $R_a = 0,2 \, \Omega$
- $P = 8 \, \text{kW}$
- $\eta = 84\%$

**Gevraagd:**
0. Stel schematisch de vermogensverdeling voor.
1. De opgenomen stroom (86,6 A).
   $$
I_{a} = \frac{P_{elec}}{U} = \frac{\frac{8000}{0,84}}{110}=86,6A
$$
2. De koperverliezen (1,5 kW).
   $$
P_{Cu}=R_{a}\cdot I_{a}^2=0,2\cdot 86,6^2=1,5kW
$$
3. De ijzer- en wrijvingsverliezen (0,024 kW).
   $$
P_{Fe}=P_{elec}-P_{Cu}-P_{as}=9523,81-1500-8000=23,81W
$$

---

## Oef 6

Een OB-motor is aangesloten op 230 V. De ankerweerstand is 2 ohm. De nominale ankerstroom is 10 A. De toegelaten aanzetstroom is tweemaal de nominale stroom.

**Gegeven:**
- $U = 230 \, \text{V}$
- $R_a = 2 \, \Omega$
- $I_{nom} = 10 \, \text{A}$
- $I_{start} = 2 \cdot I_{nom}$

**Gevraagd:**
1. Som 1 of meerdere oplossingen op en maak de bijhorende berekening.
   - Voorschakelweerstand
     $$
I_{a}=20A
$$
$$
I_{a}=\frac{E}{R_{a}+R_{voor}}\implies R_{voor}=\frac{E}{I_{a}}-R_{a}=\frac{230}{20}-2=9,5 \ohm
$$
   - Startspanning verlagen
     $$
20=\frac{E}{2}\implies E=20\cdot 2=40V
$$

---

## Oef 7

Een OB-motor is aangesloten op 750 V. De ankerweerstand is 0,1 ohm en de veldweerstand 55 ohm. De veldwikkeling is aangesloten op 110 V. De nominale ankerstroom is 100 A. Het vollastrendement is 84%.

**Gegeven:**
- $U = 750 \, \text{V}$
- $R_a = 0,1 \, \Omega$
- $R_f = 55 \, \Omega$
- $I_a = 100 \, \text{A}$
- $\eta = 84\%$

**Gevraagd:**
1. De tegen emk (740 V).
   $$
E=U-I\cdot R_{a}=750\cdot 0,1\cdot 100=740V
$$
2. Het asvermogen (63 kW).
   $$
P_{as}= P_{in}\cdot \eta = 750\cdot 100\cdot 0,84=63kW
$$
3. Het askoppel bij 500 tpm ($M_N = 1203 \, \text{Nm}$).
   $$
M_{as}(500tpm)=\frac{P_{as}}{\omega}=\frac{63kW}{500\cdot 2\pi / 60}=1203Nm
$$
4. De aanzetweerstand als de aanzetstroom 1,5 keer de nominale stroom is ($R_a = 4,9 \, \Omega$).
   $$
R_{voor}=\frac{U_{a}}{I_{a}\cdot 1,5}-R_{a}=\frac{750}{150}-0,1=4,9 \ohm
$$
5. De veldstroom ($I_f = 2 \, \text{A}$).
   $$
I_{f}= \frac{U_{f}}{R_{f}}=\frac{110}{55}=2A
$$

---

## Oef 8

Een OB-motor heeft een nominale ankerspanning van 440 V, het nominaal vermogen van 30 kW bij 500 tpm. De ankerweerstand is 0,4 ohm. De nominale vollastankerstroom is 75 A.

**Gegeven:**
- $U_{a,nom} = 440 \, \text{V}$
- $P_{nom} = 30 \, \text{kW}$
- $n_{nom} = 500 \, \text{tpm}$
- $R_a = 0,4 \, \Omega$
- $I_{a,nom} = 75 \, \text{A}$

**Gevraagd:**
1. De ankerstroom bij het aanzetten als de spanning verlaagd werd naar 50 V. ($I_a = 125 \, \text{A}$)
   $$
I_{a}=
$$
2. Het nominale askoppel. ($M_N = 573 \, \text{Nm}$)
3. Het aanzetkoppel als het inwendig koppel en het askoppel aan elkaar mogen gelijkgesteld worden. ($M_{st} = 955 \, \text{Nm}$)

---

## Oef 9

Een OB-motor heeft een nominale ankerspanning van 230 V. De ankerweerstand is 0,2 ohm en de veldweerstand is 110 ohm. De motor neemt een ankerstroom op van 50 A en draait aan 1000 tpm. Het rendement bij deze belasting is 85%.

**Gegeven:**
- $U_{a,nom} = 230 \, \text{V}$
- $R_a = 0,2 \, \Omega$
- $R_f = 110 \, \Omega$
- $I_a = 50 \, \text{A}$
- $n = 1000 \, \text{tpm}$
- $\eta = 85\%$

**Gevraagd:**
1. De tegenemk. ($E = 220 \, \text{V}$)
2. Het inwendig koppel. ($M_{in} = 105,04 \, \text{Nm}$)
3. Het uitwendig koppel. ($M_{uit} = 93,34 \, \text{Nm}$)
4. Het toerental als de motor nu minder belast wordt en slechts nog 30 A opneemt. ($n = 1018,18 \, \text{tpm}$)

---

## Oef 10

Als de OB-motor aangesloten is op een spanning van 230 V bedraagt het toerental 600 tpm bij een opgenomen ankerstroom van 190 A. De ankerweerstand is 0,05 ohm en de veldweerstand is 22 ohm.

**Gegeven:**
- $U = 230 \, \text{V}$
- $n = 600 \, \text{tpm}$
- $I_a = 190 \, \text{A}$
- $R_a = 0,05 \, \Omega$
- $R_f = 22 \, \Omega$

**Gevraagd:**
1. De tegenemk bij deze belasting. ($E = 220,5 \, \text{V}$)
2. De tegenemk indien de belasting afneemt en de ankerstroom nog 90 A is. ($E = 225,5 \, \text{V}$)
3. Het toerental bij de tweede belasting. ($n = 613,61 \, \text{tpm}$). Geef tevens de grafische voorstelling.
4. De verhouding der inwendige koppels. (2,11). Geef de grafische voorstelling.

---

## Oef 11

De OB-motor is aangesloten op een spanning van 230 V. Bij een ankerstroom van 60 A is het toerental 1070 tpm. De ankerweerstand is 0,1 ohm en de veldweerstand is 55 ohm. De motor wordt meer belast waardoor het toerental daalt tot 1050 tpm.

**Gegeven:**
- $U = 230 \, \text{V}$
- $I_a = 60 \, \text{A}$
- $n = 1070 \, \text{tpm}$
- $R_a = 0,1 \, \Omega$
- $R_f = 55 \, \Omega$
- $n' = 1050 \, \text{tpm}$

**Gevraagd:**
1. Welke ankerstroom wordt nu door de motor opgenomen? ($I_a = 101,9 \, \text{A}$)

---

## Oef 12

De OB-motor is aangesloten op een spanning van 230 V. Bij een ankerstroom van 60 A is het toerental 800 tpm. De ankerweerstand is 0,3 ohm en de veldweerstand is 110 ohm.

**Gegeven:**
- $U = 230 \, \text{V}$
- $I_a = 60 \, \text{A}$
- $n = 800 \, \text{tpm}$
- $R_a = 0,3 \, \Omega$
- $R_f = 110 \, \Omega$
- $I_{nul} = 4 \, \text{A}$

**Gevraagd:**
1. Bereken het toerental wanneer de motor onbelast draait. (863,4 tpm)

---

## Oef 13

De OB-motor is aangesloten op een spanning van 230 V. De veldspanning is 230 V. Bij 800 tpm is de ankerstroom 18 A. De ankerweerstand is 0,5 ohm en de veldweerstand is 110 ohm. Het anker en het veld worden nu op een lagere spanning van 110 V aangesloten. De ankerstroom bedraagt 11 A.

**Gegeven:**
- $U = 230 \, \text{V}$
- $U_f = 230 \, \text{V}$
- $n = 800 \, \text{tpm}$
- $I_a = 18 \, \text{A}$
- $R_a = 0,5 \, \Omega$
- $R_f = 110 \, \Omega$
- $U' = 110 \, \text{V}$
- $I'_a = 11 \, \text{A}$

**Gevraagd:**
1. Het toerental bij 11 A als de flux 75% is van zijn oorspronkelijke waarde. (504,37 tpm)
2. De verhouding der inwendige koppels (2,18).

---

## Oef 14

De OB-motor is aangesloten op een spanning van 230 V. Het nullasttoerental is 500 tpm. De veldspanning is 230 V en de veldweerstand is 115 ohm. Het verband tussen veldstroom en flux wordt gegeven door:

| Veldstroom (A) | Flux (Wb) |
|----------------|-----------|
| 0,5            | 6,0       |
| 1,0            | 9,0       |
| 1,5            | 11,0      |
| 1,75           | 11,7      |
| 2,0            | 12,0      |

**Gegeven:**
- $U = 230 \, \text{V}$
- $n_{nul} = 500 \, \text{tpm}$
- $R_f = 115 \, \Omega$

**Gevraagd:**
1. De weerstand die in de veldketen moet worden geschakeld om een toerental van 1000 tpm te bekomen. (345 ohm)
2. Het toerental bij nullast als in de veldketen een weerstand van 36,8 ohm wordt opgenomen. (545 tpm)

---

## Oef 15

De OB-motor heeft een nominale spanning van 440 V. De ankerweerstand is 0,3 ohm. De OB-motor met een nominaal toerental van 500 tpm drijft een werktuig aan waarvan het koppel constant is. De opgenomen ankerstroom is 100 A.

**Gegeven:**
- $U_{nom} = 440 \, \text{V}$
- $n_{nom} = 500 \, \text{tpm}$
- $R_a = 0,3 \, \Omega$
- $I_a = 100 \, \text{A}$

**Gevraagd:**
1. Het toerental als de ankerspanning wordt ingesteld op 100 V. (85 tpm)

---

## Oef 16

Een OB-motor heeft volgende kenmerken: $k_1 = 1$, $k_2 = 6$, $R_{a,totaal} = 1 \, \Omega$, $\phi_{nom} = 100 \, \text{mWb}$, $U_{a,nom} = 150 \, \text{V}$, $I_{a,nom} = 10 \, \text{A}$. De motor drijft een werktuig aan met een lineaire karakteristiek die gegeven wordt door de vergelijking $M = 0,0025 \, n$.

**Gegeven:**
- $k_1 = 1$
- $k_2 = 6$
- $R_{a,totaal} = 1 \, \Omega$
- $\phi_{nom} = 100 \, \text{mWb}$
- $U_{a,nom} = 150 \, \text{V}$
- $I_{a,nom} = 10 \, \text{A}$
- $M = 0,0025 \, n$

**Gevraagd:**
1. Het nominaal toerental. (1400 tpm)
2. Het nominaal koppel. (6 Nm)
3. De coördinaten van het werkingspunt. (3,6 Nm, 1440 tpm)
4. De ankerstroom en ankerspanning als het werktuig aan 800 tpm draait. (3,33 A; 83,3 V)
5. De grafische voorstelling in het $(M,n)$-assenstelsel van beide bedrijfstoestanden.
