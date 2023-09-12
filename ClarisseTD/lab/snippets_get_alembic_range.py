#
# Get the animation (kinematic + deformation) range of an Alembic object.
#
def get_abc_anim_range(object, as_frames=True):

    if object.get_class_name() not in ['CameraAlembic', 'AbcXform', 'GeometryAbcMesh', 'GeometryAbcFur', 'GeometryAbcPointCloud', 'GeometryBundleAlembic']:
        ix.log_warning('Not an Alembic object.')
        return 0, 0

    # all abc objects have the attribute anim_range
    anim_attr = object.attribute_exists('anim_range')
    if not anim_attr:
        ix.log_warning('No animation')
        return 0, 0

    start = 0
    end = 0
    anim_range = anim_attr.get_vec2d()

    # xforms and cameras don't have the deform_range
    deform_attr = object.attribute_exists('deform_range')
    if deform_attr:
        deform_range = deform_attr.get_vec2d()
        start = min(anim_range[0], deform_range[0])
        end = max(anim_range[1], deform_range[1])
    else:
        start = anim_range[0]
        end = anim_range[1]

    if as_frames:
        # return as frame numbers
        fps = ix.application.get_factory().get_time().get_fps()
        return int(start * fps), int(end * fps)
    else:
        # return as time values
        return start, end

print(get_abc_anim_range(ix.selection[0]))