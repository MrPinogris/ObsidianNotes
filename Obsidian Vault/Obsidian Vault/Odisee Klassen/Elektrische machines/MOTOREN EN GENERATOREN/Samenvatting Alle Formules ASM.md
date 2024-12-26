# Samenvatting Alle Formules van ASM

## Slip
### Absolute slip
$$s_a = n_s - n_r = \frac{60}{2\pi} \cdot (\omega_s - \omega_r)$$

### Relatieve slip
$$s = \frac{n_s - n_r}{n_s} = \frac{\omega_s - \omega_r}{\omega_s}$$

### Procentuele slip
$$s \cdot 100\%$$

### Rotorsnelheid
$$n_r = n_s \cdot (1 - s)$$
$$\omega_r = \omega_s \cdot (1 - s)$$

Meer uitleg: [[ASM en Gelijkstoom machines#Slip|Slip]].

## Synchrone snelheid
$$n_s = \frac{60 \cdot f_s}{p}$$
- $f_s$: Netfrequentie.
- $p$: Aantal polen.

Meer uitleg: [[ASM en Gelijkstoom machines#Synchrone snelheid|Synchrone snelheid]].

## Elektromotorische kracht (EMK)
### Stator (stilstand)
$$E_1 = 4,44 \cdot f_s \cdot N_s \cdot \Phi$$

### Rotor (stilstand)
$$E_{2(st)} = \frac{E_1}{k} = 4,44 \cdot f_s \cdot N_r \cdot \Phi$$

### Rotor (dynamisch)
$$E_2 = s \cdot E_{2(st)} = s \cdot \frac{E_1}{k}$$

Meer uitleg: [[ASM en Gelijkstoom machines#EMK|EMK]].

## Rotorstroom
$$I_2 = \frac{E_{2(st)}}{\sqrt{\left( \frac{R_2}{s} \right)^2 + X_{2(st)}^2}}$$

Meer uitleg: [[ASM en Gelijkstoom machines#Rotorstroom|Rotorstroom]].

## Inwendig koppel
### Luchtspleetvermogen
$$P_L = 3 \cdot \frac{R_2}{s} \cdot I_2^2$$

### Moment
$$M_i = \frac{P_i}{\omega_s}$$

### Inwendig koppel met constante
$$M_i \approx C^{te} \cdot \frac{s \cdot R_2}{R_2^2 + (s \cdot X_{2,ST})^2}$$

Meer uitleg: [[ASM en Gelijkstoom machines#Inwendig koppel|Inwendig koppel]].

## Kipslip
### Definitie
$$s_k = \frac{R_2}{X_{2,ST}}$$

### Afleiding uit momentformule
$$M_i = C^{te} \cdot \frac{s \cdot R_2}{R_2^2 + (s \cdot X_{2,ST})^2}$$

Meer uitleg: [[ASM en Gelijkstoom machines#Kipslip|Kipslip]].

## Rendement
$$\eta = \frac{P_2}{P_1} \cdot 100\%$$
- $P_2$: Nuttig vermogen.
- $P_1$: Opgenomen vermogen.

Meer uitleg: [[ASM en Gelijkstoom machines#Rendement|Rendement]].

## Frequentieafhankelijke grootheden
### Rotorfrequentie
$$f_r = s \cdot f_s$$

### Rotorreactantie
Bij stilstand:
$$X_{2(ST)} = \omega_s L_2 = 2 \pi f_s L_2$$

Bij draaiende rotor:
$$X_2 = \omega_r L_2 = 2 \pi f_r L_2 = s \cdot X_{2(ST)}$$

Meer uitleg: [[ASM en Gelijkstoom machines#Frequentieafhankelijke grootheden|Frequentieafhankelijke grootheden]].

## Equivalentieschema
### Met reflectie
Rotorimpedantie omgerekend naar de stator:
$$Z'_2 = \frac{Z_2}{k^2}$$

### Zonder reflectie
Rotor- en statorgrootheden blijven afzonderlijk.

Meer uitleg: [[ASM en Gelijkstoom machines#Equivalentieschema|Equivalentieschema]].

### Vervangweerstand van de rotor
$$R_b = \frac{R_2}{s} - R_2 = \frac{1 - s}{s} \cdot R_2$$

Meer uitleg: [[ASM en Gelijkstoom machines#Equivalentieschema|Equivalentieschema]].

## Aanloopstroom
$$I_{1,ST} = \frac{U_1}{\sqrt{(R_1 + k^2 \cdot R_2)^2 + (X_1 + k^2 \cdot X_{2,ST})^2}}$$

Meer uitleg: [[ASM en Gelijkstoom machines#Aanloopstroom|Aanloopstroom]].

## Dynamisch gedrag
$$M_i = M_T + J \cdot \alpha$$
- $M_T$: Tegenwerkend koppel.
- $J$: Traagheidsmoment.
- $\alpha$: Hoekversnelling.

Meer uitleg: [[ASM en Gelijkstoom machines#Dynamisch gedrag|Dynamisch gedrag]].
