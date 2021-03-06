import bpy

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if "frame" not in obj.keys():
            return False
        if not hasattr(obj, "animation_data"):
            return False
        if not obj.animation_data.action:
            return False
        return True

    def draw(self, context):
        obj = context.object
        scene = context.scene
        layout = self.layout
        # get current frame location
        loc_current = obj.location.copy()
        row = layout.row()
        col = row.column()
        col.prop(scene, "frame_current")
        col.prop(obj, "location")
        loc = loc_current.copy()

        # using fcurves
        frame = obj["frame"]
        action = obj.animation_data.action
        col = layout.column()

        col.label("Moved")
        col.prop(obj, '["frame"]', text="From Frame")
        row = layout.row()
        for index in [0, 1, 2]:
            fcurve = action.fcurves.find('location', index)
            if fcurve:
                loc[index] = fcurve.evaluate(frame)
            row.label("%7.4f" % (loc - loc_current)[index])

def register():
    bpy.utils.register_class(HelloWorldPanel)

def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)

if __name__ == "__main__":
    bpy.context.object["frame"] = 33 # set another frame in custom prop
    register()