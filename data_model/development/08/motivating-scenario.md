# Iteration 08

## Name
Re-engineering of assessment activity

## Description
An assessment activity is a situated action that involves gaining and producing scientific knowledge through observations of some Cultural Heritage Object (CHO) and that is parameterized according to a series of elements:
* it has a type: e.g. context description, identification, analysis, evaluation, treatment, etc.;
* it takes place somewhere;
* it is carried out and participated by some agent (e.g. a person, an organization, a software);
* it occurs within a certain time interval;
* it can be documented by some document;
* it can be described with natural language (e.g. through notes);
* it consists of some statements(s).

A statement is an assertion about the CHO that refers to some concept related to it (e.g. a characteristic of the CHO itself, but also external factors that somehow can influence the CHO in some way). A statement is characterized by:
- having some textual content;
- having a type;
- being documented by some document;
- referring to some concept that is internal in the domain of discourse expressed through the statement.

A concept is an information object that describes some qualitative or quantitative parameter that is part of the reality surrounding the observed CHO. Examples include: the economic context in which the CHO exists; the type of occurrence of the risk the CHO is subjected to; the type of deteriorating agent threatening the CHO's integrity; the magnitude of risk; the level of priority assigned to the risk; the type of treatment option selected to deal with the risk. A concept is characterized by:
* having a symbolic value, expressed as a string of text;
* having a type;
* possibly being composed of other concepts (e.g. a frequency measure can be composed of a low estimate, a high estimate and a probable estimate).

## Example 01
An assessment activity `:assessment-activity-01` consisting in the context description of a CHO `:baptistery`, is taking place in Ravenna, is being carried out by the expert Sara Fiorentino (with the involvement of other stakeholders, such as Comune di Ravenna, Soprintendenza di Ravenna and Università di Bologna), in the time interval starting from 2024-02-01 to 2024-03-01, and is being annotated with the following text: "Octagonal building with sloping roof, featuring four apsidioles corresponding to the cardinal points (partially buried). The mosaic decoration is preserved only on the dome, creating a striking contrast with the rough surface of exposed bricks in the lower part. The mosaic depicts in the center the baptism of Christ in the River Jordan, surrounded by a band with the twelve apostles parading in two rows, meeting at the throne of the etimasia, symbol of the invisible presence of Christ."
It is composed of six statements, each assigned to the CHO in question:
1. `:observation-01`, which is a descriptive statement referring to the physical properties of the CHO (`:concept-01`) with the following content: "The Baptistery is externally visible on the N, NW, and NE sides. The west side overlooks the gardens of a private residence, while the south, SW, and SE sides overlook the garden of the Department of Cultural Heritage (University of Bologna)."
2. `:observation-02`, which is a descriptive statement referring to the social environment surrounding the CHO (`:concept-02`) with the following content: "Monumental site in an urban area, open to tourists (with prior admission ticket). The small square where the building is located suffers from a bad reputation, being labeled as a 'socially risky area and a neglected place' (reported incident of an abandoned bed frame found at night in the Baptistery's trench, 11.07.2006, Source: Zaccarini, 2015). Despite the establishment of regulations in 2012 restricting vehicle access to the square, transit and parking for loading/unloading goods are still permitted."
3. `:observation-03`, which is a descriptive statement referring to the political environment surrounding the CHO (`:concept-03`) with the following content: "The monument is often a subject of debate among various political parties and the Municipality of Ravenna.". It is documented by `:document-01`
4. `:observation-04`, which is a descriptive statement referring to the legal status of the CHO (`:concept-04`) with the following content: "Owned by the State Property / Ministry of Culture. Since 1996, it has been part of the UNESCO World Heritage Sites list in Italy ('Early Christian Monuments of Ravenna')."
5. `:observation-05`, which is a descriptive statement referring to the administration of the CHO (`:concept-05`) with the following content: "Since December 2019, it has been managed by the Regional Directorate of Museums of Emilia Romagna, located in Ravenna."
6. `:observation-06`, which is a descriptive statement referring to the economic environment surrounding the CHO (`:concept-06`) with the following content: "The Law No. 77 of February 20, 2006, establishes that UNESCO sites are excellences of the Italian cultural, landscape, and natural heritage, fundamental elements of our country's representation at the international level, and states that interventions on them have priority even in terms of the allocation of financial resources."

Another assessment activity `:assessment-activity-02` -- consisting in the value estimation of the same CHO `:baptistery` -- in terms of its aesthetic function, is taking place in Ravenna, carried out by the expert Sara Fiorentino, in the time interval starting from 2024-02-01 to 2024-03-01. It is annotated with the following text: "Used original materials generally had a good condition and new materials used in a simple but innovative way in respect to historical values." It is composed of three statements:
1. `:observation-07`, which is a valutation referring to the aesthetics of the CHO;
2. `:observation-08`, which is a valutation referring to the function of the CHO;
3. `:observation-09`, which is a valutation referring to the esteemed value of the aesthetic function of the CHO, amounnting to a score equal to "3.65".

## Example 02
Two assessment activities consisting in the identification of risks related to the CHO `:baptistery`, are taking place in Ravenna and are being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-03-01 to 2024-04-01. They are:
* `assessment-activity-03`, annotated with the text "Floods and heavy rains induce erosion of the baptistery walls". It is composed of three statements assigned to the CHO:
    1. `:observation-10`, which is a condition description referring to the potential damage of water-related hazards (`:concept-10`);
    2. `:observation-11`, which is a dimensions description referring to the annual occurrence of the potential hazardous event (`:concept-11`);
    3. `:observation-12`, which is a location description referring to the region surrounding the CHO as the location of occurrence of the potential hazardous event (`:concept-12`).

* `assessment-activity-04`, which is composed of three statements assigned to the CHO:
    1. `:observation-13`, which is a condition description referring to the potential damage of fire-related hazards (`:concept-13`);
    2. `:observation-14`, which is a dimensions description referring to the centennial occurrence of the potential hazardous event (`:concept-14`);
    3. `:observation-15`, which is a location description referring to the building in which the CHO is situated as the location of occurrence of the potential hazardous event (`:concept-15`).

## Example 03
An assessment activity `:assessment-activity-05`, consisting in the analysis of risks related to a CHO `:baptistery`, is taking place in Ravenna, is documented in the document `:document-03` and is being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-04-01 to 2024-05-01, continuing `:assessment-activity-03`. It is annotated with the following text: "A flood event is expected in the baptistery approximately once every 25 years, most likely affecting the whole heritage asset value per event, resulting in a partial loss." It is composed of four statements, each assigned to the CHO in question:
1. `:observation-16`, which is a dimensions description referring to the frequency of the risk occurrence (`:concept-16`). In turn, the frequency is composed of three other concepts:
    * low estimate (`:concept-16a`), with a value of "3.0";
    * probable estimate (`:concept-16b`), with a value of "3.5";
    * high estimate (`:concept-16c`), with a value of "4.0".
2. `:observation-17`, which is a dimensions description referring to the fractional value loss determined by the risk occurrence (`:concept-17`). In turn, the fractional value loss is composed of three other concepts:
    * low estimate (`:concept-17a`), with a value of "4.5";
    * probable estimate (`:concept-17b`), with a value of "5.0";
    * high estimate (`:concept-17c`), with a value of "5.0".
3. `:observation-18`, , which is a dimensions description referring to the exposure determined by the risk occurrence (`:concept-18`). In turn, the exposure is composed of three other concepts:
    * low estimate (`:concept-18a`), with a value of "1.5";
    * probable estimate (`:concept-18b`), with a value of "2.0";
    * high estimate (`:concept-18c`), with a value of "2.5".
4. `:observation-19`, , which is a dimensions description referring to the magnitude of the risk occurrence (`:concept-19`). In turn, the magnitude is composed of three other concepts:
    * low estimate (`:concept-19a`), with a value of "9.0";
    * probable estimate (`:concept-19b`), with a value of "10.5";
    * high estimate (`:concept-19c`), with a value of "11.5".

Another assessment activity `:assessment-activity-06`, consisting in the analysis of risks related to  `:baptistery`, is taking place in Ravenna, is documented in the document `:document-03` and is being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-04-01 to 2024-05-01, continuing `:assessment-activity-04`. It is annotated with the following text: "A large fire event is expected in the museum approximately once every 300 years, with the fire affecting all or most of the heritage asset value, causing total or almost total loss of value in each affected item." It consists of four statements:
1. `:observation-20`, which is a dimensions description referring to the frequency of the risk occurrence (`:concept-20`). In turn, the frequency is composed of three other concepts:
    * low estimate (`:concept-20a`), with a value of "2.0";
    * probable estimate (`:concept-20b`), with a value of "2.5";
    * high estimate (`:concept-20c`), with a value of "3.0".
2. `:observation-21`, which is a dimensions description referring to the fractional value loss determined by the risk occurrence (`:concept-21`). In turn, the fractional value loss is composed of three other concepts:
    * low estimate (`:concept-21a`), with a value of "4.5";
    * probable estimate (`:concept-21b`), with a value of "5.0";
    * high estimate (`:concept-21c`), with a value of "5.0".
3. `:observation-22`, which is a dimensions description referring to the exposure determined by the risk occurrence (`:concept-22`). In turn, the exposure is composed of three other concepts:
    * low estimate (`:concept-22a`), with a value of "4.5";
    * probable estimate (`:concept-22b`), with a value of "5.0";
    * high estimate (`:concept-22c`), with a value of "5.0".
4. `:observation-23`, which is a dimensions description referring to the magnitude of the risk occurrence (`:concept-23`). In turn, the magnitude is composed of three other concepts:
    * low estimate (`:concept-23a`), with a value of "11.0";
    * probable estimate (`:concept-23b`), with a value of "12.5";
    * high estimate (`:concept-23c`), with a value of "13.0".

## Example 04
An assessment activity `:assessment-activity-07` consisting in the evaluation of risks related to a CHO `:baptistery`, is taking place in Ravenna and is being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-05-01 to 2024-06-01, continuing `:assessment-activity-05`. It is annotated with the following text: "The risk of flood (MR = 10.5) has a high priority. It is 100 times smaller than the fire risk. The uncertainty that has been measured amounts to a value equal to 2.5. A risk of this magnitude is equivalent to losing about 0.3% of the heritage asset value every 100 years (or 3% per millennium). The museum direction considers this level of risk as just beyond acceptable, since as a condition the value of MR is slightly higher than 10 and the value of uncertainty is higher than 2." It consists of one statement assigned to the CHO in question:
1. `:observation-24`, which is a diagnosis motivated by `:parameter-19` and referring to a high level of priority(`:concept-24`).

Another assessment activity `:assessment-activity-08` consisting in the evaluation of risks related to the CHO `:baptistery` is taking place in Ravenna and is being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-05-01 to 2024-06-01, following `:assessment-activity-06`. It is annotated with the following text: "The risk of a large fire affecting the baptistery and its contents (MR = 12.5) has an extreme priority. The uncertainty that has been measured amounts to a value equal to 1.0. A risk of this magnitude is equivalent to losing about 3% of the heritage asset value every 10 years (or 30% per century, or 100% in about 300 years). The museum direction considers this level of risk as ‘not acceptable’, since as a condition the value of MR is higher than 10 and the value of uncertainty is lower than 2." It consists of one statement assigned to the CHO in question:
1. `:observation-26`, which is a diagnosis motivated by  `:parameter-23` and referring to a extreme level of priority (`:concept-26`).

## Example 05
An assessment activity `:assessment-activity-09` consisting in the treatment of risks related to a CHO `:baptistery`, is taking place in Ravenna and is being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-06-01 to 2024-07-01, following `:assessment-activity-07`. It is annotated with the following text: "One possible action to protect a baptistery from water damage could be to install a waterproof membrane or coating on the exterior surfaces. This would help prevent water infiltration and damage to the structure. Additionally, regular maintenance such as inspecting for cracks or leaks and repairing them promptly can help mitigate water damage over time". It consists of three statements, each assigned to the CHO in question:
1. `:observation-29`, which is a plan description referring to a blocking action to try managing the described risks (`:concept-29`);
2. `:observation-30`, which is a budget description referring to a capital cost (`:concept-30`) to implement such action, amounting to "3200" euros.
3. `:observation-31`, which is a budget description referring to a maintenance cost (`:concept-31`) to implement such action, amounting to "120" euros.

Another assessment activity `:assessment-activity-10` consisting in the treatment of risks related to a heritage asset `:baptistery`, is taking place in Ravenna and is being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-06-01 to 2024-07-01, following `:assessment-activity-07`. It is annotated with the following text: "Use fire-resistant materials: Consider using fire-resistant coatings, fire-rated doors, and fireproof insulation to minimize fire damage." It consists of three statements, each assigned to the CHO in question:
1. `:observation-32`, which is a plan description referring to a blocking action to try managing the described risks (`:concept-32`);
2. `:observation-33`, which is a budget description referring to a capital cost (`:concept-33`) amounting to "5000" euros;
3. `:observation-34`, which is a budget description referring to a maintenance cost (`:concept-34`), amounting to "375" euros per month.