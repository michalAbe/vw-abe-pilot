vw-abe-pilot — UI pack (staging)
--------------------------------
Cieľ: pridať personalizované prvky (logo Škoda × Tesla, pozdrav "Hi Abe, let's go!")
bez zásahu do jadra, najprv ako nenáročný overlay/hook.

Čo je v balíku:
- ui/assets/abe/images/logo_abe_skoda_tesla.svg  -> placeholder logo
- ui/assets/abe/sounds/hi_abe_placeholder.txt    -> sem neskôr vložíme WAV/OGG s "Hi Abe, let's go!"
- ui/abe_ui_config.json                          -> jednoduchá konfigurácia UI (greeting, zap/vyp)
- openpilot/ui/abe_ui_hook.py                    -> placeholder hook na zobrazenie greeting overlay

Integrácia (staging):
1) Nahoď tieto súbory do repozitára (rovnaké cesty).
2) V budúcom kroku pridáme volanie abe_ui_hook z hlavného UI loopu (QML/Py),
   aby sa pri štarte zobrazil overlay s logom a greeting textom + optional zvuk.
3) Keď bude hook fungovať, nahradíme placeholder zvuk reálnym súborom WAV/OGG
   a upravíme logo podľa tvojich predstáv.

Poznámky:
- Tento balík je bezpečný na nahratie do repa; nič nekazí build (len placeholders).
- Keď budeš chcieť, doplníme aj custom spalsh-screen a farby témy.
