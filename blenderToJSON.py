import bpy

obj = bpy.context.object

mesh = obj.data

vertices = mesh.vertices
edges = mesh.edges

verts_out = []

# [
#   [posX, Y, Z],
#   [orgX, Y, Z],
#   [norX, Y, Y],
#   bevWt,
#   [vtxGroup1, ...],
#   hidden
# ], ...

# Put the *ABSOLUTE* path to the output file here.
# Make sure it ends with `.json`
path = ""

iofile = open(path, 'a')

iofile.write('{"vertices":[')
counter1 = 0
for vertex in vertices:
    vertex_out = []
    vertex_out.append([vertex.co.x, vertex.co.y, vertex.co.z])
    vertex_out.append([vertex.undeformed_co.x, vertex.undeformed_co.y, vertex.undeformed_co.z])
    vertex_out.append([vertex.normal.x, vertex.normal.y, vertex.normal.z])
    vertex_out.append(vertex.bevel_weight)
    vertex_out.append([])
    vertex_out.append(vertex.hide)
    counter1 += 1
    iofile.write(str(vertex_out).replace("False", "false") + ('' if counter1 == len(vertices) else ",") + "\n")
    
iofile.write("]," + "\n"*3)
iofile.write('"edges":[')
edges_out = []

# [
#   bevWt,
#   crease,
#   hidden,
#   loose,
#   sharp,
#   seam,
#   [vert1, 2]
# ], ...
counter2 = 0
for edge in edges:
    edge_out = []
    edge_out.append(edge.bevel_weight)
    edge_out.append(edge.crease)
    edge_out.append(edge.hide)
    edge_out.append(edge.is_loose)
    edge_out.append(edge.use_edge_sharp)
    edge_out.append(edge.use_seam)
    edge_out.append([v for v in edge.vertices])
    counter2 += 1
    iofile.write(str(edge_out).replace("False","false")+('' if counter2 == len(edges) else ",") + "\n")
    
iofile.write(']}')
    
iofile.close()

      
    