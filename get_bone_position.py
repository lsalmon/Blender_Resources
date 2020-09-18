import bpy
from bpy import context

'''
armature = "rig" 

tail = bpy.data.objects[armature].location + context.active_pose_bone.tail
head = bpy.data.objects[armature].location + context.active_pose_bone.head

print("tail: ")
print(tail)
print(" head: ")
print(head)

# Active object
ob = bpy.context.object

if ob.type == 'ARMATURE':
	armature = ob.data

	for bone in armature.bones:
		print(bone.name)		
'''

target_bone = 'Bip008 L Thigh'
move = (10, 10, 10)

scene = bpy.context.scene

for obj in scene.objects:
	print("Object name : ", obj.name, " , location : ", obj.location);
	if obj.name == 'Armature' and obj.type == 'ARMATURE': 
		armature = obj.data

        # bones / edit_bones info (not used for poses)
		for bone in armature.bones:
			print(bone.name)

# pose_bones (used for movement)
for bone in bpy.data.objects["Armature"].pose.bones:
    print(bone.name)

target_bone = "mixamorig:RightForeArm"


for act in bpy.data.actions:
	for fc in act.fcurves:
		if target_bone not in fc.data_path or 'location' not in fc.data_path:
			continue
			
		print("fc[", fc.array_index, "].data_path : ", fc.data_path);

		assert 0 <= fc.array_index < 3
		for p in fc.keyframe_points:
			# here we get values of a dimension for all frames for a given bone
			# ex: leg bone dimension_a[0..35] 
			# first 35 animation frames
			if p.co[0] <= 35:
				p.co[1] += move[fc.array_index]
				print("         keyframe[", p.co[0], "] : ", p.co[1]);

