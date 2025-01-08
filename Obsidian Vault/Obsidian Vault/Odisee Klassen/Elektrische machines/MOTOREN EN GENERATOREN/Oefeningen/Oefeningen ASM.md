## Oefening 1
### Gegeven
Een asynchrone motor werd zespolig uitgevoerd en draait aan 970 tpm. De netfrequentie is 50Hz.

### Gevraagd
1. De absolute slip?
   $s_{a}=n_{s}-n_{r}=1000-970=30tpm$
   $n_{s}=\frac{60\cdot50}{3}=1000tpm$
2. De relatieve slip?
   $s_{r}=\frac{s_{a}}{n_{s}}=0,03$
3. De frequentie van de rotorstroom?
   $f_{r}=f_{s}\cdot s_{r}=0,03\cdot 50=1,5Hz$

## Oefening 2

### Gegeven
Een vierpolige ASM met slip van 4% is aangesloten op een net met $f_{s}=50\text{Hz}$

### Gevraagd
1. $n_{r}$
   $$
n_{r}=n_{s}\cdot s_{r}= \frac{60\cdot50}{2}\cdot (1-0,04)= 1440tpm
$$

## Oefening 3

### Gegeven
Een achtpolige ASM is aangesloten op een net met $f_{s}=50\text{Hz}$. De $f_{r}=1\text{Hz}$

### Gevraagd
1. $s$?
   $$
s = \frac{f_{r}}{f_{r}}=\frac{1}{50}= 2\%
$$
2. $n_{r}$?
   $$
n_{r}=\frac{f_{s}-f_{r}\cdot60}{4}=\frac{49\cdot60}{4}=735\text{tpm}
$$


- [ ] Bereken LaTeX: `cmd /c start "" "C:\Users\alexa\Desktop\Obsidian\Obsidian Vault\Latex Calculator\run_calculator.bat"`
## Oefening 4

### Gegeven
Een ASM met  $P_{\text{as}}=2,2\text{kW}$ en $U_{1}=400\text{V@}50\text{Hz}$ in ster. $P=3$ $s_{n}=5\%$. $\cos \varphi_{1}=0,75$ en $\eta=81\%$ 

### Gevraagd
1. $n_{r}=\text{ ?}$
   $$
n_{r} = n_{s} \cdot s = \frac{50\cdot60}{3}\cdot 95\% = 950\text{tpm}
$$
2. $I_{1}=\text{ ?}$
   $$
P_{1}=\frac{P_{as}}{81\%}=2716\text{W}
$$
   $$
P=\sqrt{ 3 }\cdot U_{L}\cdot I_{L}\cdot \cos \varphi_{1} \implies I_{1}=\frac{P_{1}}{U_{1}\cdot \sqrt{ 3 }}= \frac{2716}{400\cdot \sqrt{ 3 }\cdot 0,75}=5,227\text{A}
$$
3. $M_{n}=\text{ ?}$
   $$
M=\frac{P_{as}}{\omega_{r}}=\frac{2200}{\frac{n_{r}}{60}\cdot 2\pi}= \frac{2200}{\frac{950}{60}\cdot 2\pi}=22,11\text{Nm}
$$

## Oefening 5
### Gegeven
ASM $P=1$, $s_{n}=6\%$, $P_{1}=1410\text{W}$, $\eta=78\%$, $\cos \varphi= 0,86$, ster: $400/230\text{V @ 50Hz}$, $I_{st}= 6\cdot I_{n}$, $M_{st}= 2,2\cdot M_{n}$.
### Gevraagd
1. $I_{st}\text{ ?}$
   $$
P_{1}=\sqrt{ 3 }\cdot U_{L}\cdot I_{L}\cdot \cos \varphi_{1}\implies \frac{I_{st}}{6}=I_{st}\implies\frac{P_{1}\cdot 6}{\sqrt{ 3 }\cdot U_{L}\cdot \cos \varphi_{1}}= \frac{1410\cdot 6}{\sqrt{ 3 }\cdot 400\cdot 0,86}= 14,1987\text{A}= I_{\text{st}}
$$
2. $M_{st}\text{ ?}$
   $$
M_{n}= \frac{P_{as}}{\omega_{r}}=\frac{P_{1}\cdot\eta}{\omega_{s}\cdot (1-s)}=\frac{1410\cdot0,78}{50\cdot 0,94}= 3,72\text{Nm}\implies M_{st}=2,2\cdot M_{n}=2,2\cdot 3,72= 8,193\text{Nm}
$$
## Oefening 6
### Gegeven
Sleepringmotor, $E_{2_{st}}=\frac{100\text{V}}{\sqrt{ 3 }}$, ster, $R_{2}=0,2\ohm$, $X_{2_{st}}=1 \ohm$, $s_{n}=4\%$
### Gevraagd
1. $I_{r_{st}}\text{ ?}$
   $$
I_{2}=\frac{E_{2_{st}}}{\sqrt{ \frac{R_{2}}{s}^2\cdot X_{2_{st}}^2 }}=\frac{\frac{100}{\sqrt{ 3 }}\text{V}}{\sqrt{ \frac{0,2\ohm}{1}^2\cdot 1\ohm}}=56,61\text{A}
$$
2. $I_{r_{n}}\text{ ?}$
   $$
I_{r_{n}}=\frac{E_{2_{st}}}{\sqrt{ \frac{R_{2}}{s}^2+ X_{2_{st}}^2 }}=\frac{\frac{100}{\sqrt{ 3 }}\text{V}}{\sqrt{ \frac{0,2\ohm}{0,04}^2+ 1^2\ohm}}=11,323\text{A}
$$
3. Hoe kan de grootte van beide stromen verklaard worden en in verband gebracht worden met elkaar?
	- Bij start is de rotorspanning veel groter en de inductantie minimaal omdat de Rotorstroom frequentie maximaal is, hierdoor is de stroom maximaal.
	- Bij nominaal draaien is de rotorfrequentie veel kleiner dus de opgewekte rotor EMK ook veel kleiner maar de reactantie veel groter omdat de frequentie veel kleiner is $X_{L}=2\pi \cdot f\cdot L$ en $E_{2} = B\cdot l \cdot v_{rel}$ als de rotor frquentie kleiner is zal de relative snelheid ook veel kleiner zij deze zijn recht evenredig verbonden

## Oefening 7
### Gegeven
Sleepringen motor, $E_{2_{st}}= \frac{500}{\sqrt{ 3 }}\text{V}$, $f_{s}= 50\text{Hz}$, $R_{2}=0,2 \ohm$, $L_{2}=0,04\text{H}$, $s_{n}= 5\%$, $R_{\text{aanzet}}= 9,8 \ohm$
### Gevraagd
1. $I_{r_{st}}\text{ ?}$
   $$
X_{st}= 2\pi \cdot f_{s}\cdot L_{2}=2\pi\cdot 50\cdot 0,04=12,566 \ohm
$$
$$
I_{r_{st}}=\frac{E_{2_{st}}}{\sqrt{ \frac{R_{2}+R_{\text{aanzet}}}{1}^2+X_{st}^2 }}=17,975\text{A}
$$
2. $\cos\varphi_{st}\text{ ?}$
   $$
\cos \varphi_{st}= \frac{R}{Z}=\frac{10}{\sqrt{ 10^2+12,566^2 }}=0,623
$$
3. $I_{r_{n}}\text{ ?}$
   $$
I_{r}=\frac{E_{2_{st}}}{\sqrt{ \frac{R_{2}}{s}^2+X_{st}^2 }}=21,89\text{A}
$$
## Oefening 8
### Gegeven
Sleepringmotor, ster $U_{1}=400\text{V@50Hz}$, $s_{n}=4\%$, $I_{s_{n}}=50\text{A}$, $\cos \varphi_{n}=0,86$, als $I_{s}=25\text{A}$ dan is $\cos \varphi=0,8$ en $P_{\text{totaal verlies}}=2400\text{W}$, totale ijzer- en wrijvingsverliezen zijn: $P_{v}= 1600\text{W}$.
### Gevraagd
1. $P_{as}\text{ ? Bij halve belasting}$
   $$
P_{1}=\sqrt{ 3 }\cdot U_{1}\cdot I_{1}\cdot \cos \varphi_{1}
$$
$$
P_{as}=P_{1}-P_{\text{totaal verlies}}=\sqrt{ 3 }\cdot 400\text{V}\cdot 25\text{A}\cdot 0,8-2400\text{W}=11456\text{W}
$$
2. $P_{as}\text{ ? Bij volle belasting}$
   $$
P_{Cu_{vollast}}=(P_{\text{totaal verlies halflast}}-P_{Fe})\cdot 2^2=800\cdot 2^2=3200\text{W}
$$
   $$
P_{as}=P_{1}-P_{Fe}-P_{Cu}=\sqrt{ 3 }\cdot 400\text{V}\cdot 50\text{A}\cdot 0,86 - 1600-3200= 24991\text{W}
$$
3. $\eta\text{ ? bij vollast}$
   $$
\eta=\frac{P_{as}}{P_{1}}=\frac{24991}{\sqrt{ 3 }\cdot 400\text{V}\cdot 50\text{A}\cdot 0,86}=83,89\%
$$

## Oefening 9
### Gegeven
ASM, $P=4$, ster $U_{1}=400\text{V@50Hz}$, $s_{n}=3\%$, $N_{s}=80$, $N_{r}=32$, $R_{2}=0,04 \ohm$, $X_{2}=0,24$, $P_{Fe}=410\text{W}$.
### Gevraagd
1. $\Phi$
   $$
E_{1}= \frac{U_{1}}{\sqrt{ 3 }}=\frac{400}{\sqrt{ 3 }}=230,94\text{V}
$$
   $$
E_{1}=4,44\cdot f_{s}\cdot N_{s}\cdot \Phi\implies \Phi=\frac{E_{1}}{4,44\cdot f_{s}\cdot N_{s}}= \frac{400\cdot \sqrt{ 3 }}{4,44\cdot 50\cdot 80}= 0,0130\text{Wb}
$$
2. $E_{2_{st}}$
   $$
E_{2_{st}}=\frac{E_{1}\cdot N_{2}}{N_{2}}=\frac{230\cdot32}{80}=92\text{V}
$$
3. $E_{2_n}$
   $$
E_{2_{n}}=E_{2_{st}}\cdot s=0,03\cdot 92=2,67\text{V}
$$
4. $I_{2_{st}}$
   $$
I_{2_{st}}=\frac{E_{2_{st}}}{Z_{2_{st}}}=\frac{92}{\sqrt{ 0,04^2+0,24^2 }}=378,11\text{A}
$$
5. $I_{2_{n}}$
   $$
I_{2}=\frac{E_{2_{st}}}{\sqrt{ \frac{R_{2}}{s}^2+X_{2_{st}}^2 }}=\frac{92}{\sqrt{ \frac{0,04}{0,03}^2+0,24^2 }}=67,9\text{A}
$$
6. $I_{1_{st}}$
   $$
\overline{I_{1_{st}}}=\overbrace{ \overline{I_{0}} }^{\approx 0 }+\overline{I_{1}'}\implies I_{2_{st}}\cdot k=378,12\cdot 0,4=151,25\text{A}
$$
7. $I_{1_{n}}$
   $$
I_{1_{n}}=\overbrace{ \overline{I_{0}} }^{\approx 0 }+\overline{I_{1}'}\approx I_{2_{n}}\cdot k=67,9\cdot 0,4= 27,16\text{A}
$$
8. $\eta_{n}\text{ met }\cos \varphi=0,8\text{ en }P_{v_{s}}=700\text{W}$
   $$
P_{toe}=3\cdot U_{1_{F}}\cdot I_{1_{F}}\cdot \cos \varphi_{1}=\sqrt{ 3 }\cdot 400\cdot 27,16\cdot 0,8= 15055\text{W}
$$
$$
P_{as}=P_{toe}-P_{v_{1}}-\overbrace{ P_{Cu_{2}} }^{ 3\cdot R_{2}\cdot I_{2_{n}}^2 }=15055-700-553,396-410=13390,2\text{W}
$$
   $$
\eta_{n} =\frac{P_{as}}{P_{toe}}=\frac{13390,2}{15055}=88,95\%
$$
9. $M_{n}$
   $$
M_{n}=\frac{P_{n}}{\underbrace{ \omega_{r} }_{ =n_{r}\cdot \frac{2\pi}{60}=n_{s}*(1-s)\cdot \frac{2\pi}{60} }}=\frac{13392}{\frac{2\pi}{60}\cdot 750\cdot(1-0,03)}=175,79\text{Nm}
$$
## Oefening 10
### Gegeven
ASM, $P_{as}=1100\text{kW}$, $n_{r}=147$, ster $U_{1}=6000\text{V@50Hz}$, $\eta=90\%$ met $\cos \varphi=0,88$, $s_{n}=2\%$
### Gevraagd
1. $p\text{ ?}$
   $$
n_{s}= \frac{n_{r}}{1-s} \implies n_{s}=\frac{60\cdot f}{P}\implies P=\frac{60\cdot f}{n_{s}}=\frac{60\cdot50}{\frac{147}{0,98}}=20\implies p=2\cdot P=40
$$
2. $I_{s_{n}}$
   $$
\frac{P_{2}}{\eta}=P_{toe}=\sqrt{ 3 }\cdot U_{L}\cdot I_{L}\cdot \cos \varphi_{1}\implies I_{s_{n}}= \frac{\frac{P_{2}}{\eta}}{\sqrt{ 3 }\cdot U_{L}\cdot \cos \varphi_{1}}=\frac{\frac{1100000}{0,9}}{\sqrt{ 3 }\cdot 6000\cdot 0,88}=133.65
$$
3. $P_{Cu}\text{ ? als }P_{\text{verlies stator}}=4\%\cdot P_{1}$
   $$
P_{1}=P_{L}+4\%\cdot P_{1}\implies P_{L}=\frac{1100000}{0,9}\cdot 0,96=1.17M\text{W}
$$
$$
P_{Cu}=3\cdot R_{2}\cdot I_{2}^2
$$
$$
P_{L}=3\cdot \frac{R_{2}}{s}\cdot I_{2}^2= \frac{P_{Cu}}{s}
$$
$$
P_{Cu}=P_{L}*s=1173333.33\cdot 0,02= 23466.67\text{W}
$$
## ==Oefening 11==
### Gegeven
ASM, $P_{as}=22\text{kW}$, $50\text{Hz}$, $P=6$, $s_{n}=4\%$, $P_{Fe}= 250\text{W}$
### Gevraagd
1. $s_{a}\text{ ?}$
   $$
n_{s}=\frac{60\cdot50}{3}=1000\text{tpm}
$$
$$
s_{a}= n_{s}\cdot s=1000\cdot 0,04=\text{tpm}
$$
2. $P_{Cu}\text{ ?}$

$$
P_{i}=22000+250=22250.0
$$
   $$
P_{L}=P_{v}+P_{Cu}+P_{as}=3\cdot \frac{R_{2}}{s}\cdot I_{2}^2=\frac{P_{Cu}}{s}=\frac{P_{i}}{1-s}=\frac{22250}{1-0,04}=23177.08
$$
$$
P_{Cu}=P_{L}-P_{i}=23177.08-22250=927.08\text{W}
$$
## Oefening 12
### Gegeven
$P=3$, $P_{as}=10\text{kW}$, $50\text{Hz}$, $P_{Cu_{r}}=400\text{W}$, $P_{v_{s}}= 100\text{W}$, $\eta=80\%$
### Gevraagd
1. $s\text{ ?}$
   $$
s = \frac{P_{Cu}}{P_{L}}=\frac{400}{10000-100}\cdot 100=4.04\%
$$
2. $n_{r}\text{ ?}$
   $$
n_{r}=n_{s}\cdot (1-s)=\frac{60\cdot50}{3}\cdot (1-0,0404)=959.6\text{tpm}
$$
3. $M_{as}$
   $$
M_{as}=\frac{P_{as}}{\omega _{r}}=\frac{10000\cdot 0.8}{\frac{2\cdot \pi}{60}\cdot959.6}=79.6
$$
## Oefening 13
### Gegeven
ASM, $R_{2}=0,01\ohm$, $X_{2_{st}}=0,06\ohm$
### Gevraagd
1. $R_{aanzet}\text{ voor }s_{k}=1$
   $$
s_{k}=\frac{R_{2}}{X_{2_{st}}}=\frac{0,01+0,05}{0,06}=1
$$
## Oefening 14
### Gegeven
ASM, $R_{1}=R_{1}$, $X_{2_{st}}=8R_{2}$
### Gevraagd
1. $R_{\text{aanzet}}\text{ bij aanzetten maximaal koppel te berijken}$
   $$
1=\frac{1R}{8R}\implies R_{aanzet}=X_{2_{st}}-R_{2}=7R_{2}
$$
## Oefening 15
### Gegeven
sleepringenmotor, $50\text{Hz}$, $E_{st}\text{(ster)}=173\text{V}$, $R_{2}=0,3\ohm$, $X_{2_{st}}=1,25\ohm$
### Gevraagd
1. $I_{r_n}\text{ bij }s_{n}=4\%$
   $$
I_{r_{n}}=\frac{E_{2_{st}}}{\sqrt{ \frac{R_{2}}{s}^2+X_{2_{st}}^2 }}=\frac{\frac{173}{\sqrt{ 3 }}}{\sqrt{ \frac{0,3}{0,04}^2+1,25^2 }}=13.14\text{A}
$$
2. $R_{\text{extra}}$ als  $I_{st}=I_{n}$
   $$
   \frac{0,3}{0,04}=0,3+R_{extra}\implies R_{extra}=\frac{0,3}{0,04}-0,3=7.2 \ohm
$$
   
## Oefening 16
### Gegeven
$P=2$, $R_{2}=0,1\ohm$, $X_{2_{st}}=0,5\ohm$, $50\text{Hz}$, $E_{2_{st}}=173\text{V}$
### Gevraagd
1. $I_{r}\text{ bij }n_{r}=1455\text{tpm}$
   $$
1-s_{n}=\frac{1455}{1500}\cdot 100=97.0\%
$$
$$
I_{r_{n}}=\frac{E_{2_{st}}}{\sqrt{ \frac{R_{2}}{s}^2+X_{2_{st}}^2 }}=\frac{\frac{173}{\sqrt{ 3 }}}{\sqrt{ \frac{0,1}{0,03}^2+0,5^2 }}=29.63\text{A}
$$
2. De weerstand die in elke rotorfase moet opgenomen worden om bij dezelfde stroom als in het eerste geval het toerental op 900 tpm terug te brengen.
$R_{voor}$ bij $n_{r} = 900$ zodat $I_{2}=I_{2_{n}}$
$$
1-s=\frac{900}{1500}=0.6\implies s=0,4
$$
$$
\frac{0,1}{0,03}=\frac{0,1+R_{voor}}{0,4}\implies R_{voor}=(\frac{0,1}{0,03}-\frac{0,1}{0,4})\cdot 0,4= 1.23\ohm
$$