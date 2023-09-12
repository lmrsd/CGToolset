import ix



prj = ix.get_item('project:/')

# get all contexts
all_contexts = ix.api.OfContextSet()
ignore_disabled_ctx = False
if ignore_disabled_ctx:
    mask = ix.api.CoreBitFieldHelper(ix.api.OfIten.FLAG_NONE, ix.api.OfIten.FLAG_NONE, ix.api.CoreBitFieldHelper.MODE_DISABLE, ix.api.CoreBitFieldHelper.MODE_DISABLE)
    prj.resolve_all_contexts(all_contexts, mask)
else:
    prj.resolve_all_contexts(all_contexts)

# filter contexts with overrides
override_contexts = ix.api.OfContextSet()
for i in range(all_contexts.get_count()):
    if all_contexts[i].is_override():
        override_contexts.add(all_contexts[i])


def attr_reader(object):
    for i in range (0,object.get_attribute_count()):
        print(object.get_attribute(i))

# do something with the override contexts:
for i in range(override_contexts.get_count()):
    print(override_contexts[i])
    ref = override_contexts[i]
    print(dir(ref))
    print(ref.get_name())
    attr_reader(ref)
    filename = ref.get_attribute('filename')
    print(filename)
    print(ref.is_reference())
    print(filename.get_value_count())
    print(filename.is_array())
    print(filename.get_string())
    print(dir(filename))
    print(filename.get_type_name(filename.get_type()))


"""

geo_item.get_attribute("filename").set_string(file_path+file_name+".abc")


# Get all 3D Views widgets
widgets = ix.api.OfObjectArray()
tt = ix.application.get_factory().get_all_objects('Context', widgets)
print(tt)


# Get the context
ctx = ix.get_item("project://scene")

print(dir(ctx))


print(dir(ix.api.AbcScene))

# We have to create some arrays that will content the objects in the context
objects_array = ix.api.OfObjectArray(ctx.get_object_count()) # ctx.get_object_count() correspond to the number of items in the context

ctx.get_objects(objects_array) # this function get all the items in the context and fill the array `objects_array` of them

for i in range(ctx.get_object_count()):
    o = objects_array[i]
    #print (objects_array[i])
    print(o,o.get_module().get_class_info_name())


#ctx_array = ix.api.OfContext(ctx.get_all_contexts_count())
print(ctx.get_all_contexts_count()) # here it is recursive
print(ctx.get_context_count()) # notrecursive
print(ctx.get_contexts)

for i in range(ctx.get_all_contexts_count()):
    print(i)
"""