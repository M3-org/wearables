import bpy
import os

# Set the output path for the glb files
output_path = "/mnt/c/Users/gamer/Documents/GitHub/wearables/"

# Open the blend file
bpy.ops.wm.open_mainfile(filepath="babby_wearables.blend")

# Iterate through each object in the scene
for obj in bpy.context.scene.objects:
    # Select the object
    obj.select_set(True)
    # Export the object as a glb file
    bpy.ops.export_scene.gltf(use_selection=True, filepath=output_path + obj.name + ".glb")
    # Deselect the object
    obj.select_set(False)

# Print a success message
print("Successfully exported all objects from babby_wearables.blend as glb files!")
