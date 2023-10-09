# SIRIUS Data Model

## Description
SIRIUS Data Model is an ontological model that is used to structure the knowledge graph storing the data used in the SIRIUS web platform. It has been developed by using the Simplified Agile Methodology for Ontology Development (Peroni, S. (2016). SAMOD: an agile methodology for the development of ontologies. figshare. http://dx.doi.org/10.6084/m9.figshare.3189769).

This repository contains the full documentation produced during the development of the data model. In particular:
* the `data` directory contains the full set of refactored *ABoxes*, one for each iteration, written in the Turtle RDF serialization;
* the `development` directory contains a folder per development iteration, each containing a full test case with:
    - a **motivating scenario**, which defines the scope of the single iteration, along with some examples;
    - a list of **informal Competency Questions**, written in natural language;
    - a **glossary of terms**, which defines a set of meaningful words and expressions collected from the scenario and the competency questions;
    - a Graffoo **visual diagram** of the model in .png format, along with its .graphml file;
    - a **terminology component** (*TBox*), which defines a formal schema based on the diagram;
    - an **assertion component** (*ABox*), which organizes the examples data according to the schema;
    - a list of **formal Competency Questions**, which reformulate the informal competency questions into proper SPARQL queries;
    - a **testing notebook**, which is used to text the SPARQL queries against the TBox and ABox;
    - a **crosswalk table**, which bridges the development step with the refactoring step by documenting the alignment between the glossary terms and the refactored terms.
* the `diagrams` directory contains the full set of Graffoo diagrams representing the refactored model of each iteration;
* the `docs` directory contains the full set of files related to the final model and its versions in time;
* the `sparql` directory contains the full set of refactored Formal Competency Questions.