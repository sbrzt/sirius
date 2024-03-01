# Iteration 08

## Name
Re-engineering of assessment activity

## Description
An assessment activity is a situated action that involves gaining and producing scientific knowledge through observations of some entity and that is parameterized according to a series of elements:
* it has a type: e.g. context description, identification, analysis, evaluation, treatment, etc.;
* it takes place somewhere;
* it is carried out by some agent(s) (e.g. a person, an organization, a software);
* it occurs within a certain time interval;
* it can be documented by some source (e.g. a document);
* it can be described with natural language (e.g. through notes);
* it produces some observation(s).

An observation is a situation during which some entity (e.g. a baptistery, a collection of books, a language) is observed and some characteristics of it (called dimensions) are assessed. Much like an assessment activity, an observation is also parametrized according to a series of elements:
* it has a type: e.g. context observation, value observation, risk observation, measurement, evaluation, treament option, etc.;
* it is carried out by some agent (e.g. a person);
* it occurs in a certain point in time;
* it can be documented by some source (e.g. a document);
* it can be described with natural language (e.g. through notes);
* it observes some dimensions of the entity it observes.

A dimension is some qualitative or quantitative property related to some entity that is being observed during an observation, such as: the economic context in which the entity exists, the type of risk the entity is subjected to, the type of deteriorating agent threatening the entity's integrity, the magnitude of risk, the level of priority assigned to the risk, the type of treatment option selected to deal with the risk, and so on. A dimension is characterized as follows:
* it has a value: e.g. an integer, a string of text, a percentage, etc.;
* it has a type: e.g. risk type (common risk, rare risk, cumulative risk), context type (physical context, political context, legal context, administrative context, economic context, socio-cultural context), measure type (frequency, fractional value loss, exposure, magnitude of risk), etc.;
* it can be expressed according to some kind of measurement unit.

## Example 01
An assessment activity consisting in the context description of a heritage asset `:baptistery`, is taking place in Ravenna, is being carried out by the expert Sara Fiorentino (with the involvement of other stakeholders, such as Comune di Ravenna, Soprintendenza di Ravenna and Università di Bologna), in the time interval starting from 2024-02-01 to 2024-03-01, and is being annotated with the following text: "Edificio a pianta ottagonale con copertura a spioventi, presenta quattro absidiole in corrispondenza dei punti cardinali (parzialmente interrate). La decorazione musiva è conservata sulla sola cupola, creando un sorprendente contrasto con la superficie grezza dei mattoni a vista nella parte inferiore. Il mosaico rappresenta al centro il battesimo di Cristo nel fiume Giordano, attorno ad esso una fascia con i dodici apostoli che sfilano in due teorie, incontrandosi presso il trono dell'etimasìa, simbolo della presenza invisibile di Cristo."
It produces six observations, each observing the asset in question:
1. `:observation-01`, which was carried out by Sara Fiorentino in date 2024-02-01, is a context observation annotated with the following text: "Il Battistero è visibile esternamente sui lati N, NO, NE. Il lato O affaccia sui giardini di un’abitazione privata, mentre i lati S, SO, SE, affacciano sul giardino del Dipartimento di Beni Culturali (Università di Bologna).". It observes a dimension `:dimension-01`, with type `physical-context`.
2. `:observation-02`, which was carried out by Sara Fiorentino in date 2024-02-02, is a context observation annotated with the following text: "Sito monumentale di area urbana, visitabile dai turisti (previo biglietto d’ingresso). La Piazzetta in cui è collocato l’edificio risente di una cattiva fama, in quanto “zona a rischio sociale e luogo dimesso” (si riporta il caso di una rete da letto abbandonata di notte nella trincea del Battistero, 11.07.2006, Fonte: Zaccarini, 2015). Nonostante l’istituzione nel 2012 di una regolamentazione all’accesso dei veicoli alla Piazzetta, resta consentito il transito e la sosta per carico/scarico merci.". It observes a dimension `:dimension-02`, with type `socio-cultural-context`.
3. `:observation-03`, which was carried out by Sara Fiorentino in date 2024-02-03, is a context observation annotated with the following text: "Il monumento è spesso motivo di dibattito tra i vari partiti ed il Comune di Ravenna". It observes a dimension `:dimension-03`, with type `political-context`. In addition, it is documented by a series of documents:
    - `:document-01`: http://www.ravennaincomune.it/wp/index.php/2020/05/23/telecamere-di-sorveglianza-allassalto-del-battistero-degli-ariani
    - `:document-02`: https://www.ravennatoday.it/cronaca/telecamere-nelle-millenarie-mura-del-battistero-degli-ariani-protesta-italia-nostra.html
    - `:document-03`: https://www.ravennaedintorni.it/societa/2020/05/30/telecamere-battistero-ariani/   
    - `:document-04`: https://www.ravennanotizie.it/cultura-spettacolo/2020/05/30/italia-nostra-ravenna-protesta-per-le-telecamere-al-battistero-degli-ariani-uno-sfregio-ai-monumenti/
    - `:document-05`: https://www.corriereromagna.it/ravenna-telecamere-installate-nelle-millenarie-mura-del-battistero/
4. `:observation-04`, which was carried out by Sara Fiorentino in date 2024-02-04, is a context observation annotated with the following text: "Di proprietà del Demanio di Stato / MiC. Dal 1996 fa parte della lista dei siti italiani patrimonio dell'umanità UNESCO («Monumenti paleocristiani di Ravenna»).". It observes a dimension `:dimension-04`, with type `legal-context`.
5. `:observation-05`, which was carried out by Sara Fiorentino in date 2024-02-05, is a context observation annotated with the following text: "Dal dicembre 2019 è gestito da Direzione regionale Musei dell’Emilia Romagna, sede di Ravenna.". It observes a dimension `:dimension-05`, with type `administrative-context`.
6. `:observation-06`, which was carried out by Sara Fiorentino in date 2024-02-06, is a context observation annotated with the following text: "La Legge n. 77 del 20 febbraio 2006, stabilisce che i siti UNESCO sono eccellenze del Patrimonio culturale, paesaggistico e naturale italiano, elementi fondanti della rappresentazione del nostro Paese a livello internazionale e afferma che gli interventi su di essi hanno la priorità anche in ordine all'assegnazione delle risorse finanziarie". It observes a dimension `:dimension-06`, with type `economic-context`.

~VALUE score diventa una dimension~

## Example 02
An assessment activity consisting in the identification of risks related to a heritage asset `:baptistery`, is taking place in Ravenna and is being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-03-01 to 2024-04-01. It produces two observations, each observing the asset in question:
1. `:observation-10`, which was carried out by Sara Fiorentino in date 2024-03-01, is a risk observation documented by `:document-06` and annotated with the following text: "Floods and heavy rains induce erosion of the baptistery walls". It observes three dimensions:
    - `:dimension-07`, with type `water-deteriorating-agent`;
    - `:dimension-08`, with type `common-risk-type`;
    - `:dimension-09`, with type `region-layer`.
2. `:observation-11`, which was carried out by Sara Fiorentino in date 2024-03-02, is a risk observation documented by `:document-06`. It observes three dimensions:
    - `:dimension-10`, with type `fire-deteriorating-agent`;
    - `:dimension-11`, with type `rare-risk-type`;
    - `:dimension-12`, with type `building-layer`.

## Example 03
An assessment activity consisting in the analysis of risks related to a heritage asset `:baptistery`, is taking place in Ravenna and is being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-04-01 to 2024-05-01. It produces two observations, each observing the asset in question:
1. `:observation-12`, which was carried out by Sara Fiorentino in date 2024-04-02, is a measurement observation informed by `:observation-10` and annotated with the following text: "A flood event is expected in the baptistery approximately once every 25 years, most likely affecting the whole heritage asset value per event, resulting in a partial loss.". It observes four dimensions:
    - `:dimension-13`, with type `frequency-measure`, has three values: 3 (low estimate), 3.5 (probable estimate), 4 (high estimate);
    - `:dimension-14`, with type `fractional-value-loss-measure`, has three values: 4.5 (low estimate), 5 (probable estimate), 5 (high estimate);
    - `:dimension-15`, with type `exposure-measure`, has three values: 1.5 (low estimate), 2 (probable estimate), 2.5 (high estimate);
    - `:dimension-16`, with type `risk-magnitude-measure`, has three values: 9 (low estimate), 10.5 (probable estimate), 11.5 (high estimate).
2. `:observation-13`, which was carried out by Sara Fiorentino in date 2024-04-17, is a measurement observation informed by `:observation-11` and annotated with the following text: "A large fire event is expected in the museum approximately once every 300 years, with the fire affecting all or most of the heritage asset value, causing total or almost total loss of value in each affected item.". It observes four dimensions:
    - `:dimension-17`, with type `frequency-measure`, has three values: 2 (low estimate), 2.5 (probable estimate), 3 (high estimate);
    - `:dimension-18`, with type `fractional-value-loss-measure`, has three values: 4.5 (low estimate), 5 (probable estimate), 5 (high estimate);
    - `:dimension-19`, with type `exposure-measure`, has three values: 4.5 (low estimate), 5 (probable estimate), 5 (high estimate);
    - `:dimension-20`, with type `risk-magnitude-measure`, has three values: 11 (low estimate), 12.5 (probable estimate), 13 (high estimate).

# Example 04
An assessment activity consisting in the evaluation of risks related to a heritage asset `:baptistery`, is taking place in Ravenna and is being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-05-01 to 2024-06-01. It produces two observations, each observing the asset in question:
1. `:observation-14`, which was carried out by Sara Fiorentino in date 2024-05-03, is a evaluation observation informed by `:observation-12`, motivated by `:dimension-16` and annotated with the following text: "The risk of flood (MR = 10.5) has a high priority. It is 100 times smaller than the fire risk. The uncertainty that has been measured amounts to a value equal to 2.5. A risk of this magnitude is equivalent to losing about 0.3% of the heritage asset value every 100 years (or 3% per millennium). The museum direction considers this level of risk as just beyond acceptable, since as a condition the value of MR is slightly higher than 10 and the value of uncertainty is higher than 2.". It observes two dimensions:
    - `:dimension-21`, with type `high-priority-level`;
    - `:dimension-22`, with type `review-asap-level`.
2. `:observation-15`, which was carried out by Sara Fiorentino in date 2024-05-15, is a evaluation observation informed by `:observation-13`, motivated by `:dimension-20` and annotated with the following text: "The risk of a large fire affecting the baptistery and its contents (MR = 12.5) has an extreme priority. The uncertainty that has been measured amounts to a value equal to 1.0. A risk of this magnitude is equivalent to losing about 3% of the heritage asset value every 10 years (or 30% per century, or 100% in about 300 years). The museum direction considers this level of risk as ‘not acceptable’, since as a condition the value of MR is higher than 10 and the value of uncertainty is lower than 2.". It observes two dimensions:
    - `:dimension-23`, with type `extreme-priority-level`;
    - `:dimension-24`, with type `treat-asap-level`.

## Example 05
An assessment activity consisting in the evaluation of risks related to a heritage asset `:baptistery`, is taking place in Ravenna and is being carried out by the expert Sara Fiorentino, in the time interval starting from 2024-06-01 to 2024-07-01. It produces two observations, each observing the asset in question:
1. `:observation-16`, which was carried out by Sara Fiorentino in date 2024-05-03, is a evaluation observation informed by `:observation-14` and annotated with the following text: "Attach the objects to their base, with a capital cost of 3000 euros". It observes three dimensions:
    - `:dimension-25`, with type `support-layer`;
    - `:dimension-26`, with type `block-stage`;
    - `:dimension-27`, with type `capital-cost`, has a value of "3000" and uses `euro` as a unit.
2. `:observation-17`, which was carried out by Sara Fiorentino in date 2024-05-03, is a evaluation observation informed by `:observation-15` and annotated with the following text: "Display the objects inside showcases (fitting, BLOCK), with a capital cost of 2000 and an annual cost of 100". It observes four dimensions:
    - `:dimension-28`, with type `fitting-layer`;
    - `:dimension-29`, with type `block-stage`;
    - `:dimension-30`, with type `capital-cost`, has a value of "2000" and uses `euro` as a unit;
    - `:dimension-31`, with type `maintenance-cost`, has a value of "100" and uses `euro` as a unit.