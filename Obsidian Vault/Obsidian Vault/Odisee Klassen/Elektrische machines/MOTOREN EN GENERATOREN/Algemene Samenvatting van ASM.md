# Algemene Samenvatting van ASM

## Inleiding tot Asynchrone Machines
Een asynchrone machine (ASM) is een elektrische machine die werkt op basis van elektromagnetische inductie. ASM's kunnen zowel als motoren als generatoren functioneren, afhankelijk van het toerental van de rotor ten opzichte van het draaiveld.

- **Motorwerking**: Rotor draait langzamer dan het draaiveld ($n_r < n_s$, $s > 0$).
- **Generatorwerking**: Rotor draait sneller dan het draaiveld ($n_r > n_s$, $s < 0$).

### Toepassingen
ASM's worden veel gebruikt in industriële toepassingen vanwege:
- Eenvoudige constructie.
- Lage kosten.
- Betrouwbaarheid.

Meer uitleg: [[ASM en Gelijkstoom machines|ASM en Gelijkstroom machines]].

---

## Belangrijke Concepten

### Slip
De slip ($s$) bepaalt het verschil in snelheid tussen het draaiveld en de rotor:
$$s = \frac{n_s - n_r}{n_s}$$
- **Motorwerking**: $0 < s < 1$, meestal tussen $3\%$ en $7\%$ bij nominale belasting.
- **Generatorwerking**: $s < 0$.
- **Bij stilstand**: $s = 1$.

Meer uitleg: [[ASM en Gelijkstoom machines#Slip|Slip]].

### Synchrone snelheid
De synchrone snelheid ($n_s$) van het draaiveld wordt bepaald door de netfrequentie ($f_s$) en het aantal polen ($p$):
$$n_s = \frac{60 \cdot f_s}{p}$$

Meer uitleg: [[ASM en Gelijkstoom machines#Synchrone snelheid|Synchrone snelheid]].

### Elektromagnetische Inductie
De werking van een ASM is gebaseerd op de Wet van Faraday:
- Bewegende geleidende delen in een magnetisch veld genereren een spanning (EMK).
- Deze spanning veroorzaakt stromen in de rotor, die een magnetisch veld opwekken dat interacteert met het draaiveld.

Meer uitleg: [[ASM en Gelijkstoom machines#Elektromagnetische Inductie|Elektromagnetische Inductie]].

---

## Werking als Motor
### Nullast
- Rotor draait bijna op synchrone snelheid ($s \approx 0$).
- Stroom in de rotor is klein.
- Koppel wordt alleen gebruikt om wrijvingsverliezen te overwinnen.

Meer uitleg: [[ASM en Gelijkstoom machines#Nullast|Nullast]].

### Nominale belasting
- Rotor draait onder nominale slip ($s \approx 2\% - 8\%$).
- Maximale efficiëntie.
- Vermogen wordt overgedragen via het magnetisch veld in de luchtspleet.

Meer uitleg: [[ASM en Gelijkstoom machines#Nominale belasting|Nominale belasting]].

### Overbelasting
- Rotor vertraagt, slip neemt toe.
- Stromen in de rotor en stator worden groter, wat leidt tot warmteverliezen en mogelijke schade.

Meer uitleg: [[ASM en Gelijkstoom machines#Overbelasting|Overbelasting]].

---

## Werking als Generator
### Basisprincipe
- Rotor draait sneller dan het draaiveld ($n_r > n_s$).
- Mechanisch vermogen wordt omgezet in elektrisch vermogen.

Meer uitleg: [[ASM Generatorprincipe|ASM Generatorprincipe]].

### Vereisten
- Extern draaiveld via een statorwikkeling of capaciteitenbank.
- Synchrone snelheid wordt overschreden.

Meer uitleg: [[ASM Generatorprincipe#Vereisten|Vereisten]].

---

## Equivalentieschema
Het equivalentieschema van een ASM wordt gebruikt om:
- Stromen, spanningen en vermogensverliezen te berekenen.
- Reflectie van rotorparameters naar de statorkring te analyseren.

Met reflectie:
- Rotorimpedantie wordt omgerekend naar de statorkring:
$$Z'_2 = \frac{Z_2}{k^2}$$

Meer uitleg: [[ASM en Gelijkstoom machines#Equivalentieschema|Equivalentieschema]].

Zonder reflectie:
- Rotor- en statorgrootheden blijven afzonderlijk.

Meer uitleg: [[ASM en Gelijkstoom machines#Equivalentieschema|Equivalentieschema zonder reflectie]].

---

## Vermogensverdeling en Rendement
### Vermogensverdeling
- **Statorverliezen**:
  $$P_{Cu_S} = 3 \cdot R_1 \cdot I_1^2$$
  $$P_{Fe_S} \text{ (constant bij constante frequentie en spanning)}$$

Meer uitleg: [[ASM en Gelijkstoom machines#Statorverliezen|Statorverliezen]].

- **Rotorverliezen**:
  $$P_{Cu_R} = 3 \cdot R_2 \cdot I_2^2$$

Meer uitleg: [[ASM en Gelijkstoom machines#Rotorverliezen|Rotorverliezen]].

- **Mechanische verliezen**:
  Ventilatie- en wrijvingsverliezen ($P_v$).

Meer uitleg: [[ASM en Gelijkstoom machines#Mechanische verliezen|Mechanische verliezen]].

### Rendement
$$\eta = \frac{P_{nuttig}}{P_{opgenomen}} \cdot 100\%$$

Meer uitleg: [[ASM en Gelijkstoom machines#Rendement|Rendement]].

---

## Dynamisch Gedrag
Wanneer de rotor niet in een statische toestand is:
$$M_i = M_T + J \cdot \alpha$$
- **$M_T$**: Tegenwerkend koppel.
- **$J$**: Traagheidsmoment.
- **$\alpha$**: Hoekversnelling.

Het verschil tussen $M_i$ en $M_T$ bepaalt de versnelling of vertraging van de rotor.

Meer uitleg: [[ASM en Gelijkstoom machines#Dynamisch gedrag|Dynamisch gedrag]].

---

## Specifieke Parameters
- **Slip bij maximaal koppel (kipslip)**:
  $$s_k = \frac{R_2}{X_{2,ST}}$$

Meer uitleg: [[ASM en Gelijkstoom machines#Kipslip|Kipslip]].

- **Aanloopstroom**:
  $$I_{1,ST} = \frac{U_1}{\sqrt{(R_1 + k^2 \cdot R_2)^2 + (X_1 + k^2 \cdot X_{2,ST})^2}}$$

Meer uitleg: [[ASM en Gelijkstoom machines#Aanloopstroom|Aanloopstroom]].

- **Frequentieregeling**:
  Bij frequenties groter dan nominale frequentie treedt veldverzwakking op, wat resulteert in een verminderd koppel.

Meer uitleg: [[ASM en Gelijkstoom machines#Frequentieregeling|Frequentieregeling]].

- **Rotorfrequentie**:
  $$f_r = s \cdot f_s$$

Meer uitleg: [[ASM en Gelijkstoom machines#Rotorfrequentie|Rotorfrequentie]].

---

## Conclusie
ASM's zijn veelzijdige machines die afhankelijk van de slip als motor of generator kunnen werken. Hun prestaties zijn sterk afhankelijk van ontwerpparameters zoals slip, rotorweerstand en synchrone snelheid. Het begrijpen van het equivalentieschema en vermogensverdeling is essentieel voor optimaal gebruik en efficiëntie.

Meer uitleg: [[ASM en Gelijkstoom machines|ASM overzicht]].
