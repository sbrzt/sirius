# Informal Competency Questions
## Question 1
### Identifier
CQ_1.1

### Question
Get the documents that document the heritage site and, for each document, return its title, its description, its external link and its link to the file.

### Expected outcome
List of: `title`, `description`, `external_link`, `file_link`

### Result
* "2020_10_10-technical_report_site", "Document that reports that the site is located in a moderately seismic rural area, nearby a river, and that there is a native community nearby that uses part of the site as a sacred place.", "", "http://purl.org/sirius/documents/report-1.pdf"
* "2020_10_10-survey_site", "Document that reports that there is a growing demand for access to the site by national and international tourism.", "https://www.example.org/surveys/survey-1.pdf", ""

### Based on 
Example 1

***

## Question 2
### Identifier
CQ_1.2

### Question
Return the weight of the values of the heritage assets, their names, their descriptions, and the groups the assets belong to.

### Expected outcome
* list of: `value_name`, `value_description`, `value_weight`, `asset`, `group`, `subgroup`

### Results
* "Social", "Objects have social significance if they are held in community esteem.", "1", `:windmill`, `:site-group`, `:building-group`
* "Historic", "An object may be historically significant for its association with people, events, places, or themes.", "5", `:site-group`, `:village-group`
* "Artistic", "An object may be aesthetically significant for its craftsmanship, style, technical excellence, beauty, demonstration of skill, or quality of design and execution.", "10", `:museum`, `:site-group`, `:building-group`

### Based on
Example 1

***

## Question 3
### Identifier
CQ_1.3

### Question
