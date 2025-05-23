# -*- coding: utf-8 -*-
"""Fuzzy_logic

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14m7RCNBqRltWi6iQmLCjlBhjx7C9GjoL
"""

!pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

suhu = np.arange(35, 41, 0.1)

rendah = fuzz.trimf(suhu, [35, 36, 36.5])
sedang = fuzz.trimf(suhu, [36, 37, 38])
tinggi = fuzz.trimf(suhu, [37.5, 39, 40])

plt.figure()
plt.plot(suhu, rendah, 'b', label='Rendah')
plt.plot(suhu, sedang, 'g', label='Sedang')
plt.plot(suhu, tinggi, 'r', label='Tinggi')
plt.title('Fuzzy Set Suhu Tubuh')
plt.xlabel('Suhu (derajat C)')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)
plt.show()

input_suhu = 22
suhu_rendah = fuzz.interp_membership(suhu, rendah , input_suhu)
suhu_sedang = fuzz.interp_membership(suhu, sedang, input_suhu)
suhu_tinggi = fuzz.interp_membership(suhu, tinggi, input_suhu)

print(f"Derajat keanggotaan suhu {input_suhu} derajat C:")
print(f"- Rendah: {suhu_rendah:.2f}")
print(f"- Sedang: {suhu_sedang:.2f}")
print(f"- Tinggi: {suhu_tinggi:.2f}")

"""1 : Ubah input_suhu jadi 22°C. Apa yang terjadi?
Jawab :Ketika nilai input_suhu diubah menjadi 22°C, hasil derajat keanggotaan untuk kategori Rendah, Sedang, dan Tinggi semuanya menjadi 0.00. Hal ini terjadi karena suhu 22°C berada di luar rentang nilai yang telah didefinisikan dalam himpunan fuzzy, yaitu antara 35°C hingga 40°C. Dengan kata lain, 22°C tidak termasuk dalam rentang yang memiliki keanggotaan pada kategori manapun, sehingga nilai keanggotaannya pada semua kategori (Rendah, Sedang, dan Tinggi) menjadi nol.


---


"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Fuzzy universe
suhu = np.arange(35, 41, 0.1)
kelembaban = np.arange(0, 101, 1)

# Fuzzy sets untuk suhu
rendah = fuzz.trimf(suhu, [35, 35, 36.5])
sedang = fuzz.trimf(suhu, [36, 37, 38])
tinggi = fuzz.trimf(suhu, [37.5, 39, 40])

# Fuzzy sets untuk kelembaban
kering = fuzz.trimf(kelembaban, [0, 0, 40])
normal = fuzz.trimf(kelembaban, [30, 50, 70])
basah = fuzz.trimf(kelembaban, [60, 100, 100])

# Visualisasi fuzzy suhu
plt.figure()
plt.plot(suhu, rendah, 'b', linewidth=1.5, label='Rendah')
plt.plot(suhu, sedang, 'g', linewidth=1.5, label='Sedang')
plt.plot(suhu, tinggi, 'r', linewidth=1.5, label='Tinggi')
plt.title('Fuzzy Set Suhu Tubuh')
plt.xlabel('Suhu (derajat C)')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)
plt.show()

# Visualisasi fuzzy kelembaban
plt.plot(kelembaban, kering, 'brown', linewidth=1.5, label='Kering')
plt.plot(kelembaban, normal, 'purple', linewidth=1.5, label='Normal')
plt.plot(kelembaban, basah, 'orange', linewidth=1.5, label='Basah')
plt.title('Fuzzy Set Kelembaban')
plt.xlabel('Kelembaban (%)')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)
plt.show()

# Input nilai
input_suhu = 35.2
input_kelembaban = 20

# Hitung derajat keanggotaan
suhu_rendah = fuzz.interp_membership(suhu, rendah, input_suhu)
suhu_sedang = fuzz.interp_membership(suhu, sedang, input_suhu)
suhu_tinggi = fuzz.interp_membership(suhu, tinggi, input_suhu)

kelembaban_kering = fuzz.interp_membership(kelembaban, kering, input_kelembaban)
kelembaban_normal = fuzz.interp_membership(kelembaban, normal, input_kelembaban)
kelembaban_basah = fuzz.interp_membership(kelembaban, basah, input_kelembaban)

# Aturan baru: jika suhu rendah DAN kelembaban kering → kipas = mati
rule_output = min(suhu_rendah, kelembaban_kering)

# Output
print(f"Input Suhu: {input_suhu} °C")
print(f"Input Kelembaban: {input_kelembaban}%\n")

print("Derajat Keanggotaan Suhu:")
print(f"- Rendah : {suhu_rendah:.2f}")
print(f"- Sedang : {suhu_sedang:.2f}")
print(f"- Tinggi : {suhu_tinggi:.2f}\n")

print("Derajat Keanggotaan Kelembaban:")
print(f"- Kering : {kelembaban_kering:.2f}")
print(f"- Normal : {kelembaban_normal:.2f}")
print(f"- Basah  : {kelembaban_basah:.2f}\n")

print("Aturan Fuzzy:")
print("Jika suhu rendah DAN kelembaban kering → kipas = mati")
print(f"Hasil inferensi (min): {rule_output:.2f}")

"""1.Tambahkan variabel kelembaban dan buat aturan baru (contoh: jika panas DAN lembab, kipas cepat) -> contoh ini tidak boleh digunakan
Jawab : Saya sudah menambahkan variabel kelembaban dan membuat aturan baru yaitu Jika suhu rendah DAN kelembaban kering → kipas = mati.



---

2.Mengapa suhu 28°C memiliki nilai keanggotaan di "Nyaman" dan "Panas"?
Jawab : karena Fungsi keanggotaan dalam fuzzy logic tidak memiliki batas yang kaku. Misalnya, suhu 28°C bisa termasuk dalam dua himpunan fuzzy sekaligus, yaitu nyaman [24, 28, 32] dan panas [28, 32, 36]. Pada suhu 28°C, nilai tersebut merupakan titik maksimum keanggotaan untuk kategori nyaman dengan derajat keanggotaan 1.0. Namun, karena 28°C juga merupakan titik awal dari kategori panas, maka suhu ini bisa memiliki derajat keanggotaan antara 0.0 hingga 1.0 dalam kategori panas, tergantung bentuk fungsi keanggotaannya. Dengan begitu, satu nilai suhu seperti 28°C dapat memiliki dua derajat keanggotaan di dua kategori berbeda.
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Universe of discourse
aqi = np.arange(0,301, 1)

# Fuzzy sets for Air Quality Index
baik = fuzz.trapmf(aqi, [0, 0, 25, 50])
sedang = fuzz.trimf(aqi, [25, 75, 125])
tidak_sehat = fuzz.trimf(aqi, [100, 150, 200])
sangat_tidak_sehat = fuzz.trimf(aqi, [175, 225, 275])
berbahaya = fuzz.trapmf(aqi, [250, 275, 300, 300])

# Visualize fuzzy sets
plt.figure(figsize=(12, 6))
plt.plot(aqi, baik, 'g', linewidth=1.5, label='baik')
plt.plot(aqi, sedang, 'y', linewidth=1.5, label='sedang')
plt.plot(aqi, tidak_sehat, 'orange', linewidth=1.5, label='tidak sehat')
plt.plot(aqi, sangat_tidak_sehat, 'r', linewidth=1.5, label='sangat tidak sehat')
plt.plot(aqi, berbahaya, 'purple', linewidth=1.5, label='berbahaya')
plt.title('Fuzzy set Indeks Kualitas Udara(AQI)')
plt.xlabel('AQI')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)
plt.show()

# Calculate membership for a specific input
input_aqi = 120
aqi_baik = fuzz.interp_membership(aqi, baik, input_aqi)
aqi_sedang = fuzz.interp_membership(aqi, sedang, input_aqi)
aqi_tidak_sehat = fuzz.interp_membership(aqi, tidak_sehat, input_aqi)
aqi_sangat_tidak_sehat = fuzz.interp_membership(aqi, sangat_tidak_sehat, input_aqi)
aqi_berbahaya = fuzz.interp_membership(aqi, berbahaya, input_aqi)

print(f"Derajat Keanggotaan AQI {input_aqi}:")
print(f"- Baik: {aqi_baik:.2f}")
print(f"- Sedang: {aqi_sedang:.2f}")
print(f"- Tidak Sehat: {aqi_tidak_sehat:.2f}")
print(f"- Sangat Tidak Sehat: {aqi_sangat_tidak_sehat:.2f}")
print(f"- Berbahaya: {aqi_berbahaya:.2f}")

"""Kontrol Air Conditioner"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Input variables
temperature = ctrl.Antecedent(np.arange(15, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(20, 101, 1), 'humidity')

# Output variable
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Membership functions for temperature
temperature['dingin'] = fuzz.trimf(temperature.universe, [15, 15, 20])
temperature['nyaman'] = fuzz.trimf(temperature.universe, [22, 26, 30])
temperature['panas'] = fuzz.trimf(temperature.universe, [28, 32, 40])

# Membership functions for humidity
humidity['kering'] = fuzz.trapmf(humidity.universe, [20, 20, 30, 45])
humidity['normal'] = fuzz.trimf(humidity.universe, [35, 50, 65])
humidity['lembab'] = fuzz.trapmf(humidity.universe, [55, 70, 100, 100])

# Membership functions for fan speed
fan_speed['mati'] = fuzz.trimf(fan_speed.universe, [0, 0, 25])
fan_speed['rendah'] = fuzz.trimf(fan_speed.universe, [0, 25, 50])
fan_speed['sedang'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['tinggi'] = fuzz.trimf(fan_speed.universe, [50, 75, 100])
fan_speed['maksimal'] = fuzz.trimf(fan_speed.universe, [75, 100, 100])

# Visualize membership functions
temperature.view()
humidity.view()
fan_speed.view()

# Define fuzzy rules
rule1 = ctrl.Rule(temperature['dingin'] & humidity['kering'], fan_speed['mati'])
rule2 = ctrl.Rule(temperature['dingin'] & humidity['normal'], fan_speed['mati'])
rule3 = ctrl.Rule(temperature['dingin'] & humidity['lembab'], fan_speed['rendah'])
rule4 = ctrl.Rule(temperature['nyaman'] & humidity['kering'], fan_speed['rendah'])
rule5 = ctrl.Rule(temperature['nyaman'] & humidity['normal'], fan_speed['sedang'])
rule6 = ctrl.Rule(temperature['nyaman'] & humidity['lembab'], fan_speed['tinggi'])
rule7 = ctrl.Rule(temperature['panas'] & humidity['kering'], fan_speed['tinggi'])
rule8 = ctrl.Rule(temperature['panas'] & humidity['normal'], fan_speed['tinggi'])
rule9 = ctrl.Rule(temperature['panas'] & humidity['lembab'], fan_speed['maksimal'])

# Create control system
ac_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
ac = ctrl.ControlSystemSimulation(ac_ctrl)

# Input values
ac.input['temperature'] = 30
ac.input['humidity'] = 75

# Compute result
ac.compute()
print(f"Untuk suhu 30°C dan kelembaban 75%, kecepatan kipas AC: {ac.output['fan_speed']:.2f}%")

# Visualize result
fan_speed.view(sim=ac)
plt.show()