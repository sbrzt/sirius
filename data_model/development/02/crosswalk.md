|                       | **TBox term**               | **Model** | **Refactored term**             | **Full URI**                                                     | **Note** |
|-----------------------|-----------------------------|-----------|---------------------------------|------------------------------------------------------------------|----------|
| **Classes**           |                             |           |                                 |                                                                  |          |
|                       | `HeritageAsset`             | CIDOC-CRM | `E24_Physical_Human-Made_Thing` | http://www.cidoc-crm.org/cidoc-crm/E24_Physical_Human-Made_Thing |          |
|                       | `RiskAssessment`            | HeRO      | `RiskAssessment`                | http://purl.org/sirius/ontology/hero/RiskAssessment              |          |
|                       | `Risk`                      | HeRO      | `Risk`                          | http://purl.org/sirius/ontology/hero/Risk                        |          |
|                       | `AgentOfDeterioration`      | HeRO      | `AgentOfDeterioration`          | http://purl.org/sirius/ontology/hero/AgentOfDeterioration        |          |
|                       | `Hazard`                    | HeRO      | `Hazard`                        | http://purl.org/sirius/ontology/hero/Hazard                      |          |
|                       | `AdverseEffect`             | HeRO      | `AdverseEffect`                 | http://purl.org/sirius/ontology/hero/AdverseEffect               |          |
|                       | *                           | HeRO      | `HazardType`                    | http://purl.org/sirius/ontology/hero/HazardType                  |          |
|                       | *                           | HeRO      | `AdverseEffectType`             | http://purl.org/sirius/ontology/hero/AdverseEffectType           |          |
| **Object properties** |                             |           |                                 |                                                                  |          |
|                       | `assignsRiskTo`             | HeRO      | `identifiesRiskFor`                 | http://purl.org/sirius/ontology/hero/identifiesRiskFor               |          |
|                       | `assigns`                   | HeRO      | `identifies`                       | http://purl.org/sirius/ontology/hero/identifies                     |          |
|                       | `isEmbodiedBy`              | HeRO      | `isClassifiedBy`                | http://purl.org/sirius/ontology/hero/isClassifiedBy              | Subproperty of http://www.ontologydesignpatterns.org/cp/owl/classification.owl#isClassifiedBy         |
|                       | `originatesFrom`            | HeRO      | `resultsFrom`                   | http://purl.org/sirius/ontology/hero/resultsFrom                 |          |
|                       | `causes`                    | HeRO      | `entails`                       | http://purl.org/sirius/ontology/hero/entails                     |          |
|                       | *                           | HeRO      | `hasType`                 | http://purl.org/sirius/ontology/hero/hasType               | FIX: added         |
|                       | *                           | Hero      | `hasType`          | http://purl.org/sirius/ontology/hero/hasType        | FIX: added         |
| **Data properties**   |                             |           |                                 |                                                                  |          |
|                       | `hasSummary`                | HeRO      | `hasNote`                | http://purl.org/sirius/ontology/hero/hasNote              |          |
|                       | *                           | Hero      | `hasNote`                       | http://purl.org/sirius/ontology/hero/hasNote                     |          |
| **Individuals**       |                             |           |                                 |                                                                  |          |
|                       | `physical-forces`           | HeRO      | `physical-forces`               | http://purl.org/sirius/ontology/hero/physical-forces             |          |
|                       | `thieves-and-vandals`       | HeRO      | `theft-and-vandalism`           | http://purl.org/sirius/ontology/hero/theft-and-vandalism         |          |
|                       | `fire`                      | HeRO      | `fire`                          | http://purl.org/sirius/ontology/hero/fire                        |          |
|                       | `water`                     | HeRO      | `water`                         | http://purl.org/sirius/ontology/hero/water                       |          |
|                       | `pests`                     | HeRO      | `pests`                         | http://purl.org/sirius/ontology/hero/pests                       |          |
|                       | `dissociation`              | HeRO      | `dissociation`                  | http://purl.org/sirius/ontology/hero/dissociation                |          |
|                       | `traffic-induced-vibration` | HeRO      | `vibration`                     | http://purl.org/sirius/ontology/hero/vibration                   |          |
|                       | `civil-works`               | HeRO      | `vibration`                     | http://purl.org/sirius/ontology/hero/vibration                   |          |
|                       | `earthquake`                | HeRO      | `vibration`                     | http://purl.org/sirius/ontology/hero/vibration                   |          |
|                       | `subsidence`                | HeRO      | `vibration`                     | http://purl.org/sirius/ontology/hero/vibration                   |          |
|                       | `fissuring`                 | HeRO      | `breakage`                      | http://purl.org/sirius/ontology/hero/breakage                    |          |
|                       | `collapse`                  | HeRO      | `collapse`                      | http://purl.org/sirius/ontology/hero/collapse                    |          |
|                       | `feature-detachment`        | HeRO      | `detachment`                    | http://purl.org/sirius/ontology/hero/detachment                  |          |
|                       | `incorrect-data-management` | HeRO      | `incorrect-action`              | http://purl.org/sirius/ontology/hero/incorrect-action            |          |
|                       | `information-loss`          | HeRO      | `information-loss`              | http://purl.org/sirius/ontology/hero/information-loss            |          |
|                       | `birds`                     | HeRO      | `aerial-animals`                | http://purl.org/sirius/ontology/hero/aerial-animals              |          |
|                       | `weeds`                     | HeRO      | `plants`                        | http://purl.org/sirius/ontology/hero/plants                      |          |
|                       | `excrements`                | HeRO      | `contamination`                 | http://purl.org/sirius/ontology/hero/contamination               |          |
|                       | `overgrowth`                | HeRO      | `overgrowth`                    | http://purl.org/sirius/ontology/hero/overgrowth                  |          |
|                       | `flood`                     | HeRO      | `flooding`                      | http://purl.org/sirius/ontology/hero/flooding                    |          |
|                       | `rainfall`                  | HeRO      | `rainfall`                      | http://purl.org/sirius/ontology/hero/rainfall                    |          |
|                       | `corrosion`                 | HeRO      | `corrosion`                     | http://purl.org/sirius/ontology/hero/corrosion                   |          |
|                       | `equipment-malfunction`     | HeRO      | `electrical-source`             | http://purl.org/sirius/ontology/hero/electrical-source           |          |
|                       | `political-motivation`      | HeRO      | `ideological-motivation`        | http://purl.org/sirius/ontology/hero/ideological-motivation      |          |
|                       | `ideological-motivation`    | HeRO      | `ideological-motivation`        | http://purl.org/sirius/ontology/hero/ideological-motivation      |          |
|                       | `economic-motivation`       | HeRO      | `financial-gain`                | http://purl.org/sirius/ontology/hero/financial-gain              |          |
|                       | `disfiguration`             | HeRO      | `disfiguration`                 | http://purl.org/sirius/ontology/hero/disfiguration               |          |
|                       | `waste-accumulation`        | HeRO      | `littering`                     | http://purl.org/sirius/ontology/hero/littering                   |          |