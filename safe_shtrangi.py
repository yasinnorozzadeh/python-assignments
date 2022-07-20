import arcade
COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 65
BOTTOM_MARGIN = 65
arcade.open_window(300,300, "Checkered page")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for row in range(10):
    for column in range(10):
        adad_1_dimond = column * COLUMN_SPACING + LEFT_MARGIN
        adad_2_dimond = row * ROW_SPACING + BOTTOM_MARGIN
        if (row+1) % 2 == 0:
            if (column+1) % 2 != 0:
                arcade.draw_circle_filled(adad_1_dimond, adad_2_dimond, 7, arcade.color.BABY_BLUE)
            else:
                arcade.draw_circle_filled(adad_1_dimond, adad_2_dimond, 7, arcade.color.RED_PURPLE)
        else:
            if (column + 1) % 2 != 0:
                arcade.draw_circle_filled(adad_1_dimond, adad_2_dimond, 7, arcade.color.RED_PURPLE)
            else:
                arcade.draw_circle_filled(adad_1_dimond, adad_2_dimond, 7, arcade.color.BABY_BLUE)
arcade.finish_render()
arcade.run()