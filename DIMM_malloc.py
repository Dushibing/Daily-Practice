#python2
import gc
import waste_memory 
foud_object = gc.get_objects()
print('%d object before'%len(found_objects))

x = waste_memory.run()
foud_object = gc.get_objects()
print('%d object after'%len(foud_object))
for obj in foud_object[:3]:
	print(repr(obj)[:100])

