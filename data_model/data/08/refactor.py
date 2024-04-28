import yaml
from rdflib import Graph, Namespace, URIRef, Literal, BNode

# Load configuration from YAML file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Extract namespace declarations and mapping rules from the configuration
namespaces = config["namespaces"]
mapping_rules = config["mapping_rules"]

# Define namespaces
old_abox = Namespace(namespaces["old_ns"]["abox"])
new_abox = Namespace(namespaces["new_ns"]["abox"])
hero = Namespace(namespaces["new_ns"]["hero"])
aat = Namespace(namespaces["new_ns"]["aat"])
comp = Namespace(namespaces["new_ns"]["comp"])
dcterms = Namespace(namespaces["new_ns"]["dcterms"])
dul = Namespace(namespaces["new_ns"]["dul"])
foaf = Namespace(namespaces["new_ns"]["foaf"])
freq = Namespace(namespaces["new_ns"]["freq"])
part = Namespace(namespaces["new_ns"]["part"])
place = Namespace(namespaces["new_ns"]["place"])
planex = Namespace(namespaces["new_ns"]["planex"])
provo = Namespace(namespaces["new_ns"]["provo"])
seq = Namespace(namespaces["new_ns"]["seq"])
ti = Namespace(namespaces["new_ns"]["ti"])
tisit = Namespace(namespaces["new_ns"]["tisit"])
wd = Namespace(namespaces["new_ns"]["wd"])

# Load the original .ttl file
original_graph = Graph()
original_graph.parse("../development/08/ABox.ttl", format="turtle")

# Create a new RDF graph for the transformed data
transformed_graph = Graph()

# Bind namespaces to prefixes
transformed_graph.bind("hero", hero)
transformed_graph.bind("aat", aat)
transformed_graph.bind("comp", comp)
transformed_graph.bind("dcterms", dcterms)
transformed_graph.bind("dul", dul)
transformed_graph.bind("foaf", foaf)
transformed_graph.bind("freq", freq)
transformed_graph.bind("part", part)
transformed_graph.bind("place", place)
transformed_graph.bind("planex", planex)
transformed_graph.bind("provo", provo)
transformed_graph.bind("seq", seq)
transformed_graph.bind("ti", ti)
transformed_graph.bind("tisit", tisit)
transformed_graph.bind("wd", wd)

# Apply mapping rules to transform the RDF graph
for s, p, o in original_graph:
    # Map subject, predicate, and object if applicable
    new_s_uri = mapping_rules.get(str(s), str(s)).replace(old_abox, new_abox)
    new_p_uri = mapping_rules.get(str(p), str(p)).replace(old_abox, new_abox)
    new_o_uri = mapping_rules.get(str(o), str(o)).replace(old_abox, new_abox)
    
    # Create RDFLib terms for subject, predicate, and object
    new_s = URIRef(new_s_uri)
    new_p = URIRef(new_p_uri)
    if isinstance(o, Literal):
        new_o = Literal(o)
    elif isinstance(o, BNode):
        new_o = BNode(o)
    else:
        new_o = URIRef(new_o_uri)

    # Add transformed triple to the new graph
    transformed_graph.add((new_s, new_p, new_o))

# Serialize the transformed graph to a new .ttl file
transformed_graph.serialize(destination="ABox.ttl", format="turtle")
