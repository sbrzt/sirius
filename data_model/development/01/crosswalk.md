|                       | **TBox term**            | **Model** | **Refactored term**           | **Full URI**                                                     |
|-----------------------|--------------------------|-----------|-------------------------------|------------------------------------------------------------------|
| **Classes**           |                          |           |                               |                                                                  |
|                       | `HeritageAsset`          | CIDOC-CRM | E24_Physical_Human-Made_Thing | http://www.cidoc-crm.org/cidoc-crm/E24_Physical_Human-Made_Thing |
|                       | `Context`                | HeRO      | Observation                   | http://purl.org/sirius/ontology/hero/Observation                 |
|                       | `ContextType`            | HeRO      | Dimension                     | http://purl.org/sirius/ontology/hero/Dimension                   |
|                       | `Place`                  | CIDOC-CRM | E53_Place                     | http://www.cidoc-crm.org/cidoc-crm/E53_Place                     |
|                       | `Stakeholder`            | CIDOC-CRM | E39_Actor                     | http://www.cidoc-crm.org/cidoc-crm/E39_Actor                     |
|                       | `RiskAssessmentActivity` | HeRO      | RiskAssessment                | http://purl.org/sirius/ontology/hero/RiskAssessment              |
|                       | `TimeSpan`               | CIDOC-CRM | E52_Time-Span                 | http://www.cidoc-crm.org/cidoc-crm/E52_Time-Span                 |
|                       | `Document`               | CIDOC-CRM | E31_Document                  | http://www.cidoc-crm.org/cidoc-crm/E31_Document                  |
|                       | `CreationEvent`          | CIDOC-CRM | E12_Production                | http://www.cidoc-crm.org/cidoc-crm/E12_Production                |
| **Object properties** |                          |           |                               |                                                                  |
|                       | `hasContext`             | HeRO      | isInfluencedBy                | http://purl.org/sirius/ontology/hero/isInfluencedBy              |
|                       | `documents`              | CIDOC-CRM | P70_documents                 | http://www.cidoc-crm.org/cidoc-crm/P70_documents                 |
|                       | `hasType`                | HeRO      | observes                      | http://purl.org/sirius/ontology/hero/observes                    |
|                       | `assignsRiskTo`          | HeRO      | assignsRiskTo                 | http://purl.org/sirius/ontology/hero/assignsRiskTo               |
|                       | `involves`               | CIDOC-CRM | P11_had_participant           | http://www.cidoc-crm.org/cidoc-crm/P11_had_participant           |
|                       | `isLocatedIn`            | CIDOC-CRM | P55_has_current_location      | http://www.cidoc-crm.org/cidoc-crm/P55_has_current_location      |
|                       | `creates`                | CIDOC-CRM | P108_has_produced             | http://www.cidoc-crm.org/cidoc-crm/P108_has_produced             |
|                       | `hasTimeStamp`           | CIDOC-CRM | P4_has_time-span              | http://www.cidoc-crm.org/cidoc-crm/P4_has_time-span              |
| **Data properties**   |                          |           |                               |                                                                  |
|                       | `hasAssetName`           | DCTerms   | title                         | http://purl.org/dc/terms/title                                   |
|                       | `hasAlternativeName`     | DCTerms   | alternative                   | http://purl.org/dc/terms/alternative                             |
|                       | `hasAssetDescription`    | DCTerms   | description                   | http://purl.org/dc/terms/description                             |
|                       | `hasCoordinates`         | CIDOC-CRM | P168_place_is_defined_by      | http://www.cidoc-crm.org/cidoc-crm/P168_place_is_defined_by      |
|                       | `fallsWithin`            | CIDOC-CRM | P82_at_some_time_within       | http://www.cidoc-crm.org/cidoc-crm/P82_at_some_time_within       |
|                       | `hasTitle`               | DCTerms   | title                         | http://purl.org/dc/terms/title                                   |
|                       | `hasDocumentDescription` | DCTerms   | description                   | http://purl.org/dc/terms/description                             |
|                       | `hasPlaceName`           | RDFS      | label                         | http://www.w3.org/2000/01/rdf-schema#label                       |
|                       | `hasStakehoderName`      | FOAF      | name                          | http://xmlns.com/foaf/0.1/name                                   |
|                       | `hasLink`                | RDFS      | seeAlso                       | http://www.w3.org/2000/01/rdf-schema#seeAlso                     |
|                       | `hasContextDescription`  | DCTerms   | description                   | http://purl.org/dc/terms/description                             |
| **Individuals**       |                          |           |                               |                                                                  |
|                       | `physical`               | HeRO      | physical-environment          | http://purl.org/sirius/ontology/hero/physical-environment        |
|                       | `socio-cultural`         | HeRO      | socio-cultural-environment    | http://purl.org/sirius/ontology/hero/socio-cultural-environment  |
|                       | `political`              | HeRO      | political-environment         | http://purl.org/sirius/ontology/hero/political-environment       |
|                       | `legal`                  | HeRO      | legal-environment             | http://purl.org/sirius/ontology/hero/legal-environment           |
|                       | `administrative`         | HeRO      | administrative-environment    | http://purl.org/sirius/ontology/hero/administrative-environment  |
|                       | `economic`               | HeRO      | economic-environment          | http://purl.org/sirius/ontology/hero/economic-environment        |