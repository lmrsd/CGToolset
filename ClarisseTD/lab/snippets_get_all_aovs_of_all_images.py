import ix
import pprint
import json


def attr_reader(object):
    for i in range(0, object.get_attribute_count()):
        print(object.get_attribute(i))


def get_imge_aovs_dict():
    objects = ix.api.OfObjectArray()
    ix.application.get_factory().get_all_objects("Image", objects)

    renderableImages = dict()

    for image in objects:
        image_name = image.get_name()
        renderableImages[image_name] = dict()

        for layer in image.get_module().get_all_layers():
            layer_name = layer.get_object().get_name()

            lay_obj = layer.get_object()
            aov_list = lay_obj.get_attribute("selected_aov_list")

            aov_list_named = [aov_list[i] for i in range(aov_list.get_value_count())]

            renderableImages[image_name][layer_name] = [aov_list_named]

    return renderableImages


json_object = json.dumps(get_imge_aovs_dict(), indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

''' DEBUG PROCESS
import ix
import pprint


def attr_reader(object):
    for i in range (0,object.get_attribute_count()):
        print(object.get_attribute(i))

objects = ix.api.OfObjectArray()
ix.application.get_factory().get_all_objects( "Image", objects )
renderableImages = []
for image in objects:
    print('#####')
    print(image)
    print(image.get_attribute( "save_as" )[0])


    aov_list = image.get_attribute("selected_aov_list")


    for layer in image.get_module().get_all_layers():
        print(layer.__class__.__name__)
        print(layer.get_object().get_name())
        print(layer.get_object().get_attribute_count())

        lay_obj = layer.get_object()
        aov_list = lay_obj.get_attribute("selected_aov_list")
        
        for index in range(aov_list.get_value_count()):
            print(aov_list[index])
      
        
        enabled_aov_list = lay_obj.get_attribute("enabled_aov_list")
        aov_blend_override_list = lay_obj.get_attribute("aov_blend_override_list")

        print(aov_list.__class__.__name__)
        print(aov_list.get_enum())
        print(str(enabled_aov_list))
        print(str(aov_blend_override_list))

        print('')


'''