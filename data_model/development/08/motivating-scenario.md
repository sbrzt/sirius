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
    - `:dimension-08`, with type `rare-risk-type`;
    - `:dimension-09`, with type `region-layer`.
2. `:observation-11`, which was carried out by Sara Fiorentino in date 2024-03-02, is a risk observation documented by `:document-06` and annotated with the following text: "Fragmentation of data related to previous incorrect monitoring and maintenance interventions provokes loss of important information related to the baptistery". It observes three dimensions:
    - `:dimension-10`, with type `dissociation-deteriorating-agent`;
    - `:dimension-11`, with type `rare-risk-type`;
    - `:dimension-12`, with type `site-layer`.