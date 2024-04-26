# Informal Competency Questions
## Question 1

### Identifier
CQ_8.1

### Question
What are the statements assigned to the CHO `:baptistery` by the assessment activity describing its context?

### Expected outcome
List of: `statement`, `note`, `agent`, `document`, `concept`, `concept_type`, `activity`

### Results
* `:observation-01`, "The Baptistery is externally visible on the N, NW, and NE sides. The west side overlooks the gardens of a private residence, while the south, SW, and SE sides overlook the garden of the Department of Cultural Heritage (University of Bologna).", "Sara Fiorentino", None, `:concept-01`, `physical-properties`, `:assessment-activity-01`
* `:observation-02`, "Monumental site in an urban area, open to tourists (with prior admission ticket). The small square where the building is located suffers from a bad reputation, being labeled as a 'socially risky area and a neglected place' (reported incident of an abandoned bed frame found at night in the Baptistery's trench, 11.07.2006, Source: Zaccarini, 2015). Despite the establishment of regulations in 2012 restricting vehicle access to the square, transit and parking for loading/unloading goods are still permitted.", "Sara Fiorentino", None, `:concept-02`, `society`, `:assessment-activity-01`
* `:observation-03`, "The monument is often a subject of debate among various political parties and the Municipality of Ravenna.", "Sara Fiorentino", "2024-02-03", http://www.ravennaincomune.it/wp/index.php/2020/05/23/telecamere-di-sorveglianza-allassalto-del-battistero-degli-ariani, `:concept-03`, `politics`, `:assessment-activity-01`
* `:observation-04`, "Owned by the State Property / Ministry of Culture. Since 1996, it has been part of the list of Italian sites designated as UNESCO World Heritage (‘Early Christian Monuments of Ravenna’).", "Sara Fiorentino", None, `:concept-04`, `legal-status`, `:assessment-activity-01`
* `:observation-05`, "Since December 2019, it has been managed by the Regional Directorate of Museums of Emilia Romagna, located in Ravenna.", "Sara Fiorentino", None, `:concept-05`, `administration`, `:assessment-activity-01`
* `:observation-06`, "The Law No. 77 of February 20, 2006, establishes that UNESCO sites are excellences of the Italian cultural, landscape, and natural heritage, fundamental elements of our country's representation at the international level, and states that interventions on them have priority even in terms of the allocation of financial resources.", "Sara Fiorentino", None, `:concept-06`, `economics`, `:assessment-activity-01`

### Based on
Example 1

***

## Question 2

### Identifier
CQ_8.2

### Question
Which are the hazards, the types of risk occurence and the risk locations referred to by statements assigned to the CHO `:baptistery` by identification activities?

### Expected outcome
List of: `activity`, `agent`, `start_date`, `end_date`, `hazard_type`, `occurrence_type`, `location_type`

### Results
* `:assessment-activity-03`, "Sara Fiorentino", "2024-03-01", "2024-04-01", `water-damage`, `annual`, `region`
* `:assessment-activity-04`, "Sara Fiorentino", "2024-03-01", "2024-04-01", `fire-damage`, `centennial`, `building`

### Based on
Example 2

***

## Question 3

### Identifier
CQ_8.3

### Question
What are the low, probable and high estimates of the measures that are referred to by statements assigned to the CHO `:baptistery` by analysis activities?

### Expected outcome
List of: `activity`, `statement`, `type`, `low_estimate`, `prob_estimate`, `high_estimate`

### Results
* `:assessment-activity-05`, `observation-16`, `frequency`, 3.0, 3.5, 4.0;
* `:assessment-activity-05`, `observation-17`, `fractional-value-loss`, 4.5, 5.0, 5.0;
* `:assessment-activity-05`, `observation-18`, `exposure`, 1.5, 2.0, 2.5;
* `:assessment-activity-05`, `observation-19`, `risk-magnitude`, 9.0, 10.5, 11.5;
* `:assessment-activity-06`, `observation-20`, `frequency`, 2.0, 2.5, 3.0;
* `:assessment-activity-06`, `observation-21`, `fractional-value-loss`, 4.5, 5.0, 5.0;
* `:assessment-activity-06`, `observation-22`, `exposure`, 4.5, 5.0, 5.0;
* `:assessment-activity-06`, `observation-23`, `risk-magnitude`, 11.0, 12.5, 13;

### Based on
Example 3

***

## Question 4

### Identifier
CQ_8.4

### Question
What are the priority levels referred to by statements assigned to the CHO `:baptistery` by evaluation activities?

### Expected outcome
List of: `activity`, `note`, `priority_level`

### Results
* `:assessment-activity-07`, "The risk of flood (MR = 10.5) has a high priority. It is 100 times smaller than the fire risk. The uncertainty that has been measured amounts to a value equal to 2.5. A risk of this magnitude is equivalent to losing about 0.3% of the CHO value every 100 years (or 3% per millennium). The museum direction considers this level of risk as just beyond acceptable, since as a condition the value of MR is slightly higher than 10 and the value of uncertainty is higher than 2.", `:high-priority`
* `:assessment-activity-08`, "The risk of a large fire affecting the baptistery and its contents (MR = 12.5) has an extreme priority. The uncertainty that has been measured amounts to a value equal to 1.0. A risk of this magnitude is equivalent to losing about 3% of the CHO value every 10 years (or 30% per century, or 100% in about 300 years). The museum direction considers this level of risk as ‘not acceptable’, since as a condition the value of MR is higher than 10 and the value of uncertainty is lower than 2.", `:extreme-priority`

### Based on
Example 4

***

## Question 5

### Identifier
CQ_8.5

### Question
What are the treatment actions, capital costs and maintenance costs being referred to by the statements assigned to the CHO `:baptistery` by treatment activities?

### Expected outcome
List of: `activity`, `note`, `action`, `capital_cost`, `maintenance_cost`

### Results
* `:assessment-activity-09`, "One possible action to protect a baptistery from water damage could be to install a waterproof membrane or coating on the exterior surfaces. This would help prevent water infiltration and damage to the structure. Additionally, regular maintenance such as inspecting for cracks or leaks and repairing them promptly can help mitigate water damage over time.", `block`, 3200, 120
* `:assessment-activity-10`, "Use fire-resistant materials: Consider using fire-resistant coatings, fire-rated doors, and fireproof insulation to minimize fire damage.", `block`, 5000, 375

### Based on
Example 5