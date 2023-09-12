import ix

"""
sl = ix.selection

for i in sl:
    print(i)
    print(dir(i))
    #print(i.get_items())
    print(i.get_all_objects_count())

    obj_count = i.get_all_objects_count()

    print('context',i.get_context_count())


    # We have to create some arrays that will content the objects in the context
    objects_array = ix.api.OfObjectArray(i.get_object_count()) # ctx.get_object_count() correspond to the number of items in the context

    print(objects_array)

    i.get_objects(obj_count) # this function get all the items in the context and fill the array `objects_array` of them

    for i in range(obj_count):
        print (objects_array[i])






        def get_transformed_bbox(geom):
    if not geom or not (geom.is_kindof("Geometry") or geom.is_kindof("GeometryBundle")):
        ix.log_warning("Please select a Geometry or GeometryBundle.")
        return None

    bbox = geom.get_module().get_bbox()
    global_matrix = geom.get_module().get_global_matrix()
    transformed_bbox = ix.api.GMathBbox3d()
    bbox.transform_bbox_and_get_bbox(global_matrix, transformed_bbox)
    return transformed_bbox

# Example:
geom = ix.selection[0]
geom_bbox = get_transformed_bbox(geom)

# Apply the geom bbox to a GeometryBox
if geom_bbox:
    box = ix.get_item('build://project/box')
    box.get_attribute('translate').set_vec3d(geom_bbox.get_center())
    box.get_attribute('scale').set_vec3d(geom_bbox.get_sizes())
"""
globalSpace = ix.api.ModuleSceneItem.SPACE_GLOBAL

print(dir(ix.selection[0]))

sl = ix.selection[0]
print(sl.get_context())
print('whattt ?', ix.selection[0].get_item_path(sl))

print(type(sl))

# Get the context
ctx = ix.get_item("build://project/scene/light_scatter_v001")

# We have to create some arrays that will content te objects in the context
objects_array = ix.api.OfObjectArray(ctx.get_object_count()) # ctx.get_object_count() correspond to the number of items in the context

ctx.get_objects(objects_array) # this function get all the items in the context and fill the array `objects_array` of them

for i in range(ctx.get_object_count()):
    o =  (objects_array[i])
    print(type(o))
    print(o.get_type())


    name = o.get_name()
    print(name)
    """
    context easier
    objects = ix.api.OfObjectArray()
    ctx.get_objects(objects)
    """


    if o.is_kindof('AbcXform') and 'lightShape' in name :
        print('FOUNNNNNNNNNNNNNND',name,o)
        print(dir(o.get_module()))
        print( o.get_module().get_global_matrix() )
        mm =  o.get_module().get_global_matrix()

        # CREATE LIGHTS
        lgt = ix.cmds.CreateObject("sphere", "LightPhysicalSphere", "Global", "build://project/scene")
        lgt.get_module().set_matrix(mm,globalSpace)
        print(dir(lgt))
        #set_matrix

        mm = o.get_module().get_global_matrix()
        mo = o.get_module().get_object_matrix()
        rot = o;
        get_module();
        get_rotation_pivot_matrix()
        print(rot, mo)

        # CREATE LIGHTS
        lgt = ix.cmds.CreateObject("sphere", "LightPhysicalSphere", "Global", "build://project/scene")
        lgt.get_module().set_matrix(mm, globalSpace)


