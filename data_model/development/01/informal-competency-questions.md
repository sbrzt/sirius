# Informal Competency Questions
## Question 1

### Identifier
CQ_1.1

### Question
Return the information about the heritage asset, including its name, alternative name, its description, the place it is located in (as well as its coordinates), and the time-span temporal horizon that identifies the creation event it has been dated to.

### Expected outcome
* list of: `name`, `alternative_name`, `description`, `place`, `coordinates`, `time_span`

### Results
* "Battistero degli Ariani", "Oratorio di Santa Maria in Cosmedin", "Edificio a pianta ottagonale con copertura a spioventi, presenta quattro absidiole in corrispondenza dei punti cardinali (parzialmente interrate). La decorazione musiva è conservata sulla sola cupola, creando un sorprendente contrasto con la superficie grezza dei mattoni a vista nella parte inferiore. Il mosaico rappresenta al centro il battesimo di Cristo nel fiume Giordano, attorno ad esso una fascia con i dodici apostoli che sfilano in due teorie, incontrandosi presso il trono dell'etimasìa, simbolo della presenza invisibile di Cristo.", "Piazzetta degli Ariani, 48121 Ravenna", "44.41871491574331, 12.20247187841604", "Late fifth century A.D."

### Based on
Example 1

***

## Question 2

### Identifier
CQ_1.2

### Question
Return the contextual information of the heritage asset in terms of its type and description.

### Expected outcome
List of: `heritage_asset`, `context_type`, `context_description`

### Results
* `:baptistery`, `:physical`, "Il Battistero è visibile esternamente sui lati N, NO, NE. Il lato O affaccia sui giardini di un’abitazione privata, mentre i lati S, SO, SE, affacciano sul giardino del Dipartimento di Beni Culturali (Università di Bologna)."
* `:baptistery`, `:socio-cultural`, "Sito monumentale di area urbana, visitabile dai turisti (previo biglietto d’ingresso). La Piazzetta in cui è collocato l’edificio risente di una cattiva fama, in quanto “zona a rischio sociale e luogo dimesso” (si riporta il caso di una rete da letto abbandonata di notte nella trincea del Battistero, 11.07.2006, Fonte: Zaccarini, 2015). Nonostante l’istituzione nel 2012 di una regolamentazione all’accesso dei veicoli alla Piazzetta, resta consentito il transito e la sosta per carico/scarico merci."
* `:baptistery`, `:political`, "Il monumento è spesso motivo di dibattito tra i vari partiti ed il Comune di Ravenna"
* `:baptistery`, `:legal`, "Di proprietà del Demanio di Stato / MiC. Dal 1996 fa parte della lista dei siti italiani patrimonio dell'umanità UNESCO («Monumenti paleocristiani di Ravenna»)."
* `:baptistery`, `:administrative`, "Dal dicembre 2019 è gestito da Direzione regionale Musei dell’Emilia Romagna, sede di Ravenna."
* `:baptistery`, `:economic`, "La Legge n. 77 del 20 febbraio 2006, stabilisce che i siti UNESCO sono eccellenze del Patrimonio culturale, paesaggistico e naturale italiano, elementi fondanti della rappresentazione del nostro Paese a livello internazionale e afferma che gli interventi su di essi hanno la priorità anche in ordine all'assegnazione delle risorse finanziarie"

### Based on
Example 1

***

## Question 3

### Identifier
CQ_1.3

### Question
Return the documents that document the contextual information of the heritage asset.

### Expected outcome
List of: `heritage_asset`, `context_type`, `document`, `document_link`

### Results
* `:baptistery`, `:political`, `:document-1`, "http://www.ravennaincomune.it/wp/index.php/2020/05/23/telecamere-di-sorveglianza-allassalto-del-baptistery"
* `:baptistery`, `:political`, `:document-2`, "https://www.ravennatoday.it/cronaca/telecamere-nelle-millenarie-mura-del-baptistery-protesta-italia-nostra.html"
* `:baptistery`, `:political`, `:document-3`, "https://www.ravennaedintorni.it/societa/2020/05/30/telecamere-battistero-ariani/"
* `:baptistery`, `:political`, `:document-4`, "https://www.ravennanotizie.it/cultura-spettacolo/2020/05/30/italia-nostra-ravenna-protesta-per-le-telecamere-al-baptistery-uno-sfregio-ai-monumenti/"
* `:baptistery`, `:political`, `:document-5`, "https://www.corriereromagna.it/ravenna-telecamere-installate-nelle-millenarie-mura-del-battistero/"

### Based on
Example 1

***

## Question 4

### Identifier
CQ_1.4

### Question
Return the names of the stakeholders involved in the risk assessment activity regarding the heritage asset.

### Expected outcome
List of: `heritage_asset`, `stakeholder_name`

### Results
* `:baptistery`, "Comune di Ravenna"
* `:baptistery`, "Soprintendenza di Ravenna"
* `:baptistery`, "Università di Bologna"
* `:baptistery`, "Cittadinanza"
* `:baptistery`, "Fondazioni locali"
* `:baptistery`, "Turisti"

### Based on
Example 1