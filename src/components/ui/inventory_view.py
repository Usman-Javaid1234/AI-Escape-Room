from components.ui.window import create_window
from math import ceil
from components.Entity import Entity
from components.sprite import Sprite
from components.button import Button
from components.ui.window import Window
from components.label import Label

items_per_row = 5
padding_size = 5
gap_size = 5
item_size = 32

class InventoryView:
    def __init__(self, inventory,slot_image="inventory_slot.png"):
        
        self.inventory = inventory

        self.slot_image = slot_image

        width = padding_size + (items_per_row * item_size) + ((items_per_row-1 ) * gap_size) + padding_size
        rows = ceil(inventory.capacity / items_per_row)
        height = padding_size + (rows * item_size) + ((rows-1) * gap_size) + padding_size

        from core.camera import camera
        x = camera.width - width
        y = 0

        self.window = create_window(x, y, width, height)
        self.slot_container_sprites = []
        self.slot_sprites = []

        inventory.listener = self

        self.render()

        

    def breakdown(self):
        from core.engine import engine
        engine.active_objs.remove(self)
        self.clear()

    



    def render(self):
        print("Called render")
        row = 0
        column = 0
        for index, slot in enumerate(self.inventory.slots):
            x = column * (item_size + gap_size) + self.window.x + padding_size
            y = row * (item_size + gap_size) + self.window.y + padding_size

            slot_image = self.selected_slot_image if index==self.inventory.equipped_slot else self.slot_image
            container_sprite = Entity(Sprite(slot_image, True), x=x, y=y)
            self.window.get(Window).items.append(container_sprite)
            if slot.type is not None:
                print(slot.type.name)
                item_sprite = Entity(Sprite(slot.type.icon_name, True), x=x, y=y)
                if slot.type.stack_size > 1:
                    label = Entity(Label("EBGaramond-ExtraBold.ttf", str(slot.amount), color=(255, 255, 0), size=30), x=x, y=y)
                    self.window.get(Window).items.append(label)
                self.window.get(Window).items.append(item_sprite)
            column += 1
            if column >= items_per_row:
                column = 0
                row += 1


    def clear(self):
        for i in self.window.get(Window).items:
            if i.has(Sprite):
                i.get(Sprite).breakdown()
            elif i.has(Label):
                i.get(Label).breakdown()
        self.window.get(Window).items.clear()


    def refresh(self):
        self.clear()
        self.render()

