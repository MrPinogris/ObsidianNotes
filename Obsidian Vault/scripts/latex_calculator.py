import sys
from sympy.parsing.latex import parse_latex
import pyperclip


# Controleer of er invoer is gegeven
try:
    if len(sys.argv) > 1:
        latex_input = sys.argv[1]
        latex_input = latex_input.replace(',', '.')  # Zorg dat decimale komma's worden verwerkt
        expression = parse_latex(latex_input)
        result = expression.evalf()

        # Rond het resultaat af op twee decimalen
        rounded_result = round(float(result), 2)

        print(f"Resultaat: {rounded_result}")

        # Kopieer naar klembord
        pyperclip.copy(str(rounded_result))
        print("Resultaat is gekopieerd naar het klembord!")
    else:
        print("Geen invoer ontvangen.")
except Exception as e:
    print(f"Fout: {e}")

