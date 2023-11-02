# Informal Competency Questions
## Question 1

### Identifier
CQ_3.1

### Question
Return the total number of items in "Battistero degli Ariani", the assets it is composed of, the number of items in each asset, the percentage of total value for each asset, the percentage of total value per item for each asset.

### Expected outcome
List of: `total_items`, `asset_part`, `items_per_part`, `perc_per_part`, `perc_per_item`

### Results
- 21, `building`, 1, 40, 40
- 21, `furniture`, 5, 5, 1
- 21, `mosaics`, 10, 40, 4
- 21, `mural-paintings`, 5, 15, 3

### Based on
Example 1

***

## Question 2

### Identifier
CQ_3.2

### Question
Return the assets which have been assigned "Artistic" contributing values and risks which exist at the "building" layer of enclosure.

### Expected outcome
List of: `asset`, `perc_value`

### Results
- `mosaics`, 40
- `mural-paintings`, 15

### Based on
Example 1

***

## Question 3

### Identifier
CQ_3.3

### Question
Return all the contributing values assigned to the assets that constitute the asset "Battistero degli Ariani". For each value, return its type,  definition, weight, note, and degree of occurrence.

### Expected outcome
List of: `asset`, `value_type`, `definition`, `weight`, `note`, `occurrence`

### Results
- `building`, `historic`, "An object may be historically significant for its association with people, events, places, or themes.", 5, 81, "Historically significant objects range those associated with famous people and important events to those illustrating daily life, used by ordinary people";
- `building`, `artistic`, "An object may be aesthetically significant for its craftsmanship, style, technical excellence, beauty, demonstration of skill, or quality of design and execution", 10, 243, "";
- `furniture`, `social`, "Objects have social significance if they are held in community esteem", 1, 3, "This may be demonstrated by social, spiritual, or cultural expressions that provide evidence of a community’s strong affection for an object or collection and of how it contributes to that community’s identity and social cohesion";
- `furniture`, `historic`, "An object may be historically significant for its association with people, events, places, or themes.", 5, 81, "Historically significant objects range those associated with famous people and important events to those illustrating daily life, used by ordinary people";
- `mosaics`, `artistic`, "An object may be aesthetically significant for its craftsmanship, style, technical excellence, beauty, demonstration of skill, or quality of design and execution", 10, 243, "";
- `mural-paintings`, `artistic`, "An object may be aesthetically significant for its craftsmanship, style, technical excellence, beauty, demonstration of skill, or quality of design and execution", 10, 243, "";

### Based on
Example 1