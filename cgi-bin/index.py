#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi, cgitb
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

cgitb.enable()

def calcular(altura, peso):
  a = float(altura)
  p = float(peso)
  resultado = float((p / (a**2)))
  return "%.2f" % resultado

print("""
<html>
    <head>
        <title>Calculadora de IMC</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="../css/estilo.css" />
    </head>
    <body>
        <h1>Calculadora IMC</h1>
        <hr/>
        <h3>O cálculo mostra se o seu peso está saudável.</h3>
        <form action="" method="POST">
            <label class="peso">Peso:</label>
            <input name="peso" class="ent1"/>
            <label class="altura">Altura:</label>
            <input name="altura" class="ent2"/>
            <button type="submit">Calcular</button>
        </form>
""")
#Create instance of FieldStorage
form = cgi.FieldStorage()
a = form.getvalue('altura')
p = form.getvalue('peso')
if a and p:
  print(f"""
          <label class="resultado">Resultado:</label>
          <label class="quadro" style="text-align:center;">
              {calcular(str(form.getvalue('altura')).replace(',', '.'), str(form.getvalue('peso')).replace(',', '.'))}
          </label>
  """)
print("""
        <table>
            <tr>
                <th>Classificação</th>
                <th>IMC</th>
            </tr>
            <tr class="linha1">
                <td>Abaixo do peso</td>
                <td>Abaixo 18,5</td>
            </tr>
            <tr class="linha2">
                <td>Peso normal</td>
                <td style="text-align:center;">18,5 - 24,9</td>
            </tr>
            <tr class="linha3">
                <td>Sobrepeso</td>
                <td style="text-align:center;">25 - 29,9</td>
            </tr>
            <tr class="linha4">
                <td>Obesidade Grau I</td>
                <td style="text-align:center;">30 - 34,9</td>
            </tr>
            <tr class="linha5">
                <td>Obesidade Grau II</td>
                <td style="text-align:center;">35 - 39,9</td>
            </tr>
            <tr class="linha6">
                <td>Obesidade Grau III ou Mórbida</td>
                <td style="text-align:center;">>= 40</td>
            </tr>
            <tr>
                <td></td>
                <td></td>
            </tr>
        </table>
    </body>
</html>
""")