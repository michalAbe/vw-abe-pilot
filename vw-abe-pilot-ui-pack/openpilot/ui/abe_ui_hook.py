# Abe UI Hook (staging)
# TODO: Integrovať do UI loopu: pri štarte načítaj ui/abe_ui_config.json
# a zobraz overlay s logom + greeting textom. Ak play_sound=True, prehraj zvuk.
#
# Pseudocode:
#   cfg = load_json('ui/abe_ui_config.json')
#   if cfg['enable_greeting']:
#       draw_overlay_text(cfg['greeting_text'])
#       draw_overlay_image(cfg['logo_path'])
#       if cfg['play_sound']:
#           play_sound(cfg['sound_path'])
#       sleep(cfg['greeting_timeout_ms'] / 1000.0)
#
# Pozn.: Toto je len placeholder, aby bol jasný entrypoint.

def abe_show_greeting(ui_ctx):
    # ui_ctx: placeholder objekt s metodami na kreslenie a prehratie zvuku
    try:
        ui_ctx.debug_note = "ABE UI hook loaded (placeholder)"
    except Exception:
        pass
