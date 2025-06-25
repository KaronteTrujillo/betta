import bpy
import os
import random

def load_betta_model(obj_path):
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Importar modelo OBJ
    bpy.ops.import_scene.obj(filepath=obj_path)
    return bpy.context.selected_objects[0]  # Retorna el objeto importado

def apply_color_to_betta(obj):
    # Crear un material nuevo
    mat = bpy.data.materials.new(name="BettaMaterial")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    
    # Asignar un color aleatorio (tonos inspirados en peces betta: azules, rojos, etc.)
    base_color = (random.uniform(0, 0.3), random.uniform(0, 0.3), random.uniform(0.5, 1.0), 1.0)  # Azul con variación
    bsdf.inputs["Base Color"].default_value = base_color
    
    # Asignar material al objeto
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

def render_to_png(output_path):
    # Configurar renderizado
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = output_path
    bpy.ops.render.render(write_still=True)

def generate_betta_image(obj_path, output_path):
    # Cargar modelo
    betta = load_betta_model(obj_path)
    
    # Aplicar color
    apply_color_to_betta(betta)
    
    # Configurar cámara y luz (básico)
    bpy.ops.object.camera_add(location=(0, -5, 2))
    bpy.context.scene.camera = bpy.context.object  # Establecer la cámara activa
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 5))
    
    # Renderizar
    render_to_png(output_path)
    
    return output_path

if __name__ == "__main__":
    obj_path = os.path.abspath("assets/betta.obj")
    output_path = os.path.abspath("outputs/betta_output.png")
    os.makedirs("outputs", exist_ok=True)
    generate_betta_image(obj_path, output_path)
