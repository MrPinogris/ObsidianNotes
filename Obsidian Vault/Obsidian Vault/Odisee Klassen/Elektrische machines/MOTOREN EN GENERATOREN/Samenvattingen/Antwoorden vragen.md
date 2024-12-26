## Antwoorden
### Theorievragen
1. **Slip**:
   - Slip is de verhouding tussen het toerentalverschil en het synchrone toerental: $s = \frac{n_s - n_r}{n_s}$.
   - Typische waarden: Motorwerking $3\% - 7\%$, Generatorwerking $s < 0$.

2. **Synchrone snelheid**:
   - De synchrone snelheid wordt berekend met de formule:
     $$n_s = \frac{60 \cdot f_s}{p}$$
     waarbij $f_s$ de netfrequentie is en $p$ het aantal polenparen.
   - Als de rotor de synchrone snelheid bereikt, is er geen relatieve beweging tussen het draaiveld en de rotor, en wordt er geen koppel opgewekt.

3. **Elektromagnetische inductie**:
   - Elektromagnetische inductie veroorzaakt stroom in de rotor door het snelheidsverschil tussen het draaiveld en de rotor.
   - Het magnetisch veld van de rotorstroom interacteert met het draaiveld om koppel te produceren.

4. **Equivalentieschema**:
   - Een equivalentieschema wordt gebruikt om de elektrische en magnetische eigenschappen van een ASM te analyseren in een vereenvoudigd model.
   - Bij reflectie worden rotorparameters omgerekend naar de statorkring; zonder reflectie blijven de rotor- en statorgrootheden gescheiden.

5. **Kipslip**:
   - Kipslip ($s_k$) is de slipwaarde waarbij het maximale koppel wordt bereikt:
     $$s_k = \frac{R_2}{X_{2,ST}}$$
   - Het is belangrijk voor het dimensioneren van de motor bij zware belasting.

6. **Aanloopstroom**:
   - De aanloopstroom wordt berekend met:
     $$I_{1,ST} = \frac{U_1}{\sqrt{(R_1 + k^2 \cdot R_2)^2 + (X_1 + k^2 \cdot X_{2,ST})^2}}$$
   - Methoden om de aanloopstroom te verminderen zijn ster-driehoek schakeling, verlaagde statorspanning of verhoogde rotorweerstand.

7. **Rendement**:
   - Het rendement wordt berekend als:
     $$\eta = \frac{P_{nuttig}}{P_{opgenomen}} \cdot 100\%$$
   - Verliezen die een rol spelen zijn koper-, ijzer-, en mechanische verliezen.

8. **Dynamisch gedrag**:
   - Wanneer $M_i \neq M_T$, resulteert het verschil in een versnelling of vertraging van de rotor:
     $$\alpha = \frac{M_i - M_T}{J}$$
   - Waarbij $J$ het traagheidsmoment is en $\alpha$ de hoekversnelling.

### Oefenvragen
1. **Slipberekening**:
   - Absolute slip: $s_a = 1500 - 1455 = 45 \ \text{RPM}$
   - Relatieve slip: $s = \frac{45}{1500} = 0.03$ of $3\%$.

2. **Synchrone snelheid**:
   - $n_s = \frac{60 \cdot 50}{2} = 1500 \ \text{RPM}$.

3. **Koppelberekening**:
   - $M_i \approx C^{te} \cdot \frac{s \cdot R_2}{R_2^2 + (s \cdot X_{2,ST})^2}$ (parameters invullen en uitwerken).

4. **Aanloopstroom**:
   - $I_{1,ST} = \frac{U_1}{\sqrt{(R_1 + k^2 \cdot R_2)^2 + (X_1 + k^2 \cdot X_{2,ST})^2}}$ (parameters invullen en uitwerken).

5. **Rendement**:
   - $\eta = \frac{13.5}{15} \cdot 100\% = 90\%$.

6. **Dynamisch gedrag**:
   - $\alpha = \frac{M_i - M_T}{J} = \frac{50 - 45}{0.1} = 50 \ \text{rad/s}^2$.
