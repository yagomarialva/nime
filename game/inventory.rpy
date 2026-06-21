# === SISTEMA DE INVENTÁRIO (Tales of Home style) ===

init python:
    class Item:
        def __init__(self, id, name, desc, icon, cost=0, effect_stat=None, effect_amount=0):
            self.id = id
            self.name = name
            self.desc = desc
            self.icon = icon
            self.cost = cost
            self.effect_stat = effect_stat
            self.effect_amount = effect_amount
            
    # Registro de todos os itens do jogo
    game_items = {
        "energy_drink": Item("energy_drink", _("Bebida Energética"), _("Restaura 30 de energia."), "🥤", 15, "energy", 30),
        "snack": Item("snack", _("Salgadinho"), _("Restaura 10 de energia."), "🍪", 5, "energy", 10),
        "book": Item("book", _("Livro de Estudos"), _("Aumenta inteligência em 5."), "📚", 30, "intelligence", 5),
        "gift_flowers": Item("gift_flowers", _("Buquê de Flores"), _("Um ótimo presente para alguém especial."), "💐", 20, None, 0),
    }

    def give_item(item_id, amount=1):
        """Dá um item ao jogador."""
        if item_id not in store.player_inventory:
            store.player_inventory[item_id] = 0
        store.player_inventory[item_id] += amount
        item_name = game_items[item_id].name if item_id in game_items else item_id
        renpy.notify(_(f"Recebeu {amount}x {item_name}"))

    def remove_item(item_id, amount=1):
        """Remove um item do inventário do jogador."""
        if item_id in store.player_inventory and store.player_inventory[item_id] >= amount:
            store.player_inventory[item_id] -= amount
            if store.player_inventory[item_id] <= 0:
                del store.player_inventory[item_id]
            return True
        return False

    def use_item(item_id):
        """Usa um item do inventário."""
        if item_id in store.player_inventory and store.player_inventory[item_id] > 0:
            item = game_items.get(item_id)
            if item and item.effect_stat:
                success = update_player_stat(item.effect_stat, item.effect_amount)
                if success:
                    remove_item(item_id, 1)
                    renpy.notify(_(f"Usou {item.name}."))
                else:
                    renpy.notify(_("Status já está no máximo!"))
            elif item:
                # Pode ser um presente, não consumível de stats
                renpy.notify(_(f"{item.name} não pode ser usado assim."))
            return True
        return False

# O dicionário do inventário (id do item -> quantidade)
default player_inventory = {}

# Screen do Inventário
screen inventory_ui():
    modal True
    zorder 200

    add Solid("#000000cc")

    frame:
        xalign 0.5 yalign 0.5
        xsize 800 ysize 600
        padding (20, 20, 20, 20)
        background Solid("#222233")

        # Header
        frame:
            xalign 0.0 yalign 0.0
            xfill True ysize 60
            background Solid("#111122")
            text _("INVENTÁRIO"):
                size 24 color "#ffffff" bold True yalign 0.5 xpos 10
                
            textbutton "✕":
                xalign 1.0 yalign 0.5 xoffset -10
                text_color "#aaaaaa" text_hover_color "#ff4444" text_size 24
                action Hide("inventory_ui")

        # Grid de Itens
        if not store.player_inventory:
            text _("Seu inventário está vazio.") size 20 color "#888888" xalign 0.5 yalign 0.5
        else:
            vpgrid:
                cols 4
                spacing 15
                xalign 0.5 ypos 80
                xsize 760 ysize 500
                scrollbars "vertical"
                mousewheel True
                
                for item_id, amount in store.player_inventory.items():
                    if amount > 0 and item_id in game_items:
                        $ item = game_items[item_id]
                        frame:
                            xsize 175 ysize 150
                            background Solid("#333344")
                            padding (10, 10, 10, 10)
                            
                            vbox:
                                xalign 0.5 yalign 0.5 spacing 5
                                text item.icon size 40 xalign 0.5
                                text item.name size 16 bold True xalign 0.5 text_align 0.5
                                text f"Qtd: {amount}" size 14 color "#aaaaaa" xalign 0.5
                                
                                textbutton _("Usar"):
                                    xalign 0.5
                                    text_size 14
                                    action Function(use_item, item_id)
                    elif amount > 0:
                        # Item fallback
                        frame:
                            xsize 175 ysize 150
                            background Solid("#333344")
                            text item_id size 14 xalign 0.5 yalign 0.5
