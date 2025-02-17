github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"
from rdflib import Graph, Namespace, Literal, FOAF
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

#Create a new class named Researcher
ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)
#TASK 6.1: Create a new class named "University"
ns = Namespace("http://somewhere#")
g.add((ns.Universidad, RDF.type, RDFS.Class))
for s, p, o in g:
    print(s, p, o)
#TASK 6.2: Add "Researcher" as a subclass of "Person"
ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for s, p, o in g:
    print(s, p, o)
#TASK 6.3: Create a new individual of Researcher named "Jane Smith"
ns = Namespace("http://somewhere#")
g.add((ns.JaneSmith, RDF.type, ns.Researcher))
g.add((ns.JaneSmith, ns.hasName, Literal("Jane Smith")))
for s, p, o in g:
    print(s, p, o)
#TASK 6.4: Add to the individual JaneSmith the email address, fullName, given and family names
ns = Namespace("http://somewhere#")
g.add((ns.JaneSmith, RDF.type, ns.Researcher))
g.add((ns.JaneSmith, ns.hasName, Literal("Jane Smith")))
g.add((ns.JaneSmith, ns.hasEmail, Literal("jane.smith@example.com")))
g.add((ns.JaneSmith, ns.hasFullName, Literal("Jane Smith")))
g.add((ns.JaneSmith, ns.hasGivenName, Literal("Jane")))
g.add((ns.JaneSmith, ns.hasFamilyName, Literal("Smith")))
for s, p, o in g:
    print(s, p, o)
#TASK 6.5: Add UPM as the university where John Smith works
g.add((ns.JohnSmith, ns.worksFor, Literal("UPM")))
for s, p, o in g:
    print(s, p, o)
#Task 6.6: Add that Jown knows Jane using the FOAF vocabulary
g.add((ns.JohnSmith, ns.knows, ns.JaneSmith))
for s, p, o in g:
    print(s, p, o)