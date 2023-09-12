
objects = ix.api.OfObjectArray()
ix.application.get_factory().get_all_objects( "Image", objects )
renderableImages = []
for image in objects:
    print(image)


# Grab Images and their layers that have enabled 'render_to_disk'
objects = ix.api.OfObjectArray()
ix.application.get_factory().get_all_objects( "Image", objects )
renderableImages = []
for image in objects:
    if image.get_attribute( "render_to_disk" )[0]:
        renderableImages.append(image.get_full_name())
    for layer in image.get_module().get_all_layers():
        if layer.get_object().get_attribute( "render_to_disk" )[0]:
            renderableImages.append( layer.get_object().get_full_name() )

# Grab Images and their layers that have enabled 'render_to_disk' and map those to their output paths
objects = ix.api.OfObjectArray()
ix.application.get_factory().get_all_objects( "Image", objects )
renderableImages = {}
for image in objects:
    if image.get_attribute( "render_to_disk" )[0]:
        renderableImages[ image.get_full_name() ] = image.get_attribute( "save_as" )[0]
    for layer in image.get_module().get_all_layers():
        if layer.get_object().get_attribute( "render_to_disk" )[0]:
            renderableImages[ layer.get_object().get_full_name() ] = layer.get_object().get_attribute( "save_as" )[0]


# need to select the image
if ix.selection.get_count()>0:
    for i in range(ix.selection.get_count()):
        selection = ix.selection[i]

        if selection.get_class_name() == "Image":
            layers = selection.get_module().get_layers()
            for j in range(layers.get_count()):
                layer_3d = layers[j].get_object()
                aov_list = layer_3d.get_attribute("selected_aov_list")
                enabled_aov_list = layer_3d.get_attribute("enabled_aov_list")
                aov_blend_override_list = layer_3d.get_attribute("aov_blend_override_list")

                ix.cmds.SetValueCount([
                    str(aov_list),
                    str(enabled_aov_list),
                    str(aov_blend_override_list)
                    ], [0, 0, 0])

aov_list = image.get_attribute("selected_aov_list")

for index in range(aov_list.get_value_count()):
  print(aov_list[index])


import os

## Select all in current project
#textures = ix.api.OfObjectVector()
#filter = "*"
#types = ix.api.CoreStringVector()
#types.add('TextureStreamedMapFile')
#ix.application.get_matching_objects(textures, filter, ix.application.get_factory().get_project(), types)

## Use manual selection
textures = []
for sel in ix.selection:
    if sel.is_kindof("TextureStreamedMapFile"):
        textures.append(sel)

ix.begin_command_batch("Replace ext to TX")
for tx in textures:
    ix.cmds.SetValue(str(tx) + ".filename", [os.path.splitext(tx.attrs.filename.attr.get_string())[0] + ".tx"])
ix.application.check_for_events()
ix.end_command_batch()


def get_all_objects(class_name):
    if ix.application.get_version().startswith("4.0"):
        objects = ix.api.OfObjectArray()
    else:
        objects = ix.api.OfObjectHandleArray()
    ix.application.get_factory().get_all_objects(class_name, objects)
    return objects


for obj in get_all_objects("TextureStreamedMapFile"):
    print(obj.get_full_name())

# Get the context
ctx = ix.get_item("project://scene")

# We have to create some arrays that will content the objects in the context
objects_array = ix.api.OfObjectArray(
    ctx.get_object_count())  # ctx.get_object_count() correspond to the number of items in the context

ctx.get_objects(
    objects_array)  # this function get all the items in the context and fill the array `objects_array` of them

for i in range(ctx.get_object_count()):
    print
    objects_array[i]


