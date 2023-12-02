# Informal Competency Questions
## Question 1

### Identifier
CQ_4.1

### Question
Return the assets that are part of an asset and the asset percentage they represent, in descending order.

### Expected outcome
List of: `asset`, `asset_part`, `percentage`

### Results
- `house`, `building`, 50
- `house`, `furniture`, 20
- `house`, `mosaics`, 20
- `house`, `paintings`, 10

### Based on
Example 1

***

## Question 2

### Identifier
CQ_4.2

### Question
Return the assets that are part of the `house` asset and the contributing values assigned to them, along with their score, dimension, aspect, note, documentation, and time interval.

### Expected outcome
List of: `asset_part`, `contributing_value`, `score`, `dimension`, `aspect`, `note`, `document`, `time_interval_start`, `time_interval_end`

### Results
- `building`, `value1`, 3.74, `artistic`, `form`, "With simplicity and minimal manipulation creatively retained and upgraded Kashani's house artistic values.", `document-a`, "2020-11-21T00:00:00Z", "2020-11-21T23:59:59Z";
- `building`, `value2`, 3.33, `historic`, `form`, "It is an example of a Qajar house which has been refurbished like other contemporary houses based on historical documents and comparative studies.", `document-a`, at time "2020-10-19T00:00:00Z", "2020-10-19T23:59:59Z";
- `building`, `value3`, 3.26, `social`, `function`, "The house design and decoration represents the middle social class in the Qajar era.", `document-a`, "2021-01-03T00:00:00Z", "2021-01-03T23:59:59Z";
- `furniture`, `value4`, 3.38, `scientific`, `form`, "The remains of the building forms and original shapes are the credible scientific source for recognition typology, structure and the idea of creating spaces in the historic Qajar houses of Kashan.", `document-b`, "2020-11-21T00:00:00Z", "2020-11-21T23:59:59Z";
- `furniture`, `value5`, 3.65, `artistic`, `substance`, "Used Original materials generally had a good condition and new materials used in a simple but innovative way in respect to historical values.", `document-b`, "2021-01-05T00:00:00Z", "2021-01-05T23:59:59Z";
- `mosaics`, `value6`, 3.75, `historic`, `function`, "Hotels for temporary residence are selected in accordance with the historical values of the house.", `document-b`, "2020-12-06T00:00:00Z", "2020-12-06T23:59:59Z";
- `mosaics`, `value7`, 4, `social`, `tradition`, "Taking advantage of professional craftsmen with different specialties played an important role in the construction and restoration of a historic house in Kashan. Weaving workshop has revived this art in Kashan", `document-b`,  "2020-11-12T00:00:00Z", "2020-11-12T23:59:59Z";
- `mosaics`, `value8`, 3.57, `scientific`, `tradition`, "The principal of scientific techniques and traditional construction process related to the formation period extensively displayed and made it possible to study them and showed traditional textile method to be taught.", `document-c`, "2020-10-18T00:00:00Z", "2020-10-18T23:59:59Z";
- `paintings`, `value9`, 4.45, `social`, `setting`, "Social and security level of the neighborhood has been increased. Reuse prosperity in Kashan caused job creation in construction industry and services.", `document-c`, "2020-11-11T00:00:00Z", "2020-11-11T23:59:59Z";
- `paintings`, `value10`, 3.98, `historic`, `feeling`, "It has revived the sense of a Qajar house in Kashan. Representing textile art caused Kashan people to take pride in their historical art.", `document-c`, "2020-11-21T00:00:00Z", "2020-11-21T23:59:59Z".

### Based on
Example 1
