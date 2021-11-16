from PhotoProject import PhotoProject
import resizegui

classobject = PhotoProject()

# Available Modulestest.jpg'
mydict = classobject.sorty()

#for keys, values in mydict.items():
#    print(keys)
#    print(values)
#filename = 'test.jpg'
#classobject.save_find_faces(filename)
#classobject.save_find_faces_all()
#classobject.compare_faces(face1,face2)
#classobject.compare_all_faces()
#classobject.cluster_faces()


root = Imagewindow(mydict)
width = 400
height = 400
root.overrideredirect(True)
root.geometry('%dx%d' % (width*1, height*1))
root.slideShow()
root.run()
