## Equivalent schema ideale ASM 

### Bolfiguur


![[Pasted image 20241228093320.png]]

1. Veld $\overline{\Phi}$
2. Draaiveld
3. $n_{s}\implies v_{rel}=-n_{s}$
4. $E_{2}=B\cdot l\cdot v$ (RHL)
5. $I_{2}\implies B \text{ loodrecht op } v_{rel}\implies E_{2_{max}}$
6. $F=B\cdot l\cdot I$ (LHR)
7. $M^+\implies n_{r}^+$
8. $\overline{\Phi_{2}}$
9. $\overline{\Phi_{1}}=-\overline{\Phi_{2}}$
10. $I_{1}$'

## Equivalent schema niet ideale ASM
### Niet ideale ASM bij nullast
$$n\approx n_s \implies s_{0}\to{0}$$$$\downarrow$$$$E_{2(0)}\ll$$$I_{2(0)}\gg$ In vergelijking met de $I_{0}$ van transfo. Door aanwezigheid luchtspleet.
$$I_{2(0)}\approx \frac{1}{2}I_{n}$$$$I_{0}=I_{\mu}+I_{v}$$$I_{0}$ ijlt fel na door grote grote $I_{\mu}$ en $I_v$
#### [[Tekeningen Machines|EQ schema Nullast]]
$$\overline{U_{1}}=R_{1}*\overline{I_{0}}+\overline{X_{1}}*\overline{I_{0}}-\overline{E_{1}}$$
![[Pasted image 20241223183135.png]]
#### [[Tekeningen Machines#ASM#Nullast|Vectordiagram nullast]]
$\overline{E_{1}}\to-90°$
$\Phi\to0°$
$\overline{I_{\mu}}\implies$[[Wetten|Hopkinson]] 
$\overline{I_{v}}$ 
$\overline{U_{1}}=R_{1}*\overline{I_{0}}+\overline{X_{1}}*\overline{I_{0}}-\overline{E_{1}}$
$\phi_{0}=(\overline{U_{1}}\angle\overline{I_{0}})$
![[Pasted image 20241223183425.png]]
### Niet ideale ASM bij stilstand (start)
#### [[Tekeningen Machines#Stilstand|EQ schema stilstand]]
![[Pasted image 20241223185137.png]]
- $\overline{U_{2}}$ is Zeer klein omdat deze gewoon kortgesloten is, hierdoor is $\overline{I_{2}}$ Zeer groot
#### [[Tekeningen Machines#Stilstand|Vectordiagram stilstand]]
$$E_{2(st)}=4,44*f_{s}*N_{r}*\Phi_{m}$$$\overline{U_{2(st)}}=0\impliesφ>90°\implies N_{r}\approx0\implies\overline{E_{2}}\to0\implies\overline{I_{2(st)}}\gg$$$\underbrace{ X_{2(st)}=5*R_{2} }_{ \text{maximaal inductief bij stilstand} }$$$$I_{2(st)}=\frac{E_{2(st)}}{\sqrt{ R^{2}_{2(st)}+X^2_{2(st)}}}$$$$\overline{U_{1}}=R_{1}*\overline{I_{0}}+\overline{X_{1}}*\overline{I_{0}}-\overline{E_{1}}$$$$\frac{\overline{I'_{1(st)}}}{\overline{I_{2(st)}}}=-\frac{1}{k}$$$$\overline{I_{1(st)}}=\overline{I_{0}}+\overline{I'_{1(st)}}$$
##### Tekenen
1. $\overline{E_{1}},-\overline{E_{1}},\overline{E_{2(st)}}$
2. $\begin{cases}\overline{I_0} = \overline{I_µ} + \overline{I_v} \\ \overline{\Phi}\end{cases}$
3. $\overline{X_{2(st)}}=5*\overline{R_{2}}\implies\overline{E_{2(st)}}=R_{2}*\overline{I_{2(st)}}+\overline{X_{2(st)}}*\overline{I_{2(st)}}\implies\text{Rechthoekig 3 hoek met verhouding }\frac{5}{1}$![[Pasted image 20241224114524.png]]
4. $\overline{I_{2st}}\rightsquigarrow79°\text{nà }\overline{E_{2(st)}}$
5. $\overline{\Phi_{1}}$
6. $\overline{\Phi_{2}}$
7. $\overline{I'_{1(st)}}$ 
8. $\overline{I_{1(st)}}$
9. $\overline{U_{1}}=R_{1}*\overline{I_{1(st)}}+\overline{X_{1}}*\overline{I_{1(st)}}-\overline{E_{1}}$
![[Pasted image 20241224093833.png]]
### Niet ideale ASM bij nominale belasting
#### [[Tekeningen Machines#Niet Ideale ASM#Belast#Equivalent schema|EQ schema]]
![[Pasted image 20241224102418.png]]
De secundaire EMK is niet cte deze is veranderlijk, recht evenredig met de slip
$$\overline{E_{2}}=s*\overline{E_{2(st)}}$$
$$
f_{s}\neq f_{r}
$$
$$
I_{2}=\frac{E_{2}}{\sqrt{ R^2_{2}+X^{2}_{2} }}
$$
$$
\underbrace{ I_{2}=\frac{s*E_{2(st)}}{\sqrt{ R^2_{2}+(s*X_{2(st)})^2 }} }_{ \text{delen door }s }
$$
$$
 I_{2}=\frac{E_{2(st)}}{\sqrt{(\frac{ R_{2}}{s})^2+X_{2(st)}^2 }} 
$$
![[Pasted image 20241224122011.png]]
De vervang weerstand $R_{b}$ is ook berekenbaar
$$
R_{b}=\frac{R_{2}}{s}-R_{2}=\frac{1-s}{s}*R_{2}
$$
![[Pasted image 20241224114338.png]]!
Als voorbeeld nemen we $s_n=0,04$ dan hebben we een verhouding van $\frac{1}{5}$
$$
\frac{R_{2}}{s_{n}}=\frac{R_{2}}{0,04}=25R_{2}\implies \frac{X_{2(st)}}{R_{2}}=\frac{5R_{2}}{25s_{n}}=\frac{5}{25}=\frac{1}{5}
$$
$$
X_{2(st)}=5R_{2}
$$
![[Pasted image 20241224115046.png]]
##### EQ schema: REFLECTIE
![[Pasted image 20241224122140.png]]


#### [[Tekeningen Machines#Belast#Vector diagram|Vector diagram]]
![[Pasted image 20241224104000.png]]
1. $\begin{cases}-\overline{E_{1}},\overline{E_{1}},\overline{E_{2(st)}}\\\overline{I_{0}}\\\overline{\Phi}\end{cases}$
2. $\overline{I_{2(n)}}$
3. $\overline{E_{2(st)}}=\frac{R_{2}}{s}*\overline{I_{2(n)}}+\overline{X_{2(st)}}*\overline{I_{2(n)}}$
4. $\overline{\Phi_{2}}$
5. $\overline{\Phi_{1}}=-\overline{\Phi_{2}}$
6. $\overline{I'_{1(n)}}$
7. $\overline{I_{1}(n)}=\overline{I_{0}}+\overline{I'_{1(n)}}$
8. $\overline{U_{1}}=-\overline{E_{1}}+R_{1}*\overline{I_{1(n)}}+\overline{X_{1}}*\overline{I_{1(n)}}$

## Rendement en Vermogensverdeling

$$
\begin{aligned}
P_{1}=P_{toe} \\
=\sqrt{ 3 }*U_{F_{1}}*I_{F_{1}}*\cos \phi_{F_{1}} \\
=\sqrt{ 3 }*U_{L_{1}}*I_{L_{1}}*\cos \phi_{F_{1}}
\end{aligned}
$$
### Stator
#### Verliezen
De koperverliezen in de stator zijn veranderlijk en ==kwadratisch afhankelijk van de statorstroom en afhankelijk van de ohmse weerstand van de statorwikkeling==
$$
P_{Cu_S}=3*R_{1}*I^2_{F_{1}}
$$
De ijzerverliezen in de stator zijn ==constant bij constante statorspanning en constante statorfrequentie==
$$
P_{Fe_{S}}=3U_{F_{1}}*I_{F_{1}0}*\cos \phi_{F_{1}0}-3R_{1}*I^2_{F_{1}0}
$$
Het resterend actief vermogen is het vermogen dat overgedragen wordt via de luchtspleet naar de rotor $P_{L}$
$$
P_{L}=P_{1}-P_{Cu_{S}}-P_{Fe_{S}}
$$
Van uit de rotor gezien is dit het gedissipeerd vermogen in de totale rotorweerstand
$$
P_{L}=3*\frac{R_{2}}{s}*I^2_{F_{2}}
$$
### Rotor
#### Inwendig vermogen
Formule wanneer rekening houdend met $P_{Fe_{R}}$
$$
P_{i}=P_{L}-P_{Cu_{R}}-P_{Fe_{R}}
$$
Formule als je de rotor ijzerverliezen verwaarloosd ($P_{Fe_{R}}$)
$$
P_{i}=3*\frac{1-s}{s}*R_{2}*I^2_{F_{2}}
$$
#### Verliezen
##### Koper
De koper verliezen gelijk verhaal als die van de stator,  ==kwadratisch afhankelijk van de rotorstroom en afhankelijk van de ohmse weerstand van de rotorwikkeling/staaf==
$$
P_{Cu_{R}}=3*R_{2}*I^2_{F_{2}}
$$
##### ijzer
==Zijn constant bij constante frequentie, deze is meestal zeer klein omdat $f_{r}$ een fractie is van $f_{s}$ , wordt vaak verwaarloosd tenzij anders opgegeven in de oefening.== 
##### Ventilatie- en wrijvingsverliezen $P_{v}$
Bovenop de Koper en ijzerverliezen moeten we ook nog deze overige verliezen aftrekken van het inwendig vermogen
#### Nuttig vermogen
$$
P_{2} \text{ of }P_{as}\text{ of }P_{n} \text{ of }P_{mech}
$$
$$P_{2}=P_{i}-P_{v}$$

### Rendement $\eta$
Het rendement is berekend door het nuttige vermogen te delen door het opgenomen vermogen
$$
\eta=\frac{P_{2}}{P_{1}}*100\%
$$


## Vermogen en rendement

### Actief opgenomen vermogen
Het driefasig opgenomen elektrisch actieve vermogen kan worden berekend met:
$$
P_1 = 3 \cdot U_{F,1} \cdot I_{F,1} \cdot \cos \varphi_{F,1}
$$
of:
$$
P_1 = \sqrt{3} \cdot U_{L,1} \cdot I_{L,1} \cdot \cos \varphi_{F,1}
$$
- $U_{F,1}$: Fasespanning.
- $U_{L,1}$: Lijnspanning.
- $I_{F,1}$: Fasestroom.
- $I_{L,1}$: Lijnstroom.
- $\cos \varphi_{F,1}$: Arbeidsfactor.

---

### Vermogensverdeling
Het opgenomen vermogen $P_1$ wordt verdeeld over verschillende verliezen en nuttig vermogen.

#### In de stator
1. **Statorkoperverliezen**:
   $$
   P_{Cu,S} = 3 \cdot R_1 \cdot I_{F,1}^2
   $$

   - $R_1$: Ohmse weerstand van de statorwikkeling.
   - $P_i$: Inwendig vermogen.

2. **Statorijzerverliezen**:
   $$
   P_{Fe,S} = 3 \cdot U_{F,1} \cdot I_{F,1,0} \cdot \cos \varphi_{F,1,0} - 3 \cdot R_1 \cdot I_{F,1,0}^2
   $$
   Deze verliezen zijn constant bij nominale spanning en frequentie.

#### Overdracht van stator naar rotor
Het luchtspleetvermogen $P_L$ is:
$$
P_L = P_1 - P_{Cu,S} - P_{Fe,S}
$$
of vanuit rotorzicht:
$$
P_L = 3 \cdot \frac{R_2}{s} \cdot I_{F,2}^2
$$

#### In de rotor
1. **Rotorkoperverliezen**:
   $$
   P_{Cu,R} = s \cdot P_L
   $$
   of:
   $$
   P_{Cu,R} = 3 \cdot R_2 \cdot I_{F,2}^2
   $$

2. **Inwendig vermogen**:
   $$
   P_i = P_L - P_{Cu,R} = P_{L}\cdot (1-s) =P_{Cu_{R}}*\frac{1-s}{s}
   $$

3. **Mechanisch nuttig vermogen**:
   $$
   P_2 = (1 - s) \cdot P_L
   $$
   of:
   $$
   P_2 = P_i - P_v
   $$
   - $P_v$: Mechanische verliezen door wrijving en ventilatie.

---

### Rendement
Het rendement wordt berekend als:
$$
\eta = \frac{P_2}{P_1} \cdot 100\%
$$
- $P_2$: Nuttig vermogen.
- $P_1$: Opgenomen vermogen.

---

### Bijzonderheden
- **Luchtspleetvermogen** is het vermogen dat via de luchtspleet wordt overgedragen aan de rotor.
- **Slip** ($s$): De verhouding tussen toerentalverschil en synchrone snelheid, essentieel voor verliesanalyse.
- **Mechanische verliezen** ($P_v$): Worden vaak constant aangenomen bij nominale snelheid.

---

### Grafisch
#### Stator
![[Pasted image 20241227100359.png]]
#### Luchtspleet
![[Pasted image 20241227100417.png]]
#### Rotor
![[Pasted image 20241227100438.png]]
![[Pasted image 20241227100449.png]]

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
$$of$$
M_{i}=f(n_{r})
$$
$$
M_{i}\approx \cancel{ \frac{1}{\omega_{s}}\cdot3\cdot \frac{U^2_{1}}{k^2} }\cdot \frac{s\cdot \cancel{ R_{2} }}{R_{2}^2+s^2\cdot X_{2_{st}}^2}
$$
Vervangen door een constante
$$
M_{i}\approx C^{te}\cdot \frac{s}{R_{2}^2+s^2\cdot X_{2_{st}}^2}
$$
#### Belangrijke punten
- $M_{i}=0\implies s=0\implies n_{r}=n_{s}\implies v_{rel}=0$
- $M_{i}\to{0}\implies s\to \pm\infty$
- $M_{i}>0$
- $\pm M_{i_{st}}\implies s=\pm1$
- $M_{i}=max$
![[Pasted image 20241225091939.png]]