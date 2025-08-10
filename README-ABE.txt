vw-abe-pilot (staging package)
--------------------------------
Toto je dočasný balík na nahratie do GitHubu, aby sme mali pripravenú štruktúru pre úpravy.

Čo je vo vnútri:
- openpilot/selfdrive/controls/abe_lane_change.py  -> miesto pre logiku zmeny pruhu cez blinker
- openpilot/selfdrive/car/volkswagen/interface.py  -> hák na aktiváciu logiky pre MEB/Enyaq
- openpilot/selfdrive/car/volkswagen/values.py     -> flagy/konštanty
- CHANGELOG.md, FILE-LIST.txt

Dôležité:
- Toto NIE JE finálny kód, iba štruktúra + TODO body. Po nahratí na GitHub doplníme reálny kód cez webový editor (copy/paste).

Postup po nahratí:
1) Skontroluj súbory na GitHube.
2) Otvor openpilot/selfdrive/controls/abe_lane_change.py a vložíme reálnu implementáciu (napíšem ti ju krokom).
3) Upravíme volkswagen/interface.py, aby volal logiku pri blinker smere (L/R) a rýchlostnom prahu.
4) Uložíš a otestujeme v aute.
